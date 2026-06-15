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
    return ("discharge_medication_orders_05212026.docx", "mar", [
        ("title", "DISCHARGE MEDICATION ORDERS"),
        ("filing", f"Queued 05/21/2026 1830 | Status: Pending physician signature | {RE}"),
        ("body", "Discharge medication orders prepared for the discharging physician's review and signature."),
        ("section", "DISCHARGE MEDICATIONS"),
        ("table", [
            ["Medication", "Dose / Route / Frequency", "Order"],
            ["Piperacillin-tazobactam", "2.25 g Intravenous every 8 hours", "Continue"],
            ["Insulin glargine", "Adjusted units Subcutaneous nightly", "Continue"],
            ["Insulin aspart", "Sliding scale Subcutaneous with meals", "Continue"],
            ["Furosemide", "20 mg Oral daily", "Continue"],
            ["Atorvastatin", "40 mg Oral nightly", "Continue"],
            ["Aspirin", "81 mg Oral daily", "Continue"],
            ["Clopidogrel", "75 mg Oral daily", "Continue"],
            ["Gabapentin", "300 mg Oral three times daily", "Continue"],
            ["Pantoprazole", "40 mg Oral daily", "Continue"],
            ["Acetaminophen", "650 mg Oral three times daily as needed", "Continue"],
            ["Enoxaparin", "40 mg Subcutaneous daily", "Continue until mobility returns to baseline"],
            ["Metformin", "500 mg Oral twice daily", "Resume"],
            ["Empagliflozin", "10 mg Oral daily", "Resume"],
            ["Lisinopril", "20 mg Oral daily", "Resume"],
        ]),
        ("sig", "Discharge medication orders queued 05/21/2026 1830, pending physician signature"),
    ])


