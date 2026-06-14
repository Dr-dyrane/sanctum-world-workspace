#!/usr/bin/env python3
"""KM07 v1 REFERRAL (nephrology referral letter; frame the cardiorenal restart as the OPEN staged question)."""
import sys, os, tempfile, shutil
REPO_ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..",".."))
sys.path.insert(0,REPO_ROOT)
from tools.mode_a_clone import (clone,set_text,insert_before,delete_paragraphs,
    edit_band_cell,edit_footer,scrub_core,integrity_gate,verify_against_base)
REPO=os.path.join(REPO_ROOT,"worlds")
GOLDEN_BASE=os.path.join(REPO,"korvin-merrow","task-setup","platform","task2","current","golden-KM02-v5.docx")
OUT=os.path.join(REPO,"korvin-merrow","task-setup","platform","task7","current"); os.makedirs(OUT,exist_ok=True)

REASON=("Dear Dr. Solthar, I am referring Korvin Merrow, a 62-year-old man with CKD stage 3, for outpatient nephrology "
        "follow-up after his 05/18 to 05/24/2026 hospitalization for a suspected urinary-source infection with sepsis "
        "physiology and AKI on CKD. I would value your continued involvement in monitoring his renal recovery and, in "
        "particular, in leading the staged reintroduction of the renal- and hemodynamic-sensitive medications that were "
        "held during the admission.")
COURSE=("His outpatient baseline creatinine is 1.6 to 1.8 mg/dL with an eGFR in the 40 to 50 range. Admission creatinine "
        "peaked at 2.62 mg/dL with a multifactorial, predominantly prerenal AKI from poor intake and infection-related "
        "hemodynamics. Sacubitril/valsartan, spironolactone, metformin, and empagliflozin were held during the admission, "
        "and furosemide was held for prerenal physiology; aspirin, atorvastatin, and a cautious dose of carvedilol were "
        "continued. By discharge his creatinine had returned to 1.80 mg/dL, at the upper end of his outpatient baseline, "
        "and the AKI had resolved by laboratory criteria.")
RESTART=("I want to be clear that this laboratory resolution is not the same as restored physiologic reserve, and it does "
         "not by itself establish that he is ready to resume his held cardiorenal and diabetes agents. Your inpatient "
         "assessment framed the restart as a staged, parameter-gated sequencing problem to be guided by the pace of renal "
         "recovery and blood pressure reserve rather than by a single favorable creatinine, and coordinated with cardiology "
         "rather than undertaken simultaneously. I am referring that open sequencing decision to you to drive: which agent "
         "is reintroduced first, against which parameters, and on what monitoring schedule, in coordination with his "
         "cardiologist Dr. Caldrane. None of the held agents has been restarted at this visit.")
REQUESTS=("I would be grateful if he could be seen within one to two weeks of discharge, sooner if any restart is initiated "
          "near discharge. In the interim I am continuing to avoid NSAIDs and applying renal dosing to any new prescription, "
          "and I will share interval metabolic panels. Please advise on the restart sequence and the laboratory and "
          "blood-pressure thresholds you want met before each step.")
CLOSING=("Thank you for your continued co-management of his renal care. Please contact me with any questions.")

def build():
    base=GOLDEN_BASE
    tmp=os.path.join(tempfile.gettempdir(),"km07ref_golden.docx")
    d=clone(base,tmp); paras=d.paragraphs
    set_text(paras[1],"REFERRAL TO NEPHROLOGY")
    set_text(paras[2],"From: Talia Quenor, MD, Primary Care  |  To: Iven Solthar, MD, Nephrology  |  06/23/2026  |  Status: Signed")
    heading_like,body_like=paras[3],paras[4]; start=3
    sig=paras[len(paras)-1]; delete_paragraphs(list(paras[start:len(paras)-1]))
    body=[(True,"Reason for referral"),(False,REASON),
          (True,"Hospital course"),(False,COURSE),
          (True,"Restart sequencing, the open question"),(False,RESTART),
          (True,"Requests and follow-up"),(False,REQUESTS),
          (False,CLOSING)]
    for is_h,t in body: insert_before(sig,heading_like if is_h else body_like,t)
    set_text(sig,"Electronically signed by Talia Quenor, MD  |  Primary Care, Mercy Vale Primary Care, Harbor Crest Clinic")
    lbl="Referral to Nephrology"
    edit_band_cell(d,"Document",lbl,"Hospital Discharge Summary")
    edit_band_cell(d,"Date","06/23/2026","05/24/2026")
    edit_band_cell(d,"Attending","Talia Quenor, MD","Elian Vossmere, MD")
    edit_band_cell(d,"Unit","Harbor Crest Clinic","5 West Medical, Room 5W-318")
    edit_band_cell(d,"Service","Primary Care","Hospital Medicine")
    edit_footer(d,"Hospital Discharge Summary",lbl)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out=os.path.join(OUT,"golden-KM07-v1.docx")
    shutil.copy(tmp,out); print("=== GOLDEN ==="); verify_against_base(out,base); print("Saved:",out)

if __name__=="__main__":
    print("Building KM07 v1 nephrology referral letter (golden only)..."); build(); print("Done.")
