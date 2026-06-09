# Governance Package v1

Date: 2026-05-31

Status: RATIFIED.

Purpose: formalize physician-approved governance architecture before World Spec construction.

This document does not draft the World Spec, create a final file inventory, create tasks, create milestones, create reference files, write prompts, create golden responses, create grader guidance, or generate synthetic files.

## Inputs

- Approved Brainstorm.
- Brainstorm Human Review GO from Stacey S.
- Ratified Clinical Story Skeleton v1.
- Locked Identity Package v1.
- Identity Package review addendum.
- Governance Package clarification.
- Governance Package ratification.
- World Spec AutoQC v6.3 watch items.

## 1. Care Team Roster

Primary Team:

- Hospitalist Service.

Consultants:

- Cardiology.
- Nephrology.
- Endocrinology.

Functional Team:

- Physical Therapy.
- Occupational Therapy.

Transition Team:

- Case Management.
- Social Work.

Stakeholders:

- Patient.
- Family/Caregiver.
- Primary Care Physician.

## 2. Authority Hierarchy

Approved authority ordering:

1. Attending Hospitalist.
2. Consulting Attending Specialists.
3. PT/OT Functional Assessments.
4. Case Management / Social Work.
5. Family Reports.
6. Patient Recollection.

Implementation note: this is a governance hierarchy for role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership during World Spec construction.

Operational rule: authority hierarchy resolves factual/documentation conflicts. Authority hierarchy does not resolve clinical recommendation disagreements. Consultant disagreements must be reconciled through evidence synthesis, timing, trends, patient status, and discharge safety, not by automatically deferring to the highest-ranked authority.

## 3. Master Source-of-Truth Hierarchy

Clinical facts:

1. Attending Documentation.
2. Verified Medication Reconciliation.
3. Pharmacy History.
4. Consultant Documentation.
5. Primary Care Documentation.
6. Family Report.
7. Patient Recollection.

Preserved prednisone-specific hierarchy:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

Implementation note: the master hierarchy governs factual conflict resolution, especially medication history, outpatient records, consultant documentation, family reports, and patient recollection. The prednisone hierarchy remains the more specific hierarchy for the steroid timeline/source-of-truth trap.

Authority hierarchy vs source-of-truth hierarchy: Authority Hierarchy is used for role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership. Source-of-Truth Hierarchy is used for factual conflict resolution. If both appear relevant, the World Spec must state which hierarchy governs the task or trap.

## 4. Confirmed Conditions

- HFrEF.
- CKD Stage 3.
- Type 2 Diabetes.
- CAD.
- Hypertension.
- Hyperlipidemia.
- OSA.
- Diabetic Neuropathy.
- PMR.
- Anemia of CKD.
- Osteoporosis/Osteopenia.

## 5. Presumed / Active Questions

- Current infection source.
- Steroid contribution.
- Adrenal suppression contribution.
- Degree of dehydration.
- Relative medication contribution.
- Discharge readiness.

Implementation note: these are unresolved interpretive questions for the world design. They should remain clinically uncertain where appropriate and should not be converted into a single hidden diagnosis.

Steroid-related bone disease clarification: confirmed osteoporosis/osteopenia reflects cumulative chronic steroid exposure. It does not prove that current symptoms are primarily caused by adrenal suppression. Current adrenal/steroid contribution remains an active interpretive question.

## 6. Final Friction Table

| Friction | Topic | Stakeholder 1 Position | Stakeholder 2 Position | Governance Guardrail |
| --- | --- | --- | --- | --- |
| Cardiology vs Nephrology | Medication restart timing | Cardiology favors restarting GDMT sooner to protect HFrEF/CAD and reduce decompensation/readmission risk. | Nephrology prioritizes renal recovery, hypotension avoidance, and safe timing after AKI on CKD. | Both positions are reasonable; correct reasoning reconciles timing, trends, and discharge safety. |
| Family vs Primary Team | Discharge readiness | Family emphasizes not back to baseline, functional concerns, cognition, and real-world home safety. | Primary Team emphasizes infection improvement, AKI improvement, mental status improvement, oral intake improvement, and available follow-up. | Both positions are defensible; the world should not make discharge obviously safe or obviously unsafe. |
| Endocrinology vs Primary Team | Steroid interpretation and risk | Endocrinology warns steroid contribution/adrenal suppression may be underappreciated given PMR prednisone history and persistent symptoms. | Primary Team wants to avoid over-attributing symptoms to steroids after sepsis-oriented management produces improvement. | Steroid discrepancy remains a trap; the friction is the human-to-human risk interpretation. |

## 7. Consultant Disagreement Themes

Cardiology:

- Restart GDMT sooner.

Nephrology:

- Prioritize renal recovery.

Endocrinology:

- Steroid contribution may be underappreciated.

Hospitalist:

- Must reconcile competing recommendations.

## 8. Administrative Deliverable Decision

Decision: YES.

At least one future task should involve:

- Transition of care.
- Discharge planning.
- Care coordination.
- Follow-up planning.

Implementation note: this supports AutoQC expectations that a typical clinical world include a mix of clinical and healthcare administration work products where appropriate. This does not create task prompts or final task specifications.

## 9. Workflow Consolidation

Single workflow umbrella:

- Acute Hospital Management.

Subdomains:

- Diagnosis.
- Medication management.
- Consultant synthesis.
- Functional assessment.
- Disposition planning.

Implementation note: this is a governance umbrella for coherence. Final World Spec task workflow lines must still use exact approved tracker workflow names and must satisfy the 3-5 distinct catalog workflow constraint.

Task-architecture watch items:

- AutoQC 2.107 workflow count must be resolved during task architecture.
- AutoQC 2.108 administrative deliverable must be secured during task architecture.
- Do not attempt to solve final task workflow count or administrative deliverable design inside Governance Package v1.

## Governance Consistency Review

### VERIFIED

Finding: care team roster matches the approved Brainstorm and ratified Clinical Story Skeleton.

Evidence: the roster includes Hospitalist Service, Cardiology, Nephrology, Endocrinology, PT/OT, Case Management/Social Work, family/caregiver, patient, and PCP, all of which are already part of the approved world logic or rough task concepts.

Impact: supports AutoQC care-team expectations and avoids unsupported consultants.

Action required: when World Spec drafting is authorized, ensure every named consultant or team appears consistently in Patient Profile, Clinical Complexity Overview, and task/file logic.

### VERIFIED

Finding: authority and source-of-truth hierarchies directly address source ambiguity and authority-trap risk.

Evidence: the master hierarchy and preserved prednisone hierarchy specify how to interpret attending documentation, med rec, pharmacy history, consultant documentation, primary care documentation, family report, and patient recollection.

Impact: supports AutoQC source-of-truth hierarchy requirements for authority traps.

Action required: carry these hierarchies into Patient Profile / Clinical Complexity Overview when World Spec drafting is authorized.

### VERIFIED

Finding: PCP is now represented in the source-of-truth hierarchy.

Evidence: Primary Care Documentation is placed after Consultant Documentation and before Family Report.

Impact: PCP longitudinal information can be considered without creating a gap between the care team roster and factual hierarchy.

Action required: later World Spec construction should use PCP documentation for longitudinal outpatient facts when appropriate.

### VERIFIED

Finding: authority hierarchy and source-of-truth hierarchy are explicitly distinguished.

Evidence: Governance Package v1 now states Authority Hierarchy handles role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership, while Source-of-Truth Hierarchy handles factual conflict resolution.

Impact: reduces risk of flattening consultant frictions into a single authority answer.

Action required: later task/trap design should state which hierarchy governs when both are relevant.

### VERIFIED

Finding: confirmed conditions are aligned with approved Brainstorm remediation and reviewer feedback.

Evidence: the condition list contains the reviewer-requested expanded comorbidity burden: HFrEF, CKD3, T2DM, CAD, HTN, hyperlipidemia, OSA, diabetic neuropathy, PMR, anemia of CKD, and osteoporosis/osteopenia.

Impact: preserves the complexity signal that resolved the Brainstorm SEND BACK.

Action required: later Patient Profile should still include enough medication and baseline detail to make these conditions clinically meaningful.

### VERIFIED

Finding: presumed/active questions preserve the mixed physiology design.

Evidence: infection source, steroid/adrenal contribution, dehydration, medication contribution, and discharge readiness are listed as active questions rather than a single final answer.

Impact: prevents drift into a hidden adrenal insufficiency puzzle or sepsis-only case.

Action required: later Clinical History should preserve uncertainty while making the chart internally coherent.

### VERIFIED

Finding: final friction table keeps frictions as people/perspective conflicts.

Evidence: the table names Cardiology vs Nephrology, Family vs Primary Team, and Endocrinology vs Primary Team, with topics and stakeholder positions.

Impact: supports AutoQC friction/trap separation and Decision Friction Table expectations.

Action required: later Failure Design tables should keep informational traps separate from this friction table.

### VERIFIED

Finding: administrative deliverable decision is aligned with existing task concepts.

Evidence: approved rough tasks already include transition-of-care/discharge readiness planning, consultant synthesis/care coordination, and readmission risk/patient safety review.

Impact: supports AutoQC expectations for clinical plus administrative work where appropriate.

Action required: final task architecture must select exact tracker workflows without exceeding the 3-5 distinct workflow constraint.

### PLAUSIBLE

Finding: "Acute Hospital Management" is useful as a workflow umbrella but may not be an exact task tracker workflow.

Evidence: the approved rough task mappings use exact P0/P1 tracker labels, while this governance decision names a single umbrella with subdomains.

Impact: helpful for narrative coherence, but final World Spec workflow lines cannot rely on the umbrella if it is not an exact tracker label.

Action required: during task architecture, use exact tracker workflow labels for each task and keep the umbrella as a conceptual organizing frame only.

### PLAUSIBLE

Finding: workflow count and administrative deliverable risks remain open task-architecture issues.

Evidence: AutoQC 2.107 and 2.108 are watch items, but Governance Package v1 intentionally does not create final task specifications.

Impact: this is appropriate now, but must be resolved before World Spec upload.

Action required: address workflow count and administrative deliverable during task architecture, not in governance ratification.

### PLAUSIBLE

Finding: the authority hierarchy may require careful explanation because attending hospitalist and consulting attendings can reasonably disagree.

Evidence: the world intentionally depends on consultant conflict; a rigid hierarchy could accidentally flatten that conflict.

Impact: if over-applied, this could weaken the core frictions.

Action required: in World Spec construction, distinguish documentation authority from clinical disagreement. Hierarchy resolves evidence conflicts; it does not erase competing recommendations.

### DISPUTED

Finding: none.

Evidence: no governance decision conflicts with the approved Brainstorm, ratified Clinical Story Skeleton, locked Identity Package, reviewer feedback, or known AutoQC v6.3 watch items.

Impact: no redesign required.

Action required: none.

### NO ISSUE

Finding: Governance Package v1 does not create tasks, milestones, file inventory, prompts, goldens, grader guidance, reference files, or synthetic files.

Evidence: this document records architecture and review only.

Impact: phase boundary remains intact.

Action required: stop before World Spec construction until Alexander explicitly authorizes the next phase.

## Final Status

Governance Package v1

Status: RATIFIED

Physician Architecture Layer

Status: COMPLETE
