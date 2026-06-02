# Project Sanctum Phase Map

Source of truth: `reference/source/New Writers Version - Instruction Guide (05_24).md`

## Official Phases

### Phase 1: Plan Your World

Goal: Design a realistic clinical scenario and document the spec.

Onboarding scope:

1. Brainstorm
2. Brainstorm AutoQC
3. Human Review: Brainstorm
4. World Spec Document
5. World Spec AutoQC
6. Human Review: World Spec

Onboarding ends after Step 6 approval.

### Phase 2: Build Your Files And Tasks

Goal: Engineering generates synthetic files from approved spec and reference templates; writer reviews files and writes tasks in RL Studio.

Status: Out of scope until approval and phase update.

Korvin Merrow current exception: Alexander has explicitly authorized local, batch-gated synthetic world-level file construction through Batch 5 ratification and lock. Batch 1 FI-W01 through FI-W07 are locked. Batch 2 FI-W08 through FI-W13 are locked. Batch 3 FI-W14 through FI-W16 are locked. Batch 4 FI-W17 through FI-W21 are locked. Batch 5 FI-W22 is locked. World-Level Synthetic File Layer is complete. Task-Level Context File Architecture / Construction is the next eligible phase and must not begin without Alexander authorization.

### Phase 3: QA Your Tasks

Goal: Address Task AutoQC findings and complete trajectory/grading audit.

Status: Out of scope until approval and phase update.

### Phase 4: Evaluate The Agent

Goal: Failure analysis, preference labeling, AutoQC, and final reviewer review.

Status: Out of scope until approval and phase update.

## Explicitly Out Of Scope Until Approval

- Task-level context file construction, supplementary file generation, or later synthetic file generation unless explicitly authorized by Alexander
- World file review
- Production task setup
- Production task prompts
- Golden responses
- Grader guidelines
- Agent runs
- Task AutoQC
- Trajectory review
- Taiga QC
- Failure analysis
- Preference labeling
- Final delivery review

## RL Studio Task vs Clinical Task

RL Studio task:

- A platform workflow container used to upload deliverables, run AutoQC, submit for review, and track status.
- During onboarding, the RL Studio task holds Brainstorm and World Spec stages.

Clinical task:

- A realistic clinician workflow the AI agent will later attempt inside the World.
- Examples: discharge medication reconciliation, discharge summary, consult note, RCA, prior authorization, coding review.
- Clinical tasks are planned conceptually during Brainstorm and specified structurally in World Spec, but production task setup is out of scope during onboarding.

## Brainstorm vs World Spec

Brainstorm:

- Conceptual sign-off document.
- Bar is viability, not build-ready completeness.
- Required sections: World Setup, Major Friction Points, Major Traps, Rough Task Ideas.
- No file inventories, document drafts, full timeline, task prompts, golden responses, or grader guidelines.

World Spec:

- Buildable blueprint for the World.
- Defines scenario, task specifications, world file plan, and world summary.
- Must be specific enough for non-domain-expert builders and reviewers to understand what files should contain.
- Contains task architecture and failure design, but the physician remains responsible for task prompt content and clinical correctness.

## Frictions vs Traps

Frictions:

- People or perspective conflicts.
- Examples: emergency/inpatient team vs endocrinology, nephrology vs cardiology, family/caregiver concerns vs inpatient discharge readiness.
- Test judgment when recommendations or goals compete.

Traps:

- Information problems embedded in the chart or source files.
- Examples: copy-forward errors, outdated medication lists, buried nursing findings, conflicting source-of-truth documents, lab timing errors, outdated consultant recommendations.
- Test chart navigation, synthesis, source hierarchy, timeline reasoning, and uncertainty handling.

These terms are not interchangeable. A strong World should have both.

## Scenario vs World vs Tasks

Scenario:

- The patient story and clinical journey.
- Describes who the patient is, what happened, why care is happening now, and how the clinical course evolves.

World:

- The complete clinical context and chart ecosystem.
- Includes documentation history, competing perspectives, information environment, and files the AI agent can access.
- The AI agent has no information beyond the World files and the task prompt.

Tasks:

- Realistic clinician workflows performed inside or against the World.
- Each task should produce a concrete, evaluable output.
- Tasks are independent encounters and do not depend on one another.
- Tasks should be anchored after the World snapshot.
