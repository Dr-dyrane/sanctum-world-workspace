#!/usr/bin/env python3
"""Build Ondina world files via Mode A clone of clean KM Epic-note bases.

For each file: clone the mapped clean base (styles.xml byte-identical) -> clear body
-> rebuild chrome + content from clinical_data -> scrub_all_metadata ->
verify_no_synthetic -> fingerprint check (no banned chars, styles preserved) -> save.
World files only; task files build separately (build_task_files.py).
"""
from __future__ import annotations
import sys, zipfile, re
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from docx import Document
from tools.mode_a_clone import scrub_all_metadata, verify_no_synthetic
import epic
import clinical_data as CD

UPLOAD = REPO / "worlds/korvin-merrow/file-review/upload/filesystem"
BASEDIR = REPO / "worlds/ondina-vasquell/phase-3-build-task-artifacts"
OUTDIR = BASEDIR / "world-files"
SUPPDIR = BASEDIR / "supplementary-files"
OUTDIR.mkdir(parents=True, exist_ok=True)
SUPPDIR.mkdir(parents=True, exist_ok=True)

# clean KM bases by grammar key (all verified token-free)
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


def build_one(spec, outdir=None):
    outdir = outdir or OUTDIR
    fname, base_key, note_type, dos, blocks = spec
    doc = Document(str(BASE[base_key]))
    epic.clear_body(doc)
    # chrome
    epic.facility_band(doc, CD.FACILITY, CD.filed(dos))
    # hospital day from note_type/dos handled inside blocks' filing; banner needs hd
    hd = next((b[1] for b in blocks if b[0] == "filing"), "")
    # derive HD label from filename date vs admit
    epic.patient_banner(doc, CD.PT["name"], CD.PT["mrn"],
                        CD.banner_grid(_hd_label(fname), dos, CD.ROSTER["attending"]))
    for kind, payload in blocks:
        RENDER[kind](doc, payload)
    out = outdir / fname
    doc.save(str(out))
    scrub_all_metadata(str(out))
    verify_no_synthetic(str(out))
    _check_clean(out)
    return out


def _hd_label(fname):
    m = re.search(r"_(\d{2})(\d{2})(\d{4})", fname)
    if not m:
        return ""
    mm, dd, yy = m.group(1), m.group(2), m.group(3)
    admit = 16  # 05/16/2026
    try:
        return f"HD{int(dd) - admit + 1}" if mm == "05" and yy == "2026" and int(dd) >= admit else "Pre-admission"
    except ValueError:
        return ""


def _attending_of(blocks):
    for k, p in blocks:
        if k == "filing" and "Author:" in p:
            return p.split("Author:")[1].split("|")[0].split(" - ")[0].strip()
    return CD.ROSTER["attending"]


def _check_clean(path):
    """No banned chars anywhere in document.xml; styles.xml present."""
    z = zipfile.ZipFile(str(path))
    doc = z.read("word/document.xml").decode()
    banned = {c for c in "—–→•°×⁹" if c in doc}
    assert not banned, f"banned char {banned} in {path.name}"
    assert "word/styles.xml" in z.namelist(), "styles.xml missing"


if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(CD.WORLD_FILES)
    for fn in CD.WORLD_FILES[lo:hi]:
        out = build_one(fn())
        print("  world  OK", out.name)
    if hi >= len(CD.WORLD_FILES):
        for fn in CD.SUPPLEMENTARY:
            out = build_one(fn(), outdir=SUPPDIR)
            print("  supp   OK", out.name)
    print(f"done slice [{lo}:{hi}]")
