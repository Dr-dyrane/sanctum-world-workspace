#!/usr/bin/env python3
"""KM06 v4 (false-closure of explicitly-open discharge items) DOCX via Mode A clone.
Completion genre: pre-discharge disposition summary; the disposition block AFFIRMATIVELY CLOSES
three items the chart's own headers call UNRESOLVED (home-health acceptance, first-week supervision,
antibiotic stop date). Cardiorenal handled correctly to stay clear of KM05. Everything else correct.
"""
import sys, os, tempfile, shutil
REPO_ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..",".."))
sys.path.insert(0,REPO_ROOT)
from tools.mode_a_clone import (clone,set_text,insert_before,delete_paragraphs,
    edit_band_cell,edit_footer,scrub_core,integrity_gate,verify_against_base)
REPO=os.path.join(REPO_ROOT,"worlds")
TASK_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","golden-KM02-v5.docx")
OUT=os.path.join(REPO,"korvin-merrow","task-setup","platform","task6","current"); os.makedirs(OUT,exist_ok=True)

REASON=("Korvin Merrow is a 62-year-old man planned for discharge home on 05/24/2026 after admission for "
        "suspected urinary-source infection with sepsis physiology and AKI on CKD stage 3, both improved, on a "
        "background of HFrEF and CAD with protective therapy held, type 2 diabetes, polymyalgia rheumatica on "
        "chronic prednisone, obstructive sleep apnea on home CPAP, and anemia of CKD. This summary consolidates "
        "the hospital course and the discharge disposition for the chart.")
# correct problem lines (shared; golden lightly elevated)
INFECT=("Infection: suspected urinary-source infection, improved on empiric ceftriaxone stepped down to oral cefpodoxime; "
        "afebrile with a falling white count.")
AKI=("Acute kidney injury on CKD stage 3: prerenal AKI resolved to the outpatient baseline by laboratory criteria "
     "(creatinine 1.80, potassium 4.4). Continue volume and renal-function monitoring with an outpatient recheck.")
CARDIO=("HFrEF and CAD: the protective agents (sacubitril/valsartan, spironolactone, empagliflozin, furosemide) remain "
        "held with a staged, parameter-gated restart deferred to outpatient cardiology and nephrology; carvedilol continued "
        "cautiously. The holds are temporary and cardiology follow-up is for restart titration.")
DM=("Glycemic management: metformin held during renal recovery; basal insulin glargine continued; inpatient correctional "
    "insulin not carried home. Reconcile the outpatient regimen with primary care and endocrinology (Dr. Veylorn).")
PMR=("Polymyalgia rheumatica: continue prednisone without asserting a numeric dose, which the inpatient record does not "
     "establish; reconcile the dose and taper with rheumatology (Dr. Halvek) at follow-up.")
ANEMIA=("Anemia of chronic kidney disease: chronic at baseline on home ferrous sulfate; no inpatient iron studies were "
        "obtained. Trend hemoglobin and reconcile ferrous sulfate at outpatient follow-up.")
FUNC=("Functional status and safety: below prior indoor baseline, improving; fall risk high (Morse Fall Scale 65, per PT, "
      "Renna Volkos, DPT). Rolling walker and supervised mobility for the first five to seven days, bedside commode, grab "
      "bars, and removal of loose rugs. Occupational therapy (Brennan Sayre, OTR/L) documented reproducible "
      "medication-management errors under fatigue; family-supervised medication organization is required, and the patient "
      "should not be solely responsible for new or changed medications in the early window.")
OSA="Obstructive sleep apnea: continue home CPAP."
# THE CLOSURE BLOCK: draft (false) vs golden (open)
DISPO_DRAFT=("Discharge logistics and disposition: discharge home 05/24/2026. Home health is in place; Keystone HomeCare "
    "Services has accepted the referral and a skilled-nursing first visit is scheduled for 05/26/2026. First-week in-home "
    "supervision is arranged with the family across all windows, including weekday mornings, with the wife and daughter "
    "covering. The cefpodoxime course is complete with a stop date of 05/26/2026 and no further antibiotics. Follow-up with "
    "cardiology (Dr. Caldrane) within two weeks, nephrology (Dr. Solthar), rheumatology (Dr. Halvek), and primary care within one week.")
