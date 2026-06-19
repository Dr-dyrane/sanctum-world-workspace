# Sanctum World Workspace

Private local workspace for Alexander Udeogaranya's Mercor Project Sanctum medical expert work.

## Purpose

This repository organizes Project Sanctum World Building work: source-of-truth materials, local operating checklists, clinical design notes, review artifacts, submission documents, and checkpoint history.

Project Sanctum Worlds are realistic clinical environments that test frontier AI models on physician-level judgment: synthesis across messy documents, prioritization, uncertainty handling, medication reasoning, specialist conflict resolution, and safe decision-making.

## Current Status (19 June 2026)

Three worlds. This README is only the front door. The authoritative, moment-to-moment status is the platform board and the live records, not this page.

- Korvin Merrow (World 1) - LIVE as `Healthcare_247_Merrow`. KM01 through KM06 delivered; KM07 through KM10 Ready for Delivery. Emergency/Internal Medicine acute hospital world: sepsis physiology, HFrEF/CAD, CKD 3, diabetes, PMR on unverified prednisone, AKI, discharge-readiness complexity.
- Ondina Vasquell (World 2) - LIVE as `Healthcare_297_Vasquell`. OV01 through OV04 Ready for Delivery; OV05 retired; OV06 v2 in task writing. Internal Medicine diabetic foot infection world: limb-threat infection, equivocal osteomyelitis, PAD, CKD 3b, payer friction, discharge safety.
- Marva Lydell (World 3) - IN PLANNING. Brainstorm package built locally; no platform action started. Cardiorenal respiratory transition-readiness thesis. Gated behind Alexander's brainstorm approval.

