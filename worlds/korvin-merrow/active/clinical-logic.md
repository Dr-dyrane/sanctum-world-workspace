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

Preparation Layer Status: COMPLETE.

World Spec Construction Status: COMPLETE.

World Spec Skeleton v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`, with ratification recorded at `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`.

World Spec v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`, with ratification recorded at `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`.

World Spec Skeleton Phase Status: COMPLETE.

World Spec v1 Status: LOCKED.

File Inventory Architecture v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`.
- Ratification: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`.
- Purpose: planned file ecosystem only, defining world-level, task-level, and supplementary/noise file categories needed to support the locked World Spec, workflows, traps, frictions, source hierarchy, and temporal architecture.
- It does not create final Section 3 rows, filenames, synthetic files, notes, labs, vitals, medication lists, discharge summaries, task prompts, expected outputs, goldens, grader guidance, reference files, templates, DOCX artifacts, AutoQC responses, or RL Studio submissions.
- Phase 3 File Inventory Architecture is complete.
- File Inventory v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`.
- File Inventory v1 ratification is recorded at `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md`.
- File Inventory Planning is complete.
- Synthetic World-Level File Construction Plan v1 is locked at `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`.
- Synthetic World-Level File Construction Plan v1 ratification is recorded at `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`.
- Synthetic File Construction Governance is complete.
- Batch 1 synthetic world-level files FI-W01 through FI-W07 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-1/`.
- Batch 1 validation review is recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`.
- Batch 1 ratification is recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md`.
- Batch 1 Construction is complete.
- Batch 2 synthetic world-level files FI-W08 through FI-W13 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-2/`.
- Batch 2 ratification is recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md`.
- Batch 2 validation review is recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`.
- Batch 2 Construction is complete.
- Batch 3 files FI-W14 through FI-W16 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-3/`.
- Batch 3 validation review is recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md`.
- Batch 3 ratification is recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md`.
- Batch 3 Construction status is complete.
- Batch 4 files FI-W17 through FI-W21 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-4/`.
- Batch 4 validation review is recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md`.
- Batch 4 ratification is recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`.
- Batch 4 Construction status is complete.
- FI-W20 File Inventory row reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/fi-w20-inventory-row-reconciliation.md`; the row now explicitly includes secondary/collateral Trap #1 and Endocrinology vs Primary Team support through lower-authority family report without changing the synthetic FI-W20 file or prednisone hierarchy.
- FI-T inventory / task-layer architecture reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`; the metadata update aligns FI-T02, FI-T04, FI-T05, and FI-T06 secondary trap/friction support with locked Task Architecture Package v1 and clarifies that P0/P1/P2 labels are tracker provenance only.
- Batch 5 FI-W22 is locked at `worlds/korvin-merrow/synthetic-files/locked/batch-5/FI-W22_discharge-facing-plan-snapshot-before-world-close.md`.
- Batch 5 validation review is at `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md`.
- Batch 5 ratification is at `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md`.
- World-Level Synthetic File Layer is complete with FI-W01 through FI-W22 locked.
- World-Level Layer Closure Audit passed at `worlds/korvin-merrow/reviews/world-level-layer-closure-audit.md`.
- Task-Level Context File Architecture v1 is locked at `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`.
- Task-Level Context File Architecture v1 ratification is recorded at `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`.
- Task-Level Context File Architecture status is complete.
- Task-Level Context File Construction is locked at `worlds/korvin-merrow/task-context-files/locked/`.
- Task-Level Context File Construction ratification is recorded at `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md`.
- Task-Level Context Files status is complete.
- Supplementary File Architecture v1 is locked at `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-v1.md`.
- Supplementary File Architecture validation review is locked at `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md`.
- Supplementary File Architecture ratification is recorded at `worlds/korvin-merrow/supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md`.
- FI-S03 Trap #5 reconciliation is complete at `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md`.
- Supplementary File Architecture determines FI-S count as four, matching locked File Inventory v1: FI-S01 through FI-S04.
- Supplementary File Construction is locked at `worlds/korvin-merrow/supplementary-files/locked/`.
- FI-S01 through FI-S04 and `supplementary-file-construction-validation-review.md` are locked artifacts.
- Supplementary File Construction ratification is recorded at `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md`.
- Supplementary Files status is complete.
- Entire File Ecosystem status is complete.
- Completed File Ecosystem: FI-W01 through FI-W22, FI-T01 through FI-T07, and FI-S01 through FI-S04.
- Task Prompt Architecture v1 is locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation review at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md`.
- Task Prompt Architecture ratification is recorded at `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`.
- Task Prompt Architecture status is complete.
- Task Prompt Construction status is locked at `worlds/korvin-merrow/task-prompts/locked/`.
- Files locked: TP-KM01 through TP-KM06 plus `task-prompt-construction-validation-review.md`.
- Task Prompt Construction ratification is recorded at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`.
- Task Prompts status is complete.
- Expected Output Architecture v1 status is locked at `worlds/korvin-merrow/expected-output-architecture/locked/`.
- Locked files: `expected-output-architecture-v1.md` and `expected-output-architecture-validation-review.md`.
- Ratification is recorded at `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`.
- Expected Output Architecture status is complete.
- Expected Output Construction status is LOCKED.
- Locked files are under `worlds/korvin-merrow/expected-outputs/locked/`.
- Files locked: EO-KM01 through EO-KM06 plus `expected-output-construction-validation-review.md`.
- Ratification is recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`.
- Expected Outputs status is complete.
- FI-T07 remains addendum support for EO-KM01 only; no EO-KM07 exists.
- Golden Architecture v1 is locked at `worlds/korvin-merrow/golden-architecture/locked/`, with ratification recorded at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`.
- Golden Architecture status is COMPLETE.
- Golden Construction status is LOCKED at `worlds/korvin-merrow/goldens/locked/`.
- Goldens status is COMPLETE.
- Grader Guidance Architecture v1 is locked at `worlds/korvin-merrow/grader-guidance-architecture/locked/`.
- Grader Guidance Architecture ratification is recorded at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`.
- Grader Guidance Construction status is LOCKED at `worlds/korvin-merrow/grader-guidance/locked/`.
- Grader Guidance Construction ratification is recorded at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`.
- Grader Guidance status is COMPLETE.
- Files constructed: GG-KM01 through GG-KM06 plus `grader-guidance-construction-validation-review.md`.
- AutoQC Architecture v1 is LOCKED at `worlds/korvin-merrow/autoqc-architecture/locked/`.
- AutoQC Architecture v1 ratification is recorded at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`.
- AutoQC Architecture status is COMPLETE.
- AutoQC Construction is LOCKED at `worlds/korvin-merrow/autoqc/locked/`.
- AutoQC Construction ratification is recorded at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`.
- AutoQC status is COMPLETE.
- Packaging Architecture v1 is in CANDIDATE REVIEW at `worlds/korvin-merrow/packaging-architecture/candidate-review/`.
- Next eligible phase is Packaging Architecture Review.
- AutoQC runs, AutoQC responses, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, DOCX artifacts, and RL Studio submission remain blocked pending explicit Alexander authorization.

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

Task-design physician-perspective guidance:

- Status: FUTURE TASK-LAYER RULE.
- Classification: not a source-of-truth hierarchy rule and not a governance redesign.
- Source-of-truth hierarchy answers: "When sources disagree, which evidence source is authoritative?"
- Task-design guidance answers: "Who is the final deliverable written by or for?"
- Future task prompts, expected outputs, goldens, and grader guidance must frame final deliverables from the physician perspective or physician voice.
- Supporting sources may come from pharmacy, nursing, PT/OT, case management, social work, family, or healthcare administration, but the deliverable must remain physician-authored, physician-reviewed, physician-supervised, or physician-communicated.
- Current locked workflows remain compatible: Discharge Medication Reconciliation, Hospital Discharge Summary Generation, Discharge Planning Documentation, and Interdisciplinary Care Plan Development and Documentation.
- Do not redesign the world, reopen Governance Package v1, or alter source-of-truth hierarchy because of this guidance.

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

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`

