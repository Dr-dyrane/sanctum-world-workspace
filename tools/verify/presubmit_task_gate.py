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
OV = REPO / "worlds/ondina-vasquell"
CAP = 540  # grader ~1 page (Sang/Kathy)

VIS = re.compile(r"<w:t[^>]*>([^<]*)</w:t>")
TRIG = re.compile(r"do not (require|reward|credit)[^.]{0,80}(visual|photo|image)"
                  r"|without (seeing|viewing) the (photo|image)|does not depend on viewing"
                  r"|reachable from the[^.]{0,40}text", re.I)
VISPAT = re.compile(r"(photo|photograph|image)\w*\s+\w{0,12}\s*(show|confirm|demonstrat|reveal|depict)"
                    r"|corroborat\w*[^.]{0,40}(erythema|purulent|drainage|cellulitis|edema|infection)"
                    r"|(shows|reveals|demonstrates)\s+(erythema|purulent|cellulitis)", re.I)
PROMPT_META = re.compile(r"\b(grader|rubric|golden|trap|do not credit|penaliz|rubric|score the)\b", re.I)
# FA/GA now live per task under tasks/taskN/pilot/ (see check_fa_ga)
# FA/GA must be failure-only (Abi 6/09) + no grader-section names (King P 6/14); flag the old both-sides format.
BOTHSIDES = re.compile(r"what the model did well|what the grader (got right|did well)"
                       r"|the grader credited|it credited the|credited the (useful|complete|model|correct)"
                       r"|did much of .{0,30}carefully", re.I)
SECNAME = re.compile(r"\bSection [ABC]\b")

# AutoQC fail-criterion: generic boilerplate filler in graders (no task-specific evaluative
# content). EXTEND this from the live AutoQC named-boilerplate list as we learn it. Matched
# case-insensitively as a substring anywhere in the grader.
BANNED_BOILERPLATE = [
    "patterns to reason about, not items to tick off",
]


def golden_text(p):
    return " ".join(VIS.findall(zipfile.ZipFile(p).read("word/document.xml").decode()))


BANNED_GLYPHS = "—–→•°×⁹"


def _fa_ga_section(t, name):
    """Body under '## <name>' up to the next '## ' header (or EOF); None if absent."""
    body, cap = [], False
    for ln in t.splitlines():
        if re.match(r"^##+\s+", ln):
            if re.sub(r"^##+\s+", "", ln).strip().lower() == name.lower():
                cap = True; continue
            if cap:
                break
        elif cap:
            body.append(ln)
    return "\n".join(body).strip() if cap else None


def check_fa_ga():
    """FA/GA house format (Abi 6/09 + King P 6/14 + KM09): failure-only, no grader-section
    names, no banned glyphs, and each of Failure Analysis / Grader Analysis is exactly two
    paragraphs under about 1000 characters. The two-paragraph + cap checks are what let the
    earlier single-paragraph OV02 draft through; they are now enforced."""
    out = []
    for p in sorted(OV.glob("tasks/task*/pilot/FA-GA-*.md")):
        t = p.read_text(errors="ignore")
        if BOTHSIDES.search(t):
            out.append((p.name, "both-sides format - use failure-only (Abi 6/09)"))
        if SECNAME.search(t):
            out.append((p.name, "names a grader section - state the content instead (no section names)"))
        bad = {c for c in BANNED_GLYPHS if c in t}
        if bad:
            out.append((p.name, f"banned glyph(s) {sorted(bad)} - use plain hyphens, 'C' not degree sign"))
        if re.search(r"recommended grader rating|grader rating\s*:", t, re.I):
            out.append((p.name, "drop the grader-rating line - not part of failure-only FA/GA prose (it is a Studio field, not the paste)"))
        for label in ("Failure Analysis", "Grader Analysis"):
            body = _fa_ga_section(t, label)
            if body is None:
                out.append((p.name, f"missing '## {label}' section"))
                continue
            paras = [b for b in re.split(r"\n\s*\n", body) if b.strip()]
            if len(paras) != 2:
                out.append((p.name, f"{label} must be two paragraphs (found {len(paras)}) - KM09 house format"))
            if len(body) > 1000:
                out.append((p.name, f"{label} is {len(body)} chars > 1000 (each part under about 1000)"))
    return out


def check_task(d: Path):
    flags = []
    graders = sorted(d.glob("grader-guidelines-*.txt"))
    goldens = sorted(d.glob("golden-*.docx"))
    prompts = sorted(d.glob("prompt-*.txt"))
    if not graders:
        return ["no grader-guidelines-*.txt"], None
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
        gl = g.lower()
        for ph in BANNED_BOILERPLATE:
            if ph in gl:
                flags.append(f"grader contains AutoQC-banned boilerplate filler {ph!r}; replace with task-specific evaluative content")
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
    # Mount manifest + referenced-task-file existence (catches the missing-upload class, e.g. OV08).
    # Upload set = non-golden .docx in current/ (golden is the grader reference, not a mounted file).
    mount_files = sorted(p.name for p in d.glob("*.docx") if not p.name.startswith("golden-"))
    run = d / "RUN-INSTRUCTIONS.md"
    if run.exists():
        m = re.search(r"mount[^:\n]*:\s*([^\n]+)", run.read_text(errors="ignore"), re.I)
        if m:
            for fn in re.findall(r"[A-Za-z0-9_]+_\d{8}\.docx", m.group(1)):
                if not (d / fn).exists():
                    flags.append(f"RUN-INSTRUCTIONS lists mount file '{fn}' missing from {d.name}/ (build it or fix the name)")
    # Per-task Studio field map: paste each Studio field from its OWN task's file. The grader's
    # named golden must match this task's golden (the existing golden-named-not-in-dir flag above
    # catches a wrong-task grader pasted into the repo; this map prevents it at upload time).
    manifest = {
        "grader": ", ".join(p.name for p in graders),
        "golden": ", ".join(p.name for p in goldens) or "MISSING",
        "prompt": ", ".join(p.name for p in prompts) or "MISSING",
        "mounts": mount_files,
    }
    return flags, manifest


def main():
    sel = sys.argv[1] if len(sys.argv) > 1 else "task*"
    dirs = sorted(glob.glob(str(OV / f"tasks/{sel}/current")))
    if not dirs:
        print(f"no task dirs matched tasks/{sel}/current"); return 1
    anyflag = False
    for dpath in dirs:
        d = Path(dpath)
        flags, manifest = check_task(d)
        tag = d.parent.name
        if flags:
            anyflag = True
            print(f"FLAG {tag}:")
            for f in flags:
                print(f"   - {f}")
        else:
            print(f"PASS {tag}")
        if manifest:
            print(f"   Studio field map ({tag}) - paste each field from its OWN matching repo file:")
            print(f"     grader-guidelines  <- {manifest['grader']}")
            print(f"     golden             <- {manifest['golden']}")
            print(f"     prompt             <- {manifest['prompt']}")
            print(f"     upload files       <- {', '.join(manifest['mounts'])} + full OV world chart")
    faga = check_fa_ga()
    if faga:
        anyflag = True
        print("FLAG fa-ga:")
        for n, f in faga:
            print(f"   - {n}: {f}")
    print("\npre-submit gate:",
          "FLAGS FOUND - fix before submit" if anyflag else "all tasks clean (mechanizable checks; human review still applies)")
    return 1 if anyflag else 0


if __name__ == "__main__":
    sys.exit(main())
