# James Carter Context

## Clinical Philosophy

Alexander is an Emergency Medicine/Internal Medicine physician.

This World reflects acute hospital work with undifferentiated adult patients, evolving information, consultant input, medication changes, and discharge safety decisions.

Do not write isolated clinical questions.

Design a complete clinical environment.

Purpose: expose the gap between information recall and true clinical judgment.

AI should not succeed by recognizing a diagnosis alone.

World should test:

- prioritization
- pattern recognition
- synthesis across documents
- uncertainty handling
- medication reasoning
- conflicting recommendation reconciliation
- safe discharge judgment

## Active World Summary

Working title: James Carter World.

Setting: Emergency Medicine / Internal Medicine / acute hospital.

Timeline: multi-day hospitalization starting in the ED.

World begins with ED evaluation of an undifferentiated patient and follows inpatient admission, evolving workup, consultant involvement, treatment changes, and discharge planning.

World snapshot endpoint: hospital day 5-7 during discharge planning.

At endpoint:

- patient clinically improved
- acute issues appear controlled
- specialists have left recommendations
- medications changed
- team deciding safest discharge plan

## Locked World Setup Decisions

Patient:

- 62-year-old male
- long-standing type 2 diabetes
- hypertension
- CKD stage 3
- HFrEF
- CAD history
- polypharmacy
- PMR history treated with chronic prednisone and recent taper

Presentation:

- altered mental status
- progressive weakness
- poor oral intake
- reduced activity
- borderline hypotension
- AKI on CKD
- family reports possible urinary symptoms and subjective fever

Initial working diagnosis:

- suspected urinary-source sepsis

Initial ED/inpatient treatment as possible sepsis is appropriate.

Course:

- infection improves
- not every symptom resolves
- overlapping contributors must be reassessed: infection, dehydration/AKI, medication effects, endocrine/steroid issue, chronic disease

Steroid thread:

- not a hidden “nobody knows he took steroids” reveal
- old notes list prednisone
- newer outpatient plan reduced/stopped prednisone
- medication reconciliation inconsistent
- clinicians must determine true steroid timeline

Baseline function:

- lives at home with spouse/family
- independent ADLs before illness
- ambulates without major assistance
- manages some meds himself
- family provides support

Discharge state:

- vitals improved
- infection controlled
- renal function improving
- still weaker than baseline
- intermittent confusion concerns
- medication plan significantly changed

Core discharge question:

- medically stable on paper vs actually safe leaving hospital

## Expected Friction Themes

Not fully finalized yet.

Candidate frictions:

1. Emergency/inpatient team vs endocrinology
   - sepsis/stabilization and practical steroid decisions vs adrenal insufficiency evaluation and steroid timeline interpretation

2. Nephrology vs cardiology
   - AKI/hypotension medication safety vs restarting HFrEF/CAD protective therapy

3. Family/caregivers vs inpatient team
   - family concerned he is not baseline vs team seeing objective medical improvement

Potential issue:

- documentation conflict alone is a trap, not a friction, unless tied to a person/role advocating a position.

## Expected Trap Themes

Not fully finalized yet.

Candidate traps:

- copy-forward progress note assumptions
- outdated medication lists
- conflicting steroid timeline across old notes, outpatient plan, med rec
- buried nursing observations about cognition, weakness, intake, orthostasis, family concerns
- lab timing problems
- outdated consultant recommendations after renal/vital changes
- discharge medication reconciliation errors
- source hierarchy ambiguity: attending plan vs consultant note vs MAR/orders vs family/patient report vs outpatient med list

Trap standard:

- each trap should require synthesis across multiple documents
- no single-file trap
- no pure diagnosis-recognition trap
- adrenal insufficiency must remain one competing concern, not the whole answer

## Rough Task Categories

Not finalized.

Candidate categories:

- ED assessment or handoff documentation
- inpatient admission H&P
- daily progress note or hospitalist reassessment
- discharge medication reconciliation
- hospital discharge summary
- consultant synthesis / response to competing recommendations
- post-discharge follow-up / transition-of-care planning
- quality/safety review if medication/documentation miss causes harm

Need tracker mapping before final.

## Unresolved Questions

Frictions:

- exact disagreement between ED/inpatient team and endocrinology
- exact medication flashpoints between nephrology and cardiology
- exact family request at discharge: delay discharge, rehab, more workup, home supports, etc.
- whether PCP/rheumatology/outpatient records become a true friction or only traps

Traps:

- final trap list
- source document/location for each trap
- world-level vs task-level status
- synthesis chain for each trap

Tasks:

- final 5-8 task ideas
- approved workflow mapping
- P0 task identification
- task-level trap distinctions
- temporal anchoring after snapshot

## Reviewer Risks

- adrenal insufficiency reads as hidden zebra puzzle
- cardiology involvement weak unless HFrEF/CAD med tension is clear
- frictions collapse into information gaps
- traps solvable from one document
- tasks too generic or not approved workflows
- discharge safety concern vague unless baseline and residual deficits are clear

