#!/usr/bin/env python3
"""One-command preflight gate for the Ondina world. Run before any stage.

Checks every docx (world, supplementary, task, and task-setup goldens) for:
  - synthetic/tool tokens (verify_no_synthetic)
  - prior-world identifiers in ANY part incl. headers/footers (verify_no_km_identifiers)
  - banned characters
  - scrubbed core metadata
  - canonical Epic template parity (fills and colors a subset of the world-file vocabulary)
And across the whole set:
  - filenames carry no duplicate " N.docx" suffix
  - the ratified clinical anchors are consistent (no contradictory variant)
Exit code 0 = green; nonzero = a gate failed (printed).
"""
from __future__ import annotations
import sys, re, glob, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.mode_a_clone import verify_no_synthetic, verify_no_km_identifiers, _core_clean
import warnings; warnings.filterwarnings("ignore")
try:
    from docx import Document
except Exception:
    Document = None

P3 = REPO / "worlds/ondina-vasquell"
GROUPS = ["world-files/*.docx", "supplementary-files/*.docx", "task-files/*.docx",
          "tasks/task*/current/*.docx"]
BANNED = set("—–→•°×⁹")

# ratified anchors that must stay consistent; forbidden variants indicate drift
FORBIDDEN = [
    ("toe pressure 38", "toe pressure must be 55 (ratified)"),
    ("Korvin", "prior-world patient name"),
    ("Merrow", "prior-world patient name"),
    ("Mercy Vale", "prior-world facility"),
    ("KM-6427819", "prior-world MRN"),
]
MRN = "OV-3358104"
GRADER_WORD_CAP = 540  # Sang/Kathy: grader ~1 page (~480-520 words); fail on length drift

# Sang five-block sectioning canon (docs/grader-guidelines-lessons.md)
SECTION_HEADERS = ["Preamble", "Register Note", "Section A", "Section B", "Section C"]
BANNED_BOILERPLATE = ["patterns to reason about, not items to tick off"]  # AutoQC fail-criterion filler; EXTEND from the live AutoQC named-boilerplate list
SECB_CLAUSE_1 = ("the model lists findings, doses, provider names, or other specifics "
                 "not in the golden and not covered by accepted alternatives")
SECB_CLAUSE_2 = "the model invents plausible clinical details absent from the source material"


def vis(f):
    return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>",
                    zipfile.ZipFile(f).read("word/document.xml").decode()))


def allparts(f):
    z = zipfile.ZipFile(f)
    return " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist()
                    if n.endswith(".xml") or n.endswith(".rels"))


def fills_colors(f):
    d = zipfile.ZipFile(f).read("word/document.xml").decode()
    return (set(re.findall(r'w:fill="([^"]+)"', d)),
            set(re.findall(r'<w:color w:val="([^"]+)"', d)))


def task_consistency_fails():
    """Per task (tasks/task*/current): grader length cap + golden-vs-grader
    'do not credit visual detail' consistency. Catches the Kathy-G class (golden
    asserts a finding the grader says not to credit) and grader-length drift (Sang)."""
    out = []
    trig = re.compile(r"do not (require|reward|credit)[^.]{0,80}(visual|photo|image)"
                      r"|without (seeing|viewing) the (photo|image)"
                      r"|does not depend on viewing"
                      r"|reachable from the[^.]{0,40}text", re.I)
    vispat = re.compile(r"(photo|photograph|image)\w*\s+\w{0,12}\s*(show|confirm|demonstrat|reveal|depict)"
                        r"|corroborat\w*[^.]{0,40}(erythema|purulent|drainage|cellulitis|edema|infection)"
                        r"|(shows|reveals|demonstrates)\s+(erythema|purulent|cellulitis)", re.I)
    for dpath in sorted(glob.glob(str(P3 / "tasks/task*/current"))):
        d = Path(dpath)
        graders = sorted(d.glob("grader-guidelines-*.txt"))
        goldens = sorted(d.glob("golden-*.docx"))
        for gpath in graders:
            gtxt = gpath.read_text(encoding="utf-8", errors="ignore")
            wc = len(gtxt.split())
            if wc > GRADER_WORD_CAP:
                out.append((gpath.name, "grader-too-long", f"{wc} words > {GRADER_WORD_CAP} (Sang: ~1 page)"))
            if trig.search(gtxt):
                for goldp in goldens:
                    m = vispat.search(vis(str(goldp)))
                    if m:
                        out.append((goldp.name, "golden-grader-conflict",
                                    f"golden asserts visual detail grader forbids: {m.group(0)[:36]!r}"))
    return out


