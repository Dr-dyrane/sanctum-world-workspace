# Task Architecture Interview v1

Date created: 2026-05-31

Status: CANDIDATE REVIEW.

Purpose: create an interview-only framework to determine final task architecture before task drafting, file planning, World Spec construction, or reference-template selection begins.

This artifact exists to resolve:

- AutoQC 2.107 workflow-count constraints.
- AutoQC 2.108 administrative-deliverable requirements.
- Final task distribution.
- Workflow consolidation strategy.

This artifact does not create tasks, task prompts, expected outputs, golden responses, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

## Review Inputs

- Approved Brainstorm.
- Ratified Clinical Story Skeleton v1.
- Ratified Governance Package v1.
- Locked Clinical Story Timeline Package v1.
- Current Clinical Logic.
- World Spec AutoQC v6.3.
- Official source-guide requirements.
- Current Brainstorm-level task map.

## Relevant AutoQC Gates

### AutoQC 2.107

Requirement: final World Spec should represent 3-5 distinct catalog workflows across the task set.

Failure mode: fewer than 3 or more than 5 distinct approved workflow categories are represented.

Interview implication: current rough task concepts may need consolidation so the world remains diverse without exceeding five distinct workflow categories.

### AutoQC 2.108

Requirement: for typical clinical worlds and medical director worlds, task set should include both direct clinical work products and at least one healthcare administration work product where appropriate.

Failure mode: task set is entirely clinical or entirely administrative when the world naturally supports both.

Interview implication: the final task architecture needs at least one administrative or operations-facing deliverable that feels natural to Korvin Merrow's discharge-safety world.

## Current Approved Rough Task Concepts

These are approved Brainstorm concepts only, not final task prompts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

## Workflow Inventory

| Candidate workflow type implied by architecture | Current source | Likely tracker category from current task map | Distinct from others? | Interview question |
| --- | --- | --- | --- | --- |
| Medication reconciliation / medication safety | Approved rough task 1; HF-AKI medication trap; Cardiology vs Nephrology friction | Discharge Medication Reconciliation | Yes, if focused on med plan safety and restart/hold logic | Should this remain its own workflow, or be folded into discharge planning / TCM if workflow count is too high? |
| Discharge documentation | Approved rough task 2; world close and discharge anchor | Hospital Discharge Summary Generation | Yes, if focused on narrative hospital-course synthesis | Is discharge summary essential as a separate work product, or could its competency be tested inside another transition document? |
| Discharge planning / disposition readiness | Approved rough task 3; primary failure target; Family vs Primary Team friction | Discharge Planning Documentation | Yes, and likely strongest administrative/operations-facing candidate | Should this become the main administrative deliverable, or should it remain a clinical discharge-readiness plan? |
| Transitional care follow-up | Approved rough task 4; +7 anchor | Transitional Care Management Documentation (TCM) | Partly distinct; overlaps with discharge planning and medication reconciliation | Is +7 follow-up necessary to test post-discharge reasoning, or does it duplicate discharge planning too much? |
| Interdisciplinary consultant synthesis / care coordination | Approved rough task 5; all three frictions; governance care team | Interdisciplinary Care Plan Development and Documentation | Yes, if focused on reconciling dated consultant recommendations | Should this stay as a distinct coordination workflow, or merge with discharge planning? |
| Readmission risk / patient safety review | Approved rough task 6; +30 anchor; discharge safety synthesis trap | Patient Risk Stratification Assessment | Yes, if framed as risk stratification; may become administrative/quality-facing | Should this be a prospective risk stratification task or a quality/safety administrative task? |
| Source-of-truth reconstruction | Steroid timeline trap; prednisone hierarchy; medication history | Could be embedded inside med rec, TCM, or consultant synthesis | Not clearly a standalone tracker workflow from current mapping | Which final tasks should carry this competency without creating a separate workflow? |
| Inpatient clinical reasoning | Sepsis anchoring, mixed physiology, consultant conflicts | Could be embedded inside discharge summary or consultant synthesis | Not necessarily a separate post-world deliverable | Does the final set need an explicitly inpatient-clinical task, or is the inpatient reasoning sufficiently tested through discharge and follow-up outputs? |