Status: LOCKED.

Purpose: provider/care-team and stakeholder architecture before note authorship, file planning, task drafting, synthetic documents, or World Spec drafting.

Locked named high-authority roles:

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

- Shared Merrow surname for Korvin Merrow and Mara Merrow is intentionally approved.
- Named providers are architecture placeholders only.
- Service-role placeholders prevent over-naming minor or rotating contributors.
- Resident remains role-based.
- Pharmacy remains role-based.
- No additional provider naming is authorized.
- Provider roster does not create notes, files, dates, task prompts, synthetic documents, or World Spec prose.

## Surgical History Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`

Status: LOCKED.

Purpose: pre-world surgical/procedural history architecture before Daily Hospital Course Framework, World Spec construction, file inventory planning, synthetic documents, task prompts, expected outputs, goldens, or grader guidance.

Confirmed surgical/procedural anchors:

- Remote percutaneous coronary intervention with coronary stent placement.
- Remote diagnostic sleep study confirming obstructive sleep apnea.

Excluded / noise-controlled procedures:

- ICD / CRT / pacemaker.
- Coronary artery bypass grafting.
- Dialysis access creation or kidney procedure.
- Major orthopedic fracture repair or joint replacement.
- Limb amputation or major diabetic foot surgery.
- Temporal artery biopsy or rheumatologic diagnostic procedure.
- Screening colonoscopy for v1 purposes.

