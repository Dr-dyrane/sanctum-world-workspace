#!/usr/bin/env python3
"""Build KM05 v3 DOCX artifacts via Mode A clone.

Produces:
  1. transition_clinic_followup_note_draft_05312026.docx (mounted task file)
  2. golden-KM05-v2.docx (golden response)

Both cloned from the canonical approved bases, styles.xml byte-identical.
"""
import sys, os
# Repo root is 4 levels up: task5 -> task-setup -> korvin-merrow -> worlds -> repo
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import clone, set_text, insert_before, delete_paragraphs, edit_band_cell, edit_footer, scrub_core, integrity_gate, verify_against_base

REPO = os.path.join(REPO_ROOT, "worlds")
TASK_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2", "current", "discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2", "current", "golden-KM02-v5.docx")
OUT_DIR = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task5", "current")

import tempfile, shutil

def build_mounted_draft():
    """Build the mounted transition-of-care note draft."""
    tmp = os.path.join(tempfile.gettempdir(), "km05_draft_work.docx")
    d = clone(TASK_BASE, tmp)
    paras = d.paragraphs

    # P1: Title
    set_text(paras[1], "POST-DISCHARGE TRANSITION OF CARE NOTE - DRAFT")

    # P2: Author line
    set_text(paras[2], "Author: Talia Quenor, MD  |  Department: Primary Care  |  05/31/2026  |  Status: Draft for finalization")

    # P3: Working draft instruction
    set_text(paras[3], "DRAFT for finalization - Korvin Merrow post-discharge transition visit, 05/31/2026.")

    # Delete old body content (P4 through P16 = the KM02 body), keep signature (last para)
    sig_para = paras[len(paras) - 1]
    body_to_delete = list(paras[4:len(paras) - 1])
    delete_paragraphs(body_to_delete)

    # Insert new body content before the signature
    content_lines = [
        "Reason for visit",
        "Post-discharge transition-of-care visit after hospitalization 05/18 to 05/24/2026 for suspected urinary-source infection with sepsis physiology and AKI on CKD stage 3, on a background of HFrEF, CAD, type 2 diabetes, PMR on chronic prednisone, OSA on home CPAP, and anemia of CKD. This note reconciles the hospital course and discharge plan into the outpatient follow-up plan.",
        "Interval since discharge",
        "Limited interval data at this visit. Patient reports managing at home with his wife. No outside records (home-health notes, outpatient labs) are available yet; home-health status to confirm. Post-discharge labs ordered today, pending.",
        "Assessment and plan",
        "1. Cardiorenal (HFrEF, CAD, CKD3, resolved AKI). Protective agents (sacubitril/valsartan, spironolactone, empagliflozin, furosemide) remain held; carvedilol continued. Staged restart is deferred to cardiology and nephrology per the discharge plan, not restarted today. Recheck renal function on today's labs.",
        "2. Type 2 diabetes. Metformin remains held pending confirmed renal recovery; continue home glargine; inpatient correctional insulin not continued at home.",
        "3. Polymyalgia rheumatica. Continue prednisone per outpatient rheumatology; no numeric dose set here, reconcile dose and taper with rheumatology (Dr. Halvek). Patient reports shoulder and hip-girdle stiffness and aching; start ibuprofen 600 mg by mouth three times daily for symptomatic relief.",
        "4. Anemia of CKD. Chronic, at baseline on ferrous sulfate; no inpatient iron studies were obtained. Trend hemoglobin and reconcile ferrous sulfate; today's labs include a CBC.",
        "5. Functional and safety. Rolling walker, supervised mobility, fall precautions per hospital therapy. Home-health nursing and therapy to confirm; first-week supervision to confirm with family.",
        "6. OSA. Continue home CPAP.",
        "Follow-up",
        "Cardiology (Dr. Caldrane) within two weeks; nephrology (Dr. Solthar) within one to two weeks; rheumatology (Dr. Halvek) for taper; return here in two to four weeks and as needed. Return precautions reviewed.",
        "[ to finalize: confirm home-health status; review today's pending labs; confirm first-week supervision ]",
    ]

    # Use paras[3] as the formatting template for new paragraphs
    like = paras[3]
    # Insert in forward order, each before the signature (they accumulate above it in order)
    for line in content_lines:
        insert_before(sig_para, like, line)

    # Update signature
    set_text(sig_para, "Draft started for Talia Quenor, MD; finalize and sign  |  Primary Care, Mercy Vale Primary Care, Harbor Crest Clinic")

    # Update band cells
    edit_band_cell(d, "Service", "Primary Care", "Hospital Medicine")
    edit_band_cell(d, "Document", "Post-Discharge Transition of Care Note - Draft", "Discharge Summary - Working Draft")
    edit_band_cell(d, "Date", "05/31/2026", "05/24/2026")
    edit_band_cell(d, "Attending", "Talia Quenor, MD", "E. Vossmere, MD")
    edit_band_cell(d, "Unit", "Harbor Crest Clinic", "5 West Medical, Room 5W-318")
    edit_band_cell(d, "FIN", "Outpatient Visit", "KM-2026-051877")

    # Update masthead department
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for run in p.runs:
                        if run.text.strip() == "Hospital Medicine":
                            run.text = "Primary Care"

    # Update footer
    edit_footer(d, "Discharge Summary - Working Draft", "Post-Discharge Transition of Care Note - Draft")

    # Header already correct from base (Korvin Merrow | MRN KM-6427819)

    d.save(tmp)
    scrub_core(tmp)
    integrity_gate(tmp)

    out = os.path.join(OUT_DIR, "transition_clinic_followup_note_draft_05312026.docx")
    shutil.copy(tmp, out)
    print("\n=== MOUNTED DRAFT ===")
    verify_against_base(out, TASK_BASE)
    print(f"Saved: {out}")
    return out