## Workflow Consolidation Analysis

Current Brainstorm-level mapping spans five selected workflow categories:

- Discharge Medication Reconciliation.
- Hospital Discharge Summary Generation.
- Discharge Planning Documentation.
- Transitional Care Management Documentation (TCM).
- Interdisciplinary Care Plan Development and Documentation.
- Patient Risk Stratification Assessment.

This is exactly at the AutoQC 2.107 upper bound if all six mappings remain distinct.

Consolidation options for physician interview:

| Option | What consolidates | Potential benefit | Potential risk | Interview question |
| --- | --- | --- | --- | --- |
| Keep five distinct workflows | Keep current six rough tasks but allow one workflow to repeat or one task to be dropped later | Preserves variety and stays within AutoQC 2.107 if distinct count remains 5 | Leaves little margin if later task architecture adds another workflow | Do you want maximum task variety with strict discipline that no sixth workflow is introduced later? |
| Consolidate TCM into discharge planning | Treat post-discharge follow-up as part of transition-of-care architecture | Reduces workflow count and keeps transition logic unified | May weaken +7 temporal reasoning and post-discharge reassessment | Is +7 follow-up a necessary competency, or can transition risk be tested at discharge? |
| Consolidate care coordination into discharge planning | Make consultant synthesis part of the discharge plan | Strengthens administrative/operations deliverable | Could under-test specialist conflict resolution | Should consultant conflict be its own deliverable, or part of a discharge coordination deliverable? |
| Consolidate risk review into care coordination or discharge planning | Make risk stratification a component of transition safety | Reduces distinct workflows | Could blur the +30 anchor and readmission-risk competency | Should +30 safety review remain distinct from discharge readiness? |
| Repeat one workflow across multiple tasks | Example: two discharge-planning variants with different requesters/anchors | Keeps workflow count low while preserving task count | Risk of near-duplicate tasks if deliverables are not clearly different | Which repeated workflow would still produce distinct work products? |

## AutoQC 2.107 Readiness Assessment

### VERIFIED

Finding: current architecture can satisfy the 3-5 workflow constraint.

Evidence: current task map uses five distinct selected workflow categories, which is within AutoQC 2.107.

Impact: no immediate architecture blocker.

Action required: during physician interview, decide whether to keep five categories or consolidate to create margin.

### PLAUSIBLE

Finding: the world may be safer with four distinct final workflows rather than five.

Evidence: the current architecture already sits at the upper AutoQC boundary; later implementation drift could accidentally add a sixth workflow.

Impact: a four-workflow plan may reduce AutoQC risk while preserving diversity.

Action required: ask Alexander which competency can be folded into another workflow without damaging realism.

### DISPUTED

Finding: final workflow count must be solved by adding a new workflow.

Evidence: not supported. Existing approved rough tasks already cover enough workflow variety.

Impact: adding workflows would increase scope and AutoQC risk.

Action required: do not add new workflow categories unless Alexander explicitly approves and the tracker supports them.

### NO ISSUE

Finding: workflow consolidation can be discussed without creating tasks.

Evidence: this artifact only frames workflow categories, consolidation options, and interview questions.

Impact: phase boundary remains intact.

Action required: none.

## Administrative Deliverable Review

Candidate administrative or operations-facing options naturally supported by the world:

| Option | Natural support in Korvin Merrow world | Strength | Risk | Interview question |
| --- | --- | --- | --- | --- |
| Discharge coordination / discharge planning | Family concern, PT/OT findings, medication changes, follow-up needs, possible home support or post-acute needs | Strongly supported | Could become too broad if it absorbs every competency | Should discharge planning be the primary administrative deliverable? |
| Care coordination | Multiple consultants, PCP continuity, family/caregiver role, medication and steroid source hierarchy | Strongly supported | May overlap with consultant synthesis unless deliverable is clearly operations-facing | Should the care coordination deliverable be addressed to the care team/case manager rather than as a physician note? |
| Transition-of-care administration | +7 anchor, medication changes, follow-up coordination, PCP handoff | Strongly supported | Could duplicate TCM clinical note if not separated | Should TCM be clinical documentation, administrative coordination, or both? |
| Utilization review | Medically improved but operationally dangerous discharge; possible rehab/support evaluation | Plausible | May feel artificial if payer/level-of-care facts are not later built | Is utilization review too operational for the first World, or useful if disposition is central? |
| Prior authorization | Possible post-acute rehab/home services/medication access | Plausible but needs later facts | Risk of requiring payer details not yet authorized | Would a prior authorization task strengthen discharge realism or distract from clinical judgment? |
| Coding review | Multi-causal hospitalization with sepsis/AKI/steroid/CKD/HF complexity | Weak-to-plausible | Could drift into billing/admin-only work and away from approved clinical strengths | Should coding be avoided unless source guidance or reviewer feedback specifically points us there? |
| Patient safety / readmission-risk operations review | +30 anchor, medication confusion, functional decline, discharge readiness | Strongly supported if framed as risk stratification or safety review | Must avoid creating a new adverse event or failure analysis phase | Should readmission-risk review count as administrative/operations work, or remain clinical risk stratification? |

## AutoQC 2.108 Readiness Assessment

### VERIFIED

Finding: the world naturally supports at least one administrative or operations-facing deliverable.

Evidence: governance package already approved an administrative deliverable decision, and approved rough tasks include discharge planning, care coordination, transition-of-care, and readmission-risk review.

Impact: AutoQC 2.108 is addressable without redesign.

Action required: physician interview must select which administrative option feels most natural.

### PLAUSIBLE

Finding: discharge planning or care coordination is likely the strongest administrative fit.

Evidence: the primary failure target is disposition safety, and the world contains PT/OT, Case Management, Social Work, family concerns, consultant recommendations, medication changes, and follow-up needs.

Impact: these options use existing architecture instead of adding payer/billing machinery.

Action required: ask Alexander whether administrative work should be discharge coordination, care coordination, transition-of-care administration, or risk/safety review.

### DISPUTED

Finding: coding review or prior authorization is required.

Evidence: AutoQC examples include administrative work such as prior authorization, coding, utilization review, and peer review, but the architecture does not require those exact categories.

Impact: forcing billing or prior authorization could feel artificial.

Action required: do not choose coding or prior authorization unless Alexander wants that operational angle and later facts support it.

### NO ISSUE

Finding: administrative deliverable can be planned without writing the deliverable.

Evidence: this interview report evaluates options only.

Impact: no phase breach.

Action required: none.

## Task Count Planning Analysis

| Count | Interpretation | Strength | Risk | Interview question |
| --- | --- | --- | --- | --- |
| 5 tasks | Minimum viable final set if one rough task is dropped or merged | Easier to keep workflow count controlled and reduce duplication | May underuse the rich world if too much is merged | What is the one competency you would be most willing to combine or omit? |
| 6 tasks | Current approved Brainstorm set | Strong balance between variety and feasibility | If each task uses a unique workflow, this sits at five distinct categories only if one category repeats or one task consolidates | Do you want to preserve all six rough task concepts? |
| 7 tasks | Adds reserve ED reassessment or extra admin task | More coverage of mixed physiology and anchoring | More scope, more workflow-count risk, higher duplicate risk | Should reserve ED reassessment stay out unless reviewer/AutoQC requires more variety? |
| 8+ tasks | Maximal coverage | Could test every trap/friction repeatedly | Likely too broad for first World Spec and increases execution burden | Should be avoided unless source guidance or reviewer feedback requires it. |

Current readiness:

- Minimum viable: 5 tasks.
- Preferred starting point: 6 tasks, because this preserves the approved Brainstorm set.
- Realistic upper limit for this first World: 6 tasks plus reserve only if specifically needed.

No final task count is selected here.

## Trap Distribution Analysis

