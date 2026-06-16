#!/usr/bin/env python3
"""Repo-wide Dr. Alexander voice gate. See docs/alexander-voice-dna.md.

Output text must read like a physician reviewing a chart, not an AI explaining what it
did. This gate flags the AI tells the voice DNA bans.

FAIL (active deliverables we author): grader-guidelines-*.txt, prompt*.txt,
golden-*.docx, fa-ga/*.md, preference-labeling/*.md.
WARN (quote-bearing or not authored by us): reviews, abi-mode-review*.md,
reference/templates/*.md, and any archived/paused/retired/history/design copy.

Quoted spans (double-quoted text, or lines beginning with '>') are ignored, so a quoted
human review or model transcript does not trip the gate.

Exit 0 = green; nonzero = a banned AI tell in an active deliverable.
"""
from __future__ import annotations
import sys, re, glob, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# AI transitions / inflation the voice DNA says to drop (humanization rules)
BANNED = ["Furthermore", "Moreover", "Consequently", "Notably", "In addition",
          "salient finding", "critical insight", "robust analysis", "comprehensive review"]
BANNED_RE = re.compile("|".join(r"\b" + re.escape(b) + r"\b" for b in BANNED), re.I)

# Process narration: reviews/FA/GA state the clinical omission, not the model's process
PROCESS_RE = re.compile(
    r"\bOCR\b|\bnavigat(?:e|ed|ing|ion)\b"
    r"|the model (?:failed to|did not) (?:review|open|read|parse|access|locate|find|click)"
    r"|the model (?:then )?(?:clicked|opened|navigated|ran the tool|called the tool)", re.I)

PARK = ("/archive/", "_retired", "_paused", "_pipeline-history", "build-phase-drafts",
        "/design/", "/_t/", "/handoff/")

# (class, glob, run_process_check)
DELIVER = [
    ("grader", "worlds/**/grader-guidelines-*.txt", False),
    ("prompt", "worlds/**/prompt*.txt", False),
    ("golden", "worlds/**/golden-*.docx", False),
    ("fa-ga", "worlds/**/fa-ga/*.md", True),
    ("pl", "worlds/**/preference-labeling/*.md", True),
]
WARN_ONLY = [
    ("review", "worlds/**/reviews/*.md", True),
    ("review", "worlds/**/abi-mode-review*.md", True),
    ("template", "reference/templates/*.md", False),
]


def is_parked(p):
    return any(tok in p for tok in PARK)


def text_of(f):
    if f.endswith(".docx"):
        try:
            x = zipfile.ZipFile(f).read("word/document.xml").decode("utf-8", "ignore")
            return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", x))
        except Exception:
            return ""
    return Path(f).read_text(encoding="utf-8", errors="ignore")


def unquote(t):
    """Drop quoted human/model text so it does not trip the gate."""
    t = "\n".join(l for l in t.splitlines() if not l.lstrip().startswith(">"))
    t = re.sub(r'"[^"]*"', " ", t)
    t = re.sub(r"[“”][^“”]*[“”]", " ", t)
    return t


def scan():
    fails, warns, n, seen = [], [], 0, set()
    for hard, group in ((True, DELIVER), (False, WARN_ONLY)):
        for cls, pat, proc in group:
            for f in glob.glob(str(REPO / pat), recursive=True):
                if f in seen:
                    continue
                seen.add(f)
                n += 1
                rel = str(Path(f).relative_to(REPO))
                t = unquote(text_of(f))
                bucket = fails if (hard and not is_parked(rel)) else warns
                for m in sorted({x.lower() for x in BANNED_RE.findall(t)}):
                    bucket.append((Path(f).name, "ai-transition", f"{m!r}  ({rel})"))
                if proc:
                    pm = PROCESS_RE.search(t)
                    if pm:
                        warns.append((Path(f).name, "process-narration", f"{pm.group(0)[:30]!r}  ({rel})"))
    return fails, warns, n


def main():
    fails, warns, n = scan()
    print(f"verify_voice: {n} output-text artifacts checked (Alexander voice DNA)")
    if warns:
        print(f"WARN: {len(warns)} voice issue(s) in reviews/templates/archived (non-blocking):")
        for nm, k, d in warns[:40]:
            print(f"  {nm:44} {k:18} {d}")
    if fails:
        print("FAIL: banned AI tells in active deliverables:")
        for nm, k, d in fails[:60]:
            print(f"  {nm:44} {k:18} {d}")
        return 1
    print("PASS: active deliverables free of banned AI transitions (Alexander voice)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