For live detail use `WORKSPACE_FILE_MAP.md`, [dashboard/km-world-dashboard.html](</Users/dyrane/Documents/Builds/sanctum-world-workspace/dashboard/km-world-dashboard.html>), `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, and each world's `00-START-HERE.md` or `WORLD-STATUS.md`.

## Current Boundary

Onboarding Steps 1-6 are complete for Korvin. Production-pipeline work has begun under explicit authorization, but every new RL Studio action, task upload, agent run, QA run, AutoQC response, scoring artifact, package, upload, or submission still requires exact Alexander authorization before execution. World 3 is in pre-brainstorm planning and authorizes no platform action from its folder.

## Worlds

| World | Status | Cockpit / entry point |
|---|---|---|
| Korvin Merrow (World 1) | Live; tasks in delivery | [worlds/korvin-merrow/README.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/worlds/korvin-merrow/README.md>), `00-MASTER-NARRATIVE.md`, `task-setup/TASK-RUNBOOK.md` |
| Ondina Vasquell (World 2) | Live; tasks in delivery | [worlds/ondina-vasquell/00-START-HERE.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/worlds/ondina-vasquell/00-START-HERE.md>), `docs/WORLD-STATUS.md` |
| Marva Lydell (World 3) | Brainstorm in progress; no platform action | [worlds/marva-lydell/00-START-HERE.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/worlds/marva-lydell/00-START-HERE.md>), `docs/WORLD-STATUS.md` |

## Start Here

For a new collaborator or a fresh AI session, read in this order. Do not try to absorb every locked package on the first pass; most prep files are supporting memory, not active instructions.

1. [AGENTS.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/AGENTS.md>) - operating guardrails and the current boundary.
2. [WORKSPACE_FILE_MAP.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/WORKSPACE_FILE_MAP.md>) - live state, structure, placement rules, task frontier.
3. [DO-NOT-REPEAT.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/DO-NOT-REPEAT.md>) - the cold-start mistakes ledger, every error written as a rule.
4. [docs/README.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/docs/README.md>) - index of all lessons and playbooks (the helper docs).
5. The world you are working: its `00-START-HERE.md` (Ondina, Marva) or `README.md` plus `00-MASTER-NARRATIVE.md` (Korvin).
6. For task-stage Korvin work: `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`, then the active `TASKN-STATE.md`.
7. For a new world: [docs/world-factory-playbook.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/docs/world-factory-playbook.md>), then `reference/workflows/internal-medicine-world-planning-canvas.md`.

## Source-Of-Truth Ladders

Use the smallest ladder that answers your question.

**Live phase and permissions:**
- `AGENTS.md`, `WORKSPACE_FILE_MAP.md`
- `dashboard/km-world-dashboard.html`
- `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`

**Helper docs (lessons and playbooks):**
- [docs/README.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/docs/README.md>) - the full docs index.
- `docs/anti-hallucination.md`, `docs/reasoning-discipline.md` - the verification doctrine.

**Official source and templates:**
- [reference/README.md](</Users/dyrane/Documents/Builds/sanctum-world-workspace/reference/README.md>) - the reference-tree map.
- `reference/source/README.md` - source-of-truth index (current vs `_superseded/`).

**Readable continuity:**
- `worlds/korvin-merrow/00-MASTER-NARRATIVE.md`, `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`

**Current task work:**
- `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`, then the active `TASKN-STATE.md`
- `worlds/ondina-vasquell/00-START-HERE.md` for Ondina tasking state
- `worlds/marva-lydell/00-START-HERE.md` for World 3 planning state

**Clinical canon lookup (Korvin):**
- `worlds/korvin-merrow/world-spec-prep/locked/` - the ratified world-spec packages (identity, governance, timeline, medication, comorbidity, calendar).
- `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`
- `worlds/korvin-merrow/active/` - brainstorm, clinical-logic, task-map.

## Template And Method Index

Use templates and methods by purpose, not by browsing.

- Repeatable brainstorm-to-spec recipe (READ FIRST for a new world): `docs/world-factory-playbook.md`.
- All lessons and playbooks: `docs/README.md`.
- Official World Spec template: `reference/templates/World_Spec_Template_05_06.docx`.
- Official AutoQC templates: `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`, `AutoQC_Section_3_World_Files_v6.6_writer.docx`, `AutoQC_Section_4_Task_Prompts_v6.6_writer.docx`; Sections 5-6 in `reference/source/autoqc-section-guides/`.
- Brainstorm templates: `reference/templates/brainstorm.docx`, `reference/templates/brainstorm.md`.
- DOCX operating method: `docs/docx-generation-method.md`.
- Reference-file design system: `worlds/korvin-merrow/reference-file-design/epic-note-design-system.md`.
- Preflight checklists: `reference/checklists/`, especially `spec-autoqc-preflight.md`.

## Task File Mount Hygiene

For any task upload or rerun, read the first trajectory's `find /docs` tree before treating scores as evidence. There must be exactly the intended task file under `/docs/filesystem`, no task-specific file under `/docs/.apps_data`, and no stale same-purpose filename. If the gate fails, delete every file in the Studio Task Files card, re-add only the current plain Filesystem file, save, refresh, and rerun. OV01 job `9765ba91` proved that a renamed task file can dodge duplicate-name AutoQC while still mounting two order sets.

## Workflow Phases

- For Korvin, brainstorm through Step 9 file review and Task 1 setup are historical. The current repeatable layer is task-pipeline support: task setup, agent runs, QA, FA/GA, PL, and final review, one authorized step at a time.
- For a new world, follow `docs/world-factory-playbook.md`: brainstorm, substrate ratification, spec assembly, reference files, transcripts, task setup.
- Do not infer permission to continue from completed history; use root `WORKSPACE_FILE_MAP.md` and the active `TASKN-STATE.md` or world cockpit.

## Folder Structure

Concise top-level map. The full, authoritative structure and placement rules live in `WORKSPACE_FILE_MAP.md`.

```text
sanctum-world-workspace/
  AGENTS.md                 # operating guardrails (read first)
  README.md                 # this front door
  WORKSPACE_FILE_MAP.md     # authoritative structure + live state
  DO-NOT-REPEAT.md          # cold-start mistakes ledger
  docs/                     # lessons + playbooks (see docs/README.md)
  reference/                # official source, templates, guidelines (see reference/README.md)
    source/                 # source-of-truth by purpose + _superseded/ (see source/README.md)
    templates/  workflows/  checklists/  world-spec-guidelines/  world-spec-examples/  skills/
  dashboard/                # km-world-dashboard.html + src/
  tools/                    # all Python build and verify scripts
  worlds/
    korvin-merrow/          # World 1 (live): README, 00-MASTER-NARRATIVE, task-setup/, world-spec-prep/, ...
    ondina-vasquell/        # World 2 (live): 00-START-HERE, docs/, tasks/, build/, ...
    marva-lydell/           # World 3 (planning): 00-START-HERE, docs/, build/ (placeholder-gated), submission/
