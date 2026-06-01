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

Review artifact: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`

Decision log: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`

Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`

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

## Governance Package v1 Candidate

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`

Status: RATIFIED.

Care team roster:

- Primary Team: Hospitalist Service.
- Consultants: Cardiology, Nephrology, Endocrinology.
- Functional Team: Physical Therapy, Occupational Therapy.
- Transition Team: Case Management, Social Work.
- Stakeholders: Patient, Family/Caregiver, Primary Care Physician.

Authority hierarchy:

1. Attending Hospitalist.
2. Consulting Attending Specialists.
3. PT/OT Functional Assessments.
4. Case Management / Social Work.
5. Family Reports.
6. Patient Recollection.

Master source-of-truth hierarchy for clinical facts:

1. Attending Documentation.
2. Verified Medication Reconciliation.
3. Pharmacy History.
4. Consultant Documentation.
5. Primary Care Documentation.
6. Family Report.
7. Patient Recollection.

Preserve the prednisone-specific hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.

Hierarchy clarification: Authority Hierarchy is used for role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership. Source-of-Truth Hierarchy is used for factual conflict resolution. Authority hierarchy does not resolve clinical recommendation disagreements; consultant disagreements require evidence synthesis, timing, trends, patient status, and discharge safety.

Confirmed conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.

Presumed / active questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.

Steroid-related bone disease clarification: osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current adrenal suppression is the dominant explanation for current symptoms.

Final friction table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.

Administrative deliverable decision: yes. At least one future task should involve transition of care, discharge planning, care coordination, or follow-up planning.

Workflow umbrella: Acute Hospital Management, with subdomains of diagnosis, medication management, consultant synthesis, functional assessment, and disposition planning. Exact future task workflow lines must still use official tracker names.

Task-architecture watch items: AutoQC 2.107 workflow count and 2.108 administrative deliverable remain deferred until task architecture.

Completed Architecture Layers:

- Brainstorm: APPROVED.
- Temporal Architecture: LOCKED.
- Clinical Story Skeleton: RATIFIED.
- Identity Package: LOCKED.
- Governance Package: RATIFIED.

Physician Architecture Layer Status: COMPLETE.

Next legal phase recommendation: World Spec Construction Preparation.

## Key Milestones Calendar Skeleton v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`

Status: LOCKED.

Canonical date framework:

- Approximate decline begins: 2026-04-27 / 04/27/2026.
- Final pre-admission week begins: 2026-05-11 / 05/11/2026.
- Day before presentation: 2026-05-17 / 05/17/2026.
- Admission / HD1: 2026-05-18 / 05/18/2026.
- HD2: 2026-05-19 / 05/19/2026.
- HD3: 2026-05-20 / 05/20/2026.
- HD4: 2026-05-21 / 05/21/2026.
- HD5: 2026-05-22 / 05/22/2026.
- HD6: 2026-05-23 / 05/23/2026.
- World snapshot / world close: 2026-05-23 18:00 / 05/23/2026 18:00.
- Discharge anchor: 2026-05-24 / 05/24/2026.
- +7 day anchor: 2026-05-31 / 05/31/2026.
- +30 day anchor: 2026-06-23 / 06/23/2026.

This skeleton is a date framework only. It does not create clinical milestone content, task architecture, file inventory, prompts, goldens, grader guidance, or synthetic files.

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`

Locked doctrine: +7 and +30 anchors are measured from discharge anchor 05/24/2026, not from HD6 world close.

## Baseline Anchor Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`

Status: LOCKED.

Locked baseline anchors:

- Baseline creatinine.
- Baseline eGFR.
- Baseline hemoglobin.
- Baseline A1c.
- Dry weight approximately 97 kg.
- Baseline mobility.
- Baseline cognition.
- Baseline medication-management ability.
- Baseline home support.

Baseline functional status remains part of the approved baseline framework through mobility, cognition, medication-management ability, and home support.

Baseline blood pressure may be considered as a future candidate anchor during construction only. Do not create a numeric baseline blood pressure value at this stage.

This package does not create admission labs, hospital-course lab trends, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic files.

## Clinical Story Timeline Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`

Status: LOCKED.

Purpose: define the story-evolution framework from pre-admission decline through HD1-HD6, discharge, +7, and +30 anchors.

This package preserves the mixed-physiology model, multi-factorial near-fall model, medically improving but operationally dangerous tension, functional-decline failure target, prednisone source-of-truth ambiguity, and friction/trap separation.

It does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.

Carry-forward file-construction note:

- Trap #3 is buried functional/cognitive evidence: important evidence exists but is easy to miss.
- Trap #5 is a reassuring but incomplete discharge/source-hierarchy artifact: a visible artifact appears sufficient if trusted alone.
- Preserve this distinction when future files are constructed.

Completed construction-preparation chain:

- Key Milestones Calendar Skeleton: LOCKED.
- Baseline Anchor Package: LOCKED.
- Clinical Story Timeline Package: LOCKED.

## Task Architecture Interview v1

