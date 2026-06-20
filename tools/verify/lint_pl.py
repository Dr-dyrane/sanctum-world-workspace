#!/usr/bin/env python3
"""Lint preference-label (PL) files for the AI-prose tells the preference-labeling
skill bans and that reviewers flag (OV05, 2026-06-19: em dashes, an identical
section template repeated verbatim across labels, formulaic openers recurring
across entries, hedge stacking).

Usage:
    python3 tools/verify/lint_pl.py <PL1.md> [PL2.md PL3.md ...]

Pass ALL of a task's PL files together (PL1, PL2, PL3) so the cross-label checks
catch the templated look: formulaic openers that recur across labels and sentences
repeated verbatim. Single-file checks run on each file.

The pasted block (what goes in the Studio Comments box) runs from the "Scale
Selection:" line to the "Guardrails" block (or end). The Status and pair lines above
it and the Guardrails block below are internal metadata and legitimately carry the
grader scores, so the grader-score-in-prose check runs only on the pasted block.

Exit 0 when there are no FAILs (WARNs allowed). Exit 1 on any FAIL. This is the PL
parallel of lint_fa_ga.py and complements verify_voice.py (voice).
"""
from __future__ import annotations
import sys, re, pathlib
from itertools import combinations

DASH = re.compile(r'[—–→←]')
AI_TRANS = re.compile(r'\b(Furthermore|Moreover|Consequently|Notably|In addition|Additionally)\b')
# the hedge-stacking phrases the OV05 review and the skill name explicitly
HEDGES = [
    "marginally cleaner of two floors", "the marginally cleaner",
    "slimmest of margins", "the slimmest of",
    "near-identical floors", "severity call between two near-identical",
    "plain a, not a full step", "plain b, not a full step",
    "slightly better because",
]
QUALIFIER = re.compile(r'\b(marginally|slightly|somewhat|arguably|narrowly|barely|modestly|a touch|a shade|the slimmest)\b', re.I)
SCALE_SEL = re.compile(r'Scale Selection:\s*[AB][1-4]\b')
SCORE = re.compile(r'\b[01]\.\d{2}\b')                 # grader-score shape 0.NN / 1.00, two decimals
SCORED_CMP = re.compile(r'\bscored?\s+(?:higher|lower|better|worse)\b', re.I)
SENT_WARN = 28
SECTION_LABEL = re.compile(
    r'^\s*(Scale Selection|Justification|Prompt adherence|Correctness|Completeness|'
    r'Methodology|Quality and clarity|Summary)\s*:\s*', re.I)


def pasted_block(t: str) -> str:
    m = re.search(r'(Scale Selection:.*?)(?:\n#+\s*Guardrails|\nGuardrails \(must survive|\Z)',
                  t, re.S | re.I)
    return m.group(1) if m else ""


INLINE_LABEL = re.compile(
    r'\b(Scale Selection|Justification|Prompt adherence|Correctness|Completeness|'
    r'Methodology|Quality and clarity|Summary)\s*:\s*', re.I)


def opener_sentence(t: str) -> str:
    """The label's de-facto opening sentence: the first substantial (>=8 word)
    sentence of the pasted block, regardless of whether a 'Justification:' label is
    used. The Scale Selection lead line and section labels are stripped first so the
    first real clinical sentence is compared, which is where formulaic openers recur."""
    block = INLINE_LABEL.sub('', pasted_block(t))
    block = re.sub(r'^\s*[AB][1-4][^.\n]*[.\n]', '', block, count=1)  # drop the tier lead
    for s in re.split(r'(?<=[.!?])\s+', block):
        s = re.sub(r'\s+', ' ', s).strip()
        if len(s.split()) >= 8:
            return s.lower()
    return ""


def content_sentences(block: str):
    # strip mandated "Label:" prefixes so the section headers do not count as repetition
    lines = [SECTION_LABEL.sub('', ln) for ln in block.splitlines()]
    text = ' '.join(lines)
    sents = [re.sub(r'\s+', ' ', s).strip().lower() for s in re.split(r'(?<=[.!?])\s+', text)]
    return [s for s in sents if len(s.split()) >= 10]


def lint_one(path: str):
    t = pathlib.Path(path).read_text(encoding='utf-8', errors='ignore')
    fails, warns = [], []
    if DASH.search(t):
        fails.append("em or en dash (or arrow) present; use hyphens and commas")
    m = AI_TRANS.search(t)
    if m:
        fails.append(f"banned AI transition: '{m.group(0)}'")
    low = t.lower()
    for h in HEDGES:
        if h in low:
            fails.append(f"hedge-stacking phrase: '{h}'")
    block = pasted_block(t)
    if not block:
        fails.append("no pasted block found; lead it with 'Scale Selection: A#/B# (...)'")
    if not SCALE_SEL.search(block):
        fails.append("no 'Scale Selection: A#/B#' line leading the pasted block")
    sm = SCORE.search(block)
    if sm:
        fails.append(f"grader score '{sm.group(0)}' in the pasted prose; scores stay in the Status and pair lines only (Rule 2)")
    if SCORED_CMP.search(block):
        fails.append("'scored higher/better' framing in the prose; decide from the work product, not the score (Rule 2)")
    q = len(QUALIFIER.findall(block))
    if q > 3:
        warns.append(f"hedge density: {q} qualifiers in one label; state the margin once and stop")
    for s in re.split(r'(?<=[.!?])\s+', block):
        n = len(s.split())
        if n > SENT_WARN:
            warns.append(f"long sentence ({n} words): {s.strip()[:60]}...")
    return fails, warns


def norm_ab(s: str) -> str:
    """Neutralize the A/B subject so a label and its mirror (the same template with
    A and B swapped) compare equal. 'a is the slightly better of two notes' and
    'b is the slightly better of two notes' both become 'x is the slightly better
    of two notes'. Run on already-lowercased text."""
    return re.sub(r'\b[ab]\b', 'x', s)


def cross(files):
    fails = []
    opener, sents = {}, {}
    for f in files:
        t = pathlib.Path(f).read_text(encoding='utf-8', errors='ignore')
        opener[f] = norm_ab(opener_sentence(t))
        sents[f] = set(norm_ab(s) for s in content_sentences(pasted_block(t)))
    for a, b in combinations(files, 2):
        na, nb = pathlib.Path(a).name, pathlib.Path(b).name
        oa, ob = opener[a], opener[b]
        if oa and ob:
            if oa == ob:
                fails.append(f"identical Justification opener in {na} and {nb}")
            else:
                k = 0
                for x, y in zip(oa.split(), ob.split()):
                    if x == y:
                        k += 1
                    else:
                        break
                if k >= 8:
                    fails.append(f"formulaic Justification opener: {na} and {nb} share the first {k} words")
        for s in (sents[a] & sents[b]):
            fails.append(f"sentence repeated verbatim across {na} and {nb}: '{s[:70]}...'")
    return fails


def main():
    files = [a for a in sys.argv[1:] if a.endswith('.md')]
    if not files:
        print("usage: lint_pl.py <PL1.md> [PL2.md PL3.md ...]")
        sys.exit(2)
    any_fail = False
    for f in files:
        fails, warns = lint_one(f)
        name = pathlib.Path(f).name
        for x in fails:
            any_fail = True
            print(f"FAIL [{name}] {x}")
        for x in warns:
            print(f"WARN [{name}] {x}")
    if len(files) >= 2:
        for x in cross(files):
            any_fail = True
            print(f"FAIL [cross-label] {x}")
    if not any_fail:
        print("clean")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
