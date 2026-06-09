# Task Architecture Package v1

Date created: 2026-05-31

Status: LOCKED.

Purpose: define the final workflow structure and task-distribution framework for Korvin Merrow World before any task drafting begins.

This package records physician decisions from the completed Task Architecture Interview and translates them into a task-architecture framework only.

This package does not create task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

## Source Inputs

- Approved Brainstorm.
- Ratified Clinical Story Skeleton v1.
- Ratified Governance Package v1.
- Locked Clinical Story Timeline Package v1.
- Current Clinical Logic.
- Task Architecture Interview v1.
- World Spec AutoQC v6.3.
- Official task tracker mappings already recorded in `worlds/korvin-merrow/active/task-map.md`.

## Physician Decisions

- Target task count: 6.
- Target workflow count: 4 distinct workflows.
- Administrative deliverable: Discharge Planning / Care Coordination.
- Transition-of-Care (TCM) remains part of the Transition/Discharge workflow and does not become its own workflow.
- Consultant synthesis remains a distinct reasoning area and should not be merged away.
- Readmission-risk reasoning may exist but should live inside existing workflow structures rather than creating a new workflow.
- Coding, billing, and prior authorization are not preferred unless later required by source material.

## 1. Final Workflow Architecture

Target:

- 6 task concepts.
- 4 distinct approved catalog workflows.

| Workflow | Purpose | Primary ownership / requester family | Architectural justification |
| --- | --- | --- | --- |
| Discharge Medication Reconciliation | Reconcile medication continuation, hold, restart, stop, taper, and follow-up logic after a complex admission. | Hospitalist, pharmacist, discharge clinician, or medication-safety reviewer. | Preserves the HF-AKI medication trap, steroid timeline/source-of-truth trap, and Cardiology vs Nephrology friction without turning every task into medication reconciliation. |
| Hospital Discharge Summary Generation | Produce an accurate narrative synthesis of the hospitalization without copying early assumptions forward. | Attending hospitalist or discharging service. | Tests temporal synthesis, sepsis anchoring after partial improvement, consultant chronology, medication changes, and unresolved follow-up issues as a clinical summary work product. |
| Discharge Planning Documentation | Serve as the transition/discharge workflow umbrella for discharge readiness, TCM-style follow-up planning, care coordination, and readmission-risk reasoning. | Hospitalist, case management, social work, transition-of-care team, or PCP-facing transition team. | Carries the administrative deliverable decision naturally through disposition safety, family concerns, PT/OT information, follow-up planning, and care coordination. TCM and readmission-risk reasoning remain inside this workflow rather than becoming separate catalog workflows. |
| Interdisciplinary Care Plan Development and Documentation | Reconcile consultant recommendations and stakeholder priorities into one coordinated plan. | Hospitalist-led interdisciplinary team, care coordination team, or consultant-synthesis requester. | Preserves consultant synthesis as a distinct reasoning area and supports all three primary frictions without merging specialist conflict into discharge planning alone. |

## 2. AutoQC 2.107 Compliance

AutoQC 2.107 requires 3-5 distinct catalog workflows across the task set.

Final target:

- Distinct workflow count: 4.
- Compliance posture: within the required 3-5 range.

| Approved rough task concept | Assigned workflow | Consolidation rationale |
| --- | --- | --- |
| Discharge medication reconciliation / medication safety review | Discharge Medication Reconciliation | Remains distinct because medication safety is a core competency and the HF-AKI trap should not be diluted into generic discharge planning. |
| Hospital discharge summary generation | Hospital Discharge Summary Generation | Remains distinct because it tests narrative synthesis, temporal course, and copy-forward avoidance. |
| Transition-of-care / discharge readiness plan | Discharge Planning Documentation | Carries the administrative deliverable and disposition-safety failure target. |
| Post-hospital follow-up assessment note | Discharge Planning Documentation | TCM remains part of the transition/discharge workflow instead of creating a fifth workflow. The +7 reasoning anchor can still be preserved later without using TCM as a separate catalog workflow. |
| Consultant recommendation synthesis / care coordination note | Interdisciplinary Care Plan Development and Documentation | Remains distinct because consultant synthesis is a core reasoning area and should not be merged away. |
| Readmission risk / patient safety review | Discharge Planning Documentation | Readmission-risk reasoning lives inside transition/discharge planning and care coordination rather than creating a separate risk-stratification workflow. |

Rationale for consolidation:

- The approved Brainstorm produced six strong task concepts, but the Brainstorm-level mapping originally spanned five distinct workflow categories.
- Physician decision sets the target at four workflows to reduce AutoQC 2.107 risk and prevent later implementation drift into a sixth workflow.
- TCM and readmission-risk reasoning are preserved as reasoning components, not separate workflow categories.
- Consultant synthesis remains distinct because merging it would weaken the specialist-conflict design.

Do-not-cross boundary:

- This table is workflow architecture only. It is not a final task list, final prompts, expected outputs, grading plan, or file plan.

## 3. AutoQC 2.108 Readiness

AutoQC 2.108 requires typical clinical worlds to include both direct clinical work products and healthcare-administration work products where appropriate.

Ratification note: AutoQC 2.108 remains a documented reviewer-risk bet, not a blocker.

Administrative deliverable location:

- Discharge Planning Documentation.
- Care Coordination.

Why it fits naturally:

- The primary failure target is discharge readiness, functional decline recognition, and disposition safety.
- The world includes PT/OT functional concerns, family baseline knowledge, medication changes, consultant recommendations, follow-up needs, Case Management, and Social Work.
- The patient is medically improving but operationally dangerous, making discharge planning and care coordination clinically necessary rather than artificial.

Clinical work products represented by architecture:

- Discharge medication reconciliation.
- Hospital discharge summary.
- Consultant recommendation synthesis / interdisciplinary care planning.
- Post-discharge follow-up reasoning embedded in transition/discharge workflow.

Administrative / operations-facing work represented by architecture:

- Discharge planning / care coordination.
- Transition-of-care planning.
- Readmission-risk reasoning inside discharge planning and care coordination.

Administrative options not selected:

| Option | Reason not selected for v1 architecture |
| --- | --- |
| Coding review | Would shift emphasis toward billing/admin abstraction and away from the approved clinical strengths. |
| Prior authorization | Could become realistic later only if source material or future file construction requires payer/post-acute authorization facts. Not preferred now. |
| Utilization review | Plausible but not the best first administrative fit; discharge planning and care coordination are more directly supported by the current world. |
| Standalone readmission-risk workflow | Readmission-risk reasoning is preserved, but it lives inside transition/discharge planning rather than creating another workflow category. |

Contingency if challenged later:

- Utilization Review may be considered as a second administrative deliverable.
- Do not add Utilization Review now.
- This is a contingency only, not part of locked v1 workflow architecture.

## 4. Trap Distribution Analysis

| Trap | Supported task families / workflows | Distribution assessment |
| --- | --- | --- |
| Steroid timeline/source-of-truth trap | Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Interdisciplinary Care Plan Development and Documentation; Discharge Planning Documentation when follow-up/steroid plan matters | Well supported. Risk is overuse if every task becomes prednisone reconstruction; later drafting should vary whether the trap is central or secondary. |
| HF-AKI medication reconciliation and time-sensitive consultant trap | Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Discharge Planning Documentation | Strongly supported. This remains a core medication-management challenge but should not dominate all six task concepts. |
| Buried functional/cognitive status trap | Discharge Planning Documentation; Hospital Discharge Summary Generation; follow-up/readmission reasoning inside Discharge Planning Documentation | Well supported. This trap should remain evidence-finding focused: important nursing/PT/family information exists but is easy to miss. |
| Sepsis anchoring after partial improvement trap | Hospital Discharge Summary Generation; Discharge Planning Documentation; Interdisciplinary Care Plan Development and Documentation | Supported. Later task construction should preserve "sepsis was reasonable initially" and avoid turning steroid physiology into a hidden answer. |
| Discharge plan source-hierarchy trap | Discharge Planning Documentation; Interdisciplinary Care Plan Development and Documentation; Discharge Medication Reconciliation where discharge medication plan appears sufficient but is incomplete | Strongly supported. This trap should remain distinct from Trap #3: the issue is over-trusting a visible but incomplete discharge/source-hierarchy artifact. |

Trap overload assessment:

- HF-AKI medication logic and discharge-readiness logic are naturally heavy because they are central to the world.
- Steroid timeline should appear meaningfully but not dominate the world.
- Trap #3 and Trap #5 must remain distinct during later task drafting and file construction.

Trap #3 vs Trap #5 distinction:

- Trap #3: buried functional/cognitive evidence. The failure is not finding or integrating important evidence that exists in less-prominent sources.
- Trap #5: reassuring but incomplete discharge/source-hierarchy artifact. The failure is trusting a visible artifact as sufficient without reconciling it against other sources.

## 5. Friction Distribution Analysis

| Friction | Architectural representation | Distribution assessment |
| --- | --- | --- |
| Cardiology vs Nephrology | Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Discharge Planning Documentation | Strongly represented through medication restart timing, renal recovery, hypotension risk, and HFrEF/CAD protection. Does not need to appear as the dominant conflict in every task concept. |
| Family vs Primary Team | Discharge Planning Documentation; Hospital Discharge Summary Generation; transition/follow-up and readmission-risk reasoning inside Discharge Planning Documentation | Strongly represented through medically improved but operationally risky discharge. This is the main disposition-safety friction. |
| Endocrinology vs Primary Team | Interdisciplinary Care Plan Development and Documentation; Discharge Medication Reconciliation; Hospital Discharge Summary Generation | Adequately represented through steroid interpretation and taper/risk planning. Must remain a risk-interpretation friction, not a hidden missed-diagnosis reveal. |

