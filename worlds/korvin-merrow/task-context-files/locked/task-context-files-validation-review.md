# Task-Level Context Files Validation Review

Date created: 2026-06-02

Status: CANDIDATE REVIEW

Purpose: validate Task-Level Context File Construction for FI-T01 through FI-T07 against locked Task-Level Context File Architecture v1, locked File Inventory v1, locked World Spec v1, Governance Package v1, FI-W01 through FI-W22, ratifications, and reconciliation records.

## Authorized File Creation Validation

### VERIFIED

Authorized task-context files were created under `worlds/korvin-merrow/task-context-files/candidate-review/`:

| File ID | Candidate file | Locked inventory row matched | Status |
| --- | --- | --- | --- |
| FI-T01 | `FI-T01_discharge-medication-reconciliation-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T02 | `FI-T02_discharge-summary-drafting-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T03 | `FI-T03_discharge-readiness-care-coordination-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T04 | `FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T05 | `FI-T05_early-post-discharge-follow-up-assessment-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T06 | `FI-T06_patient-safety-readmission-risk-review-request-context.md` | Yes | CANDIDATE REVIEW |
| FI-T07 | `FI-T07_medication-safety-handoff-task-context-addendum.md` | Yes | CANDIDATE REVIEW |

No FI-S files were created.

## Cross-Artifact Consistency Verification

### VERIFIED

Construction cross-checked:

- locked Task-Level Context File Architecture v1;
- locked File Inventory v1;
- FI-T inventory / task-layer architecture reconciliation record;
- locked Task Architecture Package v1;
- locked World Spec v1;
- ratified Governance Package v1;
- FI-W01 through FI-W22 locked world files;
- Batch 1 through Batch 5 validation and ratification records.

No silent broadening or narrowing of trap coverage, friction coverage, workflow mapping, priority labels, file responsibilities, source hierarchy, or prednisone hierarchy was introduced.

## Inventory Row Alignment

### VERIFIED

Each FI-T candidate preserves its locked inventory row:

- FI-T01: Discharge Medication Reconciliation; Traps #1, #2, #5; Cardiology vs Nephrology; Endocrinology vs Primary Team.
- FI-T02: Hospital Discharge Summary Generation; Traps #2, #4, #5; secondary Endocrinology vs Primary Team and Family vs Primary Team support.
- FI-T03: Discharge Planning Documentation; Traps #3, #5; Family vs Primary Team.
- FI-T04: Interdisciplinary Care Plan Development and Documentation; Traps #1, #2, #5; Trap #4 secondary; all three frictions.
- FI-T05: Discharge Planning Documentation; Traps #1, #2, #4, #5; Trap #3 secondary; Family vs Primary Team; Endocrinology vs Primary Team support through steroid-plan coherence.
- FI-T06: Discharge Planning Documentation; Traps #2, #3, #5; Family vs Primary Team; Cardiology vs Nephrology secondary support.
- FI-T07: Discharge Medication Reconciliation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team.

## World-File Synthesis Validation

### VERIFIED

Each FI-T candidate requires synthesis across locked world files:

- FI-T01 requires medication, pharmacy, prednisone, trend, MAR, consultant, functional medication-management, and FI-W22 synthesis.
- FI-T02 requires ED/admission, hospitalist course, trends, consultant chronology, functional/family evidence, and FI-W22 synthesis.
- FI-T03 requires baseline, hospitalist, objective trend, nursing, PT, OT, family, case management/social work, and FI-W22 synthesis.
- FI-T04 requires hospitalist, consultants, MAR, objective trends, family, functional, and discharge-facing synthesis.
- FI-T05 requires reconstruction from FI-W01 through FI-W22 and adds no new +7 facts.
- FI-T06 requires world-level discharge-readiness, functional, medication, consultant, family, transition, and source-hierarchy synthesis and adds no +30 outcome.
- FI-T07 requires FI-T01-style medication synthesis and does not add missing medication facts.

No FI-T file can replace FI-W01 through FI-W22.

## Anti-Answer-File Validation

### VERIFIED

The FI-T files are request-framing / task-context files only.

They do not contain:

- task prompts;
- expected outputs;
- golden responses;
- grader guidance;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- final medication lists;
- final discharge summaries;
- final disposition decisions;
- final consultant synthesis;
- final prednisone taper plans;
- post-world clinical outcomes.

## FI-W22 Incompleteness Validation

### VERIFIED

FI-W22 remains visible, organized, authoritative-looking, and incomplete. FI-T01, FI-T02, FI-T03, FI-T04, FI-T05, FI-T06, and FI-T07 all treat FI-W22 as a source that must be reconciled against the broader chart, not as a substitute for the world.

## Trap Preservation Validation

### VERIFIED

All five traps remain active:

- Trap #1: Prednisone source-of-truth remains a hierarchy problem, with rheumatology as highest outpatient prednisone authority.
- Trap #2: HF/AKI medication timing remains a synthesis problem across trends, MAR actions, consultants, and discharge context.
- Trap #3: Buried functional/cognitive evidence remains distributed across nursing, PT, OT, family, and care-coordination sources.
- Trap #4: Sepsis anchoring remains a mixed-physiology reassessment problem, not a hidden diagnosis reveal.
- Trap #5: Discharge source hierarchy remains active because visible discharge-facing sources are incomplete.

Trap #3 and Trap #5 remain distinct.

## Friction Preservation Validation

### VERIFIED

All three frictions remain active and defensible:

- Cardiology vs Nephrology remains a medication timing/sequencing friction.
- Endocrinology vs Primary Team remains a steroid-risk interpretation friction.
- Family vs Primary Team remains a discharge-readiness friction.

No FI-T file declares a winner, makes a stakeholder careless, or resolves the final clinical decision.

## Source Hierarchy Validation

### VERIFIED

Source hierarchies are preserved:

- Master source-of-truth hierarchy is unchanged.
- Authority hierarchy is unchanged.
- Prednisone hierarchy is unchanged.
- Hospitalist-synthesizes-not-defers governance is preserved.
- P0/P1/P2 labels remain tracker-provenance metadata only.

## Physician-Perspective Framing Validation

### VERIFIED

The FI-T files preserve physician-facing responsibility. Supporting evidence may come from pharmacy, nursing, PT/OT, case management, social work, family, consultants, or administrative sources, but future deliverables remain physician-authored, physician-reviewed, physician-supervised, or physician-communicated when later authorized.

## Unauthorized Artifact Check

### VERIFIED

This construction did not create:

- FI-S files;
- supplementary files;
- task prompts;
- expected outputs;
- goldens;
- grader guidance;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- new synthetic world-level files;
- post-world clinical evidence.

## Carry-Forward / Future Prompt-Layer Watch Items

### RECORDED

Reviewer A returned LOCK READY / GO. Reviewer B returned GO WITH MINOR NOTES. No true defects, architecture defects, or governance defects were identified. The following items are carry-forward / future prompt-layer watch items only:

1. FI-T01 vs FI-T07 differentiation must be preserved at prompt-construction time.

   - FI-T01 should remain the full discharge medication reconciliation context.
   - FI-T07 should remain a focused medication-safety handoff/addendum context.
   - Future prompts must not create two near-duplicate medication reconciliation tasks.

2. FI-T02 discharge-summary prompt construction must preserve anti-transcription emphasis.

   - Future prompt construction should require synthesis by clinical evolution, not copied problem-list transcription.
   - Trap #4 sepsis anchoring must remain active.
   - FI-W22 must not substitute for the full hospital course.

3. FI-T03 / FI-T06 physician-voice watch item.

   - Supporting evidence may come from case management, social work, quality/safety, PT/OT, nursing, pharmacy, and family.
   - Future deliverables must remain physician-authored, physician-reviewed, physician-supervised, or physician-communicated.

4. FI-S construction remains a separate blocked phase.

5. Task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, and submission artifacts remain blocked until explicit authorization.

## Final Validation Status

Task-Level Context File Construction:

- FI-T01 through FI-T07 created.
- Status: CANDIDATE REVIEW.
- Next eligible phase: Task-Level Context File Construction Review.