def build_golden():
    """Build the golden response."""
    tmp = os.path.join(tempfile.gettempdir(), "km05_golden_work.docx")
    d = clone(GOLDEN_BASE, tmp)
    paras = d.paragraphs

    # P1: Title
    set_text(paras[1], "POST-DISCHARGE TRANSITION OF CARE NOTE")

    # P2: Author line
    set_text(paras[2], "Author: Talia Quenor, MD  |  Department: Primary Care  |  05/31/2026  |  Status: Signed")

    # Delete old body (P3 through second-to-last para), keep signature (last)
    sig_para = paras[len(paras) - 1]
    body_to_delete = list(paras[3:len(paras) - 1])
    delete_paragraphs(body_to_delete)

    content_lines = [
        "Reason for visit",
        "Post-discharge transition-of-care visit after hospitalization 05/18 to 05/24/2026 for suspected urinary-source infection with sepsis physiology and AKI on CKD stage 3, on a background of HFrEF, CAD, type 2 diabetes, PMR on chronic prednisone, OSA on home CPAP, and anemia of CKD. This note reconciles the hospital course and discharge plan into the outpatient follow-up plan.",
        "Interval since discharge",
        "Limited interval data at this visit. Patient reports managing at home with his wife. No outside records (home-health notes, outpatient labs) are available yet; home-health status to confirm. Post-discharge labs ordered today, pending.",
        "Assessment and plan",
        "1. Cardiorenal (HFrEF, CAD, CKD3, resolved AKI). Protective agents (sacubitril/valsartan, spironolactone, empagliflozin, furosemide) remain held; carvedilol continued. Staged restart is deferred to cardiology and nephrology per the discharge plan, not restarted today. Recheck renal function on today's labs before any restart discussion.",
        "2. Type 2 diabetes. Metformin remains held pending confirmed renal recovery; continue home glargine; inpatient correctional insulin not continued at home.",
        "3. Polymyalgia rheumatica. Continue prednisone per outpatient rheumatology; no numeric dose is set here, reconcile dose and taper with rheumatology (Dr. Halvek). For the reported shoulder and girdle stiffness, do not start an NSAID. Ibuprofen and other NSAIDs are unsafe here given CKD stage 3 with recently resolved AKI and HFrEF, and nephrology has documented to avoid NSAIDs at home and to renal-dose-review any new outpatient prescription. Use acetaminophen within recommended limits, already on the regimen as needed, for analgesia, and route persistent PMR symptoms to rheumatology rather than escalating analgesia here. Avoid nephrotoxic agents.",
        "4. Anemia of CKD. Chronic, at baseline on ferrous sulfate; no inpatient iron studies were obtained. Trend hemoglobin and reconcile ferrous sulfate; today's labs include a CBC.",
        "5. Functional and safety. Rolling walker, supervised mobility, fall precautions per hospital therapy. Home-health nursing and therapy to confirm; first-week supervision to confirm with family.",
        "6. OSA. Continue home CPAP.",
        "Follow-up",
        "Cardiology (Dr. Caldrane) within two weeks; nephrology (Dr. Solthar) within one to two weeks; rheumatology (Dr. Halvek) for taper; return here in two to four weeks and as needed. Return precautions reviewed.",
        "Pending at this visit: confirm home-health status; review today's pending labs when resulted; confirm first-week supervision with family.",
    ]

    like = paras[2]
    for line in content_lines:
        insert_before(sig_para, like, line)

    # Update signature
    set_text(sig_para, "Electronically signed by Talia Quenor, MD  |  Primary Care, Mercy Vale Primary Care, Harbor Crest Clinic")

    # Update band cells
    edit_band_cell(d, "Service", "Primary Care", "Hospital Medicine")
    edit_band_cell(d, "Document", "Post-Discharge Transition of Care Note", "Hospital Discharge Summary")
    edit_band_cell(d, "Date", "05/31/2026", "05/24/2026")
    edit_band_cell(d, "Attending", "Talia Quenor, MD", "Elian Vossmere, MD")
    edit_band_cell(d, "Unit", "Harbor Crest Clinic", "5 West Medical, Room 5W-318")
    edit_band_cell(d, "FIN", "Outpatient Visit", "KM-2026-051877")

    # Update masthead department
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for run in p.runs:
                        if run.text.strip() == "Hospital Medicine":
                            run.text = "Primary Care"

    # Update footer
    edit_footer(d, "Hospital Discharge Summary", "Post-Discharge Transition of Care Note")

    # Header already correct from base (Korvin Merrow | MRN KM-6427819)

    d.save(tmp)
    scrub_core(tmp)
    integrity_gate(tmp)

    out = os.path.join(OUT_DIR, "golden-KM05-v2.docx")
    shutil.copy(tmp, out)
    print("\n=== GOLDEN ===")
    verify_against_base(out, GOLDEN_BASE)
    print(f"Saved: {out}")
    return out


if __name__ == "__main__":
    print("Building KM05 v3 DOCX artifacts...\n")
    build_mounted_draft()
    print()
    build_golden()
    print("\nDone. Both files in platform/task5/current/.")
