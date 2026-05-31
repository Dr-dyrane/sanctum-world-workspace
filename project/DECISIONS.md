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

## 2026-05-31 - Baseline Anchor Package v1 Candidate Review

Decision: Baseline Anchor Package v1 is prepared for physician review as comparator anchors for later World Spec construction.

Artifact:

- `worlds/korvin-merrow/world-spec-prep/candidate-review/baseline-anchor-package-v1.md`

Candidate anchors:

- Baseline functional status.
- Baseline creatinine.
- Baseline eGFR.
- Baseline hemoglobin.
- Baseline A1c.
- Dry weight.
- Baseline mobility.
- Baseline cognition.
- Baseline medication-management ability.
- Baseline home support.

Status:

- Baseline Anchor Package v1: CANDIDATE REVIEW.

Boundaries:

- Candidate baseline anchors are not admission labs.
- Candidate baseline anchors are not hospital-course lab trends.
- This package does not create file inventory, task architecture, World Spec prose, prompts, golden responses, grader guidance, templates, reference files, or synthetic files.
