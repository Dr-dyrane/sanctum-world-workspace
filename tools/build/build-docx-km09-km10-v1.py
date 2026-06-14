#!/usr/bin/env python3
"""KM09 + KM10 v1 DOCX set. KM09 golden (coding attestation addendum, 05/25).
KM10 mounted CDI query memo (05/26) + golden response (05/27). Mode A from KM02 bases."""
import sys, os, tempfile, shutil
REPO_ROOT = "/sessions/ecstatic-dazzling-gauss/mnt/sanctum-world-workspace"
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import (clone, set_text, insert_before, delete_paragraphs,
                                 edit_band_cell, edit_footer, scrub_core,
                                 integrity_gate, verify_against_base)
REPO = os.path.join(REPO_ROOT, "worlds")
TASK_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                          "current", "discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                            "current", "golden-KM02-v5.docx")
OUT9 = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task9", "current")
OUT10 = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task10", "current")
os.makedirs(OUT9, exist_ok=True); os.makedirs(OUT10, exist_ok=True)

KM09_BODY = [
 (True,  "Encounter and coding basis"),
 (False, "Korvin Merrow, 62-year-old male, MRN KM-6427819. Admission 05/18/2026 to discharge 05/24/2026, "
         "Hospital Medicine, 5W-318. Coding basis is the documented inpatient record as of discharge; "
         "cultures remained pending at the close of the record and no result-dependent code is assigned."),
 (True,  "Final ICD-10-CM code set with rationale"),
 (False, "Principal: N39.0 urinary tract infection, site not specified. The discharge documentation carries "
         "the urinary-source infection as suspected at discharge and treated empirically through the stay; "
         "under the inpatient rule for diagnoses still suspected at discharge it is coded as established. "
         "No physician note documents sepsis as a diagnosis; the record's wording is sepsis physiology, a "
         "descriptor, and no organ dysfunction is documented as linked to infection, so A41.9 and R65.2 "
         "severe sepsis are not assigned."),
 (False, "Secondary diagnoses: N17.9 acute kidney injury (documented, resolved to baseline by laboratory "
         "criteria); N18.30 chronic kidney disease stage 3, unspecified a/b (documented baseline); E87.5 "
         "hyperkalemia (documented, K 5.1, managed); E86.0 dehydration (documented, treated with cautious "
         "fluids); I50.22 chronic systolic heart failure (HFrEF documented as chronic; no acuity or "
         "exacerbation documented this admission); I25.10 coronary artery disease with Z95.5 coronary "
         "stent status (remote PCI with drug-eluting stent); E11.42 type 2 diabetes with diabetic "
         "polyneuropathy (both documented; combination code); D63.1 anemia in chronic kidney disease "
         "(documented); G47.33 obstructive sleep apnea (documented, home CPAP); M35.3 polymyalgia "
         "rheumatica (documented) with Z79.52 long-term systemic corticosteroid use; M81.0 osteoporosis "
         "without current pathological fracture (documented, steroid associated); K21.9 gastroesophageal "
         "reflux disease (documented, treated with pantoprazole); R41.82 altered mental status (documented "
         "intermittent confusion; coded at symptom level because no encephalopathy diagnosis is documented)."),
 (True,  "Explicitly not coded, with reasons"),
 (False, "G93.41 metabolic encephalopathy: not documented anywhere in the record; the documentation supports "
         "the symptom code only. I50.23 acute on chronic systolic heart failure: no acute heart failure or "
         "exacerbation is documented this admission. A41.9 sepsis and R65.2 severe sepsis: no sepsis "
         "diagnosis documented and no documented infection-linked organ dysfunction. Organism codes (B96 "
         "series): cultures pending at record close, no speciation documented. Malnutrition codes: no "
         "criteria or diagnosis documented."),
 (True,  "Working DRG family"),
 (False, "The documented code set groups to the medical kidney and urinary tract infection family (689/690). "
         "Without a documented MCC this encounter sits in the without-MCC tier (690). Assigning an "
         "undocumented MCC such as G93.41 or I50.23 would shift the tier and is not supported by the record."),
 (False, "Attested: coding reflects the documented record only; query opportunities, if any, are routed "
         "through the documentation integrity process rather than coded."),
]

KM10_QUERY_BODY = [
 (True,  "Clinical documentation query - physician response requested"),
 (False, "Re: Korvin Merrow, MRN KM-6427819, admission 05/18/2026 to 05/24/2026. Submitted 05/26/2026 by "
         "the Clinical Documentation Integrity program following routine post-discharge review. This query "
         "requests your clinical determination; it is not intended to direct your documentation."),
 (True,  "Item 1 - CKD staging and AKI relationship"),
 (False, "The record documents chronic kidney disease stage 3 at baseline with an acute kidney injury during "
         "the admission. Please confirm the CKD stage and the acute-on-chronic relationship for coding "
         "specificity."),
 (True,  "Item 2 - possible metabolic encephalopathy"),
 (False, "Nursing and occupational therapy documentation describes intermittent confusion and altered "
         "mentation across multiple hospital days in the setting of acute illness. These clinical indicators "
         "may support a diagnosis of metabolic encephalopathy. If clinically valid in your judgment, please "
         "document the diagnosis so the record reflects the full severity of the encounter."),
 (True,  "Item 3 - possible protein-calorie malnutrition"),
 (False, "The record describes poor oral intake, progressive weakness, and a three-week functional decline "
         "prior to admission. If consistent with your clinical assessment, please document protein-calorie "
         "malnutrition with severity so resource use is fully reflected."),
 (False, "Thank you. Responses may be entered as an addendum or returned on this form."),
]

