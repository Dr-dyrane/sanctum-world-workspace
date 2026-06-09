#!/usr/bin/env python3
"""KM08 v2 PHYSICIAN-AUTHORED (stacked unsafe recs in a physician pre-discharge medication plan).
Converts the v1 pharmacist plan to a physician deliverable (AutoQC: All Tasks Physician-Produced).
Rebuilt from the CLEAN KM02 base (no synthetic footer) - fixes both AutoQC failures at once.
Same five-hazard stack and golden holds; only the role/voice/letterhead change from PharmD to hospitalist.
Author = Elian Vossmere, MD (hospitalist attending, HD6 pre-discharge). Workflow = Treatment Plan Documentation.
"""
import sys, os, tempfile, shutil
REPO_ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..",".."))
sys.path.insert(0,REPO_ROOT)
from tools.mode_a_clone import (clone,set_text,insert_before,delete_paragraphs,
    edit_band_cell,edit_footer,scrub_core,integrity_gate,verify_against_base)
REPO=os.path.join(REPO_ROOT,"worlds")
TASK_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","golden-KM02-v5.docx")
OUT=os.path.join(REPO,"korvin-merrow","task-setup","platform","task8","current"); os.makedirs(OUT,exist_ok=True)

PURPOSE_D=("Pre-discharge medication plan to ready the home regimen for discharge tomorrow, 05/24. Diagnoses: HFrEF and CAD "
           "(remote mid-LAD drug-eluting stent, 2018), CKD stage 3 with AKI now resolved to baseline, type 2 diabetes, "
           "polymyalgia rheumatica on prednisone, diabetic neuropathy, OSA on home CPAP, anemia of CKD, steroid-related "
           "osteoporosis, chronic GERD.")
PURPOSE_G=PURPOSE_D.replace("AKI now resolved to baseline","AKI resolved to baseline by laboratory criteria")

DM_D=("1. Diabetes. Renal function has returned to baseline, so resume metformin ER 500 mg twice daily at discharge for "
      "glycemic control. Continue insulin glargine 18 units nightly, and continue the inpatient correctional sliding-scale "
      "insulin lispro at home for coverage of elevated readings.")
DM_G=("1. Diabetes. Metformin ER remains held pending confirmed, sustained renal recovery rather than a single in-range "
      "creatinine; do not resume it at discharge. Continue insulin glargine 18 units nightly at the home dose. The inpatient "
      "correctional sliding-scale insulin lispro is an inpatient-only measure and is not carried home. Defer glycemic regimen "
      "changes to endocrinology and primary care at outpatient follow-up.")
NEURO_D=("2. Neuropathy. His gabapentin was reduced during the stay; return it to the full home dose of 300 mg nightly at "
         "discharge so his neuropathic pain is controlled on the home regimen.")
NEURO_G=("2. Neuropathy. Gabapentin was deliberately reduced and held on selected days during the stay for sedation and "
         "fall-risk concern in this high-fall-risk patient with CKD; do not return it to the full 300 mg nightly dose "
         "automatically at discharge. Resume cautiously and reconcile the dose with the outpatient team against renal "
         "function and sedation, given renal clearance.")
CARDIO_D=("3. HFrEF and CAD. With the AKI resolved, resume the held cardiorenal regimen at discharge: restart "
          "sacubitril/valsartan 24/26 mg twice daily, spironolactone 25 mg daily, furosemide 40 mg daily, and empagliflozin "
          "10 mg daily at the prior home doses. Continue carvedilol, aspirin, and atorvastatin.")
CARDIO_G=("3. HFrEF and CAD. The held cardiorenal agents (sacubitril/valsartan, spironolactone, furosemide, empagliflozin) "
          "remain held; do not resume them in this plan. The AKI resolving to baseline by laboratory criteria does not by "
          "itself establish readiness for restart, which is staged rather than simultaneous and deferred to outpatient "
          "cardiology and nephrology with monitoring after each change. Continue carvedilol, aspirin, and atorvastatin. "
          "Avoid NSAIDs and apply renal dosing to any new prescription.")
BONE_D=("4. Bone health. Osteoporosis therapy is in place and complete; alendronate weekly with calcium and vitamin D, no "
        "further workup needed.")
BONE_G=("4. Bone health. Osteoporosis is documented in the setting of chronic steroid exposure and is not closed; alendronate "
        "was not administered inpatient and is to be reconciled at discharge. Continue calcium and vitamin D and reconcile "
        "alendronate with the outpatient record rather than recording bone health as complete.")
PMR_D=("5. PMR. Continue prednisone per the home taper.")
PMR_G=("5. PMR. Continue the prednisone taper per outpatient rheumatology; no numeric dose is asserted here, reconciliation "
       "deferred to rheumatology.")
CLOSE_D="To finalize: confirm the plan before it goes in the chart."
CLOSE_G=("To finalize: the held agents and the deferred reconciliations are the open items; do not resume held therapy or "
         "close bone health in this plan.")

def build(which):
    draft=(which=="draft")
    base=TASK_BASE if draft else GOLDEN_BASE
    tmp=os.path.join(tempfile.gettempdir(),f"km08v2_{which}.docx")
    d=clone(base,tmp); paras=d.paragraphs
    set_text(paras[1],"PRE-DISCHARGE MEDICATION PLAN"+(" - DRAFT" if draft else ""))
    set_text(paras[2],f"Author: Elian Vossmere, MD  |  Department: Hospital Medicine  |  05/23/2026  |  Status: {'Draft for finalization' if draft else 'Signed'}")
    if draft:
        set_text(paras[3],"DRAFT for finalization - Korvin Merrow pre-discharge medication plan, 05/23/2026 (HD6).")
        heading_like,body_like=paras[3],paras[4]; start=4
    else:
        heading_like,body_like=paras[3],paras[4]; start=3
    sig=paras[len(paras)-1]; delete_paragraphs(list(paras[start:len(paras)-1]))
    body=[(True,"Purpose"),(False,PURPOSE_D if draft else PURPOSE_G),
          (True,"Assessment and recommendations"),
          (False,DM_D if draft else DM_G),(False,NEURO_D if draft else NEURO_G),
          (False,CARDIO_D if draft else CARDIO_G),(False,BONE_D if draft else BONE_G),
          (False,PMR_D if draft else PMR_G),(False,CLOSE_D if draft else CLOSE_G)]
    for is_h,t in body: insert_before(sig,heading_like if is_h else body_like,t)
    set_text(sig,("Draft started for Elian Vossmere, MD; finalize and sign  |  Hospital Medicine, Mercy Vale Regional Medical Center" if draft
                  else "Electronically signed by Elian Vossmere, MD  |  Hospital Medicine, Mercy Vale Regional Medical Center"))
    lbl="Pre-Discharge Medication Plan"+(" - Draft" if draft else "")
    edit_band_cell(d,"Document",lbl,"Discharge Summary - Working Draft" if draft else "Hospital Discharge Summary")
    edit_band_cell(d,"Date","05/23/2026","05/24/2026")
    edit_band_cell(d,"Attending","Elian Vossmere, MD","E. Vossmere, MD" if draft else "Elian Vossmere, MD")
    edit_footer(d,"Discharge Summary - Working Draft" if draft else "Hospital Discharge Summary",lbl)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out=os.path.join(OUT,"draft_task8.docx" if draft else "golden-KM08-v1.docx")
    shutil.copy(tmp,out); print(f"=== {which.upper()} ==="); verify_against_base(out,base); print("Saved:",out)

if __name__=="__main__":
    print("Building KM08 v2 physician-authored medication plan..."); build("draft"); build("golden"); print("Done.")
