# Next-World Diabetic Foot Planning Canvas

Date: 2026-06-12. Status: Candidate 1 ratified for planning only. This is a filled local cockpit derived from `internal-medicine-world-planning-canvas.md` and `next-world-candidate-scorecard.md`. It is not a Brainstorm submission, not a World Spec, not a file plan authorization, and not a build request.

## Scope Lock

No world folder, substrate, task artifact, prompt, golden, grader, generated image, uploaded file, AutoQC run, trajectory run, or platform action follows from this document until Alexander authorizes that phase.

No-repeat receipt:

- Tasks before files. The task slate and forced slots come before any chart substrate.
- World files must be raw material, not answer-key synthesis.
- Wound photo is substrate only. KM08 already spent photo-as-headline-trap.
- A score below 70 is not required; the bankable unit is a legitimate clinical or material deliverable failure.
- Same-author draft traps need true placeholders or an explicit correct-errors instruction.

## 1. World Thesis

| Question | Working answer |
|---|---|
| What real internal medicine workflow pain does this world model? | A limb-threat diabetic foot infection admission where hospital medicine has to coordinate podiatry, vascular surgery, infectious disease, endocrine, nephrology, wound care, PT/OT, case management, CDI, HIM, payer review, and family pressure while the patient is clinically improving but not yet safe. |
| What pressure makes the clinician move too fast? | Bed pressure, payer pushback on inpatient/SNF/DME, family preference for home, apparent improvement after antibiotics/debridement, and partial consultant signoffs that look cleaner than the raw record. |
| What clinical mistake would be serious in real care? | Under-recognizing limb threat, using the wrong renal antibiotic dose or unsafe substitute, misclassifying the wound/coding specificity, discharging without safe offloading/DME/follow-up, or accepting an unsupported CDI/payer/HIM position. |
| Why would a strong model plausibly make that mistake? | It will know general diabetes and sepsis, but it is weaker at local source hierarchy, wound-photo context, ABI/TBI interpretation, osteomyelitis uncertainty, renal dosing under changing eGFR, DME/SNF logistics, and coding/CDI distinctions that depend on treating documentation. |
| Which facts should be raw and scattered rather than summarized? | Wound dimensions, drainage, probe-to-bone language, x-ray/MRI wording, culture provenance, antibiotic start/stop times, renal function trend, vascular studies, operative findings, offloading orders, PT/OT restrictions, pharmacy fills, case-management barriers, payer denial language, and attending addenda. |
| Which single source would accidentally become an answer key if included? | A polished discharge summary, ID final antibiotic plan, vascular final recommendation, or coding/CDI final response that states the final synthesis. These should not be shared world-level answer keys. If needed, they become task-level external surfaces or remain absent. |
| What is the world snapshot date? | TBD before Brainstorm. Constraint: all tasks must be strictly after snapshot and not future-dated. |
| What is the latest allowed task anchor date? | TBD before Brainstorm. Constraint: no task relies on public knowledge after July 2025 even if chart documents are dated 2026. |

## 2. Personnel Lattice

Core inpatient team:

- Hospitalist attending, final attending voice for task goldens.
- PGY-3 senior resident, carries overnight plan and consultant synthesis.
- PGY-1 intern, writes daily progress notes and discharge prep.
- Medical student, contributes wound-exam and family-call notes with partial information.
- Night-float resident, creates one realistic but non-final handoff surface.

Services and staff:

- Podiatry for debridement, wound classification, offloading, and operative findings.
- Vascular surgery for PAD, ABI/TBI interpretation, revascularization timing, and limb-threat disposition.
- Infectious disease for antibiotic choice, source control, culture interpretation, and duration.
- Endocrinology or diabetes educator for insulin transition, steroid or infection hyperglycemia, and home regimen safety.
- Nephrology for AKI on CKD, contrast risk, renal dosing, and medication holds.
- Wound care nurse for measurements, photo upload, dressing plan, and documentation ambiguity.
- Bedside nursing for drainage, fever, mobility compliance, and family teaching.
- PT/OT for offloading adherence, transfer safety, stairs, DME, and home versus SNF.
- Pharmacist for renal dosing, allergy reconciliation, drug interactions, and payer substitute.
- Case manager for home health, SNF, DME, transport, and insurance barriers.
- CDI specialist for query pressure.
- HIM coder for code family, POA, and principal diagnosis sequencing.
- Payer reviewer for inpatient/SNF/DME denial.
- Family caregiver, source of home-med and home-support conflict.

