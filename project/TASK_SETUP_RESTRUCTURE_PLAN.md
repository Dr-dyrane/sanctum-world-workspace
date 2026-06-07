# Task Setup Restructure Plan

Status: APPROVED AND EXECUTED

Created: 2026-06-07

Executed: 2026-06-07

Scope: `worlds/korvin-merrow/task-setup/` and its immediate task-stage neighbors.

Alexander explicitly authorized this restructure after KM02 v3 was snapshotted. This document is retained as the rationale and audit trail for the new task setup tree.

## Purpose

The current task setup area has become a mixed working surface. Task 2 now contains design notes, build artifacts, platform copies, run evidence, QA notes, FA/GA drafts, learning docs, and bundle ZIPs in one visible layer. Task 3 has begun and should not inherit that sprawl.

This plan defines a clean, repeatable task-stage tree so future collaborators can answer four questions quickly:

1. What is current?
2. What was submitted or run?
3. What is historical evidence?
4. What is local convenience material only?

## Current Snapshot

As of the planning pass, the working tree is dirty. Do not restructure before resolving or explicitly preserving these live edits.

Known active dirty areas:

- `AGENTS.md`
- `docs/reasoning-discipline.md`
- `docs/workspace-guardrails-lessons.md`
- `docs/world-pipeline-playbook.md`
- `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
- `worlds/korvin-merrow/task-setup/platform/task2/README.md`
- `worlds/korvin-merrow/task-setup/platform/task2/golden-KM02-v5.docx`
- deleted `worlds/korvin-merrow/task-setup/platform/task2/prompt-task2.txt`
- `worlds/korvin-merrow/task-setup/platform/task2/hold/prompt-task2-CLEAN-SUPERSEDED.txt`
- `worlds/korvin-merrow/task-setup/task2/*` active KM02 edits
- `worlds/korvin-merrow/task-setup/task2/escalation-run-v3/`
- `worlds/korvin-merrow/task-setup/task3/`

Current root shape:

```text
worlds/korvin-merrow/task-setup/
  CHECKPOINT-AUDIT-pre-task2.md
  TASK-RUNBOOK.md
  step10-review-packet.md
  task1-lifecycle-log.md
  platform/
  reviews/
  task1/
  task2/
  task3/
```

Task 2 is the main bloat source. It currently mixes approximately 40+ files across:

- design and red-team docs
- source markdown and DOCX build artifacts
- clean-pilot run evidence
- escalation v2 run evidence
- escalation v3 run evidence
- QA and Taiga logs
- FA/GA drafts
- learning/retrospective docs
- ignored bundle ZIPs

## Non-Goals

This plan must not:

- modify clinical content
- alter locked canon
- alter platform-submitted content
- edit DOCX content
- run RL Studio actions
- run AutoQC
- delete evidence
- track bundle ZIPs unless Alexander explicitly promotes them
- rewrite Task 1 history
- collapse Task 2 v2 and v3 evidence into one run

## Target Principles

1. Each task folder should be lifecycle-bucketed.
2. A task root may contain only a short state README plus lifecycle folders.
3. Current platform materials must be separated from build sources and historical runs.
4. Raw trajectory/run evidence must live under `runs/`.
5. QA records must live under `qa/`.
6. FA/GA records must live under `fa-ga/`.
7. Bundles are local convenience artifacts and should remain ignored unless explicitly approved.
8. Every task starts with the folder scaffold before artifact creation.
9. No restructure happens while live platform work is mid-edit unless the live state is explicitly snapshotted first.

## Proposed Tree

```text
worlds/korvin-merrow/task-setup/
  README.md                         # optional cockpit if approved later
  TASK-RUNBOOK.md                   # shared task operating guide
  CHECKPOINT-AUDIT-pre-task2.md     # historical pre-Task2 checkpoint
  step10-review-packet.md           # historical Step 10 planning packet
  task1-lifecycle-log.md            # Task 1 canonical lifecycle log
  reviews/
  platform/
    _templates/
    task1/
      current/
      archive/
    task2/
      current/
      hold/
      archive/
    task3/
      current/
      hold/
      archive/
  task1/
    fa-ga/
    preference-labeling/
    trajectories/
    archive/
  task2/
    TASK2-STATE.md
    design/
    build/
    runs/
      clean-pilot/
      escalation-v2/
      escalation-v3/
    qa/
    fa-ga/
    learnings/
    bundles/
    archive/
  task3/
    TASK3-STATE.md
    design/
    build/
    runs/
    qa/
    fa-ga/
    learnings/
    bundles/
    archive/
```

## Task 2 Classification Plan

Move by role, preserving contents exactly.

### Task 2 Design

Target: `worlds/korvin-merrow/task-setup/task2/design/`

Candidate files:

- `KM02-design-plan-for-review.md`
- `RED-TEAM-BRIEF-KM02.md`
- `prompt-task2-v1-DRAFT.txt`
- `colleague-draft-KM02.md`
- `Golden-KM02-v2-DRAFT.md`

Purpose: design history, red-team prep, rationale, and draft concepts. Not platform-current unless copied into `platform/task2/current/`.

### Task 2 Build

Target: `worlds/korvin-merrow/task-setup/task2/build/`

Candidate files:

- `golden-KM02-source.md`
- `golden-KM02-v5.docx`
- `grader-guidance-KM02-v1.md`

Purpose: local source/build record for golden and grader artifacts. Platform-facing copies live separately.

### Task 2 Runs

Target: `worlds/korvin-merrow/task-setup/task2/runs/`

Candidate moves:

- `pilot-run-clean/` -> `runs/clean-pilot/`
- `escalation-run/` -> `runs/escalation-v2/`
- `escalation-run-v3/` -> `runs/escalation-v3/`

Run-specific summaries should live with the run they describe unless they are cross-run lessons:

- `KM02-pilot-failure-analysis.md` -> `runs/clean-pilot/`
- `KM02-escalation-results.md` -> `runs/escalation-v2/` unless v3 supersedes it
- v3 run summaries inside `escalation-run-v3/` -> `runs/escalation-v3/`

Purpose: immutable evidence from actual runs. Do not upload from these folders.

### Task 2 QA

Target: `worlds/korvin-merrow/task-setup/task2/qa/`

Candidate files:

- `KM02-taiga-qa-log.md`

Purpose: Taiga/AutoQC/QA gate records, including exact platform-field lessons.

### Task 2 FA/GA

Target: `worlds/korvin-merrow/task-setup/task2/fa-ga/`

Candidate files:

- `FA-GA-current.md`
- `FA-GA-v2-PRIOR.md` if it remains inside v3 evidence and is intentionally preserved

Purpose: prepared or submitted FA/GA text. Label status clearly: draft, submitted, superseded, or historical.

### Task 2 Learnings

Target: `worlds/korvin-merrow/task-setup/task2/learnings/`

Candidate files:

- `KM02-learnings.md`

Purpose: cross-task lessons that should inform Tasks 3-6.

### Task 2 Bundles

Target: `worlds/korvin-merrow/task-setup/task2/bundles/`

Candidate files:

- `KM02-redteam-bundle.zip`
- `KM02-difficulty-bundle.zip`
- `KM02-escalation-bundle.zip`
- `KM02-v3-claude-bundle.zip`

Default rule: keep ZIPs ignored. If a bundle needs tracking, replace it with a manifest or source folder when possible.

## Platform Folder Plan

The `platform/` folder should mean "what RLS sees or saw", not general design work.

Use:

```text
platform/taskN/current/
platform/taskN/hold/
platform/taskN/archive/
```

### Platform Task 1

Move current live artifacts into:

```text
platform/task1/current/
```

Keep `platform/task1/archive/` as historical.

Do not rewrite Task 1 records.

### Platform Task 2

Target:

```text
platform/task2/current/
platform/task2/hold/
platform/task2/archive/
```

Current candidate files should be identified from the latest Task 2 platform state before moving. Do not infer current status from file names alone.

Known platform Task 2 materials include:

- `golden-KM02-v5.docx`
- `grader-guidelines-task2.txt`
- `README.md`
- `hold/prompt-task2-CLEAN-SUPERSEDED.txt`
- `hold/discharge_summary_draft_incomplete.md`
- `escalation/prompt-task2-escalation.txt`
- `escalation/discharge_summary_draft_incomplete_05242026.docx`

Before executing:

1. Decide whether the active platform set is v3 or earlier.
2. Put only the active prompt/golden/grader/mounted file in `current/`.
3. Put optional held files in `hold/`.
4. Put superseded clean-pilot and older escalation files in `archive/`.

## Task 3 Setup Plan

Task 3 is early and should start clean.

Target:

```text
task3/
  TASK3-STATE.md
  design/
  build/
  runs/
  qa/
  fa-ga/
  learnings/
  bundles/
  archive/
```

Candidate moves:

- `task3/KM03-design-plan-for-review.md` -> `task3/design/`
- `task3/KM03-review-bundle.zip` -> `task3/bundles/` and keep ignored unless Alexander explicitly promotes it

Do not create Task 3 prompts, goldens, grader guidance, QA artifacts, or run artifacts unless Alexander authorizes that phase.

## Task State Files

Each active task should have a small state file:

- `task2/TASK2-STATE.md`
- `task3/TASK3-STATE.md`

Each state file should answer:

1. Current platform status
2. Current active artifacts
3. Current run/gate
4. Next authorized step
5. Forbidden steps
6. Where historical evidence lives

These state files should be short. They should not duplicate full run logs.

## Continuity Updates Required After Execution

If this restructure is executed, update:

- `project/STATUS.md`
- `docs/status-dashboard.md`
- `project/WORKSPACE_FILE_MAP.md`
- `project/PHASE_MAP.md`
- `AGENTS.md`
- `worlds/korvin-merrow/README.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`

Update links and navigation. Do not rewrite clinical content.

## Hygiene Rule To Add After Execution

Add this rule to workspace hygiene guidance:

Task-stage work must use lifecycle buckets from the start. A `taskN/` folder must not become a mixed flat folder. Every task artifact belongs to exactly one class:

- design
- build
- platform-current
- platform-hold
- platform-archive
- run evidence
- QA
- FA/GA
- preference labeling
- review
- learning
- bundle/archive

Current platform artifacts live under `platform/taskN/current/`. Raw run outputs live under `taskN/runs/<run-name>/`. ZIP bundles are local convenience artifacts and stay ignored unless explicitly promoted.

## Execution Sequence When Authorized

1. Capture a safety snapshot:
   - `git status --short --branch`
   - list current dirty files
   - identify live files that must not move yet
2. Decide whether to commit current live Task 2/3 changes before restructuring.
3. Create target folders.
4. Move files with content-preserving `git mv` where files are tracked.
5. Move ignored bundles without tracking them unless explicitly approved.
6. Add `TASK2-STATE.md` and `TASK3-STATE.md` only if approved.
7. Update continuity surfaces.
8. Run verification.
9. Commit with:
   - `checkpoint: reorganize task setup tree and hygiene rules`

## Verification Checklist

Confirm:

- no locked canon modified
- no DOCX content modified during moves
- no platform artifacts edited, only moved
- no ZIP bundles accidentally tracked
- no stale references to old Task 2 root paths in continuity surfaces
- new Task 2 current state is findable in under 60 seconds
- Task 3 starts from a clean scaffold
- `git status --short --branch` is clean after commit

## Recommended Next Decision

Before execution, Alexander and Claude should decide:

1. Is Task 2 v3 the active platform set?
2. Which prompt/golden/grader/mounted file are current?
3. Should any ZIP bundle be tracked, or should all bundles remain ignored?
4. Should `TASK2-STATE.md` and `TASK3-STATE.md` be created during restructure?
5. Should current dirty Task 2/3 work be committed before moves?

Recommended answer unless new information contradicts it:

- Commit or explicitly snapshot current live Task 2/3 edits first.
- Keep ZIP bundles ignored.
- Create short `TASK2-STATE.md` and `TASK3-STATE.md`.
- Move all Task 2 run evidence into `runs/`.
- Move platform artifacts into `platform/taskN/current|hold|archive`.