Friction balance:

- No friction is unsupported.
- Family vs Primary Team and Cardiology vs Nephrology are naturally strongest because discharge safety and medication management are central.
- Endocrinology vs Primary Team is preserved through consultant synthesis and steroid plan reasoning, but later drafting should avoid letting it become the entire case.

## 6. Architecture Consistency Review

### VERIFIED

Finding: final workflow count satisfies AutoQC 2.107.

Evidence: the architecture uses four distinct approved workflow categories: Discharge Medication Reconciliation, Hospital Discharge Summary Generation, Discharge Planning Documentation, and Interdisciplinary Care Plan Development and Documentation.

Impact: the plan is within the required 3-5 workflow range.

Action required: during World Spec drafting, do not introduce a fifth or sixth workflow unless Alexander explicitly reopens task architecture.

### VERIFIED

Finding: AutoQC 2.108 readiness is supported.

Evidence: Discharge Planning Documentation carries the administrative deliverable through discharge planning, care coordination, transition-of-care planning, and readmission-risk reasoning.

Impact: the task set can include both clinical and healthcare-administration work products without adding coding, billing, or prior authorization.

Action required: later task drafting must make the administrative deliverable explicit.

### VERIFIED

Finding: architecture is consistent with the approved Brainstorm.

Evidence: all six approved rough task concepts are preserved at the concept-family level, and the reserve ED reassessment remains excluded from the primary architecture.

Impact: no task concept redesign occurred.

Action required: none before physician review.

### VERIFIED

Finding: architecture is consistent with Governance Package v1.

Evidence: the plan keeps consultant synthesis distinct, preserves the administrative deliverable decision, and uses workflow consolidation rather than adding unrelated workflows.

Impact: governance decisions are implemented without reopening governance.

Action required: none before physician review.

### VERIFIED

Finding: architecture is consistent with the locked Clinical Story Timeline Package.

Evidence: discharge anchor, +7 reasoning, and +30 reasoning remain available, but TCM and readmission-risk reasoning are folded into the transition/discharge workflow rather than creating new workflow categories.

Impact: temporal reasoning remains available without violating workflow-count discipline.

Action required: later task drafting must preserve anchors after world close.

### VERIFIED

Finding: architecture is consistent with the locked Baseline Anchor Package.

Evidence: functional baseline, cognition, medication-management ability, home support, dry weight, and baseline clinical anchors remain relevant to discharge planning, med rec, summary generation, and consultant synthesis.

Impact: baseline anchors can support later tasks without creating admission labs or hospital-course trends here.

Action required: none before physician review.

### PLAUSIBLE

Finding: Discharge Planning Documentation can carry TCM and readmission-risk reasoning without becoming too broad.

Evidence: physician decision explicitly keeps TCM inside the transition/discharge workflow and places readmission-risk reasoning inside existing workflow structures.

Impact: this is coherent, but later drafting must avoid making multiple discharge-planning tasks feel duplicative.

Action required: later task drafting should differentiate requester, time anchor, reasoning emphasis, and deliverable surface within the same workflow.

Carry-forward requirement: because Discharge Planning Documentation carries three task concepts, later task construction must differentiate them by requester, time anchor, reasoning emphasis, and deliverable surface.

### PLAUSIBLE

Finding: four workflows may be safer than five for reviewer/AutoQC compliance.

Evidence: the prior mapping reached five distinct workflows, the upper boundary of AutoQC 2.107. Four gives margin while preserving task diversity.

Impact: reduces accidental workflow drift.

Action required: maintain workflow discipline during World Spec construction.

### DISPUTED

Finding: coding, billing, prior authorization, or utilization review must be added to satisfy administrative work.

Evidence: AutoQC 2.108 requires administrative work where appropriate, but this world naturally supports discharge planning and care coordination as the administrative deliverable.

Impact: forcing billing or payer work would risk scope drift.

Action required: do not add these unless later source material or reviewer feedback requires them.

### DISPUTED

Finding: readmission-risk reasoning requires a standalone Patient Risk Stratification workflow.

Evidence: physician decision states readmission-risk reasoning may exist but should live inside existing workflow structures rather than creating a new workflow.

Impact: preserving it inside Discharge Planning Documentation maintains reasoning coverage while controlling workflow count.

Action required: do not use Patient Risk Stratification Assessment as a distinct workflow in v1 architecture.

### NO ISSUE

Finding: this package does not draft tasks or create downstream artifacts.

Evidence: it defines workflow architecture and task-distribution framework only.

Impact: construction-preparation boundary remains intact.

Action required: stop before task drafting, expected outputs, file inventory, World Spec sections, templates, reference files, synthetic documents, goldens, or grader guidance.

## Final Status

Task Architecture Package v1

Status: LOCKED