## 3. Structure Slate

| Task | Structure | Approved workflow string | Deliverable | Native forced slot | Expected wrong move | Why it matters | Post-snapshot anchor | Grader mode | Reachability plan |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S2 forced inventory | Medication safety / reconciliation adaptation | Physician discharge med-rec safety table | Every med row needs continue, hold, change, stop, or defer | Carry admission eGFR antibiotic dosing or accept unsafe renal substitute | Antibiotic failure, toxicity, readmission | TBD after snapshot | Chart-aware | Catcher expected through MAR, eGFR trend, ID/pharmacy notes |
| 2 | S2 forced inventory | Inpatient Medical Coding and DRG Assignment | Physician coding attestation against HIM worksheet | Principal diagnosis, POA, code family per row | Misclassify diabetic foot ulcer as pressure injury or overcall osteomyelitis POA | DRG, quality, audit risk | TBD after snapshot | Chart-aware | Catcher expected by operative note, imaging, wound-care wording |
| 3 | S3 external | Clinical Documentation Improvement (CDI) Query Response Review | Attending CDI query response | Agree, decline, unable to determine, or clarify item by item | Accept unsupported osteomyelitis specificity or sepsis severity language | Documentation integrity and overcoding risk | TBD after snapshot | Chart-aware | External query gives fair forced stance |
| 4 | S3 external | Claims Denial Analysis and Appeal Preparation | Physician appeal for DME, SNF, or inpatient days | Appeal, accept, or narrow appeal | Accept denial by underweighting offloading and mobility restrictions | Unsafe discharge, coverage failure | TBD after snapshot | Chart-aware | Payer denial wrong by genre |
| 5 | S3 external | Pharmacy Insurance Claim Rejection Resolution | Physician/pharmacist response to rejected antibiotic or diabetes med | Substitute, appeal, hold, or request exception | Choose formulary substitute unsafe for eGFR, QT, allergy, or interaction | Medication harm | TBD after snapshot | Chart-aware | Catcher expected from allergy, eGFR, ECG, culture |
| 6 | S4 determination | Inpatient vs observation determination or utilization review concurrent stay | Physician advisor status or continued-stay determination | Verdict slot | Treat post-debridement improvement as discharge readiness | Wrong level of care, payer dispute | TBD after snapshot | Chart-aware | Case must be designed borderline |
| 7 | S5 abstraction | HEDIS Medical Record Chart Abstraction and Review or HCC Risk Coding Review | Fixed-field diabetes/HCC/quality abstraction | Each field needs value, exclusion, or unable to determine | Miss a quiet lookback exclusion or count an unsupported complication | Quality and risk adjustment error | TBD after snapshot | Chart-aware | Forced fields make deferral impossible |
| 8 | S6 synthesis with embedded forced table | Specialist Referral Letter and Documentation Preparation | Vascular or wound-care referral letter with required disposition table | Table forces source-control, perfusion, antibiotics, offloading, follow-up | Write a pleasant referral but omit a required unresolved limb-threat disposition | Care continuity failure | TBD after snapshot | Chart-aware | Table creates forced slot |
| 9 | S7 investigation | Patient Safety Event Investigation and Root Cause Analysis | Physician safety review of missed offloading or delayed consult | Attribution and prevention finding | Blame a single person when the chart shows system-level and order-level causes | Safety and quality failure | TBD after snapshot | Chart-aware | Variety slot, expected mid difficulty |
| 10 | S1 completion | Medical Transcription and Clinical Documentation Completion | Finalize discharge instructions from a started draft | Ratify or refute the one open decision | Fill same-author draft with routine closure not supported by chart | Discharge harm | TBD after snapshot | Chart-aware | True placeholder plus A0.4/A0.5 built-byte gate |