```

## How To Use This Repo

1. Read `AGENTS.md` and `WORKSPACE_FILE_MAP.md` first.
2. Check the active `TASKN-STATE.md`, `TASK-RUNBOOK.md`, or the world cockpit before acting.
3. Check `WORKSPACE_FILE_MAP.md` before creating, moving, renaming, or deleting files.
4. Confirm the current phase gate.
5. Use official templates from `reference/templates/` and current sources via `reference/source/README.md`.
6. Keep source/reference material separate from authored work.
7. Update `WORKSPACE_FILE_MAP.md` when structure, official sources/templates, submission artifacts, or duplicate-purpose files change.
8. Commit checkpoints after major milestones.

## Repository Hygiene

- Keep root files limited to `README.md`, `AGENTS.md`, `WORKSPACE_FILE_MAP.md`, `DO-NOT-REPEAT.md`, `.gitignore`, and unavoidable repository controls.
- Keep official source and templates under `reference/`; cite current sources via `reference/source/README.md`, never a `_superseded/` file.
- Keep durable documentation under `docs/`, indexed by `docs/README.md`.
- Keep each world's authored work under `worlds/<world>/` lifecycle folders; the cockpit (`00-START-HERE.md` or `README.md`) is the entry point.
- Keep world-specific historical artifacts inside that world's `history/`, `_pipeline-history/`, `archive/`, or `_superseded/` folders, not at a live surface.
- Do not create a new folder or README unless it clarifies navigation better than updating `WORKSPACE_FILE_MAP.md`.

## Assistant Roles

- Alexander: physician expert, clinical source of truth, final approver.
- Codex: local workspace manager, source controller, git checkpoint manager, reviewer simulation, continuity system.
- Claude: official Sanctum drafting assistant for structure, formatting, consistency, and template-heavy drafting after the guide recommends it.
- ChatGPT: ad hoc reasoning/review support if used, subject to the same source-of-truth and authorship boundaries.

AI may organize, critique, audit, and format. AI must not originate final clinical decisions, task prompts, golden responses, grader guidelines, or downstream evaluation content outside the authorized phase. Task prompts, goldens, grader guidance, FA/GA, and PL remain physician-owned even when AI helps review or de-risk them.

## Source-Of-Truth Policy

- Official Sanctum instructions live under `reference/`; the current version of each is named in `reference/source/README.md`.
- Project state and workspace structure live in root `WORKSPACE_FILE_MAP.md`, active `TASKN-STATE.md` files, the dashboard, and the performance report.
- Clinical authored work lives under each world's folder.
- Physician decisions come from Alexander.
- Official templates are used as bases for submission artifacts.

## Privacy And Confidentiality

This repository may be pushed to a public GitHub remote after Alexander explicitly marks the current tree public-safe. Public-safe means no credentials, real patient data, authenticated-only links, browser exports, session material, or prohibited proprietary downloads are tracked. All patient identities (Korvin Merrow, Ondina Vasquell, Marva Lydell, and any future world) must be fictional.

## Rollback And Checkpoints

Use git for local checkpoints, rollback, and change review. Before any RL Studio upload, prefer a clean working tree or a clearly documented pending state.

```powershell
git status --short --branch
git log --oneline -10
git diff
git restore --source <commit> -- <path>
```

## Do Not Commit Or Publish

- Credentials, tokens, API keys, cookies, browser profiles, or session exports
- Real patient data or PHI
- Authenticated-only links that expose private work
- Raw proprietary downloads unless intentionally approved for repository storage
- RL Studio exports containing sensitive reviewer or platform information without review
- Work that violates the current phase boundary
