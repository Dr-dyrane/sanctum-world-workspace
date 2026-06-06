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

Current Korvin status: Step 5 World Spec AutoQC is complete at 108/109, with the sole open prednisone dose/frequency warning preserved as intentional design and justified in notes. Step 6 Human Review: World Spec is APPROVED by Stacey S. The requested Reference File Origin routing correction was resolved and re-uploaded.

Onboarding approval condition has been met. Official production pipeline position: Task-Level Materials / Task 1 Taiga QA feedback / pre-FA-GA. World-level Files are complete: Step 9 generated-file review closed, Final Files AutoQC passed 78/78 after three revisions, and `Healthcare_247_Merrow` was created on 2026-06-05 with 26 world files synced. Task 1 setup completed, corrective v4 Task Writing rerun completed, Task AutoQC was submitted at 2/68 with both warnings justified, and batch v2 trajectories ran with scores 78, 72, 92, 95, 93, 92, 92, 92, 90, 94. Grading transcripts show the lower runs had real metformin ER omission failures rather than mere grader underscoring. Env Linter V2 is clean; Data Quality has only the recurring `enable_anthropic_api` false positive. The immediate next platform sequence is save DQ-1 as `tech issue`, run 5.1 Taiga QA Feedback AutoQC, clear 5.2, then start Failure Analysis / Grader Analysis. The canonical Task 1 lifecycle log is `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`; Tasks 2-6 planning remains in `worlds/korvin-merrow/task-setup/step10-review-packet.md`.

### Phase 2: Build Your Files And Tasks

Goal: Engineering generates synthetic files from approved spec and reference templates; writer reviews files and writes tasks in RL Studio.

Status: Limited local exception authorized by Alexander through Final Submission Resolution v1 candidate construction; FI-W01 through FI-W22, FI-T01 through FI-T07, FI-S01 through FI-S04, Task Prompt Architecture v1, TP-KM01 through TP-KM06, Expected Output Architecture v1, EO-KM01 through EO-KM06, Golden Architecture v1, Golden-KM01 through Golden-KM06, Grader Guidance Architecture v1, GG-KM01 through GG-KM06, AutoQC Architecture v1, AutoQC Construction v1, Packaging Architecture v1, Packaging Construction, Submission Preparation, Execution Preparation, and Transcript Resolution v1 are locked. The Entire File Ecosystem, Task Prompt Architecture, Task Prompts, Expected Output Architecture, Expected Outputs, Golden Architecture, Goldens, Grader Guidance Architecture, Grader Guidance, AutoQC Architecture, AutoQC, Packaging Architecture, Packaging, Submission Preparation, Execution Preparation, and Transcript Resolution are complete.

