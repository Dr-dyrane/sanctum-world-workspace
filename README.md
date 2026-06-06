# Sanctum World Workspace

Private local workspace for Alexander Udeogaranya's Mercor Project Sanctum medical expert work.

## Purpose

This repository organizes Project Sanctum World Building work: source-of-truth materials, local operating checklists, clinical design notes, review artifacts, submission documents, and checkpoint history.

Project Sanctum Worlds are realistic clinical environments that test frontier AI models on physician-level judgment: synthesis across messy documents, prioritization, uncertainty handling, medication reasoning, specialist conflict resolution, and safe decision-making.

## Current Status

- Active world: Korvin Merrow World
- RL Studio task ID: `cyau8803`
- World Spec: approved by Stacey S after RL Studio upload and Spec AutoQC.
- World created: `Healthcare_247_Merrow`, with Final Files AutoQC 78/78 after three revisions.
- Task 1: final human review complete / approved by Abi Osagie on 2026-06-06.
- Current gate: await Alexander-authorized next task/pipeline step, likely Task 2 setup.
- Live state source: `project/STATUS.md`. This README is only the front door.

## Current Boundary

Onboarding Steps 1-6 are complete for Korvin. Later production-pipeline work has begun under explicit authorization, but every new RL Studio action, task upload, agent run, QA run, AutoQC response, scoring artifact, package, upload, or submission still requires exact Alexander authorization before execution.

Historical onboarding-only checklists are preserved under `project/` and `reference/`, but `project/STATUS.md`, `project/PHASE_MAP.md`, `docs/status-dashboard.md`, `docs/world-pipeline-playbook.md`, and `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` now govern the live phase.

## Active World

Korvin Merrow is an Emergency Medicine / Internal Medicine acute hospital world. The approved Brainstorm centers on a 62-year-old male with diabetes, hypertension, CKD stage 3, HFrEF/CAD, polypharmacy, PMR with unclear prednisone taper, suspected urinary-source sepsis, AKI, medication-management tension, and discharge-readiness complexity.

The clinical design principle is realistic hospital complexity, not a rare disease puzzle.

## Workflow Phases

- Brainstorm, World Spec, file ecosystem, submission preparation, execution artifact generation, Step 9 file review, and Task 1 setup/evaluation are historical for Korvin.
- Current repeatable operating layer is task-pipeline support: task setup, agent runs, QA, FA/GA, PL, and final review, one authorized step at a time.
- Do not infer permission to continue from completed history; use the current phase in `project/STATUS.md`.

## Folder Structure

```text
AGENTS.md
README.md
docs/
  CONTRIBUTING.md
  agent-workflow.md
  git-workflow.md
  security-and-privacy.md
  status-dashboard.md
  tooling-audit.md
project/
  STATUS.md
  DECISIONS.md
  EXECUTION_CHECKLIST.md
  PASS_PLAN.md
  PHASE_MAP.md
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

1. [project/STATUS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/STATUS.md>) for live state.
2. [project/WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/WORKSPACE_FILE_MAP.md>) for where things live and what not to duplicate.
3. [docs/status-dashboard.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/docs/status-dashboard.md>) for the quick dashboard.
4. [worlds/korvin-merrow/00-MASTER-NARRATIVE.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/00-MASTER-NARRATIVE.md>) for the readable end-to-end story.
5. [worlds/korvin-merrow/task-setup/task1-lifecycle-log.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/task1-lifecycle-log.md>) for Task 1 history and lessons.
6. [worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md>) before any future task setup.

Do not start by browsing every prep file. Most prep files are supporting memory, not active instructions.

## How To Use This Repo

1. Read [project/STATUS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/STATUS.md>) first.
2. Check [project/PASS_PLAN.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/PASS_PLAN.md>) and [project/EXECUTION_CHECKLIST.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/EXECUTION_CHECKLIST.md>) before acting.
3. Check [project/WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/WORKSPACE_FILE_MAP.md>) before creating, moving, renaming, or deleting files.
4. Confirm the current phase gate.
5. Use official templates from `reference/templates/`.
6. Keep source/reference material separate from authored work.
7. Update the workspace file map when structure, official sources/templates, submission artifacts, or duplicate-purpose files change.
8. Commit checkpoints after major milestones.

## Repository Hygiene

- Keep root files limited to `README.md`, `AGENTS.md`, `.gitignore`, and unavoidable repository controls.
- Keep official source and templates under `reference/`.
- Keep current project state under `project/`.
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
- Project state lives in `project/STATUS.md`.
- Workspace structure and duplication tracking live in `project/WORKSPACE_FILE_MAP.md`.
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
