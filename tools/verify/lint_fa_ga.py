#!/usr/bin/env python3
"""Lint ONE FA/GA file against the locked fa-ga-canonical voice and structure rules.

Usage:
    python3 tools/verify/lint_fa_ga.py worlds/.../FA-GA-OVNN-current.md [more files]

Exit 0 when there are no FAILs (WARNs are allowed). Exit 1 on any FAIL.

This complements presubmit_task_gate.py. The gate checks the whole task* tree for the
structural basics (two paragraphs, <=1000 chars, dashes, banned credit phrases, rating
line). This linter checks the SINGLE file being drafted, including the voice rules the
gate does not enforce: the FA opens with "On trajectory N", only the analyzed run is
named (no other-run scores or distribution in the body), the writer's own score appears
as the required Overall Failure Score line, and sentences stay short enough to read in one breath.

The Status line above "## Failure Analysis" is internal metadata. It legitimately carries
the full distribution and the run hashes, so the single-run and distribution checks run
ONLY on the Failure Analysis and Grader Analysis bodies, never the Status line.
"""
from __future__ import annotations
import sys, re, pathlib

RATING = re.compile(r'\b(Great|Good|Mediocre|Poor)\b')           # Studio rating words (capitalized)
BANNED = ["the grader credited", "it credited the", "credited the correct",
          "credited the useful", "credited the complete", "credited the model",
          "what the grader got right", "what the model did well"]
OTHER_RUNS = re.compile(r'\b(every|all|each|several|other|both|two|three|four|five|six|'
                        r'seven|eight|nine|ten)\s+runs?\b', re.I)
SCORE_RANGE = re.compile(r'0\.\d{1,2}\s*(?:to|through|-|and)\s*0\.\d{1,2}')
DISTRIB = re.compile(r'\b(distribution|uniformly|bimodal|across runs|no high outlier|'
                     r'mean (?:of |about )?0?\.?\d)\b', re.I)
OVERALL_SCORE = re.compile(r'Overall Failure Score:\s*(?:0(?:\.\d{1,2})?|1(?:\.0{1,2})?)\s*/\s*1\.0')
CITES = re.compile(r'\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b')  # a dated source-document reference; the FA must name at least one
SENT_WARN = 24  # words; the breath rule aims for ~15, warn past 24

def section(t: str, name: str):
    m = re.search(rf"^##+\s+{re.escape(name)}\s*$(.*?)(?=^##+\s+|\Z)", t, re.S | re.M)
    return m.group(1).strip() if m else None

def sentences(b: str):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', b) if s.strip()]

def lint(path: str):
    t = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    fails, warns = [], []

    if t.count('—') or t.count('–'):
        fails.append("em or en dash present; use hyphens, commas, periods")
    m = RATING.search(t)
    if m:
        fails.append(f"grader-rating word '{m.group(0)}' present; the rating goes only in the Studio field, never the file")
    for b in BANNED:
        if b in t.lower():
            fails.append(f"banned credit phrase: '{b}'")

    fa = section(t, "Failure Analysis")
    ga = section(t, "Grader Analysis")
    if fa is None:
        fails.append("missing '## Failure Analysis' section")
    if ga is None:
        fails.append("missing '## Grader Analysis' section")

    for name, body in (("FA", fa), ("GA", ga)):
        if not body:
            continue
        paras = [p for p in re.split(r'\n\s*\n', body) if p.strip()]
        if len(paras) != 2:
            fails.append(f"{name}: must be exactly two paragraphs (found {len(paras)})")
        if len(body) > 1000:
            fails.append(f"{name}: {len(body)} chars > 1000")
        m = OTHER_RUNS.search(body)
        if m:
            fails.append(f"{name}: mentions other runs ('{m.group(0)}'); analyze only this run, keep the distribution in the Status line")
        m = SCORE_RANGE.search(body)
        if m:
            fails.append(f"{name}: score range '{m.group(0)}' is the distribution; keep it in the Status line, name only this run's score")
        m = DISTRIB.search(body)
        if m:
            fails.append(f"{name}: distribution language '{m.group(0)}'; keep it in the Status line")
        if ';' in body:
            warns.append(f"{name}: semicolon present; the breath rule prefers two short sentences")
        for s in sentences(body):
            n = len(s.split())
            if n > SENT_WARN:
                warns.append(f"{name}: long sentence ({n} words), consider splitting -> \"{s[:55]}...\"")

    if fa:
        if not fa.startswith("On trajectory "):
            fails.append("FA must open with 'On trajectory N' (the 1-10 count, not the run hash)")
        if not OVERALL_SCORE.search(fa):
            fails.append("FA must include the writer's own score line: 'Overall Failure Score: X.XX / 1.0'")
        if not CITES.search(fa):
            fails.append("FA cites no specific source document; name the consult, order, or note by author or date "
                         "(e.g. 'the wound-care consult (Olwyn, CWOCN, 05/20)') so a reviewer can verify. "
                         "The rubric requires specific documents, not generic references")
    if ga and 'trajectory' not in ga.lower():
        warns.append("GA does not name the trajectory; the house form is 'The grader scored trajectory N at X'")

    return fails, warns

def main():
    if len(sys.argv) < 2:
        print("usage: python3 tools/verify/lint_fa_ga.py <FA-GA-file.md> [more]")
        sys.exit(2)
    rc = 0
    for p in sys.argv[1:]:
        fails, warns = lint(p)
        print(f"== {p} ==")
        for w in warns:
            print(f"  WARN  {w}")
        for f in fails:
            print(f"  FAIL  {f}")
        if fails:
            rc = 1
            print(f"  -> {len(fails)} FAIL, {len(warns)} WARN")
        else:
            print(f"  -> clean{(' (' + str(len(warns)) + ' WARN)') if warns else ''}")
    sys.exit(rc)

if __name__ == "__main__":
    main()