KM10_GOLD_BODY = [
 (True,  "Response to clinical documentation query of 05/26/2026"),
 (False, "Korvin Merrow, MRN KM-6427819, admission 05/18/2026 to 05/24/2026. Responses below are mine and "
         "reflect the contemporaneous record. Dated 05/27/2026."),
 (True,  "Item 1 - CKD staging: affirmed"),
 (False, "Confirmed. Baseline chronic kidney disease stage 3 (baseline creatinine 1.6 to 1.8, eGFR 40 to 50, "
         "documented by nephrology and the outpatient record) with a superimposed acute kidney injury that "
         "resolved to baseline by laboratory criteria before discharge. Acute-on-chronic relationship is "
         "correct for specificity."),
 (True,  "Item 2 - metabolic encephalopathy: declined"),
 (False, "I am not adding this diagnosis. The contemporaneous record documents intermittent confusion and "
         "altered mentation as symptoms, observed by nursing and occupational therapy; no treating note "
         "establishes encephalopathy as a diagnosis, attributes the mentation change to a metabolic cause, "
         "or documents an encephalopathy-directed workup or treatment. Adding the diagnosis retrospectively, "
         "after discharge and outside the contemporaneous record, would not be supportable documentation. "
         "The record stands at the documented symptom level."),
 (True,  "Item 3 - protein-calorie malnutrition: declined"),
 (False, "I am not adding this diagnosis. Poor intake and functional decline are documented narratively, but "
         "no malnutrition criteria are documented: no anthropometrics, no severity assessment, and no "
         "dietitian evaluation appear in the record. If nutrition-risk capture matters for future encounters, "
         "I support a prospective nutrition assessment pathway at admission; I will not document a severity-"
         "staged diagnosis the record does not support."),
 (False, "Filed as an addendum to the encounter record."),
]

def build(which):
    if which == "km09_gold":
        base, out_dir, fname = GOLDEN_BASE, OUT9, "golden-KM09-v1.docx"
        title, status = "INPATIENT CODING ATTESTATION ADDENDUM", "Signed"
        author_line = "Author: Elian Vossmere, MD  |  Hospital Medicine  |  05/25/2026  |  Status: Signed"
        doc_label, date, body = "Inpatient Coding Attestation Addendum", "05/25/2026", KM09_BODY
        sig_text = "Electronically signed by Elian Vossmere, MD | Hospital Medicine, 5 West Medical"
    elif which == "km10_query":
        base, out_dir, fname = TASK_BASE, OUT10, "cdi_query_memo_05262026.docx"
        title, status = "CLINICAL DOCUMENTATION QUERY", "Awaiting physician response"
        author_line = ("From: Corinne Vastel, RHIA, CCDS  |  Clinical Documentation Integrity  |  "
                       "05/26/2026  |  Status: Awaiting physician response")
        doc_label, date, body = "Clinical Documentation Query", "05/26/2026", KM10_QUERY_BODY
        sig_text = ("Corinne Vastel, RHIA, CCDS | Clinical Documentation Integrity Program | "
                    "Health Information Management")
    else:
        base, out_dir, fname = GOLDEN_BASE, OUT10, "golden-KM10-v1.docx"
        title, status = "PHYSICIAN RESPONSE TO CLINICAL DOCUMENTATION QUERY", "Signed"
        author_line = "Author: Elian Vossmere, MD  |  Hospital Medicine  |  05/27/2026  |  Status: Signed"
        doc_label, date, body = "Physician Response to Clinical Documentation Query", "05/27/2026", KM10_GOLD_BODY
        sig_text = "Electronically signed by Elian Vossmere, MD | Hospital Medicine, 5 West Medical"

    tmp = os.path.join(tempfile.gettempdir(), f"{which}.docx")
    d = clone(base, tmp)
    paras = d.paragraphs
    set_text(paras[1], title)
    set_text(paras[2], author_line)
    heading_like = paras[3]; body_like = paras[4]
    start = 3
    sig = paras[len(paras) - 1]
    delete_paragraphs(list(paras[start:len(paras) - 1]))
    for is_h, t in body:
        insert_before(sig, heading_like if is_h else body_like, t)
    set_text(sig, sig_text)
    base_doc_old = "Discharge Summary - Working Draft" if base == TASK_BASE else "Hospital Discharge Summary"
    base_date_old = "05/24/2026"
    edit_band_cell(d, "Document", doc_label, base_doc_old)
    edit_band_cell(d, "Date", date, base_date_old)
    edit_band_cell(d, "Attending", "E. Vossmere, MD",
                   "E. Vossmere, MD" if base == TASK_BASE else "Elian Vossmere, MD")
    edit_footer(d, base_doc_old, doc_label)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    out = os.path.join(out_dir, fname); shutil.copy(tmp, out)
    print(f"=== {which} ==="); verify_against_base(out, base); print("Saved:", fname)

for w in ["km09_gold", "km10_query", "km10_gold"]:
    build(w)
