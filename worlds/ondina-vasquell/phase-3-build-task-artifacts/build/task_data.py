#!/usr/bin/env python3
"""Task-level reference files (E1-T*) - SEPARATE from world files.

These are the severity-forward external surfaces and same-author drafts the tasks
must rebut or complete. Each is plausible but rebuttable from the chart and NEVER
pre-answers its task: external docs carry a wrong-by-genre claim; the started draft
(E1-T10) leaves a true placeholder; the unreconciled order set (E1-T1) presents the
specific discrepancies and leaves the conclusion open. These are reference artifacts,
not prompts/goldens/graders (those are writer-authored).

No banned characters. Synthetic external issuers (logged in DERIVED_ISSUERS).
"""
from clinical_data import PT, ROSTER, ENC

DERIVED_ISSUERS = [
    ("MA plan", "Meridian Advantage Health Plan", "synthetic Medicare Advantage payer"),
    ("PBM", "CoreScript Pharmacy Benefits", "synthetic pharmacy benefit manager"),
    ("HIM coder", ROSTER["attending"], "HIM lead Corwin Adeyle, RHIA, CCS (ratified roster)"),
]

RE = f"RE: {PT['name']} | MRN {PT['mrn']} | {ENC['csn']}"


def T1():
    R = ROSTER
    return ("preliminary_discharge_order_set_05212026.docx", "mar", [
        ("title", "PRELIMINARY DISCHARGE ORDER SET (DRAFT - NOT RECONCILED)"),
        ("filing", f"Generated 05/21/2026 1800 | Status: Draft, pending reconciliation | {RE}"),
        ("body", "Auto-populated draft discharge orders carried forward from active inpatient orders. Not yet reconciled against home medications or current renal function."),
        ("section", "MEDICATIONS CARRIED FORWARD"),
        ("table", [
            ["Medication", "Dose / Route / Frequency", "Note on draft"],
            ["Piperacillin-tazobactam", "2.25 g Intravenous every 8 hours", "Admission empiric dose carried forward; oral step-down and duration not set"],
            ["Insulin glargine", "Inpatient-adjusted units Subcutaneous nightly", "Reconcile to home 26 units versus inpatient adjustment"],
            ["Insulin aspart", "Sliding scale Subcutaneous with meals", "Continue"],
            ["Furosemide", "20 mg Oral daily", "Continue"],
            ["Atorvastatin", "40 mg Oral nightly", "Continue"],
            ["Aspirin", "81 mg Oral daily", "Continue"],
            ["Clopidogrel", "75 mg Oral daily", "Continue"],
            ["Gabapentin", "300 mg Oral three times daily", "Continue; renal check"],
            ["Pantoprazole", "40 mg Oral daily", "Continue"],
            ["Acetaminophen", "650 mg Oral three times daily as needed", "Continue"],
            ["Metformin", "500 mg Oral twice daily", "Status ambiguous: held inpatient, not marked resume or continue-hold"],
            ["Empagliflozin", "10 mg Oral daily", "Status ambiguous: held inpatient, not marked resume or continue-hold"],
            ["Lisinopril", "20 mg Oral daily", "Status ambiguous: held inpatient, not marked resume or continue-hold"],
        ]),
        ("body", "This draft has not been reconciled. The intravenous antibiotic line, the held oral agents, and the insulin dose require clinician reconciliation before discharge. No reconciliation decision is recorded here."),
        ("sig", "System-generated preliminary order set"),
    ])


