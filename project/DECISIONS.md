# Project Decisions

Record confirmed project decisions here.

## 2026-05-31 - Clinical Story Skeleton v1 Ratified

Decision: Clinical Story Skeleton v1 for Korvin Merrow is locked and ratified after Codex GO review and Claude hostile review minor findings.

Recommendation: GO to Identity Package and Governance Package preparation.

Artifacts:

- `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`

Ratified guardrails:

- Friction is Endocrinology vs Primary Team, not Endocrinology vs Documentation.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team remains balanced with defensible positions on both sides.
- Near-fall remains intentionally multi-factorial with no single intended explanation.

Boundaries:

- Do not draft World Spec yet.
- Do not create final file inventory.
- Do not create task prompts, golden responses, grader guidance, or synthetic chart files.

## 2026-05-31 - Identity Package v1 Locked

Decision: Identity Package v1 for Korvin Merrow is locked.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`

Locked values:

- Name: Korvin Merrow
- DOB: 1964-02-18
- Age: 62
- MRN: KM-6427819
- Height: 178 cm (5'10")
- Weight: 97 kg (214 lb)
- BMI: 30.6
- Allergy: Lisinopril (cough)
- Code Status: Full Code

Consistency:

- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- No conflict with approved Brainstorm or ratified Clinical Story Skeleton.

Boundaries:

- Do not draft World Spec yet.
- Do not create milestones, final file inventory, task prompts, golden responses, grader guidance, or synthetic chart files.

## 2026-05-31 - Identity Package Review Addendum Recorded

Decision: Claude Identity Package hostile-review observations are accepted as carry-forward implementation notes only. Identity Package v1 remains locked.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`

Carry-forward notes:

- Treat lisinopril cough as an ACE-inhibitor intolerance during World Spec construction.
- Provide a coherent prior ACE-inhibitor transition history for current ARNI therapy during Patient Profile / Clinical History design.
- Explicitly place baseline function, baseline creatinine, dry weight, and similar baseline anchors during Patient Profile / Clinical History design.

Boundaries:

- Do not change MRN, DOB, age, anthropometrics, allergy, or code status.
- Do not reopen Identity Package v1.
- Do not start Governance Package or World Spec drafting from these notes.

## 2026-05-31 - Governance Package v1 Ratified

Decision: Governance Package v1 is ratified before World Spec construction. Physician Architecture Layer is complete.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`

Locked candidate architecture:

- Care Team Roster: Hospitalist Service; Cardiology; Nephrology; Endocrinology; Physical Therapy; Occupational Therapy; Case Management; Social Work; Patient; Family/Caregiver; Primary Care Physician.
- Authority Hierarchy: attending hospitalist > consulting attending specialists > PT/OT functional assessments > Case Management / Social Work > family reports > patient recollection.
- Master Source-of-Truth Hierarchy for clinical facts: attending documentation > verified medication reconciliation > pharmacy history > consultant documentation > primary care documentation > family report > patient recollection.
- Prednisone-specific hierarchy remains rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Confirmed Conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.
- Presumed / Active Questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.
- Final Friction Table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.
- Administrative Deliverable Decision: yes.
- Workflow umbrella: Acute Hospital Management.

Boundaries:

- Do not draft World Spec yet.
- Do not create milestones, final file inventory, task prompts, reference files, golden responses, grader guidance, or synthetic chart files.

Clarifications:

- Authority Hierarchy and Source-of-Truth Hierarchy are distinct.
- Authority Hierarchy governs role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership.
- Source-of-Truth Hierarchy governs factual conflict resolution.
- Authority hierarchy resolves factual/documentation conflicts; it does not resolve clinical recommendation disagreements.
- Consultant disagreements must be reconciled through evidence synthesis, timing, trends, patient status, and discharge safety.
- Confirmed steroid-related osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current symptoms are primarily caused by adrenal suppression.
- AutoQC 2.107 workflow count and 2.108 administrative deliverable remain task-architecture watch items.

Ratification:

- Claude closeout review: would ratify today, YES.
- Claude final recommendation: GO.
- Governance Package v1 Status: RATIFIED.
- Physician Architecture Layer Status: COMPLETE.

Completed Architecture Layers:

- Brainstorm: APPROVED.
- Temporal Architecture: LOCKED.
- Clinical Story Skeleton: RATIFIED.
- Identity Package: LOCKED.
- Governance Package: RATIFIED.

Next legal phase recommendation:

- World Spec Construction Preparation.

## 2026-05-31 - Key Milestones Calendar Skeleton v1 Locked

Decision: Key Milestones Calendar Skeleton v1 is the locked canonical date framework for World Spec construction preparation.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`

