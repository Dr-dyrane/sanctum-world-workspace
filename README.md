# Sanctum World Workspace

Private local workspace for Alexander Udeogaranya's Mercor Project Sanctum medical expert work.

## Purpose

This repository organizes Project Sanctum World Building work: source-of-truth materials, local operating checklists, clinical design notes, review artifacts, submission documents, and checkpoint history.

Project Sanctum Worlds are realistic clinical environments that test frontier AI models on physician-level judgment: synthesis across messy documents, prioritization, uncertainty handling, medication reasoning, specialist conflict resolution, and safe decision-making.

## Current Status (2026-06-11)

- Active world: Korvin Merrow World, created as `Healthcare_247_Merrow` (live, 26 files; World Spec approved by Stacey S; Final Files AutoQC 78/78 after three revisions).
- Target is 10 tasks and all 10 have piloted.
- Tasks 1-6: Ready for Delivery (per-task Preference Label / final-review tails pending).
- Task 7: v3 reseeded after Abi retired the v2 design as unfair; fair mid-band (mean 0.525), bankable pending the golden-reachability check.
- Task 8: awaiting first human review (gabapentin uptitration, bimodal ~0.67).
- Tasks 9-10: piloted with FA/GA drafted (KM09 sepsis-to-principal ~0.31; KM10 CDI query response, all-floor ~0.25, reachability open).
- Live state source: `dashboard/km-world-dashboard.html`, `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, root `WORKSPACE_FILE_MAP.md`, and each active `TASKN-STATE.md`. This README is only the front door.

## Current Boundary

Onboarding Steps 1-6 are complete for Korvin. Later production-pipeline work has begun under explicit authorization, but every new RL Studio action, task upload, agent run, QA run, AutoQC response, scoring artifact, package, upload, or submission still requires exact Alexander authorization before execution.

Historical onboarding-only checklists are archived. Root `WORKSPACE_FILE_MAP.md`, `AGENTS.md`, `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`, active `TASKN-STATE.md` files, the dashboard, and `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md` govern the live task phase.

## New Collaborator Quickstart

Read this repo progressively. Do not try to absorb every locked package on the first pass.

1. Read [AGENTS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/AGENTS.md>) for operating guardrails and current boundaries.
2. Read [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>) for the live phase, active task frontier, and file placement rules.
3. Read [worlds/korvin-merrow/00-MASTER-NARRATIVE.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/00-MASTER-NARRATIVE.md>) to understand how the world was built and what Task 1 taught us.
4. Read [worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md>) before touching any task-stage work.
5. Read the active `TASKN-STATE.md` before proposing, drafting, building, or uploading anything for that task.

Current gate: KM07 pilot result pending and KM08 upload awaits exact Alexander authorization. All RL Studio actions still require exact authorization.

## Source-Of-Truth Ladders

Use the smallest ladder that answers your question.

**Live phase and permissions:**
- [AGENTS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/AGENTS.md>)
- [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>)
- [dashboard/km-world-dashboard.html](</C:/Users/Dyrane/Documents/sanctum-world-workspace/dashboard/km-world-dashboard.html>)
- [worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md>)

**Readable continuity:**
- [worlds/korvin-merrow/00-MASTER-NARRATIVE.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/00-MASTER-NARRATIVE.md>)
- [worlds/korvin-merrow/task-setup/task1-lifecycle-log.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/task1-lifecycle-log.md>)
- [docs/reasoning-discipline.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/docs/reasoning-discipline.md>)

**Current task work:**
- [worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md>)
- [worlds/korvin-merrow/task-setup/CHECKPOINT-AUDIT-pre-task2.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/CHECKPOINT-AUDIT-pre-task2.md>)
- [worlds/korvin-merrow/task-setup/task2/KM02-design-plan-for-review.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/task2/KM02-design-plan-for-review.md>) for Task 2 study only.

**Clinical canon lookup:**
- [worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md>)
- [worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md>)
- Locked packages and ratifications under `worlds/korvin-merrow/world-spec-prep/` only when a specific clinical-canon question requires them.

**Workspace structure and duplication:**
- [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>)
- [worlds/korvin-merrow/README.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/README.md>)

## Template And Method Index

Use templates and methods by purpose, not by browsing.

- Official World Spec template: `reference/templates/World_Spec_Template_05_06.docx`.
- Official AutoQC templates: `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`, `AutoQC_Section_3_World_Files_v6.6_writer.docx`, and `AutoQC_Section_4_Task_Prompts_v6.6_writer.docx`.
- Brainstorm templates: `reference/templates/brainstorm.docx` and `reference/templates/brainstorm.md`.
- Template links and provenance: `reference/templates/template-links.md`.
- DOCX operating method: [docs/docx-generation-method.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/docs/docx-generation-method.md>).
- Reference-file design system: [worlds/korvin-merrow/reference-file-design/epic-note-design-system.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/reference-file-design/epic-note-design-system.md>).
- Reference-file generator: `tools/generate_reference_files.py`.
- Golden response shell for task-stage platform work: `worlds/korvin-merrow/task-setup/platform/_templates/golden-template-worldstyle.docx`.
- Preflight checklists: `reference/checklists/`, especially `spec-autoqc-preflight.md`.

## Active World

Korvin Merrow is an Emergency Medicine / Internal Medicine acute hospital world. The approved Brainstorm centers on a 62-year-old male with diabetes, hypertension, CKD stage 3, HFrEF/CAD, polypharmacy, PMR with unclear prednisone taper, suspected urinary-source sepsis, AKI, medication-management tension, and discharge-readiness complexity.

The clinical design principle is realistic hospital complexity, not a rare disease puzzle.

## Workflow Phases

- Brainstorm, World Spec, file ecosystem, submission preparation, execution artifact generation, Step 9 file review, and Task 1 setup/evaluation are historical for Korvin.
- Current repeatable operating layer is task-pipeline support: task setup, agent runs, QA, FA/GA, PL, and final review, one authorized step at a time.
- Do not infer permission to continue from completed history; use root `WORKSPACE_FILE_MAP.md` and the active `TASKN-STATE.md`.

## Folder Structure

```text
AGENTS.md
README.md
docs/
  CONTRIBUTING.md
  agent-workflow.md
  git-workflow.md
  security-and-privacy.md
  tooling-audit.md