## 4. Trap Inventory Ledger

| Trap | Task(s) | Warm or cold | Forced by what | Chart contradicts or mandates what | Fairness route | Expected model failure | Catch evidence needed | Grader hard-error status |
|---|---|---|---|---|---|---|---|---|
| Renal antibiotic dosing under changing eGFR | 1, 5 | Cold | Med row and pharmacy response | Dose should follow current renal function and selected agent, not copied admission dose | Forced inventory, external pharmacy document | Carries unsafe dose or accepts unsafe substitute | MAR, creatinine/eGFR trend, ID note, pharmacy note | Hard if unsafe discharge med |
| Diabetic ulcer versus pressure injury code family | 2, 7 | Cold | Coding rows and abstraction fields | Wound location, etiology, and documentation support diabetic foot ulcer, not routine pressure injury unless separately documented | Forced inventory | Uses wrong code family or POA status | Wound RN, podiatry, nursing skin assessment | Hard for coding task |
| Osteomyelitis specificity unsupported by imaging/tissue | 2, 3 | Cold | HIM/CDI external surfaces | Imaging or operative note may be suspicious but not definitive, or pathology/culture source is limited | External adversarial document | Accepts specificity query without treating evidence | X-ray/MRI wording, op note, cultures, pathology | Hard for CDI/coding |
| Vascular adequacy overstated | 4, 6, 8 | Cold | Payer appeal, status verdict, referral table | Palpable pulse or Doppler signal does not equal adequate perfusion if ABI/TBI says otherwise | External payer, determination, table | Treats vascular issue as resolved | ABI/TBI tracing, vascular consult, wound status | Hard if discharge/appeal unsafe |
| Offloading and DME logistics underweighted | 4, 6, 8, 9 | Cold | Appeal, status, referral, RCA | Safe mobility requires offloading device, training, home layout fit, and supplies | External denial, determination, investigation | Says home is safe from medical improvement alone | PT/OT, case management, nursing teaching | Hard for discharge safety |
| Lookback-window or denominator disqualifier | 7 | Cold | Fixed abstraction fields | A quiet date or exclusion changes quality capture | Forced abstraction | Counts wrong numerator/denominator | Prior outpatient note, lab bundle, dates | Hard for abstraction |
| Culture provenance mismatch | 1, 3, 5 | Cold | Med row, CDI item, pharmacy response | Superficial swab, tissue, blood culture, and operative culture carry different authority | Forced inventory, external query | Treats all cultures equally | Culture reports, op note, ID note | Medium to hard |
| Contrast-on-CKD risk misframed | 6, 8 | Cold | Determination and referral table | Need for angiography or revascularization is not the same as completed/cleared renal risk | Determination, table | Treats pending vascular decision as resolved | Nephrology, vascular, creatinine trend | Medium to hard |
| Same-author discharge draft closure | 10 | Cold | Completion slot | Draft must leave scored decision open, no routine assertion | True placeholder | Fills unsupported final closure | Built draft byte quote, chart sources | Hard if placeholder ignored |
| Photo overuse as headline | All | Warm/spent | None | Photo supports chart, but is not the scored trap by itself | Guardrail | Repeats KM08 mechanism | Wound photo visibility check | Do not use as central floor |

## 5. Source Geometry Board

Plan at least 30 world-level files. These are concepts only. They are not file builds.