Canonical anchors:

- Approximate decline begins: 04/27/2026.
- Admission / HD1: 05/18/2026.
- HD6 world snapshot: 05/23/2026 18:00.
- Discharge anchor: 05/24/2026.
- +7 day anchor: 05/31/2026.
- +30 day anchor: 06/23/2026.

Doctrine:

- +7 and +30 anchors are measured from discharge anchor 05/24/2026.
- They are not measured from HD6 world close.

Status:

- Key Milestones Calendar Skeleton v1: LOCKED.

Boundaries:

- Date framework only.
- Do not treat this as final World Spec prose, a final milestone table, task architecture, file inventory, prompts, goldens, grader guidance, or synthetic files.

## 2026-05-31 - Baseline Anchor Package v1 Locked

Decision: Baseline Anchor Package v1 is locked as comparator anchors for later World Spec construction.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`

Locked anchors:

- Baseline functional status.
- Baseline creatinine.
- Baseline eGFR.
- Baseline hemoglobin.
- Baseline A1c.
- Dry weight approximately 97 kg.
- Baseline mobility.
- Baseline cognition.
- Baseline medication-management ability.
- Baseline home support.

Status:

- Baseline Anchor Package v1: LOCKED.

Physician sign-off:

- Completed.
- Dry weight approximately 97 kg: APPROVED.
- Baseline anchor framework: APPROVED.

Claude ratification review:

- True defects: NONE.
- Blockers: NONE.
- Would lock today: YES.
- Final recommendation: GO.

Carry-forward note:

- Baseline blood pressure may be considered as a future candidate anchor during construction.
- Do not create a numeric baseline blood pressure value at this stage.

Boundaries:

- Baseline anchors are not admission labs.
- Baseline anchors are not hospital-course lab trends.
- This package does not create file inventory, task architecture, World Spec prose, prompts, golden responses, grader guidance, templates, reference files, or synthetic files.

## 2026-05-31 - Clinical Story Timeline Package v1 Candidate Review

Decision: Clinical Story Timeline Package v1 is created as the candidate story-evolution framework for World Spec construction preparation.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`

Purpose:

- Answer what changes over time from pre-admission decline through HD1-HD6, discharge, +7, and +30 anchors.
- Preserve mixed physiology, multi-factorial near-fall logic, medically improving but operationally dangerous discharge tension, functional-decline failure target, prednisone source-of-truth ambiguity, and friction/trap separation.

Status:

- Clinical Story Timeline Package v1: LOCKED.

## 2026-05-31 - Clinical Story Timeline Package v1 Ratification

Decision: Clinical Story Timeline Package v1 is ratified and locked.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`

Ratification:

- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`

Review basis:

- Cascade MCP Claude Review returned GO, LOCK READY, no true defects, no blockers.
- Claude Code Review returned GO, LOCK READY, no true defects, no blockers.

Carry-forward note:

- Preserve the distinction between Trap #3 and Trap #5 during future file construction.
- Trap #3 is buried functional/cognitive evidence: important evidence exists but is easy to miss.
- Trap #5 is a reassuring but incomplete discharge/source-hierarchy artifact: a visible artifact appears sufficient if trusted alone.

Construction-preparation chain:

- Key Milestones Calendar Skeleton: LOCKED.
- Baseline Anchor Package: LOCKED.
- Clinical Story Timeline Package: LOCKED.

Boundary:

- This decision does not authorize World Spec drafting, labs, vitals, medication schedules, file inventory, task architecture, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.

## 2026-05-31 - Task Architecture Interview v1 Planning Scaffold

Decision: create an interview-only framework for final task architecture decisions.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`

Purpose:

- Resolve AutoQC 2.107 workflow-count constraints.
- Resolve AutoQC 2.108 administrative-deliverable requirements.
- Frame final task distribution and workflow consolidation strategy before task drafting.

Status:

- Task Architecture Interview v1: historical planning scaffold.
- Task Architecture Package v1 is the authoritative locked architecture.
- `worlds/korvin-merrow/active/task-map.md` has been reconciled; old Brainstorm-level workflow mappings are superseded.

Boundary:

- This does not create tasks, task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

## 2026-05-31 - Task Architecture Package v1 Candidate Review

Decision: create formal task-architecture package from completed physician interview decisions.

Original candidate artifact:

- `worlds/korvin-merrow/world-spec-prep/candidate-review/task-architecture-package-v1.md`

Current artifact after ratification:

- `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`

Physician decisions recorded:

- Target task count: 6.
- Target workflow count: 4 distinct workflows.
- Administrative deliverable: Discharge Planning / Care Coordination.
- TCM remains part of the Transition/Discharge workflow and does not become its own workflow.
- Consultant synthesis remains distinct.
- Readmission-risk reasoning lives inside existing workflow structures rather than creating a new workflow.
- Coding, billing, and prior authorization are not preferred unless later required by source material.

Candidate workflow architecture:

- Discharge Medication Reconciliation.
- Hospital Discharge Summary Generation.
- Discharge Planning Documentation.
- Interdisciplinary Care Plan Development and Documentation.

Status:

- Task Architecture Package v1: CANDIDATE REVIEW at creation; later RATIFIED and LOCKED.

Boundary:

- This does not create task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

## 2026-05-31 - Task Architecture Package v1 Ratification

Decision: Task Architecture Package v1 is ratified and locked.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`

