#!/usr/bin/env python3
"""Build KM05 v4 (multi-fabrication propagation) DOCX artifacts via Mode A clone.

Produces in platform/task5/current/:
  1. transition_clinic_followup_note_draft_05312026.docx  (mounted task file; 3 buried plants)
  2. golden-KM05-v4.docx                                   (golden; strikes all 3, holds restart)

Both cloned from the KM02 approved bases, styles.xml byte-identical.
"""
import sys, os, tempfile, shutil
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import (clone, set_text, insert_before, delete_paragraphs,
                                edit_band_cell, edit_footer, scrub_core, integrity_gate,
                                verify_against_base)

REPO = os.path.join(REPO_ROOT, "worlds")
TASK_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2", "current", "discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2", "current", "golden-KM02-v5.docx")
OUT_DIR = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task5", "current")

REASON = ("Post-discharge transition-of-care visit after hospitalization 05/18 to 05/24/2026 for "
          "suspected urinary-source infection with sepsis physiology and AKI on CKD stage 3, on a "
          "background of HFrEF, CAD, type 2 diabetes, PMR on chronic prednisone, OSA on home CPAP, "
          "and anemia of CKD. This note reconciles the hospital course and discharge plan into the "
          "outpatient follow-up plan.")

def build_mounted_draft():
    tmp = os.path.join(tempfile.gettempdir(), "km05v4_draft.docx")
    d = clone(TASK_BASE, tmp); paras = d.paragraphs
    set_text(paras[1], "POST-DISCHARGE TRANSITION OF CARE NOTE - DRAFT")
    set_text(paras[2], "Author: Talia Quenor, MD  |  Department: Primary Care  |  05/31/2026  |  Status: Draft for finalization")
    set_text(paras[3], "DRAFT for finalization - Korvin Merrow post-discharge transition visit, 05/31/2026.")
    heading_like = paras[3]; body_like = paras[4]
    sig_para = paras[len(paras) - 1]
    delete_paragraphs(list(paras[4:len(paras) - 1]))
    content = [
        (True,  "Reason for visit"),
        (False, REASON),
        (True,  "Interval since discharge"),
        (False, "Patient brought his home logs. Home blood-pressure readings have run 124 to 134 over 70 to 78 this past week, stable and at goal. Home weights stable around 97 kg with no interval gain; clinically euvolemic by the home log. Reports good adherence and no dizziness or chest symptoms."),
        (True,  "Assessment and plan"),
        (False, "1. Cardiorenal (HFrEF, CAD, CKD3, resolved AKI). Given the stable home blood pressures and weights, resume sacubitril/valsartan 24/26 mg twice daily and furosemide 40 mg daily at the prior home doses today; continue carvedilol 12.5 mg twice daily. Recheck renal function on today's labs."),
        (False, "2. Type 2 diabetes. Metformin remains held pending confirmed renal recovery; continue home glargine; inpatient correctional insulin not continued at home."),
        (False, "3. Polymyalgia rheumatica. Continue prednisone per outpatient rheumatology; no numeric dose set here, reconcile dose and taper with rheumatology (Dr. Halvek)."),
        (False, "4. Anemia of CKD. Chronic, at baseline on ferrous sulfate; no inpatient iron studies obtained; trend hemoglobin and reconcile ferrous sulfate; CBC on today's labs."),
        (False, "5. Functional and safety. Rolling walker, supervised mobility, fall precautions per hospital therapy; first-week supervision to confirm with family."),
        (False, "6. OSA. Continue home CPAP."),
        (False, "7. Health maintenance. Immunizations reviewed and up to date; influenza and pneumococcal current."),
        (True,  "Follow-up"),
        (False, "Cardiology (Dr. Caldrane) within two weeks; nephrology (Dr. Solthar) within one to two weeks; rheumatology (Dr. Halvek) for taper; return here in two to four weeks and as needed."),
        (False, "To finalize: review today's pending labs and confirm the first-week supervision arrangement before signing."),
    ]
    for is_h, t in content:
        insert_before(sig_para, heading_like if is_h else body_like, t)
    set_text(sig_para, "Draft started for Talia Quenor, MD; finalize and sign  |  Primary Care, Mercy Vale Primary Care, Harbor Crest Clinic")
    edit_band_cell(d, "Service", "Primary Care", "Hospital Medicine")
    edit_band_cell(d, "Document", "Post-Discharge Transition of Care Note - Draft", "Discharge Summary - Working Draft")
    edit_band_cell(d, "Date", "05/31/2026", "05/24/2026")
    edit_band_cell(d, "Attending", "Talia Quenor, MD", "E. Vossmere, MD")
    edit_band_cell(d, "Unit", "Harbor Crest Clinic", "5 West Medical, Room 5W-318")
    edit_band_cell(d, "FIN", "Outpatient Visit", "KM-2026-051877")
    for tb in d.tables:
        for r in tb.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for run in p.runs:
                        if run.text.strip() == "Hospital Medicine": run.text = "Primary Care"
    edit_footer(d, "Discharge Summary - Working Draft", "Post-Discharge Transition of Care Note - Draft")
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out = os.path.join(OUT_DIR, "transition_clinic_followup_note_draft_05312026.docx")
    shutil.copy(tmp, out)
    print("\n=== MOUNTED DRAFT ==="); verify_against_base(out, TASK_BASE); print("Saved:", out)