Guardrails:

- Surgical/procedural history should stay clinically realistic but quiet.
- Keep PCI remote so aspirin-only baseline remains consistent.
- Procedural provenance should be decided during future file inventory architecture.
- PCI supports established CAD, chronic cardiovascular medication rationale, and cardiology involvement.
- Sleep study supports locked OSA diagnosis and baseline reserve context.
- Surgical history must not create a new dominant disease arc.
- Surgical history must not explain the admission, near-fall, weakness, hypotension, altered mental status, steroid concern, AKI, or discharge readiness by itself.
- Surgical history does not create operative reports, procedure notes, hospital-course events, file inventory, task prompts, synthetic documents, or World Spec prose.

## Daily Hospital Course Framework v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`

Status: LOCKED.

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`

Purpose: canonical HD1-HD6 evolution model between locked architecture and later World Spec/file/task construction.

Scope:

- Defines what changes on each hospital day.
- Captures daily clinical state, changes, improvements, remaining concerns, active frictions, active traps, relevant provider groups, and disposition readiness.
- Preserves the improving but not safely solved design principle.
- Preserves mixed physiology and no hidden single answer.
- Preserves Trap #3 vs Trap #5 distinction.

Boundaries:

- Does not create labs, lab trends, vitals, medication doses, medication schedules, medication orders, consultant notes, discharge summaries, operative reports, procedure notes, file inventory, tasks, prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files.

Preparation Layer:

- Status: COMPLETE.
- Daily Hospital Course Framework v1 completes the preparation layer before World Spec construction.
- World Spec Construction is complete after World Spec v1 lock; downstream artifacts remain unstarted until specifically authorized.

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

## Synthetic World-Level Files

Batch 1 Synthetic World-Level File Construction:

- Status: LOCKED.
- Locked files: FI-W01 through FI-W07.
- Canonical folder: `worlds/korvin-merrow/synthetic-files/locked/batch-1/`.
- Validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`.

Batch 2 Synthetic World-Level File Construction:

- Status: LOCKED.
- Files locked: FI-W08 through FI-W13.
- Locked folder: `worlds/korvin-merrow/synthetic-files/locked/batch-2/`.
- Ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md`.
- Validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`.
- Batch 2 Construction: COMPLETE.

Batch 2 clinical logic:

- Builds the HD1-HD6 hospital-course spine.
- Preserves infection-versus-mixed-physiology uncertainty.
- Preserves steroid-versus-nonsteroid uncertainty.
- Strengthens HF/AKI medication-restart substrate without creating a final medication plan.
- Preserves baseline-versus-admission-value separation.
- Preserves Trap #3 as buried functional/cognitive evidence and Trap #5 as visible but incomplete discharge/source-hierarchy reasoning.
- Uses FI-W06 outpatient rheumatology provenance only according to the locked HD4 availability constraint.

Batch 3 Synthetic World-Level File Construction:

- Status: LOCKED.
- Files locked: FI-W14 through FI-W16.
- Locked folder: `worlds/korvin-merrow/synthetic-files/locked/batch-3/`.
- Validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md`.
- Ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md`.
- Batch 3 Construction status: COMPLETE.

Batch 3 clinical logic:

- Builds the consultant layer on top of the Batch 1 provenance and Batch 2 hospital-course spine.
- Preserves Cardiology vs Nephrology as a defensible timing and risk-balancing friction.
- Preserves Endocrinology vs Primary Team as steroid-risk interpretation, not a hidden diagnosis reveal.
- Preserves hospitalist-synthesizes-not-defers governance.
- Preserves FI-W12 trend data and FI-W13 MAR/action data as inputs, not final answers.

Boundary:

- FI-T01 through FI-T07, supplementary files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, submission materials, and RL Studio activity remain blocked until explicitly authorized.

Batch 4 Synthetic World-Level File Construction:

- Status: LOCKED.
- Files locked: FI-W17 through FI-W21.
- Locked folder: `worlds/korvin-merrow/synthetic-files/locked/batch-4/`.
- Validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md`.
- Ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`.
- Batch 4 Construction status: COMPLETE.

Batch 4 clinical logic:

- Carries the functional, cognitive, caregiver, and discharge-readiness substrate.
- Preserves Trap #3 as buried-but-discoverable evidence distributed across nursing, PT, OT, family, and case management/social work.
- Preserves Trap #3 vs Trap #5 by avoiding a visible discharge-facing artifact inside Batch 4; FI-W22 carries that visible-but-incomplete role as a locked Batch 5 file.
- Preserves Family vs Primary Team as a balanced friction rather than making either side obviously correct.
- Preserves medication-restart uncertainty, prednisone uncertainty, insulin lispro inpatient-only logic, and consultant caveat synthesis.
- FI-W20's collateral steroid-history role remains lower-authority family report. It supports Trap #1 and Endocrinology vs Primary Team without becoming a prednisone source-of-truth file, endocrine answer file, or override of rheumatology provenance.

Batch 5 Synthetic World-Level File Construction:

- Status: LOCKED.
- File locked: FI-W22.
- Locked folder: `worlds/korvin-merrow/synthetic-files/locked/batch-5/`.
- Validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md`.
- Ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md`.
- Batch 5 Construction status: COMPLETE.
- World-Level Synthetic File Layer status: COMPLETE.
- Completed World-Level Files: FI-W01 through FI-W22.

Batch 5 clinical logic:

- Implements Trap #5 as the visible but incomplete discharge-facing artifact.
- Preserves FI-W22 as useful, readable, and reassuring enough to be over-trusted by a superficial reviewer.
- Does not duplicate the distributed Trap #3 substrate from nursing, PT, OT, family, and case management/social work.
- Does not resolve final disposition, medication restart timing, prednisone history, consultant disagreement, family concern, functional support level, or service sufficiency.
- Preserves FI-W12 trend data and FI-W13 MAR/action source as inputs rather than final answers.
- Preserves rheumatology as the highest outpatient prednisone authority.
- Preserves all three frictions and hospitalist-synthesizes-not-defers governance.

Boundary:

- FI-W22 is locked and the world-level synthetic file layer is complete. Task-Level Context File Architecture v1 is locked and complete. FI-T01 through FI-T07 are locked at `worlds/korvin-merrow/task-context-files/locked/`, with ratification recorded at `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md`. FI-S01 through FI-S04 are locked at `worlds/korvin-merrow/supplementary-files/locked/`, with ratification recorded at `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md`. Entire File Ecosystem is complete. Task Prompt Architecture v1 is locked and complete. Task Prompt Construction is locked at `worlds/korvin-merrow/task-prompts/locked/` with TP-KM01 through TP-KM06 locked. Task Prompt Construction ratification is recorded at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`. Expected Output Architecture v1 is locked. Expected Output Construction is locked at `worlds/korvin-merrow/expected-outputs/locked/` with EO-KM01 through EO-KM06 locked. Golden Construction is locked at `worlds/korvin-merrow/goldens/locked/` with ratification recorded at `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`. Grader Guidance Construction is locked with GG-KM01 through GG-KM06 under `worlds/korvin-merrow/grader-guidance/locked/`, with ratification recorded at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`. AutoQC Architecture v1 is locked under `worlds/korvin-merrow/autoqc-architecture/locked/`, with ratification recorded at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Construction is locked under `worlds/korvin-merrow/autoqc/locked/`, with ratification recorded at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC is complete. Do not run AutoQC, create AutoQC responses, create rubrics, create DOCX artifacts, create submission materials, or conduct RL Studio activity until explicitly authorized.

Task-Level Context File Architecture v1:

- Status: LOCKED.
- Locked path: `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`.
- Ratification: `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`.
- Purpose: define future FI-T01 through FI-T07 architecture only.
- It does not construct FI-T files, FI-S files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or final task outputs.
- Task-level context files must frame requester/date/workflow context without backfilling missing world evidence.
- FI-W22 must remain visible but incomplete and must not become a task answer file.
- Trap #3 remains buried functional/cognitive evidence; Trap #5 remains over-trust of a visible but incomplete discharge-facing source.
- Prednisone hierarchy, master source-of-truth hierarchy, authority hierarchy, and medication-restart uncertainty remain unchanged.
- P0/P1/P2 labels are tracker-provenance metadata only; they do not create new workflow categories or override locked Task Architecture Package v1.
- Cross-artifact consistency verification is a standing governance rule before any future architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, or governance artifact is created, modified, ratified, or locked.
- Task-Level Context File Architecture status: COMPLETE.
- Task-Level Context File Construction status: LOCKED.
- Locked files: FI-T01 through FI-T07 at `worlds/korvin-merrow/task-context-files/locked/`.
- Validation review: `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md`.
- Ratification: `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md`.
- Task-Level Context Files status: COMPLETE.
- Supplementary File Architecture status: COMPLETE.
- Locked architecture: `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-v1.md`.
- Locked validation review: `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md`.
- Ratification: `worlds/korvin-merrow/supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md`.
- FI-S03 Trap #5 reconciliation: `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md`.
- Supplementary File Construction: LOCKED.
- Locked files: `worlds/korvin-merrow/supplementary-files/locked/`.
- Files locked: FI-S01 through FI-S04 plus `supplementary-file-construction-validation-review.md`.
- Ratification: `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md`.
- Supplementary Files: COMPLETE.
- Entire File Ecosystem: COMPLETE.
- Task Prompt Architecture v1: LOCKED.
- Task Prompt Architecture: COMPLETE.
- Task Prompt Construction: LOCKED.
- Locked files: `worlds/korvin-merrow/task-prompts/locked/`.
- Files locked: TP-KM01 through TP-KM06 plus `task-prompt-construction-validation-review.md`.
- Task Prompts: COMPLETE.
- Expected Output Architecture v1: LOCKED.
- Locked files: `worlds/korvin-merrow/expected-output-architecture/locked/`.
- Ratification: `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`.
- Expected Output Architecture: COMPLETE.
- Expected Output Construction: LOCKED.
- Locked files: EO-KM01 through EO-KM06 plus `expected-output-construction-validation-review.md` at `worlds/korvin-merrow/expected-outputs/locked/`.
- Ratification: `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`.
- Expected Outputs: COMPLETE.
- Golden Architecture v1 is locked at `worlds/korvin-merrow/golden-architecture/locked/`, with audit reconciliation preserved there and ratification recorded at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`.
- Golden Architecture status: COMPLETE.
- Golden Construction status: LOCKED.
- Locked files: Golden-KM01 through Golden-KM06 plus `golden-construction-validation-review.md` at `worlds/korvin-merrow/goldens/locked/`.
- Ratification: `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`.
- Goldens status: COMPLETE.
- Golden Construction preserves medication algorithm nuance, Cardiology vs Nephrology tension, prednisone hierarchy, FI-W22 visible-but-incomplete status, FI-S supporting/background status, no invented follow-up facts, and no retrospective outcome invention.
- Grader Guidance Architecture v1 is locked at `worlds/korvin-merrow/grader-guidance-architecture/locked/`.
- Grader Guidance Architecture ratification is recorded at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`.
- Grader Guidance Architecture v1 preserves the principle that future grader guidance should reward strong physician reasoning rather than verbatim matching to the golden.
- Architecture guardrails: no GG-KM07, FI-T07 remains addendum support for GG-KM01 only, FI-W22 remains visible but incomplete, FI-S files remain background/supporting only, hierarchy remains reasoning rather than shortcut logic, and frictions remain defensible disagreements rather than automatic winner selection.
- Grader Guidance Construction is LOCKED at `worlds/korvin-merrow/grader-guidance/locked/`.
- Files constructed: GG-KM01 through GG-KM06 plus `grader-guidance-construction-validation-review.md`.
- No GG-KM07, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, AutoQC responses, DOCX artifacts, submission materials, or RL Studio activity have been created.
- AutoQC Architecture v1 is LOCKED at `worlds/korvin-merrow/autoqc-architecture/locked/`.
- AutoQC Construction is LOCKED at `worlds/korvin-merrow/autoqc/locked/`.
- AutoQC status is COMPLETE.
- Packaging Architecture v1 is in CANDIDATE REVIEW at `worlds/korvin-merrow/packaging-architecture/candidate-review/`.
- Next eligible phase: Packaging Architecture Review.

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