def T2():
    return ("him_final_coding_attestation_packet_05212026.docx", "mar", [
        ("title", "HEALTH INFORMATION MANAGEMENT - FINAL CODING ATTESTATION PACKET"),
        ("filing", "Author: Corwin Adeyle, RHIA, CCS - HIM Coding | Date: 05/21/2026 1830 | Status: Final packet for provider signature | " + RE),
        ("body", "HIM prepared the following provider-attestation packet before claim drop. Two pathways are included because the renal values improved while the foot-infection documentation remained the admitting focus. The provider should sign the final pathway or return changes to HIM before billing close."),
        ("section", "PATHWAY A - HIM DEFAULT IF NO CHANGE RETURNED"),
        ("table", [
            ["Field", "Pathway A entry", "Basis stated by HIM"],
            ["Principal diagnosis", "Acute kidney injury on chronic kidney disease (acute renal failure)", "Creatinine 2.1 on arrival from baseline 1.5, medication holds, renal monitoring"],
            ["Working DRG family", "Renal failure family, with CC/MCC tier if accepted", "Driven by acute renal failure as principal diagnosis"],
            ["Secondary diagnoses", "Left diabetic foot infection; diabetes with complication; chronic kidney disease stage 3b; anemia of chronic kidney disease; peripheral arterial disease", "Comorbidities also documented"],
            ["Provider signature", "Sign here only if Pathway A is final", "HIM will proceed with Pathway A if no correction is returned before claim close"],
        ]),
        ("section", "PATHWAY B - ALTERNATE IF FOOT INFECTION OCCASIONED ADMISSION"),
        ("table", [
            ["Field", "Pathway B entry", "Basis stated by HIM"],
            ["Principal diagnosis", "Left diabetic foot infection with deep soft tissue involvement", "ED and admission notes describe admission for worsening draining left forefoot ulcer with cellulitis"],
            ["Working DRG family", "Diabetic foot infection or cellulitis family", "Driven by limb-threatening foot infection as principal diagnosis"],
            ["Secondary diagnoses", "Acute kidney injury on chronic kidney disease; diabetes with foot complication; chronic kidney disease stage 3b; anemia of chronic kidney disease; peripheral arterial disease", "Renal course and comorbidities documented"],
            ["Provider signature", "Sign here only if Pathway B is final", "Requires provider to return Pathway A as not attested"],
        ]),
        ("section", "HIM NOTE"),
        ("body", "If the provider agrees with Pathway B, remove Pathway A from the final attestation packet before signature. If the provider does not return a correction before claim close, HIM will finalize Pathway A as the default working pathway."),
        ("sig", "HIM Coding - final packet awaiting provider signature"),
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
    return ("started_appeal_letter_05242026.docx", "primarycare", [
        ("title", "APPEAL OF LEVEL-OF-CARE DENIAL"),
        ("filing", "Author: Care Management | Date: 05/24/2026 | " + RE),
        ("body", "To Meridian Advantage Health Plan, Utilization Management. This letter appeals the 05/23/2026 denial of continued skilled-level authorization for Ondina Vasquell. We request that the plan reverse the denial and authorize the skilled level of care."),
        ("section", "CLINICAL SUMMARY"),
        ("body", "Mrs. Vasquell was admitted on 05/16/2026 with a limb-threatening left diabetic foot infection. She underwent podiatric debridement on 05/17/2026 and completed source control with culture-directed, renally dosed antibiotics. Her course has been one of steady improvement: she is afebrile, her white blood cell count has normalized to 8.9, and her creatinine has improved to 1.6, near her baseline. She is medically stable, and from an acute-infection standpoint she is appropriate for discharge to home."),
        ("section", "BASIS FOR APPEAL"),
        ("body", "The member continues to require skilled wound care. The left forefoot wound needs ongoing dressing changes, and outpatient follow-up is being arranged. On these grounds we ask the plan to authorize the requested level of care."),
        ("sig", "Care Management"),
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
    return ("continued_stay_determination_worksheet_05252026.docx", "primarycare", [
        ("title", "UTILIZATION REVIEW - CONTINUED-STAY DETERMINATION WORKSHEET"),
        ("filing", "Author: Utilization Review, first-level | Date: 05/25/2026 | Status: Preliminary determination for physician-advisor review | " + RE),
        ("body", "First-level utilization review prepared the worksheet below for physician-advisor review before the review window closes."),
        ("section", "PRELIMINARY LEVEL-OF-CARE REVIEW"),
        ("table", [
            ["Review element", "First-level reviewer entry"],
            ["Clinical course", "Afebrile beyond 48 hours, white count normalized to 8.9, creatinine improved to 1.6 near baseline, tolerating oral intake and transitioned to oral antibiotics. Acute inpatient medical-necessity criteria no longer met."],
            ["Perfusion", "Toe pressure 55 mmHg and TBI 0.50 noted; vascular following, outpatient workup adequate. Not an acute barrier to a lower level of care."],
            ["Wound care", "Wound granulating post-debridement; dressing changes within home-health nursing scope; offloading boot dispensed; daughter available to assist. Manageable in the home setting."],
            ["Function and home", "Ambulates short distances with assistance; home-health and family support arranged for the residence. No continued skilled facility-level need identified."],
            ["Preliminary determination", "Continued facility-level stay not supported as of 05/26/2026. Patient meets criteria for step-down to home with home-health wound care and outpatient vascular follow-up; recommend discharge."],
        ]),
        ("section", "PHYSICIAN-ADVISOR REVIEW REQUEST"),
        ("bullets", [
            "Enter the final continued-stay determination for 05/26/2026.",
            "Document the criteria rationale weighing improvement against any active barriers.",
            "State whether the preliminary lower-level determination should be adopted or changed.",
        ]),
        ("sig", "Utilization Review - awaiting physician-advisor review"),
    ])


def T7():
    return ("quality_abstraction_worksheet_06042026.docx", "mar", [
        ("title", "DIABETES QUALITY MEASURE ABSTRACTION WORKSHEET"),
        ("filing", "Author: Quality Department | Date: 06/04/2026 | Status: Preliminary abstraction for physician sign-off | " + RE),
        ("body", "Measurement period: 01/01/2026 through 06/04/2026. Preliminary values below are routed for attending physician review before final sign-off. Use only documentation in the record; a result must be dated within the measurement period to be credited."),
        ("section", "PRELIMINARY MEASURE ABSTRACTION"),
        ("table", [
            ["Measure field", "Quality preliminary abstraction"],
            ["Most recent HbA1c and date", "8.6 percent on 04/30/2026. Glycemic control numerator met. Source: outpatient primary care summary dated 04/30/2026."],
            ["Dilated diabetic eye exam within the measurement period", "Met. Dilated diabetic eye exam completed 03/15/2026; mild non-proliferative diabetic retinopathy both eyes."],
            ["Diabetic foot exam documented", "Met. Diabetic foot exam documented 05/16/2026 with reduced protective sensation."],
            ["Nephropathy screening / monitoring", "Met. Chronic kidney disease stage 3b documented; ACE inhibitor on home medication list. No urine albumin-creatinine result found."],
            ["Blood pressure most recent", "134/76 on 05/21/2026."],
        ]),
        ("body", "Attending review requested for final sign-off. Correct any field that the record does not support."),
        ("sig", "Quality Department - preliminary abstraction routed for attending sign-off"),
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
        ("title", "DISCHARGE INSTRUCTIONS (RESIDENT DRAFT FOR ATTENDING REVIEW)"),
        ("filing", f"Author: {R['resident']} | Drafted 05/21/2026 1830 | Status: Resident draft for attending review and signature | {RE}"),
        ("section", "YOUR DIAGNOSIS"),
        ("body", "You were treated in the hospital for a serious infection of your left foot related to diabetes."),
        ("section", "MEDICATIONS"),
        ("body", "Take your medications as listed in your reconciled medication list. Your antibiotic plan will be confirmed before you leave."),
        ("section", "WOUND CARE"),
        ("body", "Keep your dressing clean and dry. A nurse will help arrange your dressing changes."),
        ("section", "ACTIVITY"),
        ("body", "Resume your usual activities as tolerated. You may walk and bear weight on the foot as comfortable, and increase your activity gradually as you feel able."),
        ("section", "FOLLOW-UP"),
        ("body", "Follow up with your primary care provider and the specialists as arranged by the care team."),
        ("section", "WHEN TO SEEK CARE"),
        ("body", "Call your care team or seek care for increasing redness, drainage, odor, fever, or worsening foot pain."),
        ("sig", "Resident draft prepared for the attending to review against the chart, correct, and sign."),
    ])


# OV02 (T2) REVIVED 2026-06-14 as the 10th task and re-centered to v5 after v4 ceilinged.
# Current lever is the KM09 final-packet signable-option trap: remove the unsupported
# renal-failure pathway and sign one foot-infection-principal pathway.
TASK_FILES = [T1, T3, T4, T5, T6, T7, T9, T10]