Artifact: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`

Status: COMPLETE / SUPERSEDED BY LOCKED TASK ARCHITECTURE PACKAGE.

Purpose: interview-only framework for resolving AutoQC 2.107 workflow-count constraints, AutoQC 2.108 administrative-deliverable requirements, final task distribution, and workflow consolidation strategy.

This artifact does not create tasks, task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

## Task Architecture Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`

Status: LOCKED.

Physician decisions:

- Target task count: 6.
- Target workflow count: 4 distinct workflows.
- Administrative deliverable: Discharge Planning / Care Coordination.
- TCM remains part of the Transition/Discharge workflow and does not become its own workflow.
- Consultant synthesis remains a distinct reasoning area.
- Readmission-risk reasoning lives inside existing workflow structures rather than creating a new workflow.
- Coding, billing, and prior authorization are not preferred unless later required by source material.

Candidate workflow architecture:

- Discharge Medication Reconciliation.
- Hospital Discharge Summary Generation.
- Discharge Planning Documentation.
- Interdisciplinary Care Plan Development and Documentation.

Carry-forward:

- AutoQC 2.108 remains a documented reviewer-risk bet, not a blocker.
- Discharge Planning Documentation / Care Coordination is the primary administrative deliverable.
- Utilization Review is contingency only if challenged later; do not add it now.
- Discharge Planning Documentation carries three task concepts and must be differentiated later by requester, time anchor, reasoning emphasis, and deliverable surface.

This package does not create task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

## Medication Expansion Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`

Decision addendum: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`

Status: LOCKED.

Purpose: baseline medication architecture targeting realistic 18-22 medication polypharmacy before medication schedules, reconciliation outputs, hospital-course medication changes, discharge lists, file inventory, or World Spec drafting.

Accepted physician decisions:

- Insulin lispro removed from baseline architecture.
- Insulin lispro reserved for future inpatient-only candidate use.
- Baseline medication count finalized at 20.
- Nitroglycerin retained.
- Polyethylene glycol retained.
- Senna retained.
- Cholecalciferol retained.

Preserved architecture:

- All other baseline medications preserved.
- All medication categories preserved.
- All trap architecture preserved.
- All friction architecture preserved.
- Baseline diabetes architecture remains metformin plus basal insulin.
- Future inpatient glycemic-management reasoning remains available for discharge and medication-reconciliation construction.

Carry-forward watch items:

- Future inpatient glycemic-management reasoning.
- Future medication reconciliation construction.
- Locked comorbidity architecture: 14 baseline conditions.
- AutoQC 2.107 workflow-count discipline.
- AutoQC 2.108 administrative-deliverable reviewer-risk contingency.

This package does not create doses, frequencies, schedules, medication timelines, admission medication lists, discharge medication lists, medication reconciliation outputs, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, templates, reference files, synthetic documents, or World Spec prose.

## Comorbidity Expansion Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`

Status: LOCKED.

Purpose: baseline chronic-condition architecture targeting approximately 12-15 comorbidities before labs, hospital-course events, task drafting, file planning, or World Spec drafting.

Ratified baseline comorbidity count: 14 conditions.

Preserved already-approved conditions:

- HFrEF.
- CAD.
- Hypertension.
- Hyperlipidemia.
- CKD stage 3.
- Type 2 diabetes mellitus.
- Diabetic peripheral neuropathy.
- Obstructive sleep apnea.
- Polymyalgia rheumatica.
- Anemia of CKD.
- Osteoporosis/osteopenia.

Retained secondary additions:

- Class I obesity by locked BMI 30.6.
- Chronic gastroesophageal reflux / chronic acid-suppression indication.
- Chronic constipation tendency.

Guardrails:

- These additions should remain secondary baseline complexity.
- They should not create new dominant arcs.
- They should not answer open clinical questions.
- They should not collapse the mixed physiology model.
- They should not convert the case into a single-cause explanation for the near-fall or discharge risk.

This package does not create labs, vitals, medication doses, medication schedules, hospital-course events, provider names, surgical history, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, templates, reference files, synthetic documents, or World Spec prose.

## Provider Roster Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/candidate-review/provider-roster-package-v1.md`

Status: CANDIDATE REVIEW.

Purpose: provider/care-team and stakeholder architecture before note authorship, file planning, task drafting, synthetic documents, or World Spec drafting.

Proposed named high-authority roles:

- Attending hospitalist: Dr. Elian Vossmere.
- Cardiology attending: Dr. Maris Caldrane.
- Nephrology attending: Dr. Iven Solthar.
- Endocrinology attending: Dr. Nerea Veylorn.
- Primary care physician: Dr. Talia Quenor.
- Outpatient rheumatology attending: Dr. Soren Halvek.
- Family/caregiver stakeholder: Mara Merrow.

Service-role placeholders:

- Hospitalist resident / covering clinician.
- Bedside nursing team.
- Physical Therapy.
- Occupational Therapy.
- Case Management.
- Social Work.
- Pharmacy / medication reconciliation pharmacist.

Guardrails:

- Named providers are architecture placeholders only.
- Service-role placeholders prevent over-naming minor or rotating contributors.
- Provider roster does not create notes, files, dates, task prompts, synthetic documents, or World Spec prose.

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