dashboard/
  km-world-dashboard.html
WORKSPACE_FILE_MAP.md
reference/
  source/
    New Writers Version - Instruction Guide (05_24).docx
    New Writers Version - Instruction Guide (05_24).md
    _Task Selection Categories For Team.xlsx
  templates/
  workflows/
  checklists/
  world-spec-guidelines/
worlds/
  korvin-merrow/
    README.md
    active/
      brainstorm.md
      clinical-logic.md
      task-map.md
      world-spec.md
    history/
    planning/
    remediation/
    reviews/
    submission/
    world-spec-prep/
      candidate-review/
      decision-logs/
      locked/
      planning-scaffolds/
      ratifications/
      reviews/
```

## Start Here

For a new collaborator or a future AI session, use this order:

1. [AGENTS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/AGENTS.md>) for operating instructions.
2. [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>) for live state, structure, and task frontier.
3. [worlds/korvin-merrow/00-MASTER-NARRATIVE.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/00-MASTER-NARRATIVE.md>) for the readable end-to-end story.
4. [dashboard/km-world-dashboard.html](</C:/Users/Dyrane/Documents/sanctum-world-workspace/dashboard/km-world-dashboard.html>) for the visual dashboard.
5. [worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md>) before any future task setup.
6. The active `TASKN-STATE.md` for the task you are working.

Do not start by browsing every prep file. Most prep files are supporting memory, not active instructions.

## How To Use This Repo

1. Read [AGENTS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/AGENTS.md>) and [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>) first.
2. Check the active `TASKN-STATE.md`, `TASK-RUNBOOK.md`, and any task-specific plan before acting.
3. Check [WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>) before creating, moving, renaming, or deleting files.
4. Confirm the current phase gate.
5. Use official templates from `reference/templates/`.
6. Keep source/reference material separate from authored work.
7. Update the workspace file map when structure, official sources/templates, submission artifacts, or duplicate-purpose files change.
8. Commit checkpoints after major milestones.

## Repository Hygiene

- Keep root files limited to `README.md`, `AGENTS.md`, `WORKSPACE_FILE_MAP.md`, `.gitignore`, and unavoidable repository controls.
- Keep official source and templates under `reference/`.
- Keep current project/task state in root `WORKSPACE_FILE_MAP.md`, active `TASKN-STATE.md` files, the dashboard, and the performance report.
- Keep durable documentation under `docs/`.
- Keep world-specific authored/canonical work under `worlds/korvin-merrow/` lifecycle folders; `active/` is historical/current-authored context, not the only active surface.
- Keep world-specific historical artifacts under `worlds/korvin-merrow/history/`.
- Keep reviewer remediation briefs under `worlds/korvin-merrow/remediation/`.
- Keep review artifacts in `worlds/korvin-merrow/reviews/`.
- Keep submission artifacts in `worlds/korvin-merrow/submission/`.
- Keep World Spec preparation artifacts in `worlds/korvin-merrow/world-spec-prep/`.
- Do not create a new folder or README unless it clarifies navigation better than updating `WORKSPACE_FILE_MAP.md`.

## Assistant Roles

- Alexander: physician expert, clinical source of truth, final approver.
- Codex: local workspace manager, source controller, git checkpoint manager, reviewer simulation, continuity system.
- Claude: official Sanctum drafting assistant for structure, formatting, consistency, and template-heavy drafting after the guide recommends it.
- ChatGPT: ad hoc reasoning/review support if used, subject to the same source-of-truth and authorship boundaries.

AI may organize, critique, audit, and format. AI must not originate final clinical decisions, task prompts, golden responses, grader guidelines, or downstream evaluation content outside the authorized phase. Task prompts, goldens, grader guidance, FA/GA, and PL remain physician-owned even when AI helps review or de-risk them.

## Source-Of-Truth Policy

- Official Sanctum instructions live under `reference/`.
- Project state and workspace structure live in root `WORKSPACE_FILE_MAP.md`, active `TASKN-STATE.md` files, the dashboard, and the performance report.
- Clinical authored work lives under `worlds/korvin-merrow/active/`.
- Physician decisions come from Alexander.
- Official templates are used as bases for submission artifacts.

## Privacy And Confidentiality

Keep this repository private. Do not publish Mercor, Sanctum, RL Studio, internal templates, proprietary guide content, authenticated links, credentials, browser exports, or any real patient data.

Korvin Merrow and all future patient identities must be fictional.

## Rollback And Checkpoints

Use git for local checkpoints, rollback, and change review. Before any RL Studio upload, prefer a clean working tree or a clearly documented pending state.

Useful commands:

```powershell
git status --short --branch
git log --oneline -10
git diff
git restore --source <commit> -- <path>
```

## Do Not Commit Publicly

Do not commit publicly:

- Credentials, tokens, API keys, cookies, browser profiles, or session exports
- Real patient data or PHI
- Authenticated-only links that expose private work
- Raw proprietary downloads unless intentionally approved for private reference storage
- RL Studio exports containing sensitive reviewer or platform information without review
- Work that violates the current phase boundary
