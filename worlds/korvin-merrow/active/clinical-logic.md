# Korvin Merrow Clinical Logic

## Active Project Context

This file preserves the evolving clinical reasoning and design philosophy for the Korvin Merrow World. It is not the final Brainstorm deliverable.

## Role Perspective

This world is designed from Alexander Udeogaranya's background as an Emergency Medicine and Internal Medicine physician managing undifferentiated adult patients in acute hospital settings and coordinating care across specialties.

## Core Mental Model

This is not a set of isolated clinical questions.

This is a complete clinical environment.

Definitions:

- Scenario = the patient story and clinical journey.
- World = the complete clinical context, chart ecosystem, documentation history, competing perspectives, and information environment.
- Tasks = realistic clinician workflows performed inside that environment.

## Purpose

Expose the gap between information recall and true clinical judgment.

The AI should not succeed by recognizing a diagnosis alone.

The world should test:

- prioritization
- pattern recognition
- synthesis across multiple documents
- handling uncertainty
- reconciling conflicting information
- safe decision-making when recommendations compete

## Clinical Environment

Emergency Medicine / Internal Medicine / acute hospital setting.

## Working Patient

Korvin Merrow is a 62-year-old male with:

- type 2 diabetes mellitus
- hypertension
- CKD stage 3
- HFrEF
- CAD history
- hyperlipidemia
- anemia of CKD
- osteoporosis/osteopenia from chronic steroid exposure
- obstructive sleep apnea
- diabetic peripheral neuropathy
- medication complexity/polypharmacy
- PMR with unclear chronic prednisone taper history

Locked Identity Package v1:

- DOB: 1964-02-18
- MRN: KM-6427819
- Height: 178 cm (5'10")
- Weight: 97 kg (214 lb)
- BMI: 30.6
- Allergy: lisinopril (cough)
- Code Status: Full Code

Identity checks:

- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with height 178 cm and weight 97 kg.
- The identity package does not alter the mixed physiology story, discharge safety target, approved frictions, or approved traps.

Identity review addendum:

- Treat lisinopril cough as ACE-inhibitor intolerance during later World Spec construction.
- Later medication history should coherently explain prior ACE-inhibitor transition in the context of current sacubitril/valsartan therapy.
- Baseline function, baseline creatinine, dry weight, and similar baseline anchors should be explicitly placed during Patient Profile / Clinical History design.
- These notes do not reopen Identity Package v1.

Approved compact medication list:

- sacubitril/valsartan 24/26 mg BID
- carvedilol 12.5 mg BID
- furosemide 40 mg daily
- spironolactone 25 mg daily
- empagliflozin 10 mg daily
- aspirin 81 mg daily
- atorvastatin 40 mg nightly
- metformin ER 500 mg BID
- insulin glargine 18 units nightly
- prednisone with inconsistent documented taper/dose
- alendronate 70 mg weekly
- calcium/vitamin D daily
- ferrous sulfate 325 mg every other day
- gabapentin 300 mg nightly

## Presentation

Patient arrives with:

- altered mental status
- progressive weakness
- poor oral intake
- near-fall/lightheadedness
- family-noticed confusion
- possible urinary symptoms
- borderline hypotension

Initial working diagnosis: sepsis.

The case evolves beyond the first impression.

## Locked Temporal Architecture

- 6-day hospitalization.
- World close: Hospital Day 6 at 18:00.
- Discharge anchor after world close.
- +7 day post-discharge anchor.
- +30 day post-discharge anchor.

Tasks must remain temporally after the world close and independent from one another.

## Locked Underlying Clinical Story

This is a mixed physiology world.

The clinical burden comes from interaction among:

- infection
- steroid exposure/taper uncertainty
- CKD/HF physiology
- polypharmacy
- functional decline

This is not a single-diagnosis world. It should not collapse into a hidden adrenal insufficiency reveal or a sepsis-only case.

## Locked Clinical Evolution

The patient has approximately 3 weeks of decline before presentation.

The decline includes worsening weakness, reduced oral intake, near-fall/lightheadedness, family-noticed confusion, and possible urinary symptoms.

## Locked Clinical Story Skeleton v1

Status: RATIFIED after review on 2026-05-31.

Review artifact: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-review.md`

Decision log: `worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md`

Ratification artifact: `worlds/korvin-merrow/world-spec-prep/clinical-story-skeleton-ratification.md`

Baseline:

- Lives with family.
- Independent but slowed by chronic illness.
- Occasional cane use.
- Mild age-related forgetfulness only.
- Chronic diseases generally stable before current decline.

PMR / prednisone:

- Several-year PMR history.
- Chronic prednisone exposure.
- Multiple prior flares and taper attempts.
- Recent taper initiated because symptoms appeared controlled.
- Prednisone history contains reconstructable source-of-truth inconsistencies across documentation, medication history, family understanding, and patient recollection.

Three-week decline:

- Reduced stamina.
- Reduced activity.
- Poor appetite.
- Reduced fluid intake.
- Increasing weakness.
- Increasing family dependence.
- Possible urinary symptoms.
- Progressive unsteadiness.
- Progressive cognitive slowing.

Escalation:

- Medication-management mistakes.
- Increased dependence.
- Lightheadedness.
- Near-fall event.
- Family recognizes meaningful deviation from baseline and seeks care.

ED presentation:

- Suspected urinary-source infection.
- Dehydration.
- AKI risk.
- Altered baseline mental status.
- Functional decline.
- Sepsis-oriented management is clinically reasonable.
- Infection is a contributor, not the entire explanation.

Hospital course:

- HD1: admission and stabilization.
- HD2: partial improvement and consultant involvement begins.
- HD3: PT/OT identify functional concerns.
- HD4: consultant tensions emerge and steroid-history inconsistencies are recognized.
- HD5: medical improvement continues and disposition questions become dominant.
- HD6: patient appears medically improved but discharge remains debatable.

Discharge state:

- Infection improved.
- AKI improving.
- Hemodynamics stable.
- Mental status improved.
- Oral intake improved.
- Functional reserve uncertain.
- Medication restart strategy not fully settled.
- Steroid interpretation imperfect.
- Family concern persists.
- Disposition risk remains meaningful.

Near-fall framework:

- Multi-factorial.
- Not attributable to a single cause.
- Contributors include poor intake, volume depletion, medication effects, neuropathy, deconditioning, infection physiology, and steroid-related physiology.

## Ratified Governance Guardrails

### Endocrine Friction

Use: Endocrinology vs Primary Team.

Do not use: Endocrinology vs Documentation.

Documentation is evidence. Documentation is not a friction participant. The steroid-record discrepancy remains a trap. The friction remains a human-to-human disagreement about steroid risk interpretation and management.

### Prednisone Source-of-Truth Hierarchy

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

This hierarchy should guide later World Spec governance when prednisone exposure, taper timing, and adrenal suppression risk need to be reconstructed.

### Family vs Primary Team Balance

Both positions are defensible.

Family position:

- Not back to baseline.
- Functional concerns remain.
- Safety concerns remain.

Primary team position:

- Infection improved.
- AKI improving.
- Mental status improved.
- Oral intake improving.
- Follow-up available.
- Discharge is clinically defensible.

The discharge-readiness friction should remain a gray-zone judgment problem, not an obvious unsafe-discharge case.

### Near-Fall Guardrail

The near-fall event is intentionally multi-factorial.

No single contributor is intended to explain the event.

Potential contributors include poor intake, volume depletion, medication effects, neuropathy, deconditioning, infection physiology, and steroid-related physiology.

## Locked World Tone

The patient is medically improving but operationally dangerous to discharge.

The world should make the patient look better by some objective markers while still creating a realistic discharge safety problem.

## Primary Failure Target

The primary failure target is:

- functional decline
- disposition safety
- discharge readiness reasoning

The intended failure is not missing a rare diagnosis. The intended failure is over-weighting medical stabilization and under-weighting the functional, medication, and transition-of-care risk.

## Complexity Targets

World Spec development should exceed reviewer minimums:

- target 12-15 comorbidities
- target 18-22 medications

Any expansion should strengthen the existing cardiorenal, diabetes, steroid, neuropathy, bone-health, and discharge-reconciliation logic without adding unrelated noise.

## Competing Clinical Concerns

- adrenal insufficiency from previous steroid exposure
- acute kidney injury
- electrolyte abnormalities
- medication-related complications
- possible cardiac involvement
- discharge safety concerns

## World Journey

Follow the patient through:

- emergency evaluation
- inpatient admission
- evolving diagnostic workup
- consultant recommendations
- medication changes
- treatment decisions
- discharge planning

## Expected World Documents

Potential documents may include:

- ED notes
- admission notes
- daily progress notes
- nursing documentation
- medication administration records
- laboratory trends
- imaging reports
- consultant notes
- discharge documentation

## Major Clinical Friction Themes

1. Emergency/inpatient team: focused on immediate stabilization and sepsis management.
2. Endocrinology: questions adrenal crisis/adrenal insufficiency contribution.
3. Nephrology: concerned about kidney injury and medication safety.
4. Cardiology: balances restarting long-term protective medications.
5. Family/caregivers: concerned patient has not returned to baseline despite medical stability.

## Design Principle

Do not make this a rare disease puzzle.

Complexity comes from realistic medicine:

- common diseases
- messy documentation
- competing priorities
- evolving information

## Source Of Truth

`AGENTS.md` keeps operating context.

Detailed evolving clinical design belongs under `worlds/korvin-merrow/active/` and locked preparation decisions belong under `worlds/korvin-merrow/world-spec-prep/`.