def T2():
    return ("him_preliminary_coding_worksheet_05212026.docx", "mar", [
        ("title", "HEALTH INFORMATION MANAGEMENT - PRELIMINARY CODING WORKSHEET"),
        ("filing", "Author: Corwin Adeyle, RHIA, CCS - HIM Coding | Date: 05/21/2026 | Status: Draft for provider attestation | " + RE),
        ("body", "Preliminary code assignment for provider review and attestation. Please confirm or correct."),
        ("section", "PROPOSED DIAGNOSES"),
        ("table", [
            ["Code family", "Proposed", "Basis stated by coder"],
            ["Pressure injury / ulcer (L89 family)", "Proposed as principal wound code", "Foot ulcer noted on chart"],
            ["Acute osteomyelitis", "Proposed present on admission (Y)", "MRI mentions marrow edema"],
            ["Diabetes with complication", "Proposed secondary", "Diabetic patient"],
            ["Acute kidney injury", "Proposed secondary", "Creatinine elevation on admission"],
        ]),
        ("body", "Please attest to the proposed codes. If a code does not reflect the documentation, correct it and provide the supporting basis."),
        ("sig", "HIM Coding - awaiting provider attestation"),
    ])


def T3():
    return ("cdi_query_memo_05232026.docx", "mar", [
        ("title", "CLINICAL DOCUMENTATION INTEGRITY QUERY"),
        ("filing", "Author: Bristol Ndiaye, RN, CCDS - CDI | Date: 05/23/2026 | Status: Open query | " + RE),
        ("section", "QUERY"),
        ("body", "The MRI of the left foot dated 05/18/2026 describes marrow edema in the metatarsal heads. To support severity of illness, please document whether the patient has acute osteomyelitis. If yes, please specify acute osteomyelitis and the site."),
        ("section", "RESPONSE OPTIONS"),
        ("bullets", [
            "Acute osteomyelitis, specify site",
            "Other diagnosis (please specify)",
            "Clinically undetermined / unable to determine",
        ]),
        ("body", "Please respond based on the complete clinical picture and the documentation in the record."),
        ("sig", "CDI - open query awaiting provider response"),
    ])


def T4():
    return ("medicare_advantage_denial_letter_05232026.docx", "primarycare", [
        ("title", "MERIDIAN ADVANTAGE HEALTH PLAN - NOTICE OF DENIAL"),
        ("filing", "Utilization Management | Medical Director: Ellery Stovall, MD | Date: 05/23/2026 | " + RE),
        ("section", "DETERMINATION"),
        ("body", "We have reviewed the request for skilled nursing facility placement. Based on the records provided, the member is afebrile, the white blood cell count has normalized, and the member is taking oral intake. We have determined that the member's needs can be met at home and that skilled nursing facility placement is not authorized at this time."),
        ("section", "APPEAL RIGHTS"),
        ("body", "If you disagree with this determination, you may appeal and submit additional clinical information supporting the requested level of care."),
        ("sig", "Meridian Advantage Health Plan, Utilization Management"),
    ])


def T5():
    return ("pharmacy_benefit_rejection_05242026.docx", "primarycare", [
        ("title", "CORESCRIPT PHARMACY BENEFITS - CLAIM REJECTION"),
        ("filing", "Pharmacy Benefit Manager | Date: 05/24/2026 | Status: Rejected, substitution offered | " + RE),
        ("section", "REJECTION"),
        ("body", "The submitted outpatient antibiotic claim is rejected as non-preferred on the member's formulary."),
        ("section", "FORMULARY-PREFERRED ALTERNATIVES"),
        ("bullets", [
            "Trimethoprim-sulfamethoxazole (preferred, lowest tier)",
            "An oral fluoroquinolone (preferred)",
        ]),
        ("body", "Please prescribe a preferred alternative or submit a prior authorization with clinical justification for the non-preferred agent."),
        ("sig", "CoreScript Pharmacy Benefits"),
    ])


