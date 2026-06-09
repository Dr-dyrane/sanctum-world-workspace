#!/usr/bin/env python3
"""KM08 v3 INPATIENT-VS-OBSERVATION STATUS DETERMINATION (physician) - MERGED.
Merges the planner's stronger content (criteria-based rationale + the 'interval improvement does not retroactively
reduce status to observation' point) into the STANDARD KM02-clone DOCX (3-row [1,1,3] band). Defects from the
planner zip fixed: no square brackets, named author (Vossmere), 'admitting' not 'discharging'.
Judgment trap via draft attribution: draft leans OBSERVATION; correct = INPATIENT on severity-of-illness +
intensity-of-service, not on the favorable trajectory. Admission day 05/18/2026 (HD1)."""
import sys, os, tempfile, shutil
REPO_ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..",".."))
sys.path.insert(0,REPO_ROOT)
from tools.mode_a_clone import (clone,set_text,insert_before,delete_paragraphs,
    edit_band_cell,edit_footer,scrub_core,integrity_gate,verify_against_base)
REPO=os.path.join(REPO_ROOT,"worlds")
TASK_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","golden-KM02-v5.docx")
OUT=os.path.join(REPO,"korvin-merrow","task-setup","platform","task8","current"); os.makedirs(OUT,exist_ok=True)

QUESTION=("Admission status determination: inpatient versus observation for this hospitalization beginning 05/18/2026, with "
          "criteria-based rationale.")
COURSE=("62-year-old man with HFrEF, CAD (remote mid-LAD drug-eluting stent, 2018), CKD stage 3, type 2 diabetes, polymyalgia "
        "rheumatica on prednisone, and OSA, admitted with a suspected urinary-source infection and sepsis physiology "
        "(WBC 15.6 with left shift, pyuria, low-grade fever, tachycardia) and AKI on CKD with an admission creatinine of "
        "2.62 mg/dL against a 1.6 to 1.8 baseline and BUN 48. Empiric intravenous antibiotics and cautious crystalloid "
        "resuscitation were started, the home cardiorenal regimen was held pending hemodynamic and renal stabilization, and "
        "he required serial renal and hemodynamic monitoring over the hospital course.")
STATUS_DRAFT=("He is trending better and is expected to turn the corner quickly, so observation status looks appropriate for "
              "a short stay.")
STATUS_GOLD=("Inpatient status is appropriate. The presentation meets inpatient-level criteria: sepsis physiology from a "
             "suspected urinary source requiring intravenous antibiotics, and AKI on CKD stage 3 with an admission creatinine "
             "of 2.62 mg/dL requiring intravenous fluids and serial renal and electrolyte monitoring, in a patient with HFrEF "
             "and CAD whose protective regimen was held and required monitored stabilization. The documented severity and the "
             "need for multiple days of inpatient-level renal, hemodynamic, and infection monitoring exceed what observation "
             "is intended to cover, and the hospitalist record documents active inpatient management with the patient not at "
             "discharge candidacy through the early course. The interval improvement over the stay reflects effective inpatient "
             "treatment and does not retrospectively reduce the admission to observation; status is determined on the severity "
             "and the intensity of services required at and after admission, not on the favorable trajectory alone.")
CLOSE_DRAFT="To finalize: confirm the status and the criteria-based rationale before signing."
CLOSE_GOLD=("To finalize: inpatient is the determination on severity and intensity of services; observation understates the "
            "sepsis physiology, the AKI on CKD, and the inpatient-level monitoring required, and must not be inferred from the "
            "favorable trajectory.")

def build(which):
    draft=(which=="draft")
    base=TASK_BASE if draft else GOLDEN_BASE
    tmp=os.path.join(tempfile.gettempdir(),f"km08v3m_{which}.docx")
    d=clone(base,tmp); paras=d.paragraphs
    set_text(paras[1],"ADMISSION STATUS DETERMINATION - INPATIENT VERSUS OBSERVATION"+(" - DRAFT" if draft else ""))
    set_text(paras[2],f"Author: Elian Vossmere, MD  |  Department: Hospital Medicine  |  05/18/2026 (HD1)  |  Status: {'Draft for finalization' if draft else 'Signed'}")
    if draft:
        set_text(paras[3],"DRAFT for finalization - Korvin Merrow admission status determination, 05/18/2026 (HD1).")
        heading_like,body_like=paras[3],paras[4]; start=4
    else:
        heading_like,body_like=paras[3],paras[4]; start=3
    sig=paras[len(paras)-1]; delete_paragraphs(list(paras[start:len(paras)-1]))
    body=[(True,"Question"),(False,QUESTION),
          (True,"Presentation and course"),(False,COURSE),
          (True,"Status determination and rationale"),(False,STATUS_DRAFT if draft else STATUS_GOLD),
          (False,CLOSE_DRAFT if draft else CLOSE_GOLD)]
    for is_h,t in body: insert_before(sig,heading_like if is_h else body_like,t)
    set_text(sig,("Draft started for Elian Vossmere, MD; finalize and sign  |  Hospital Medicine, Mercy Vale Regional Medical Center" if draft
                  else "Electronically signed by Elian Vossmere, MD  |  Hospital Medicine, Mercy Vale Regional Medical Center  |  NPI 1528374960  |  05/18/2026"))
    lbl="Admission Status Determination"+(" - Draft" if draft else "")
    edit_band_cell(d,"Document",lbl,"Discharge Summary - Working Draft" if draft else "Hospital Discharge Summary")
    edit_band_cell(d,"Date","05/18/2026","05/24/2026")
    edit_band_cell(d,"Attending","Elian Vossmere, MD","E. Vossmere, MD" if draft else "Elian Vossmere, MD")
    edit_footer(d,"Discharge Summary - Working Draft" if draft else "Hospital Discharge Summary",lbl)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out=os.path.join(OUT,"admission_status_determination_draft_05182026.docx" if draft else "golden-KM08-v3.docx")
    shutil.copy(tmp,out); print(f"=== {which.upper()} ==="); verify_against_base(out,base); print("Saved:",out)

if __name__=="__main__":
    print("Building KM08 v3 MERGED inpatient-vs-observation determination..."); build("draft"); build("golden"); print("Done.")