Ratification:

- `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`

Review basis:

- Two independent reviews returned GO, would ratify today YES, true defects none, and SEND BACK risks none.
- AutoQC 2.107 is resolved.
- Four workflows are exact approved catalog labels.
- TCM and readmission-risk reasoning are correctly embedded rather than separate workflows.

Locked workflows:

1. Discharge Medication Reconciliation.
2. Hospital Discharge Summary Generation.
3. Discharge Planning Documentation.
4. Interdisciplinary Care Plan Development and Documentation.

Carry-forward notes:

- AutoQC 2.108 remains a documented reviewer-risk bet, not a blocker.
- Primary administrative deliverable is Discharge Planning Documentation / Care Coordination.
- Utilization Review is contingency only if challenged later; do not add it now.
- Discharge Planning Documentation carries three task concepts and must be differentiated later by requester, time anchor, reasoning emphasis, and deliverable surface.

Construction-preparation chain:

- Key Milestones Calendar Skeleton: LOCKED.
- Baseline Anchor Package: LOCKED.
- Clinical Story Timeline Package: LOCKED.
- Task Architecture Package: LOCKED.

Boundary:

- This does not authorize task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec drafting, templates, reference files, or synthetic documents.

Boundaries:

- Does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, milestones beyond locked dates, World Spec prose, prompts, golden responses, grader guidance, templates, reference files, or synthetic documents.

## 2026-06-02 - Cross-Artifact Consistency Verification Rule Recorded

Decision: Cross-artifact consistency verification is a standing governance rule for Korvin Merrow architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, and governance work.

Artifacts:

- `AGENTS.md`
- `project/PHASE_MAP.md`
- `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`

Rule:

- Before creating, modifying, ratifying, or locking applicable governance artifacts, cross-check locked canonical sources: World Spec, Governance Package, File Inventory, Architecture Packages, ratified review decisions, and previously reconciled governance decisions.
- If proposed work expands, narrows, redistributes, reprioritizes, relabels, or reclassifies trap coverage, friction coverage, workflow coverage, priority tiers, source-of-truth mappings, authority hierarchies, file responsibilities, inventory rows, or matrix entries, the change must be supported by a locked canonical source and cited, or the discrepancy must be surfaced and documented before artifact creation, ratification, or lock.
- Do not silently broaden coverage.
- Do not silently narrow coverage.
- Do not silently reinterpret inventory rows.
- Do not silently promote historical, planning, superseded, tracker, or provenance metadata into governing architecture.

Associated reconciliation:

- FI-T inventory / task-layer architecture reconciliation aligned File Inventory metadata with locked Task Architecture Package v1 for FI-T02, FI-T04, FI-T05, and FI-T06 secondary trap/friction support.
- Task-Level Context File Architecture v1 treats P0/P1/P2 labels as tracker-provenance metadata only.

Boundaries:

- This does not create FI-T files, FI-S files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or task outputs.
- This reconciliation did not itself ratify or lock Task-Level Context File Architecture v1; ratification occurred later in the 2026-06-02 lock decision below.
- This does not change source-of-truth hierarchy, authority hierarchy, prednisone hierarchy, or workflow count.

## 2026-06-02 - Task-Level Context File Architecture v1 Locked

Decision: Task-Level Context File Architecture v1 is ratified and locked.

Artifacts:

- `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`
- `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`
- `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`

Review basis:

- Reviewer B: LOCK READY / GO.
- Reviewer A recertification: LOCK READY / GO.
- Reconciliation status: COMPLETE.
- True defects: NONE.

Status:

- Task-Level Context File Architecture v1: LOCKED.
- Task-Level Context File Architecture: COMPLETE.

Next eligible phase:

- Task-Level Context File Construction.

Boundaries:

- Historical boundary at architecture lock: do not create FI-T01 through FI-T07 until explicitly authorized. Superseded by the later Task-Level Context File Construction authorization and candidate construction record below.
- Do not create FI-S01 through FI-S04 until explicitly authorized.
- Do not create task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or final task outputs until explicitly authorized.
- This lock does not change source-of-truth hierarchy, authority hierarchy, prednisone hierarchy, medication-restart uncertainty, or the locked four-workflow architecture.

## 2026-06-02 - Task-Level Context File Construction Candidate Review

Decision: Task-Level Context File Construction is complete for candidate review.

Artifacts:

- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T01_discharge-medication-reconciliation-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T02_discharge-summary-drafting-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T03_discharge-readiness-care-coordination-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T05_early-post-discharge-follow-up-assessment-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T06_patient-safety-readmission-risk-review-request-context.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/FI-T07_medication-safety-handoff-task-context-addendum.md`
- `worlds/korvin-merrow/task-context-files/candidate-review/task-context-files-validation-review.md`

Status:

- Task-Level Context File Construction: CANDIDATE REVIEW.
- FI-T01 through FI-T07: CANDIDATE REVIEW.

Construction basis:

- Locked Task-Level Context File Architecture v1.
- Locked File Inventory v1.
- Locked World Spec v1.
- Ratified Governance Package v1.
- Locked FI-W01 through FI-W22.
- Ratifications and reconciliation records.

Validation findings:

- FI-T01 through FI-T07 are request-framing / task-context files only.
- Each FI-T forces synthesis across locked world files.
- No FI-T replaces FI-W01 through FI-W22.
- FI-W22 remains visible but incomplete.
- All five traps, all three frictions, source hierarchies, and physician-perspective framing are preserved.

Next eligible phase:

- Task-Level Context File Construction Review.

Boundaries:

- Do not lock FI-T files until explicitly authorized.
- Do not create FI-S files, supplementary files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or final task outputs until explicitly authorized.

## 2026-06-02 - Task-Level Context File Construction Locked

Decision: Task-Level Context File Construction is ratified and locked.

Artifacts:

- `worlds/korvin-merrow/task-context-files/locked/FI-T01_discharge-medication-reconciliation-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T02_discharge-summary-drafting-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T03_discharge-readiness-care-coordination-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T05_early-post-discharge-follow-up-assessment-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T06_patient-safety-readmission-risk-review-request-context.md`
- `worlds/korvin-merrow/task-context-files/locked/FI-T07_medication-safety-handoff-task-context-addendum.md`
- `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md`
- `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md`

Review basis:

- Reviewer A: LOCK READY / GO.
- Reviewer B: Clinical Architecture Status STRONG; Final Recommendation GO WITH MINOR NOTES.
- Carry-forward watch items recorded in `task-context-files-validation-review.md`.
- True defects: NONE.
- Architecture defects: NONE.
- Governance defects: NONE.

Status:

- Task-Level Context File Construction: LOCKED.
- FI-T01 through FI-T07: LOCKED.
- Task-Level Context Files: COMPLETE.

Next eligible phase:

- Supplementary File Architecture / Construction.

Boundaries:

- Do not create FI-S files, supplementary files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or final task outputs until explicitly authorized.

## 2026-06-02 - Supplementary File Architecture v1 Candidate Review

Decision: Supplementary File Architecture v1 is created for candidate review.

Artifacts:

- `worlds/korvin-merrow/supplementary-file-architecture/candidate-review/supplementary-file-architecture-v1.md`
- `worlds/korvin-merrow/supplementary-file-architecture/candidate-review/supplementary-file-architecture-validation-review.md`

Architecture basis:

- Locked World Spec v1.
- Ratified Governance Package v1.
- Locked File Inventory Architecture v1.
- Locked File Inventory v1.
- Locked Task-Level Context File Architecture v1.
- Locked FI-W01 through FI-W22.
- Locked FI-T01 through FI-T07.
- Ratification and reconciliation records.

Status:

- Supplementary File Architecture v1: CANDIDATE REVIEW.

Determinations:

- Supplementary files are required for the planned file ecosystem because locked File Inventory v1 contains four FI-S rows.
- Exact FI-S count: 4.
- Future FI-S rows: FI-S01 through FI-S04.
- No FI-S files were constructed.

Next eligible phase:

- Supplementary File Architecture Review.

Boundaries:

- Do not lock Supplementary File Architecture v1 until explicitly authorized.
- Do not create FI-S files, supplementary files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or final task outputs until explicitly authorized.