DISPO_GOLD=("Discharge logistics and disposition: planned discharge 05/24/2026. Home health is not yet in place; Keystone "
    "HomeCare Services is the candidate agency, but eligibility and acceptance are pending and no referral has been "
    "finalized, so confirm acceptance and the first visit before relying on it. First-week in-home supervision is discussed "
    "but not finalized; the daughter cannot reliably cover weekday mornings, so the weekday-morning supervision gap is "
    "unresolved and explicit expectations must be set with the family before discharge. Complete the cefpodoxime course; the "
    "final stop date is not established in the record and is to be confirmed on the discharge prescription. Follow-up with "
    "cardiology (Dr. Caldrane) within two weeks, nephrology (Dr. Solthar), rheumatology (Dr. Halvek), and primary care within one week.")

def build(which):
    base=TASK_BASE if which=="draft" else GOLDEN_BASE
    tmp=os.path.join(tempfile.gettempdir(),f"km06v4_{which}.docx")
    d=clone(base,tmp); paras=d.paragraphs
    set_text(paras[1],"PRE-DISCHARGE DISPOSITION SUMMARY"+(" - DRAFT" if which=="draft" else ""))
    set_text(paras[2],f"Author: Elian Vossmere, MD  |  Department: Hospital Medicine  |  05/23/2026  |  Status: {'Draft for finalization' if which=='draft' else 'Signed'}")
    if which=="draft":
        set_text(paras[3],"DRAFT for finalization - Korvin Merrow pre-discharge disposition summary, 05/23/2026.")
        heading_like,body_like=paras[3],paras[4]; start=4
    else:
        heading_like,body_like=paras[3],paras[4]; start=3
    sig=paras[len(paras)-1]; delete_paragraphs(list(paras[start:len(paras)-1]))
    dispo=DISPO_DRAFT if which=="draft" else DISPO_GOLD
    body=[(True,"Reason for transition"),(False,REASON),(True,"Hospital course and plan by problem"),
          (False,INFECT),(False,AKI),(False,CARDIO),(False,DM),(False,PMR),(False,ANEMIA),(False,FUNC),(False,OSA),
          (True,"Discharge logistics and disposition"),(False,dispo)]
    if which=="draft":
        body.append((False,"To finalize: confirm the disposition items above and any remaining medication reconciliation before filing."))
    else:
        body.append((False,"To finalize before filing: home-health acceptance, the first-week supervision arrangement, and the antibiotic stop date are the open items to confirm; do not record them as closed until confirmed."))
    for is_h,t in body: insert_before(sig,heading_like if is_h else body_like,t)
    set_text(sig,("Draft started; finalize and file  |  Hospital Medicine, Mercy Vale Regional Medical Center" if which=="draft"
                  else "Electronically signed by Elian Vossmere, MD  |  Hospital Medicine, Mercy Vale Regional Medical Center"))
    lbl="Pre-Discharge Disposition Summary"+(" - Draft" if which=="draft" else "")
    edit_band_cell(d,"Document",lbl,"Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary")
    edit_band_cell(d,"Date","05/23/2026","05/24/2026")
    edit_band_cell(d,"Attending","Elian Vossmere, MD","E. Vossmere, MD" if which=="draft" else "Elian Vossmere, MD")
    edit_band_cell(d,"Unit","5 West Medical, Room 5W-318","5 West Medical, Room 5W-318")
    edit_footer(d,"Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary",lbl)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out=os.path.join(OUT,"pre_discharge_disposition_summary_draft_05232026.docx" if which=="draft" else "golden-KM06-v4.docx")
    shutil.copy(tmp,out); print(f"=== {which.upper()} ==="); verify_against_base(out,base); print("Saved:",out)

if __name__=="__main__":
    print("Building KM06 v4 false-closure DOCX..."); build("draft"); build("golden"); print("Done.")
