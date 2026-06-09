# Reviewer Medication Decision Brief

Reviewer: Stacey S

Date: 2026-05-30

Purpose: prepare physician approval for reviewer-requested medication specificity. This brief proposes realistic candidate medication lists but does not lock medications, doses, or final Brainstorm content until Alexander approves.

## Reviewer Issue

Reviewer noted that the Brainstorm names medication categories but not specific agents/doses. The reviewer requested a medication list with drug names and doses.

## Design Goals

- Preserve the existing HF-AKI medication reconciliation trap.
- Make medication complexity concrete enough for Brainstorm approval.
- Avoid creating a new medication puzzle unrelated to the core hospital course.
- Use common, clinically plausible medications for HFrEF/CAD/CKD/PMR/diabetes.
- Keep doses realistic but adjustable by physician approval.

## Proposed Baseline/Home Medication List

### Heart failure / CAD / hypertension

| Medication | Candidate dose | Indication | Trap relevance |
| --- | --- | --- | --- |
| Sacubitril/valsartan | 49/51 mg PO twice daily | HFrEF guideline-directed therapy, BP control | Held during AKI/hypotension; restart timing creates Nephrology vs Cardiology tension. |
| Carvedilol | 12.5 mg PO twice daily | HFrEF/CAD rate and mortality benefit | May be held or reduced for hypotension/bradycardia; inappropriate discontinuation increases HF/CAD risk. |
| Furosemide | 40 mg PO daily | HFrEF volume management | Volume status and AKI tension; too much diuresis worsens AKI/hypotension, too little risks congestion. |
| Spironolactone | 25 mg PO daily | HFrEF mineralocorticoid receptor antagonist | Hyperkalemia/renal-function risk in CKD/AKI; restart requires renal/K trend. |
| Empagliflozin | 10 mg PO daily | HFrEF and diabetes benefit | Held during acute illness/poor intake/AKI; discharge restart requires renal status and intake assessment. |
| Aspirin | 81 mg PO daily | CAD secondary prevention | Usually continued unless bleeding/contraindication; should not be accidentally omitted. |
| Atorvastatin | 80 mg PO nightly | CAD/hyperlipidemia secondary prevention | Long-term protective medication; omission is a reconciliation quality issue. |
| Nitroglycerin SL | 0.4 mg SL every 5 minutes PRN chest pain, max 3 doses | CAD angina rescue | Mostly background CAD specificity. |

### Diabetes

| Medication | Candidate dose | Indication | Trap relevance |
| --- | --- | --- | --- |
| Metformin ER | 1000 mg PO daily with evening meal | Type 2 diabetes | Hold during AKI/acute illness; restart depends on renal recovery. |
| Insulin glargine | 18 units subcutaneously nightly | Type 2 diabetes basal control | Inpatient dose may differ with poor intake/steroids; discharge reconciliation risk. |
| Insulin lispro | Sliding scale with meals while inpatient | Inpatient hyperglycemia management | If included, clarify inpatient-only vs home regimen to avoid copy-forward discharge error. |

### PMR / steroid exposure / bone protection

| Medication | Candidate dose | Indication | Trap relevance |
| --- | --- | --- | --- |
| Prednisone | unclear: old list 10 mg daily; outpatient taper intended 2.5-5 mg daily or stopped | PMR, recent chronic steroid exposure | Core steroid timeline/source-of-truth trap; exact current exposure must be reconstructed. |
| Alendronate | 70 mg PO weekly | Steroid-associated osteoporosis/osteopenia | Supports steroid-risk downside and med-list complexity. |
| Calcium carbonate/vitamin D3 | 600 mg/800 IU PO twice daily | Bone protection | Background medication reconciliation. |

### CKD / anemia / neuropathy / other chronic medications

| Medication | Candidate dose | Indication | Trap relevance |
| --- | --- | --- | --- |
| Ferrous sulfate | 325 mg PO every other day | Anemia of CKD or iron deficiency component | Background complexity; should not drive acute AMS. |
| Gabapentin | 300 mg PO nightly | Diabetic peripheral neuropathy | Renal dosing and delirium/weakness consideration during AKI; discharge safety relevance. |
| Acetaminophen | 650 mg PO every 6 hours PRN pain | Chronic pain/PMR discomfort | Low-risk background PRN. |
| CPAP | nightly, if OSA approved | Obstructive sleep apnea | Not a medication; may affect discharge planning and cognition/fatigue context. |

## Medications That Drive The HF-AKI Trap

Highest-yield agents:

- Sacubitril/valsartan
- Furosemide
- Spironolactone
- Empagliflozin
- Carvedilol

Reasoning:

- These are clinically reasonable to hold or adjust during AKI, hypotension, poor intake, or unstable volume status.
- They are also long-term protective in HFrEF/CAD, so careless omission at discharge is unsafe.
- They create a real Nephrology vs Cardiology tension without requiring rare disease logic.

## Medications That Drive Discharge-Reconciliation Complexity

Highest-yield agents:

- Prednisone, because the true dose/taper status is unclear across sources.
- Sacubitril/valsartan, spironolactone, furosemide, empagliflozin, and carvedilol, because acute holds may become stale.
- Metformin, because AKI/CKD affects restart safety.
- Insulin glargine/lispro, because inpatient steroid/poor-intake dosing may not equal home regimen.
- Gabapentin, because AKI and confusion/weakness raise renal dosing and safety questions.
- Aspirin/atorvastatin, because long-term CAD secondary prevention should not be omitted without reason.

## Candidate Simplified Medication Set

If the Brainstorm needs brevity rather than a full home-med table, the minimum specific medication set could be:

- Sacubitril/valsartan 49/51 mg PO twice daily
- Carvedilol 12.5 mg PO twice daily
- Furosemide 40 mg PO daily
- Spironolactone 25 mg PO daily
- Empagliflozin 10 mg PO daily
- Aspirin 81 mg PO daily
- Atorvastatin 80 mg PO nightly
- Metformin ER 1000 mg PO daily
- Insulin glargine 18 units nightly
- Prednisone with inconsistent documentation: old 10 mg daily vs later taper to 2.5-5 mg daily or stopped
- Gabapentin 300 mg nightly
- Alendronate 70 mg weekly

## Physician Decisions Needed

- Approve exact HFrEF regimen: ARNI vs ACE inhibitor/ARB; include or exclude spironolactone.
- Approve diabetes regimen: metformin only, basal insulin, sliding-scale inpatient insulin, or SGLT2 as dual HFrEF/DM therapy.
- Approve exact prednisone ambiguity: old dose, taper plan, and likely current dose range.
- Approve whether gabapentin is included as neuropathy/AMS/renal-dose complexity.
- Approve whether alendronate/calcium/vitamin D are included for steroid-associated osteoporosis.
- Approve whether medication list should appear in Brainstorm as a compact list or table.

## Guardrails

- Do not lock these medications until Alexander approves.
- Do not add medication-specific task prompts.
- Do not invent lab values or exact inpatient medication administration changes yet.
- Do not turn the case into a medication trivia exercise.
