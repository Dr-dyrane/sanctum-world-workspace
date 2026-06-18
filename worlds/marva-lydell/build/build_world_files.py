#!/usr/bin/env python3
"""Build world and supplementary files through the canonical Epic renderer."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

from docx import Document

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from tools.mode_a_clone import scrub_all_metadata, verify_no_synthetic, verify_no_km_identifiers, make_deterministic
import clinical_data as CD
import epic

UPLOAD = REPO / "worlds/korvin-merrow/file-review/upload/filesystem"
WORLD_ROOT = Path(__file__).resolve().parents[1]
OUTDIR = WORLD_ROOT / "world-files"
SUPPDIR = WORLD_ROOT / "supplementary-files"
OUTDIR.mkdir(parents=True, exist_ok=True)
SUPPDIR.mkdir(parents=True, exist_ok=True)

BASE = {
    "ed": UPLOAD / "ed_provider_assessment_05182026.docx",
    "consult": UPLOAD / "nephrology_consultation_05212026.docx",
    "endo": UPLOAD / "endocrinology_consultation_05212026.docx",
    "progress": UPLOAD / "hospitalist_progress_hd4_05212026.docx",
    "casemgmt": UPLOAD / "case_management_social_work_discharge_note_05222026.docx",
    "mar": UPLOAD / "medication_administration_record_05232026.docx",
    "trend": UPLOAD / "renal_infection_hemodynamic_trend_summary_05232026.docx",
    "pharmacy": UPLOAD / "pharmacy_refill_history_report_05182026.docx",
    "primarycare": UPLOAD / "primary_care_outpatient_baseline_summary_05182026.docx",
    "pt": UPLOAD / "physical_therapy_assessment_05202026.docx",
    "ot": UPLOAD / "occupational_therapy_assessment_05202026.docx",
    "family": UPLOAD / "family_communication_care_conference_05222026.docx",
}

RENDER = {
    "title": lambda d, p: epic.note_title(d, p),
    "filing": lambda d, p: epic.filing_line(d, p),
    "section": lambda d, p: epic.section(d, p),
    "body": lambda d, p: epic.body(d, p),
    "bullets": lambda d, p: epic.bullets(d, p),
    "table": lambda d, p: epic.data_table(d, p),
    "sig": lambda d, p: epic.signature(d, p),
}


def _parse_author_dept(filing):
    author = dept = ""
    if "Author:" in filing:
        seg = filing.split("Author:", 1)[1].split("|", 1)[0].strip()
        if " - " in seg:
            author, dept = [x.strip() for x in seg.split(" - ", 1)]
        else:
            author = seg
    return author, dept


def build_one(spec, outdir=None):
    outdir = outdir or OUTDIR
    fname, base_key, note_type, dos, blocks = spec
    if base_key not in BASE:
        raise ValueError(f"Unknown base key {base_key} for {fname}")
    doc = Document(str(BASE[base_key]))
    epic.clear_body(doc)
    filing_txt = next((p for k, p in blocks if k == "filing"), "")
    author, dept = _parse_author_dept(filing_txt)
    epic.clear_and_set_hf(doc, CD.PT["name"], CD.PT["mrn"], CD.FACILITY, note_type)
    epic.masthead(doc, CD.FACILITY, dept)
    epic.blue_bar(doc)
    demo = f"{CD.PT.get('age', '')} y  |  {CD.PT.get('sex', '')}  |  DOB {CD.PT.get('dob', '')}"
    epic.storyboard(doc, CD.PT["name"], demo, CD.PT["mrn"], [
        ("Date of Service", dos),
        ("Author", author or "See note"),
        ("Allergies", CD.PT["allergies"]),
        ("Document", note_type),
    ])
    epic.note_title(doc, next((p for k, p in blocks if k == "title"), note_type))
    if filing_txt:
        epic.filing_line(doc, filing_txt)
    epic.encounter_block(doc, CD.encounter_pairs(dos))
    for kind, payload in blocks:
        if kind in ("title", "filing"):
            continue
        RENDER[kind](doc, payload)
    out = outdir / fname
    doc.save(str(out))
    scrub_all_metadata(str(out))
    verify_no_synthetic(str(out))
    verify_no_km_identifiers(str(out))
    make_deterministic(str(out))
    _check_clean(out)
    return out


def _check_clean(path):
    z = zipfile.ZipFile(str(path))
    doc = z.read("word/document.xml").decode()
    banned_chars = "".join(chr(c) for c in (0x2014, 0x2013, 0x2192, 0x2022, 0x00B0, 0x00D7, 0x2079, 0x00B9, 0x2070))
    banned = {c for c in banned_chars if c in doc}
    assert not banned, f"banned char {banned} in {path.name}"
    assert "word/styles.xml" in z.namelist(), "styles.xml missing"


if __name__ == "__main__":
    if "<<" in repr(CD.PT) or "<<" in repr(CD.ENC):
        raise SystemExit("Phase A substrate placeholders remain in clinical_data.py. Ratify before building.")
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(CD.WORLD_FILES)
    for fn in CD.WORLD_FILES[lo:hi]:
        print("  world  OK", build_one(fn()).name)
    if hi >= len(CD.WORLD_FILES):
        for fn in CD.SUPPLEMENTARY:
            print("  supp   OK", build_one(fn(), outdir=SUPPDIR).name)
    print(f"done slice [{lo}:{hi}]")