| # | Planned world-level file concept | Modality | Raw facts it carries | What it must not summarize | Tasks requiring it | Leakage risk |
|---|---|---|---|---|---|---|
| 1 | ED triage note | Text | Arrival vitals, fever, foot complaint, fall, family report | Final diagnosis | 1, 3, 6 | Low |
| 2 | ED physician note | Text | Initial differential, sepsis workup, foot exam | Final source-control plan | 2, 3, 6 | Medium |
| 3 | Admission H&P | Text | Baseline diseases, initial problem list, first med holds | Final discharge synthesis | 1, 2, 3 | Medium |
| 4 | Home medication reconciliation | Table/text | Patient report, caregiver report, pharmacy source tags | Final med decisions | 1, 5, 10 | Medium |
| 5 | Pharmacy fill history | Table | Fill dates, quantities, prescribers | Which med is correct | 1, 5 | Low |
| 6 | MAR through hospital day 4 | Table | Antibiotic timing, holds, insulin, anticoagulation | Final med plan | 1, 5, 10 | Medium |
| 7 | Lab trend bundle | Table | WBC, creatinine/eGFR, glucose, CRP/ESR | Final interpretation | 1, 3, 5, 6 | Low |
| 8 | Blood culture report | Lab report | Organism, timing, sensitivities | Source conclusion alone | 1, 3, 5 | Medium |
| 9 | Wound culture report | Lab report | Superficial or tissue source, susceptibilities | Treat all cultures as equal | 1, 3, 5 | Medium |
| 10 | Foot x-ray report | Imaging text | Gas, cortical change, foreign body, uncertainty | Definitive osteomyelitis if uncertain | 2, 3, 8 | Medium |
| 11 | MRI foot report or radiology addendum | Imaging text | Marrow signal, abscess, equivocal osteomyelitis wording | Final coding conclusion | 2, 3, 8 | High |
| 12 | Bedside wound photo | Image | Visual wound substrate | Headline scored trap | 2, 4, 8, 9 | High if overused |
| 13 | Wound care nurse note | Text/photo reference | Measurements, drainage, dressing, photo upload | Etiology overreach | 2, 4, 7, 8 | Medium |
| 14 | Podiatry consult | Text | Probe-to-bone, debridement plan, offloading | Final vascular/ID plan | 2, 3, 4, 8 | Medium |
| 15 | Podiatry operative note | Text | Debridement findings, tissue/bone sampling, depth | Post-op final synthesis | 2, 3, 8 | Medium |
| 16 | Pathology report | Lab/path | Bone/tissue result, margin uncertainty | Overstate if pending | 2, 3 | High |
| 17 | ABI/TBI scanned tracing | Scan/image | Perfusion data with noncompressible vessels | Plain-text answer key | 4, 6, 8 | High but fair |
| 18 | Vascular surgery consult | Text | PAD interpretation, revascularization risk/plan | Final discharge clearance | 4, 6, 8 | Medium |
| 19 | Infectious disease consult | Text | Antibiotic rationale, culture hierarchy, duration uncertainty | Final easy plan | 1, 3, 5 | High if too final |
| 20 | Nephrology consult | Text | AKI/CKD, contrast and dosing comments | Final med list | 1, 5, 6, 8 | Medium |
| 21 | Endocrine/diabetes educator note | Text | Insulin transition, home ability, glucose education | Final discharge regimen | 1, 7, 10 | Medium |
| 22 | Point-of-care glucose log | Table | Infection/steroid hyperglycemia pattern | Final insulin decision | 1, 7, 10 | Low |
| 23 | Nursing skin and mobility flowsheet | Table/text | Offloading adherence, drainage, transfers | Final safety decision | 4, 6, 9 | Medium |
| 24 | PT evaluation | Text | Weight-bearing restrictions, stairs, walker, assist | Final placement answer | 4, 6, 9 | Medium |
| 25 | OT evaluation | Text | ADLs, teach-back, dressing/offloading use | Final home readiness answer | 4, 6, 9 | Medium |
| 26 | Case management note | Text | SNF/home health/DME/payer barriers | Appeal answer | 4, 6 | Medium |
| 27 | Family meeting note | Text | Caregiver availability, home layout, disagreement | Final disposition | 4, 6, 10 | Medium |
| 28 | Payer communication note | Text | Initial denial language or criteria request | Appeal conclusion | 4, 6 | High if too explicit |
| 29 | CDI query draft or CDI note | Text | External severity push | Correct response | 3 | Task-level candidate, not shared if it pre-answers |
| 30 | HIM preliminary coding worksheet | Text/table | External coding stance | Correct coding answer | 2 | Task-level candidate, not shared if it pre-answers |
| 31 | Medication bottle photo | Image | Home label mismatch | Correct med list | 1, 5 | Medium |
| 32 | Home glucose log photo | Image | Patient-reported values, timing ambiguity | Final insulin decision | 1, 7, 10 | Medium |
| 33 | Discharge planning checklist | Form | Equipment and teaching gaps | Final discharge summary | 4, 6, 10 | Medium |

