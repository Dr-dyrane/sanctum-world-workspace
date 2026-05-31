# Sanctum World Workspace

Private local workspace for Alexander Udeogaranya's Mercor Project Sanctum medical expert work.

## Purpose

This repository organizes Project Sanctum World Building work: source-of-truth materials, local operating checklists, clinical design notes, review artifacts, submission documents, and checkpoint history.

Project Sanctum Worlds are realistic clinical environments that test frontier AI models on physician-level judgment: synthesis across messy documents, prioritization, uncertainty handling, medication reasoning, specialist conflict resolution, and safe decision-making.

## Current Status

- Active world: Korvin Merrow World
- RL Studio task ID: `cyau8803`
- Brainstorm status: approved after SEND BACK remediation
- Brainstorm AutoQC: revised pass achieved, `0 failed / 51 passed`
- Human review: GO from Stacey S
- Current gate: Clinical Story Skeleton v1 ratified / ready for Identity Package
- World Spec: preparation packet exists, but drafting has not started and remains blocked until Alexander explicitly authorizes drafting

## Onboarding Scope

Current scope is Project Sanctum Phase 1 World Building onboarding, steps 1-6 only:

1. Brainstorm
2. Brainstorm AutoQC
3. Human Brainstorm Review
4. World Spec Document
5. World Spec AutoQC
6. Human World Spec Review

Do not move into synthetic file generation, production task creation, golden responses, grader guidelines, failure analysis, preference labeling, or downstream evaluation unless Alexander explicitly updates the project phase.

## Active World

Korvin Merrow is an Emergency Medicine / Internal Medicine acute hospital world. The approved Brainstorm centers on a 62-year-old male with diabetes, hypertension, CKD stage 3, HFrEF/CAD, polypharmacy, PMR with unclear prednisone taper, suspected urinary-source sepsis, AKI, medication-management tension, and discharge-readiness complexity.

The clinical design principle is realistic hospital complexity, not a rare disease puzzle.

## Workflow Phases

- Brainstorm: concept pitch with World Setup, Frictions, Traps, and Rough Task Ideas.
- Brainstorm AutoQC: automated RL Studio check.
- Human Brainstorm Review: reviewer returns `GO` or `SEND BACK`.
- World Spec preparation: allowed after Brainstorm GO, including identity/governance/story readiness work.
- World Spec drafting: begins only after Alexander explicitly authorizes drafting.
- World Spec AutoQC and Human Review: onboarding ends after Step 6 approval.

## Folder Structure

```text
AGENTS.md
README.md
CONTRIBUTING.md
docs/
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
  templates/
  workflows/
  checklists/
  world-spec-guidelines/
worlds/
  korvin-merrow/
    brainstorm.md
    world-spec.md
    clinical-logic.md
    frictions.md
    traps.md
    task-map.md
    reviewer-feedback.md
    reviews/
    submission/
    world-spec-prep/
```

## Start Here

For a new collaborator or a future AI session, use this order:

1. [project/STATUS.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/STATUS.md>) for live state.
2. [project/WORKSPACE_FILE_MAP.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/project/WORKSPACE_FILE_MAP.md>) for where things live and what not to duplicate.
3. [worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md>) for the current World Spec cockpit.
4. [worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md](</C:/Users/Dyrane/Documents/sanctum-world-workspace/worlds/korvin-merrow/world-spec-prep/physician-decision-log-02.md>) for the ratified Clinical Story Skeleton.

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

- Keep root files limited to repository-level orientation and agent rules.
- Keep official source and templates under `reference/`.
- Keep current project state under `project/`.
- Keep durable documentation under `docs/`.
- Keep world-specific authored work under `worlds/korvin-merrow/`.
- Keep review artifacts in `worlds/korvin-merrow/reviews/`.
- Keep submission artifacts in `worlds/korvin-merrow/submission/`.
- Keep World Spec preparation artifacts in `worlds/korvin-merrow/world-spec-prep/`.
- Do not create a new folder or README unless it clarifies navigation better than updating `WORKSPACE_FILE_MAP.md`.

## Assistant Roles

- Alexander: physician expert, clinical source of truth, final approver.
- Codex: local workspace manager, source controller, git checkpoint manager, reviewer simulation, continuity system.
- Claude: official Sanctum drafting assistant for structure, formatting, consistency, and template-heavy drafting after the guide recommends it.
- ChatGPT: ad hoc reasoning/review support if used, subject to the same source-of-truth and authorship boundaries.

AI may organize, critique, audit, and format. AI must not originate final clinical decisions, task prompts, golden responses, grader guidelines, or downstream evaluation content outside the authorized phase.

## Source-Of-Truth Policy

- Official Sanctum instructions live under `reference/`.
- Project state lives in `project/STATUS.md`.
- Workspace structure and duplication tracking live in `project/WORKSPACE_FILE_MAP.md`.
- Clinical authored work lives under `worlds/korvin-merrow/`.
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
