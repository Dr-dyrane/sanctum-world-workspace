#!/usr/bin/env python3
"""Pre-submit task gate: per-task mechanizable checks from
reference/checklists/reviewer-failure-patterns.md. Run before a task leaves the bench
(usage: python3 tools/verify/presubmit_task_gate.py [task4]). Default scans all tasks.

Green = no mechanizable reviewer-failure pattern detected. Nonzero exit on any FLAG.
Judgment items (task too answer-giving, trap fairness/realism) are NOT mechanized;
human review still applies. This catches the cheap, recurring send-back reasons.
"""
from __future__ import annotations
import sys, re, glob, zipfile
from pathlib import Path
import warnings; warnings.filterwarnings("ignore")

REPO = Path(__file__).resolve().parents[2]
P3 = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts"
CAP = 540  # grader ~1 page (Sang/Kathy)

VIS = re.compile(r"<w:t[^>]*>([^<]*)</w:t>")
TRIG = re.compile(r"do not (require|reward|credit)[^.]{0,80}(visual|photo|image)"
                  r"|without (seeing|viewing) the (photo|image)|does not depend on viewing"
                  r"|reachable from the[^.]{0,40}text", re.I)
VISPAT = re.compile(r"(photo|photograph|image)\w*\s+\w{0,12}\s*(show|confirm|demonstrat|reveal|depict)"
                    r"|corroborat\w*[^.]{0,40}(erythema|purulent|drainage|cellulitis|edema|infection)"
                    r"|(shows|reveals|demonstrates)\s+(erythema|purulent|cellulitis)", re.I)
PROMPT_META = re.compile(r"\b(grader|rubric|golden|trap|do not credit|penaliz|rubric|score the)\b", re.I)


def golden_text(p):
    return " ".join(VIS.findall(zipfile.ZipFile(p).read("word/document.xml").decode()))


def check_task(d: Path):
    flags = []
    graders = sorted(d.glob("grader-guidelines-*.txt"))
    goldens = sorted(d.glob("golden-*.docx"))
    prompts = sorted(d.glob("prompt-*.txt"))
    if not graders:
        return ["no grader-guidelines-*.txt"]
    if not goldens:
        flags.append("no golden-*.docx")
    for gpath in graders:
        g = gpath.read_text(errors="ignore")
        for block in ["Preamble", "Register Note", "Section A", "Section B", "Section C"]:
            if block not in g:
                flags.append(f"grader missing five-block element: {block}")
        named = set(re.findall(r"golden-[\w.\-]+\.docx", g))
        if not named:
            flags.append("Preamble does not name a golden .docx verbatim")
        elif goldens and not (named & {p.name for p in goldens}):
            flags.append(f"grader names a golden not present in dir: {sorted(named)}")
        if "Two failure modes to watch for" not in g:
            flags.append("Section B missing verbatim two-failure-mode clause")
        if "patterns to reason about, not items to tick off" not in g:
            flags.append("Section C missing verbatim opener")
        if not re.search(r"correct restraint", g, re.I):
            flags.append("Section C missing correct-restraint (credit not penalize) pattern")
        wc = len(g.split())
        if wc > CAP:
            flags.append(f"grader too long: {wc} words > {CAP} (Sang: ~1 page)")
        if TRIG.search(g):
            for goldp in goldens:
                if VISPAT.search(golden_text(goldp)):
                    flags.append(f"golden-grader conflict: {goldp.name} asserts visual detail the grader forbids")
    for ppath in prompts:
        pt = ppath.read_text(errors="ignore")
        if len(pt.split()) > 90:
            flags.append(f"prompt long ({len(pt.split())} words): keep it a short first-person ask")
        if PROMPT_META.search(pt):
            flags.append("prompt carries meta-guidance (grader/trap/score language): move it to the grader")
    return flags


def main():
    sel = sys.argv[1] if len(sys.argv) > 1 else "task*"
    dirs = sorted(glob.glob(str(P3 / f"platform/{sel}/current")))
    if not dirs:
        print(f"no task dirs matched platform/{sel}/current"); return 1
    anyflag = False
    for dpath in dirs:
        d = Path(dpath)
        flags = check_task(d)
        tag = d.parent.name
        if flags:
            anyflag = True
            print(f"FLAG {tag}:")
            for f in flags:
                print(f"   - {f}")
        else:
            print(f"PASS {tag}")
    print("\npre-submit gate:",
          "FLAGS FOUND - fix before submit" if anyflag else "all tasks clean (mechanizable checks; human review still applies)")
    return 1 if anyflag else 0


if __name__ == "__main__":
    sys.exit(main())