Korvin Merrow current exception: Alexander has explicitly authorized local, batch-gated file ecosystem construction through Supplementary File Construction ratification and lock, has authorized Task Prompt Architecture v1 ratification and lock, has authorized Task Prompt Construction ratification and lock, has authorized Expected Output Architecture v1 ratification and lock, has authorized Expected Output Construction ratification and lock, has authorized Golden Architecture v1 ratification and lock, has authorized Golden Construction ratification and lock, has authorized Grader Guidance Architecture v1 ratification and lock, has authorized Grader Guidance Construction ratification and lock, has authorized AutoQC Architecture v1 ratification and lock, has authorized AutoQC Construction v1 ratification and lock, has authorized Packaging Architecture v1 ratification and lock, has authorized Packaging Construction ratification and lock, has authorized Submission Preparation ratification and lock, has authorized Execution Preparation v1 ratification and lock, has authorized Transcript Resolution v1 lock, has authorized Final Submission Resolution v1 lock and Execution Artifact Generation, and later directly authorized RL Studio upload plus Spec AutoQC. Batch 1 through Batch 5 world-level files are locked. FI-T01 through FI-T07 are locked. FI-S01 through FI-S04 are locked. Entire File Ecosystem is complete. Task Prompt Architecture v1 is locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` and ratification at `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`. Task Prompt Architecture is complete. Task Prompt Construction is locked at `worlds/korvin-merrow/task-prompts/locked/`, with ratification at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`. Task Prompts are complete. Expected Output Architecture v1 is locked at `worlds/korvin-merrow/expected-output-architecture/locked/`, with ratification at `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`. Expected Output Architecture is complete. Expected Output Construction is locked at `worlds/korvin-merrow/expected-outputs/locked/`, with ratification at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`. Expected Outputs are complete. FI-T07 is preserved as addendum support for EO-KM01 only, and no EO-KM07 exists. Golden Architecture v1 is locked at `worlds/korvin-merrow/golden-architecture/locked/`, with ratification at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`. Golden Architecture is complete. Golden Construction is locked at `worlds/korvin-merrow/goldens/locked/`, with ratification at `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`. Goldens are complete. Grader Guidance Architecture v1 is locked at `worlds/korvin-merrow/grader-guidance-architecture/locked/`, with ratification at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`. Grader Guidance Architecture is complete. Grader Guidance Construction is locked at `worlds/korvin-merrow/grader-guidance/locked/`, with ratification at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`. Grader Guidance is complete. FI-T07 is preserved as addendum support for GG-KM01 only, and no GG-KM07 exists. AutoQC Architecture v1 locked artifacts are under `worlds/korvin-merrow/autoqc-architecture/locked/`, with ratification at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Architecture is complete. AutoQC Construction locked artifacts are under `worlds/korvin-merrow/autoqc/locked/`, with ratification at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC is complete. Packaging Architecture locked artifacts are under `worlds/korvin-merrow/packaging-architecture/locked/`, with ratification at `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Architecture is complete. Packaging Construction locked artifacts are under `worlds/korvin-merrow/packaging/locked/`, with ratification at `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`. Packaging is complete. Submission Preparation locked artifacts are under `worlds/korvin-merrow/submission-preparation/locked/`, with ratification at `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md`. Submission Preparation is complete. Execution Preparation v1 locked artifacts are under `worlds/korvin-merrow/execution-preparation/locked/`, with ratification at `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`. Transcript Resolution v1 locked artifacts are under `worlds/korvin-merrow/transcript-resolution/locked/`. Final Submission Resolution v1 locked artifacts are under `worlds/korvin-merrow/final-submission-resolution/locked/`, with ratification at `worlds/korvin-merrow/final-submission-resolution/ratifications/final-submission-resolution-ratification.md`. Execution Artifact Generation is complete/canonicalized. Additional AutoQC runs, AutoQC responses, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, manifests, final submission packages, additional uploads, additional submissions, RL Studio activity, and RL Studio submission artifacts must not begin without separate explicit authorization.

### Phase 3: QA Your Tasks

Goal: Address Task AutoQC findings and complete trajectory/grading audit.

Status: Task 1 corrective v4 rerun is complete and the project is at Taiga QA feedback / pre-FA-GA. Further task uploads beyond Task 1, additional agent runs, additional QA runs, platform responses, Failure Analysis / Grader Analysis, and preference labeling remain gated on explicit Alexander authorization for the exact action.

### Phase 4: Evaluate The Agent

Goal: Failure analysis, preference labeling, AutoQC, and final reviewer review.

Status: Out of scope until generated-file review, task setup, trajectory runs, and QA gates are complete and Alexander explicitly authorizes evaluation work.

## Explicitly Out Of Scope Until Approval

- Scoring rubrics, scoring thresholds, pass/fail bands, point allocations, AutoQC responses, or later task-layer output generation unless explicitly authorized by Alexander
- Rerunning world file review / Final Files AutoQC without an explicit corrective authorization
- Additional RL Studio task mutation, task upload, agent runs, or QA runs without explicit authorization
- Production task prompts
- Additional golden responses
- Grader guideline reopening or expansion beyond the locked GG-KM01 through GG-KM06 files
- Additional agent runs
- Additional Task AutoQC
- Additional trajectory review beyond the active Task 1 review gate
- Taiga QC outside the active Task 1 Section 4/5 review gate
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