| Trap | Natural task support | Overload risk | Under-support risk | Interview question |
| --- | --- | --- | --- | --- |
| Steroid timeline/source-of-truth trap | Medication reconciliation, discharge summary, TCM/follow-up, consultant synthesis | Moderate if every task becomes about prednisone | Low; multiple tasks naturally need steroid timeline | Which tasks should require prednisone reconstruction, and which should only note it as an unresolved follow-up issue? |
| HF-AKI medication reconciliation/time-sensitive consultant trap | Medication reconciliation, consultant synthesis, discharge planning, readmission risk | Moderate-high if task set becomes med-rec heavy | Low; cardiorenal medication logic is central | Should medication restart timing be concentrated in one or two tasks to avoid repetition? |
| Buried functional/cognitive status trap | Discharge planning, TCM/follow-up, readmission risk, discharge summary | Low-moderate | Moderate if final tasks focus too much on meds/consultants | Which final deliverables must force the agent to find nursing/PT/family evidence? |
| Sepsis anchoring after partial improvement trap | Discharge summary, TCM/follow-up, risk review, consultant synthesis | Low | Moderate if all tasks start too late and ignore early course | Which tasks should test reassessment after initial sepsis improvement? |
| Discharge plan source-hierarchy trap | Discharge planning, care coordination, readmission risk, TCM/follow-up | Moderate if merged with Trap #3 | Moderate if no administrative deliverable is chosen | How should we keep visible-but-incomplete discharge artifacts distinct from buried functional evidence? |

Trap #3 vs Trap #5 guardrail:

- Trap #3 asks: did the clinician find the buried functional/cognitive evidence?
- Trap #5 asks: did the clinician avoid over-trusting a visible but incomplete discharge/source-hierarchy artifact?
- Future file construction must keep these separate.

## Friction Distribution Analysis

| Friction | Natural task support | Dominance risk | Underuse risk | Interview question |
| --- | --- | --- | --- | --- |
| Cardiology vs Nephrology | Medication reconciliation, consultant synthesis, discharge planning, readmission risk | Moderate if every task becomes GDMT restart timing | Low | Which tasks should explicitly require reconciling cardiorenal medication priorities? |
| Family vs Primary Team | Discharge planning, TCM/follow-up, readmission risk, discharge summary | Moderate if every task becomes discharge readiness | Low | Which task should be the main functional/disposition-safety test? |
| Endocrinology vs Primary Team | Consultant synthesis, medication reconciliation, discharge summary, TCM/follow-up | Low-moderate if steroid issue dominates | Moderate if prednisone becomes only a trap and not a friction | Where should steroid risk interpretation appear without making adrenal insufficiency the hidden answer? |

Friction support appears sufficient. The main interview risk is preventing Cardiology vs Nephrology and Family vs Primary Team from crowding out Endocrinology vs Primary Team.

## Interview Sequence

### 1. Workflow Count

Questions:

- Do you want to preserve all six approved rough task concepts as final task candidates?
- Should the final architecture target four distinct workflows for safety, or keep five distinct workflows for maximum variety?
- Which of these can reasonably share a workflow without becoming duplicates: discharge planning, TCM, care coordination, readmission-risk review?

### 2. Administrative Deliverable

Questions:

- Which administrative/operations-facing angle feels most real for this patient: discharge coordination, care coordination, transition-of-care administration, utilization review, prior authorization, coding review, or readmission-risk operations review?
- Which options feel artificial for this World and should be excluded?
- Should the administrative deliverable be requested by Case Management/Social Work, a hospitalist, a PCP, a quality/safety team, or another realistic requester?

### 3. Task Count

Questions:

- Is the physician-preferred task count 5, 6, or 7?
- Should the reserve ED reassessment remain reserve-only?
- If one rough task must be merged, which one is least essential?

### 4. Trap Coverage

Questions:

- Which trap should be the primary stress test for each final task category?
- Which traps should appear only as secondary background?
- How many tasks should require explicit steroid timeline reconstruction?
- How many tasks should require explicit HF-AKI medication timing reasoning?
- Which task should best preserve the Trap #3 vs Trap #5 distinction?

### 5. Friction Coverage

Questions:

- Which task should carry the main Cardiology vs Nephrology conflict?
- Which task should carry the main Family vs Primary Team conflict?
- Which task should carry the main Endocrinology vs Primary Team conflict?
- Should any final task intentionally require synthesis across all three frictions?

### 6. Final Architecture Readiness

Questions:

- Does the final architecture still feel like acute hospital medicine rather than billing/admin abstraction?
- Does the final architecture preserve the primary failure target: disposition safety and functional decline recognition?
- Does any proposed consolidation make the world too narrow or repetitive?