def grader_section_fails():
    """Lint grader sectioning vs the Sang five-block (docs/grader-guidelines-lessons.md):
    five labeled blocks in order, golden named in the Preamble, a chart-aware Register Note,
    the verbatim Section B two-failure-mode clause, no AutoQC-banned Section C filler opener, and a
    credit-restraint pattern. Active tasks/task*/current -> fail; _paused/_retired -> warn
    (closes the scope hole where parked graders were never checked)."""
    active = sorted(glob.glob(str(P3 / "tasks/task*/current")))
    parked = (sorted(glob.glob(str(P3 / "tasks/_paused/*/task*/current")))
              + sorted(glob.glob(str(P3 / "tasks/_retired/*/current"))))
    reg_aware = re.compile(r"(verify|check)\b[^.]{0,80}\bagainst\b"
                           r"|against the (mounted |provided )?(chart|record)", re.I)
    restraint = re.compile(r"credit(ed)? not (penalize|docked)|to credit not penalize", re.I)
    fails, warns = [], []
    for parked_flag, scope in ((False, active), (True, parked)):
        bucket = warns if parked_flag else fails
        for dpath in scope:
            for gpath in sorted(Path(dpath).glob("grader-guidelines-*.txt")):
                t = gpath.read_text(encoding="utf-8", errors="ignore")
                nm = gpath.name
                if parked_flag and len(t.split()) > GRADER_WORD_CAP:
                    bucket.append((nm, "grader-too-long", f"{len(t.split())} words > {GRADER_WORD_CAP}"))
                positions, missing = [], []
                for h in SECTION_HEADERS:
                    m = re.search(r"(?m)^\s*" + re.escape(h), t)
                    positions.append(m.start()) if m else missing.append(h)
                if missing:
                    bucket.append((nm, "missing-block", ", ".join(missing)))
                elif positions != sorted(positions):
                    bucket.append((nm, "block-order", "five blocks out of order"))
                pre = t.split("Register Note")[0]
                if not re.search(r"golden-[\w.\-]+\.docx", pre):
                    bucket.append((nm, "golden-unnamed", "Preamble does not name golden-*.docx"))
                reg = t
                if "Register Note" in t:
                    reg = re.split(r"(?m)^\s*Section A", t.split("Register Note", 1)[1])[0]
                if not reg_aware.search(reg):
                    bucket.append((nm, "register-not-chart-aware", "no 'verify ... against the chart/record'"))
                if SECB_CLAUSE_1 not in t or SECB_CLAUSE_2 not in t:
                    bucket.append((nm, "sectionB-clause", "missing/paraphrased two-failure-mode clause"))
                tl = t.lower()
                for ph in BANNED_BOILERPLATE:
                    if ph in tl:
                        bucket.append((nm, "boilerplate", f"AutoQC-banned filler {ph!r}; open Section C with task-specific content"))
                if not restraint.search(t):
                    bucket.append((nm, "no-restraint", "no credit-restraint pattern"))
    return fails, warns


def main():
    fails = []
    files = []
    for g in GROUPS:
        files += sorted(glob.glob(str(P3 / g)))
    # world vocabulary
    wf, wc = set(), set()
    for f in glob.glob(str(P3 / "world-files/*.docx")):
        a, b = fills_colors(f); wf |= a; wc |= b
    # per-file gates
    for f in files:
        name = Path(f).name
        body = zipfile.ZipFile(f).read("word/document.xml").decode()
        try: verify_no_synthetic(f)
        except AssertionError as e: fails.append((name, "synthetic", str(e)[:50]))
        try: verify_no_km_identifiers(f)
        except AssertionError as e: fails.append((name, "prior-world", str(e)[:50]))
        if {c for c in BANNED if c in body}: fails.append((name, "banned", {c for c in BANNED if c in body}))
        if not _core_clean(f): fails.append((name, "metadata", "not scrubbed"))
        ff, cc = fills_colors(f)
        if not ff <= wf: fails.append((name, "fills-not-subset", ff - wf))
        if not cc <= wc: fails.append((name, "colors-not-subset", cc - wc))
        if re.search(r" \d+\.docx$", name): fails.append((name, "dup-suffix", "filename has ' N.docx'"))
        if Document:
            try: Document(f)
            except Exception as e: fails.append((name, "corrupt", str(e)[:40]))
    # cross-file consistency
    for f in files:
        t = vis(f) + " " + allparts(f)
        for tok, why in FORBIDDEN:
            if tok.lower() in t.lower(): fails.append((Path(f).name, "drift", f"{tok!r}: {why}"))
        for m in set(re.findall(r"OV-\d{6,}", t)):
            if m != MRN: fails.append((Path(f).name, "mrn-variant", m))
    # task-level golden/grader consistency + grader length (Kathy G 6/15)
    fails += task_consistency_fails()
    # grader sectioning lint (Sang five-block); parked graders -> non-blocking warnings
    sec_fails, sec_warns = grader_section_fails()
    fails += sec_fails
    # report
    print(f"verify_ondina: {len(files)} docx checked across world, supplementary, task, goldens")
    if sec_warns:
        print(f"WARN: {len(sec_warns)} grader-sectioning issue(s) in _paused/_retired (non-blocking):")
        for n, k, d in sec_warns[:40]:
            print(f"  {n:46} {k:24} {d}")
    if fails:
        print("FAIL:")
        for n, k, d in fails[:60]:
            print(f"  {n:46} {k:24} {d}")
        return 1
    print("PASS: all gates green (synthetic, prior-world, banned, metadata, template parity, filenames, anchor consistency, grader length, golden-grader consistency, grader sectioning)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