Task-level candidates, held out unless the specific task needs them:

- CDI query.
- HIM preliminary coding worksheet.
- Payer denial.
- Pharmacy rejection.
- Same-author started discharge instruction draft with true placeholders only.

## 6. Candidate 1 Guardrails

- Do not create a shared discharge summary as a world-level file.
- Do not let ID, vascular, or podiatry write a final all-answers synthesis at world level.
- Do not make the photo the central scored failure.
- Do not repeat KM09 sepsis-to-principal anchoring as the coding core.
- Do not repeat KM10 encephalopathy-style CDI overreach.
- Do not repeat KM05/KM06 home-reading restart as a headline trap.
- Every off-text asset needs agent and grader visibility before pilot interpretation.
- Every clinical guideline or policy needed by the task must be pre-July 2025 or attached as a realistic source file.

## 7. Brainstorm Export Draft

World setup:

The proposed world is a complex internal medicine hospitalization for a patient with diabetes, CKD, PAD, neuropathy, and functional vulnerability admitted with a limb-threat diabetic foot infection. The admission is medically improving after antibiotics and podiatry intervention, but the safe plan remains unstable because renal dosing, perfusion, offloading, wound classification, source control, home support, and payer coverage do not line up cleanly.

Major friction points:

- Hospital medicine wants a coherent discharge plan, while podiatry, vascular surgery, ID, nephrology, endocrine, and wound care each control only part of the risk.
- Family preference for home conflicts with PT/OT, offloading requirements, wound supplies, and home-health availability.
- HIM/CDI and payer review pressure pull documentation toward specificity and lower-cost disposition before the treating record fully supports it.
- Pharmacy and insurance restrictions create medication substitutes that look administratively easy but clinically unsafe.

Major traps:

- Renal antibiotic dosing and formulary substitution under changing eGFR.
- Diabetic foot ulcer versus pressure injury classification.
- Osteomyelitis specificity and POA status when imaging, operative findings, and pathology do not fully agree.
- Perfusion and vascular adequacy overstated from incomplete or misunderstood ABI/TBI data.
- Offloading, DME, and mobility barriers underweighted once infection markers improve.
- Quality abstraction lookback-window or exclusion logic buried in raw notes.

Rough task idea:

Ten tasks across S1, S2, S3, S4, S5, S6, and S7. The task slate should include med rec, coding attestation, CDI query response, payer appeal, pharmacy rejection response, status/continued-stay determination, quality/HCC abstraction, vascular referral with a forced disposition table, safety event review, and exactly one true-placeholder completion task.

## 8. Open Decisions Before Brainstorm

- Patient age, sex, language, insurance type, and home setting.
- World snapshot date and task anchor sequence.
- Which external surfaces are world-level versus task-level.
- Whether vascular data uses ABI/TBI, toe pressures, duplex, CTA, or angiography note.
- Whether osteomyelitis remains uncertain or is confirmed late, and which task uses that uncertainty.
- Whether the main payer appeal centers on inpatient status, SNF days, home health, wound VAC, or offloading boot.
- Whether the photo is generated, searched, or represented as a clinical image attachment after modality rules are confirmed.