## Unresolved Physician Decisions

Do not answer these without Alexander:

- Final task count.
- Final distinct workflow count target.
- Which rough task concepts remain separate vs consolidated.
- Which administrative deliverable is most natural.
- Which workflow labels should be reused or merged.
- Whether TCM remains a separate workflow or folds into transition/discharge planning.
- Whether readmission-risk review remains clinical risk stratification or becomes operations/safety review.
- Whether consultant synthesis remains distinct or merges into care coordination/discharge planning.
- Which task carries each primary friction.
- Which task carries each primary trap.
- How to preserve Trap #3 vs Trap #5 distinction in final task architecture.

## Task Architecture Interview Report

### VERIFIED

Finding: task architecture work is now the correct place to resolve AutoQC 2.107 and 2.108.

Evidence: Governance Package v1 explicitly deferred workflow count and administrative deliverable implementation to task architecture.

Impact: this interview artifact addresses the correct pending gate without reopening governance.

Action required: physician interview must resolve workflow count and administrative deliverable direction before World Spec drafting.

### VERIFIED

Finding: current approved rough tasks can satisfy AutoQC 2.107 if controlled carefully.

Evidence: current task map lists five distinct workflow categories, exactly within the 3-5 allowed range.

Impact: no redesign is required, but no sixth distinct workflow should be added accidentally.

Action required: choose whether to keep five distinct workflows or consolidate to four.

### VERIFIED

Finding: the world naturally supports an administrative or operations-facing deliverable.

Evidence: discharge safety, PT/OT concerns, Case Management/Social Work, family concerns, medication changes, follow-up needs, and care coordination are already approved architecture elements.

Impact: AutoQC 2.108 can be satisfied without artificial billing or payer expansion.

Action required: Alexander must choose the best administrative angle.

### PLAUSIBLE

Finding: discharge planning, care coordination, or transition-of-care administration are the strongest administrative candidates.

Evidence: these options directly follow from the approved discharge-readiness failure target and governance care team roster.

Impact: they likely preserve realism better than coding or prior authorization.

Action required: physician interview should rank these options.

### PLAUSIBLE

Finding: six tasks is the strongest starting point, but five tasks may be cleaner if duplication appears.

Evidence: six tasks are already approved at Brainstorm level; five may reduce overlap if TCM, discharge planning, care coordination, and risk review become too similar.

Impact: task count should be decided after workflow consolidation discussion.

Action required: ask Alexander whether all six rough concepts remain necessary.

### PLAUSIBLE

Finding: Trap #3 and Trap #5 are both needed, but their distinction is fragile.

Evidence: both touch discharge readiness, but Trap #3 concerns buried functional/cognitive evidence while Trap #5 concerns over-trusting a visible but incomplete discharge/source-hierarchy artifact.

Impact: final task architecture and later file construction must prevent these from collapsing into one generic discharge trap.

Action required: select at least one final task where each trap is clearly tested differently.

### DISPUTED

Finding: source-of-truth reconstruction should become a standalone task workflow.

Evidence: current architecture supports source reconstruction as a competency inside med rec, TCM, consultant synthesis, or discharge planning. No approved rough task requires a separate standalone source-reconstruction workflow.

Impact: standalone source reconstruction could become artificial and add workflow-count risk.

Action required: keep source reconstruction embedded unless Alexander explicitly decides otherwise.

### DISPUTED

Finding: utilization review, prior authorization, or coding must be added.

Evidence: AutoQC 2.108 requires administrative work where appropriate, but does not require these exact examples. The current world already supports discharge planning, care coordination, transition-of-care administration, and risk/safety review.

Impact: forcing a payer/coding task could drift away from the world’s clinical strengths.

Action required: consider these only if Alexander finds them realistic for this case.

### NO ISSUE

Finding: this artifact does not create tasks or draft final deliverables.

Evidence: it only inventories candidate workflow types, frames interview questions, and identifies unresolved physician decisions.

Impact: construction-preparation boundary remains intact.

Action required: stop before final task architecture until Alexander completes the interview.

## Final Status

Task Architecture Interview v1

Status: CANDIDATE REVIEW
