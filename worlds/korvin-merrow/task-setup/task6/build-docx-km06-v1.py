#!/usr/bin/env python3
"""Build KM06 v1 (orthostatic propagation) DOCX via Mode A clone.

platform/task6/current:
  1. pre_discharge_safety_review_draft_05232026.docx  (mounted; one buried fabrication)
  2. golden-KM06-v1.docx                                (golden; catches it)
Cloned from KM02 approved bases, styles.xml byte-identical.
"""
import sys, os, tempfile, shutil
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import (clone, set_text, insert_before, delete_paragraphs,
                                edit_band_cell, edit_footer, scrub_core, integrity_gate,
                                verify_against_base)
REPO = os.path.join(REPO_ROOT, "worlds")
TASK_BASE = os.path.join(REPO, "korvin-merrow","task-setup","platform","task2","current","discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow","task-setup","platform","task2","current","golden-KM02-v5.docx")
OUT_DIR = os.path.join(REPO, "korvin-merrow","task-setup","platform","task6","current")
os.makedirs(OUT_DIR, exist_ok=True)

REASON = ("Korvin Merrow, 5W-318, is flagged high fall and injury risk for the transition home after "
          "hospitalization 05/18 to 05/24/2026 for suspected urinary-source infection with sepsis physiology "
          "and AKI on CKD stage 3, on a background of HFrEF, CAD, type 2 diabetes, PMR on chronic prednisone, "
          "OSA, and anemia of CKD. Morse Fall Scale 65 (high risk), unchanged across the stay. Near-fall at "
          "home on 05/17/2026 preceded admission. This review consolidates the risk picture for the safety committee.")
FACTORS = ("Orthostatic symptoms and limited blood-pressure reserve during recovery from AKI, with lightheadedness "
           "on standing documented. Sedating medication: gabapentin held on one day for SBP 98 with lightheadedness. "
           "Deconditioning and limited endurance with gait and transfer impairment. Cognitive and "
           "medication-management errors under fatigue.")

def build(which):
    base = TASK_BASE if which=="draft" else GOLDEN_BASE
    tmp = os.path.join(tempfile.gettempdir(), f"km06_{which}.docx")
    d = clone(base, tmp); paras = d.paragraphs
    title = "PRE-DISCHARGE PATIENT SAFETY REVIEW - FALL AND INJURY RISK"
    status = "Draft for safety committee" if which=="draft" else "Signed"
    set_text(paras[1], title + (" - DRAFT" if which=="draft" else ""))
    set_text(paras[2], f"Author: Elian Vossmere, MD  |  Department: Hospital Medicine  |  05/23/2026  |  Status: {status}")
    if which=="draft":
        set_text(paras[3], "DRAFT for the safety committee - Korvin Merrow pre-discharge fall and injury-risk review, 05/23/2026.")
        heading_like, body_like = paras[3], paras[4]
        start = 4
    else:
        heading_like, body_like = paras[3], paras[4]
        start = 3
    sig = paras[len(paras)-1]
    delete_paragraphs(list(paras[start:len(paras)-1]))

    if which=="draft":
        content = [
            (True,  "Reason for review"),
            (False, REASON),
            (True,  "Contributing factors"),
            (False, FACTORS),
            (False, "Orthostatic vital signs were obtained today and were negative, with no significant postural blood-pressure drop, so orthostatic hypotension is not a current contributor."),
            (True,  "Care gaps and recommendations"),
            (False, "Rolling walker and supervised mobility for the early post-discharge period; bedside commode initially, grab bars, and removal of loose rugs. First-week in-home supervision arrangement to confirm with family."),
            (False, "To finalize: complete the contributing factors and the care gaps and confirm the recommendations for the safety committee before filing."),
        ]
        sigtext = "Draft started for the safety committee; finalize and file  |  Hospital Medicine, Mercy Vale Regional Medical Center"
    else:
        content = [
            (True,  "Reason for review"),
            (False, REASON),
            (True,  "Contributing factors"),
            (False, FACTORS + " The near-fall at home on 05/17/2026 anchors the risk."),
            (True,  "Care gaps and recommendations"),
            (False, "Orthostatic vital signs are not on file. No orthostatic measurement was obtained; orthostatic vitals were recommended by nephrology and endocrinology and remain documented as not fully captured. Given the documented orthostatic symptoms, measure orthostatic vitals and act on them before or at discharge and carry the monitoring into follow-up; do not record them as obtained or negative."),
            (False, "Rolling walker and supervised mobility for the early period; bedside commode initially, grab bars, and removal of loose rugs. Reinforce the family-filled weekly organizer and family verification for the cognitive and medication-management risk. Confirm the first-week in-home supervision arrangement with the family before discharge."),
            (False, "Out of scope for this review: cardiorenal restart sequencing and the steroid taper are deferred to cardiology, nephrology, and rheumatology and are not fall-and-injury-risk items."),
        ]
        sigtext = "Electronically signed by Elian Vossmere, MD  |  Hospital Medicine, Mercy Vale Regional Medical Center"

    for is_h, t in content:
        insert_before(sig, heading_like if is_h else body_like, t)
    set_text(sig, sigtext)

    doc_label = "Pre-Discharge Patient Safety Review - Draft" if which=="draft" else "Pre-Discharge Patient Safety Review"
    edit_band_cell(d, "Document", doc_label, "Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary")
    edit_band_cell(d, "Date", "05/23/2026", "05/24/2026")
    edit_band_cell(d, "Attending", "Elian Vossmere, MD", "E. Vossmere, MD" if which=="draft" else "Elian Vossmere, MD")
    edit_band_cell(d, "Unit", "5 West Medical, Room 5W-318", "5 West Medical, Room 5W-318")
    edit_footer(d, "Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary", doc_label)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out = os.path.join(OUT_DIR, "pre_discharge_safety_review_draft_05232026.docx" if which=="draft" else "golden-KM06-v1.docx")
    shutil.copy(tmp, out)
    print(f"\n=== {which.upper()} ==="); verify_against_base(out, base); print("Saved:", out)

if __name__ == "__main__":
    print("Building KM06 v1 orthostatic-propagation DOCX...")
    build("draft"); build("golden")
    print("\nDone.")