def T6():
    return ("payer_concurrent_review_request_05252026.docx", "primarycare", [
        ("title", "MERIDIAN ADVANTAGE HEALTH PLAN - CONCURRENT REVIEW REQUEST"),
        ("filing", "Utilization Management | Date: 05/25/2026 | Status: Continued-stay review | " + RE),
        ("section", "REQUEST"),
        ("body", "This is a concurrent review of the continued inpatient stay. The member has shown clinical improvement. Please submit clinical justification for continued inpatient level of care, or indicate readiness for a lower level of care."),
        ("section", "INFORMATION REQUESTED"),
        ("bullets", [
            "Current clinical status and active treatments requiring inpatient care",
            "Skilled needs that cannot be provided at a lower level of care",
            "Anticipated discharge plan and barriers",
        ]),
        ("sig", "Meridian Advantage Health Plan, Utilization Management"),
    ])


def T7():
    return ("quality_abstraction_worksheet_06042026.docx", "mar", [
        ("title", "DIABETES QUALITY MEASURE ABSTRACTION WORKSHEET"),
        ("filing", "Author: Quality Department | Date: 06/04/2026 | Status: For abstraction | " + RE),
        ("body", "Complete each field by entering the value found, marking the exclusion, or marking undetermined. Use only documentation in the record."),
        ("section", "MEASURE FIELDS"),
        ("table", [
            ["Measure field", "Value / Exclusion / Undetermined"],
            ["Most recent HbA1c and date", "To be abstracted"],
            ["Dilated diabetic eye exam within the measurement period", "To be abstracted"],
            ["Diabetic foot exam documented", "To be abstracted"],
            ["Nephropathy screening / monitoring", "To be abstracted"],
            ["Blood pressure most recent", "To be abstracted"],
        ]),
        ("body", "Enter findings from the record. Where the record does not support a field, mark it undetermined rather than inferring."),
        ("sig", "Quality Department - abstraction pending"),
    ])


def T9():
    return ("safety_event_intake_summary_06112026.docx", "primarycare", [
        ("title", "PATIENT SAFETY EVENT INTAKE SUMMARY"),
        ("filing", "Author: Patient Safety | Date: 06/11/2026 | Status: Intake for review | " + RE),
        ("section", "EVENT DESCRIPTION"),
        ("body", "Intake summary for review of a wound-offloading lapse during the admission. Nursing flowsheet entries document episodes where the left forefoot offloading device was not consistently maintained during ambulation, and occupational therapy documented that offloading teach-back was not achieved. This summary collects the event details for a contributing-factors review."),
        ("section", "FOR REVIEW"),
        ("bullets", [
            "Timeline of offloading device use and lapses",
            "Teaching attempts and language-access factors",
            "System and communication contributors",
        ]),
        ("body", "This is an intake summary. It records the event and does not assign cause or conclusion."),
        ("sig", "Patient Safety - review pending"),
    ])


def T10():
    R = ROSTER
    return ("started_discharge_instruction_draft_05212026.docx", "primarycare", [
        ("title", "DISCHARGE INSTRUCTIONS (DRAFT - INCOMPLETE)"),
        ("filing", f"Author: {R['resident']} | Started 05/21/2026 | Status: Draft, incomplete | {RE}"),
        ("section", "YOUR DIAGNOSIS"),
        ("body", "You were treated in the hospital for a serious infection of your left foot related to diabetes."),
        ("section", "MEDICATIONS"),
        ("body", "Take your medications as listed in your reconciled medication list. Your antibiotic plan will be confirmed before you leave."),
        ("section", "WOUND CARE"),
        ("body", "Keep your dressing clean and dry. A nurse will help arrange your dressing changes."),
        ("section", "OFFLOADING AND ACTIVITY"),
        ("body", "PENDING: offloading and activity instructions to be completed by the discharging clinician before discharge."),
        ("section", "FOLLOW-UP"),
        ("body", "Follow up with your primary care provider and the specialists as arranged by the care team."),
        ("section", "WHEN TO SEEK CARE"),
        ("body", "Call your care team or seek care for increasing redness, drainage, odor, fever, or worsening foot pain."),
        ("sig", "Draft started; sections remain to be completed prior to discharge."),
    ])


TASK_FILES = [T1, T2, T3, T4, T5, T6, T7, T9, T10]