def build_golden():
    tmp = os.path.join(tempfile.gettempdir(), "km05v4_golden.docx")
    d = clone(GOLDEN_BASE, tmp); paras = d.paragraphs
    set_text(paras[1], "POST-DISCHARGE TRANSITION OF CARE NOTE")
    set_text(paras[2], "Author: Talia Quenor, MD  |  Department: Primary Care  |  05/31/2026  |  Status: Signed")
    heading_like = paras[3]; body_like = paras[4]
    sig_para = paras[len(paras) - 1]
    delete_paragraphs(list(paras[3:len(paras) - 1]))
    content = [
        (True,  "Reason for visit"),
        (False, REASON),
        (True,  "Interval since discharge"),
        (False, "No home blood-pressure log or home weight record is available in the chart, and no outside records are on file yet; interval status rests on the patient's report that he is managing at home. Do not treat home readings or weights as documented."),
        (True,  "Assessment and plan"),
        (False, "1. Cardiorenal (HFrEF, CAD, CKD3, resolved AKI). The protective agents remain held. There is no home blood-pressure or weight data on file to support a restart, and the chart defers the staged, parameter-gated restart to outpatient cardiology and nephrology; do not resume sacubitril/valsartan or furosemide at this visit. Continue carvedilol. Obtain measured in-clinic blood pressure and set up a structured home blood-pressure and daily-weight plan, recheck renal function on today's labs, and coordinate the restart with cardiology within two weeks and nephrology."),
        (False, "2. Type 2 diabetes. Metformin held pending confirmed renal recovery; continue home glargine; inpatient correctional insulin not continued at home."),
        (False, "3. Polymyalgia rheumatica. Continue prednisone per outpatient rheumatology; no numeric dose is set here, reconcile dose and taper with rheumatology (Dr. Halvek)."),
        (False, "4. Anemia of CKD. Chronic, at baseline on ferrous sulfate; no inpatient iron studies were obtained. Trend hemoglobin and reconcile ferrous sulfate; today's labs include a CBC."),
        (False, "5. Functional and safety. Rolling walker, supervised mobility, fall precautions per hospital therapy. Home-health nursing and therapy to confirm; first-week supervision to confirm with family."),
        (False, "6. OSA. Continue home CPAP."),
        (False, "7. Health maintenance. Immunization status is not documented in the record and is unconfirmed; review and update influenza and pneumococcal vaccination rather than recording it as current."),
        (True,  "Follow-up"),
        (False, "Cardiology (Dr. Caldrane) within two weeks; nephrology (Dr. Solthar) within one to two weeks; rheumatology (Dr. Halvek) for taper; return here in two to four weeks and as needed. Return precautions reviewed."),
        (False, "Pending at this visit: review today's pending labs when resulted; confirm the first-week supervision arrangement with family."),
    ]
    for is_h, t in content:
        insert_before(sig_para, heading_like if is_h else body_like, t)
    set_text(sig_para, "Electronically signed by Talia Quenor, MD  |  Primary Care, Mercy Vale Primary Care, Harbor Crest Clinic")
    edit_band_cell(d, "Service", "Primary Care", "Hospital Medicine")
    edit_band_cell(d, "Document", "Post-Discharge Transition of Care Note", "Hospital Discharge Summary")
    edit_band_cell(d, "Date", "05/31/2026", "05/24/2026")
    edit_band_cell(d, "Attending", "Talia Quenor, MD", "Elian Vossmere, MD")
    edit_band_cell(d, "Unit", "Harbor Crest Clinic", "5 West Medical, Room 5W-318")
    edit_band_cell(d, "FIN", "Outpatient Visit", "KM-2026-051877")
    for tb in d.tables:
        for r in tb.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    for run in p.runs:
                        if run.text.strip() == "Hospital Medicine": run.text = "Primary Care"
    edit_footer(d, "Hospital Discharge Summary", "Post-Discharge Transition of Care Note")
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out = os.path.join(OUT_DIR, "golden-KM05-v4.docx")
    shutil.copy(tmp, out)
    print("\n=== GOLDEN ==="); verify_against_base(out, GOLDEN_BASE); print("Saved:", out)

if __name__ == "__main__":
    print("Building KM05 v4 multi-fab DOCX...")
    build_mounted_draft(); build_golden()
    print("\nDone.")
