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

Status: Limited local exception authorized by Alexander through Task Prompt Architecture v1 candidate construction; FI-W01 through FI-W22, FI-T01 through FI-T07, and FI-S01 through FI-S04 are locked, the Entire File Ecosystem is complete, and Task Prompt Architecture v1 is in candidate review.

Korvin Merrow current exception: Alexander has explicitly authorized local, batch-gated file ecosystem construction through Supplementary File Construction ratification and lock, and has authorized Task Prompt Architecture v1 construction. Batch 1 through Batch 5 world-level files are locked. FI-T01 through FI-T07 are locked. FI-S01 through FI-S04 are locked. Entire File Ecosystem is complete. Task Prompt Architecture v1 is in candidate review at `worlds/korvin-merrow/task-prompt-architecture/candidate-review/task-prompt-architecture-v1.md`, with validation at `worlds/korvin-merrow/task-prompt-architecture/candidate-review/task-prompt-architecture-validation-review.md`. Next eligible phase is Task Prompt Architecture Review. Task prompt construction, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, and RL Studio submission artifacts must not begin without separate explicit authorization.

### Phase 3: QA Your Tasks

Goal: Address Task AutoQC findings and complete trajectory/grading audit.

Status: Out of scope until approval and phase update.

### Phase 4: Evaluate The Agent

Goal: Failure analysis, preference labeling, AutoQC, and final reviewer review.

Status: Out of scope until approval and phase update.

## Explicitly Out Of Scope Until Approval

- Task prompt construction or later task-layer output generation unless explicitly authorized by Alexander
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

## Cross-Artifact Consistency Gate

Before any architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, or governance artifact is created, modified, ratified, or locked, collaborators must explicitly cross-check applicable locked canonical sources:

- World Spec
- Governance Package
- File Inventory
- Architecture Packages
- Ratified review decisions
- Previously reconciled governance decisions

If proposed work expands, narrows, redistributes, reprioritizes, relabels, or reclassifies trap coverage, friction coverage, workflow coverage, priority tiers, source-of-truth mappings, authority hierarchies, file responsibilities, inventory rows, or matrix entries, the change must either be supported by a locked canonical source and explicitly cited, or the discrepancy must be surfaced and documented before ratification or lock.

Historical, planning, superseded, tracker, or provenance metadata must not be silently promoted into governing architecture.

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
