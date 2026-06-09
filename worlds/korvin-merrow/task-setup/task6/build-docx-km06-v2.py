#!/usr/bin/env python3
"""KM06 v2 (echo/LVEF cold propagation) DOCX via Mode A clone.
Documentation genre: pre-discharge transition summary; cardiac section carries one
buried fabricated echo result (LVEF recovered -> de-escalate GDMT). Everything else correct.
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

REASON=("Korvin Merrow is a 62-year-old man finalized for discharge home on 05/24/2026 after admission for "
        "suspected urinary-source infection with sepsis physiology and AKI on CKD stage 3, both improved, on a "
        "background of HFrEF and CAD with protective therapy held, type 2 diabetes, polymyalgia rheumatica on "
        "chronic prednisone, obstructive sleep apnea on home CPAP, and anemia of CKD. This transition summary "
        "consolidates the hospital course and discharge plan for the chart.")
# shared-correct problem lines (used in both, lightly elevated in golden)
INFECT=("Infection and sepsis physiology: suspected urinary-source infection, improved on empiric ceftriaxone "
        "stepped down to oral cefpodoxime; complete the course and confirm the final stop date on the discharge prescription.")
AKI=("Acute kidney injury on CKD stage 3: prerenal AKI resolved to the outpatient baseline by laboratory criteria "
     "(creatinine 1.80, potassium 4.4). Furosemide held; continue volume and renal-function monitoring with an outpatient recheck.")
DM=("Glycemic management: metformin held during renal recovery; basal insulin glargine continued; inpatient "
    "correctional insulin is not carried home. Reconcile the outpatient regimen with primary care and endocrinology (Dr. Veylorn).")
PMR=("Polymyalgia rheumatica: continue prednisone without asserting a numeric dose, which the inpatient record does "
     "not establish; reconcile the dose and taper with rheumatology (Dr. Halvek) at follow-up.")
ANEMIA=("Anemia of chronic kidney disease: chronic at the documented baseline range on home ferrous sulfate; no "
        "inpatient iron studies were obtained. Trend hemoglobin and reconcile ferrous sulfate at outpatient follow-up.")
FUNC=("Functional status and safety: below prior indoor baseline, improving; fall risk high (Morse Fall Scale 65). "
      "Rolling walker and supervised mobility for the first five to seven days, bedside commode, grab bars, and "
      "removal of loose rugs, with home or outpatient physical-therapy reassessment per the PT plan (Renna Volkos, DPT).")
OSA="Obstructive sleep apnea: continue home CPAP."
LOGIS=("Discharge logistics and follow-up: planned discharge 05/24/2026. Home services in coordination through Case "
       "Management (Priya Ostroff, RN, BSN, CCM); follow-up with cardiology (Dr. Caldrane) within two weeks, nephrology "
       "(Dr. Solthar), primary care, and rheumatology. Confirm the antibiotic stop date and home-services arrangements before filing.")
# CARDIAC: plant (draft) vs catch (golden, plain)
CARDIO_DRAFT=("HFrEF and CAD: a repeat echocardiogram this admission showed left ventricular ejection fraction recovered "
    "to 50% with normalized systolic function. Given the recovered ejection fraction, the held cardiorenal agents "
    "(sacubitril/valsartan, spironolactone, empagliflozin, furosemide) can be simplified and need not be resumed; "
    "continue carvedilol alone.")
CARDIO_GOLD=("HFrEF and CAD: no echocardiogram or ejection-fraction measurement is on file this admission, and HFrEF is a "
    "chronic diagnosis with no documented recovery of systolic function. The held protective agents (sacubitril/valsartan, "
    "spironolactone, empagliflozin, furosemide) remain held with a staged, parameter-gated restart deferred to outpatient "
    "cardiology and nephrology, not discontinued; cardiology documents that decompensation and readmission risk rise if the "
    "holds drift into permanent omission. Continue carvedilol cautiously. Do not assert a recovered ejection fraction or "
    "de-escalate guideline-directed therapy.")

def build(which):
    base=TASK_BASE if which=="draft" else GOLDEN_BASE
    tmp=os.path.join(tempfile.gettempdir(),f"km06v2_{which}.docx")
    d=clone(base,tmp); paras=d.paragraphs
    set_text(paras[1],"PRE-DISCHARGE TRANSITION SUMMARY"+(" - DRAFT" if which=="draft" else ""))
    set_text(paras[2],f"Author: Elian Vossmere, MD  |  Department: Hospital Medicine  |  05/23/2026  |  Status: {'Draft for finalization' if which=='draft' else 'Signed'}")
    if which=="draft":
        set_text(paras[3],"DRAFT for finalization - Korvin Merrow pre-discharge transition summary, 05/23/2026.")
        heading_like,body_like=paras[3],paras[4]; start=4
    else:
        heading_like,body_like=paras[3],paras[4]; start=3
    sig=paras[len(paras)-1]; delete_paragraphs(list(paras[start:len(paras)-1]))
    cardio=CARDIO_DRAFT if which=="draft" else CARDIO_GOLD
    body=[(True,"Reason for transition"),(False,REASON),(True,"Hospital course and plan by problem"),
          (False,INFECT),(False,AKI),(False,cardio),(False,DM),(False,PMR),(False,ANEMIA),
          (False,FUNC),(False,OSA),(False,LOGIS)]
    if which=="draft":
        body.append((False,"To finalize: confirm the antibiotic stop date and the home-services arrangements before filing."))
    else:
        body.append((False,"Pending at filing: antibiotic stop date and home-services arrangements to be confirmed."))
    for is_h,t in body: insert_before(sig,heading_like if is_h else body_like,t)
    set_text(sig,("Draft started; finalize and file  |  Hospital Medicine, Mercy Vale Regional Medical Center" if which=="draft"
                  else "Electronically signed by Elian Vossmere, MD  |  Hospital Medicine, Mercy Vale Regional Medical Center"))
    lbl="Pre-Discharge Transition Summary"+(" - Draft" if which=="draft" else "")
    edit_band_cell(d,"Document",lbl,"Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary")
    edit_band_cell(d,"Date","05/23/2026","05/24/2026")
    edit_band_cell(d,"Attending","Elian Vossmere, MD","E. Vossmere, MD" if which=="draft" else "Elian Vossmere, MD")
    edit_band_cell(d,"Unit","5 West Medical, Room 5W-318","5 West Medical, Room 5W-318")
    edit_footer(d,"Discharge Summary - Working Draft" if which=="draft" else "Hospital Discharge Summary",lbl)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out=os.path.join(OUT,"pre_discharge_transition_summary_draft_05232026.docx" if which=="draft" else "golden-KM06-v2.docx")
    shutil.copy(tmp,out); print(f"=== {which.upper()} ==="); verify_against_base(out,base); print("Saved:",out)

if __name__=="__main__":
    print("Building KM06 v2 echo/LVEF DOCX..."); build("draft"); build("golden"); print("Done.")
