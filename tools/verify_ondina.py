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

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from tools.mode_a_clone import verify_no_synthetic, verify_no_km_identifiers, _core_clean
import warnings; warnings.filterwarnings("ignore")
try:
    from docx import Document
except Exception:
    Document = None

P3 = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts"
GROUPS = ["world-files/*.docx", "supplementary-files/*.docx", "task-files/*.docx",
          "platform/task*/current/*.docx"]
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
    # report
    print(f"verify_ondina: {len(files)} docx checked across world, supplementary, task, goldens")
    if fails:
        print("FAIL:")
        for n, k, d in fails[:60]:
            print(f"  {n:46} {k:18} {d}")
        return 1
    print("PASS: all gates green (synthetic, prior-world, banned, metadata, template parity, filenames, anchor consistency)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
