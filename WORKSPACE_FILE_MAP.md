# Workspace File Map
**Last updated: 2026-06-11 (KM07 v3 reseed + all-10-piloted status refresh; Quill latest-guidance examples registered)**

Single source of truth for repo structure, placement rules, and navigation.
Read this + `AGENTS.md` at the start of any new session before touching files.

---

## Root

```
sanctum-world-workspace/
  DO-NOT-REPEAT.md             ← COLD-START mistakes ledger; read first, every mistake as a rule
  AGENTS.md                    ← operating instructions (always read first)
  README.md                    ← repo overview
  WORKSPACE_FILE_MAP.md        ← this file
  .gitignore                   ← updated 6/9
  _archive/                    ← dead root folders (gitignored); do not read for active work
  dashboard/                   ← km-world-dashboard.html + KM-WORLD-DASHBOARD-PROMPT.md (informational only)
  docs/                        ← lessons, playbooks, domain knowledge
  reference/                   ← Sanctum source docs, templates, guidelines
                                 reference/templates/ now holds the client's latest-guidance worked
                                 example (Quill CDI world+task: Brainstorm, WorldSpec, Task prompt,
                                 Golden Response, Grader Guidelines, FA_GA, Preferential Labeling) +
                                 README.md explaining it and its deltas vs KM conventions
  tools/                       ← all Python scripts (canonical home)
  worlds/
    korvin-merrow/             ← the only live world
```

---

## tools/

All Python scripts live here. **Never create a .py file inside a task folder.**

```
tools/
  mode_a_clone.py              ← LIVE: Mode A clone engine (used by all build scripts)
  generate_reference_files.py  ← LIVE: reference file generator (do NOT use for task artifacts)
  build-world-performance-xlsx.py  ← LIVE: performance spreadsheet builder
  build/                       ← LIVE build scripts (one per task, current version only)
    build-docx-km05-v4.py
    build-docx-km06-v5.py
    build-docx-km07-referral-v1.py
    build-docx-km08-v4.py
  verify/                      ← substrate verification scripts
    verify-km08-substrate.py
    verify-km08-pain.py
  archive/                     ← dead/superseded scripts (reference only, never execute)
    build-docx-km05.py
    build-docx-km06-v1..v4.py
    build-docx-km07-v1.py
    build-docx-km08-physician-v2.py
    build-docx-km08-status-v3.py
    qc-km05*.py
```

---

## worlds/korvin-merrow/

```
worlds/korvin-merrow/
  00-MASTER-NARRATIVE.md       ← readable world history (reference)
  README.md                    ← world overview
  _pipeline-history/           ← all pre-task pipeline artifacts (read-only history)
                                 autoqc/, *-architecture/, execution-preparation/,
                                 submission-preparation/, remediation/, etc.
  active/                      ← brainstorm.md, clinical-logic.md, task-map.md (stale placeholders
                                 → _pipeline-history/active-placeholders/, 6/10)
  planning/                    ← KORVIN_MERROW_PASS_PLAN.md (pre-build pass plan, historical)
  file-inventory/              ← locked file inventory
  file-review/                 ← upload/filesystem/ = AGENT-READ chart DOCXs (26 files)
  final-submission-resolution/ ← locked submission artifacts
  goldens/locked/              ← locked golden DOCXs
  history/                     ← world build history
  reference-file-design/       ← Epic note design system
  reviews/                     ← reviewer records
  submission/                  ← submission artifacts
  supplementary-files/         ← FI-S locked files
  synthetic-files/             ← locked synthetic chart files
  task-context-files/          ← FI-T locked task-context files
  task-prompts/                ← historical task prompt drafts
  task-setup/                  ← ALL active task work lives here
  world-spec-prep/             ← world spec planning history
```

---

## worlds/korvin-merrow/task-setup/

The active working layer. **platform/** is the single source of truth for uploadable sets.

```
task-setup/
  TASK-RUNBOOK.md              ← READ FIRST before any task-stage work
  task1-lifecycle-log.md       ← canonical Task 1 history and lessons
  CHECKPOINT-AUDIT-pre-task2.md
  KM-RETROSPECTIVE-tasks1-2.md ← tasks 1-2 error ledger (kept at root: cited by 10+ docs via this path)
  step10-review-packet.md      ← tasks 2-6 planning packet (kept at root: cited by WORLD_SPEC_KICKOFF)
  KM-WORLD-PERFORMANCE-REPORT.md
  KM-World-Performance.xlsx
  KM-vs-QUILL-SANCTUM-MAPPING-REVIEW.md  ← KM-vs-exemplar gap map + anticipated-corrections queue (6/11)
  platform/                    ← UPLOAD SETS (single source of truth per task)
    task1/current/             ← KM01: med-rec safety review (delivered)
    task2/current/             ← KM02: discharge summary (delivered)
    task3/current/             ← KM03: transition-of-care summary (delivered)
    task4/current/             ← KM04: interdisciplinary care plan (delivered)
    task5/current/             ← KM05: post-discharge transition note (delivered)
    task6/current/             ← KM06: post-discharge follow-up, insulin (delivered)
    task7/current/             ← KM07 v3: nephrology referral letter, placeholder-synthesize (under first human review)
    task8/current/             ← KM08 v4: gabapentin uptitration addendum (under first human review)
    task9/current/             ← KM09: coding attestation, sepsis-to-principal (under first human review)
    task10/current/            ← KM10: CDI query response (under first human review; reachability not yet confirmed)
    task*/archive/             ← superseded platform sets (do not upload from archive)
  task1/                       ← fa-ga/, preference-labeling/, handoff/, trajectories/
  task2/                       ← TASK2-STATE.md + fa-ga/, runs/, learnings/, preference-labeling/
  task3/                       ← TASK3-STATE.md + fa-ga/, runs/, design/, preference-labeling/
  task4/                       ← TASK4-STATE.md + KM04-prebuild-review-and-build-gates.md (kept at root:
                                 cited by relative ../ paths in locked design docs) + fa-ga/, runs/, design/
  task5/                       ← TASK5-STATE.md + KM05-prebuild-review-and-build-gates.md (same reason)
                                 + fa-ga/, runs/, design/ (incl. KM05-LIFECYCLE-GUIDE.md), preference-labeling/;
                                 superseded v2/v3 plans → design/archive/ (6/10)
  task6/                       ← TASK6-STATE.md + fa-ga/ (FA-GA-current.md is canonical; conflicting
                                 FA-GA-v5.md → fa-ga/archive/), runs/, design/ (retired v1/v3 plans →
                                 design/archive/), preference-labeling/, handoff/ (NOTE-FOR-ABI-task6.md)
  task7/                       ← TASK7-STATE.md + design/ (v2-PLAN, v3-placeholder-plan), runs/ (v2 + v3
                                 results + golden-reachability structural pass), fa-ga/, qa/, learnings/
                                 (KM07-learnings.md: the fairness + chart-aware-grader lessons)
  task8/                       ← TASK8-STATE.md + design/KM08-PLAN.md + fa-ga/, runs/
  task9/                       ← TASK9-STATE.md + design/ (KM09-PLAN, bite-risk-assessment), fa-ga/, runs/
  task10/                      ← TASK10-STATE.md + design/KM10-PLAN.md + fa-ga/, runs/
```

---

## platform/task8/current/ — KM08 v4.1 (READY TO UPLOAD, 6/10 anchor-fix pass)

```
prompt-task8-v4.txt                             ← discharge-day (5/24) pain/sleep addendum prompt
neuropathic_pain_sleep_addendum_draft_05242026.docx  ← Mode A clone, de-telegraphed, byte-verified
golden-KM08-v4.docx                            ← Mode A clone, byte-verified
grader-guidelines-task8-v4.txt                 ← Sang five-block, verbatim clauses, ~520 words
RUN-INSTRUCTIONS-v4.md                         ← workflow = Progress Note Daily Rounding Documentation
```

Build script: `tools/build/build-docx-km08-v41.py` (supersedes build-docx-km08-v4.py: 05/22 pre-snapshot anchor + telegraphing draft)
Design doc: `task8/design/KM08-PLAN.md` (single source of truth; gates 2-3 record the 6/10 fixes)
KM07 v2 build script: `tools/build/build-docx-km07-v2.py` (genre-true PCP base)
Pilot preregistrations: `task7/runs/KM07-v2-pilot-preregistration.md`, `task8/runs/KM08-v41-pilot-preregistration.md` (locked pre-pilot, never edited after)

---

## Navigation ladder (read in this order for any new session)

0. `DO-NOT-REPEAT.md` (repo root) — the cold-start mistakes ledger; read it before the ladder so you inherit the scar tissue without re-paying for it.
1. `AGENTS.md` — operating instructions and guardrails
2. `WORKSPACE_FILE_MAP.md` — this file; structure + placement rules
3. `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md` — before any task-stage work
4. `worlds/korvin-merrow/task-setup/taskN/TASKN-STATE.md` — for the task you are working
5. `worlds/korvin-merrow/task-setup/platform/taskN/current/` — active uploadable set
6. `docs/grader-guidelines-lessons.md` — before editing any grader
7. `docs/reasoning-discipline.md` — before any one-way-door decision
8. `docs/task-structure-dossier.md` — before brainstorming any new world or task slate (Abi variety mandate, 6/10: every world carries at least 5 distinct structural categories; sheet snapshot at `reference/source/task-selection-categories-snapshot-2026-06-10.csv`)
9. `docs/task-difficulty-lessons.md` — before designing any task mechanism (the cold/forced/contradicted difficulty rule AND the fairness doctrine in sections 5-6: never floor a planted claim with no correction instruction)
10. `docs/clinical-voice-lessons.md` — before authoring any world file, golden, or reference template (the World #1 pipeline voice standard)
11. `reference/templates/README.md` — the client's latest-guidance worked example (CDI world+task) and its deltas vs KM conventions
12. `docs/git-workflow.md` — before any git work (the sandbox delete-grant lesson: git is blocked until `mcp__cowork__allow_cowork_file_delete` is approved, then full git works)

---

## Placement rules

| Artifact type | Where it lives |
|---|---|
| Build scripts (current) | `tools/build/` |
| Build scripts (dead/old) | `tools/archive/` |
| Substrate/verify scripts | `tools/verify/` |
| Uploadable task set | `platform/taskN/current/` |
| Superseded task sets | `platform/taskN/archive/YYYY-MM-DD-reason/` |
| Task state + history | `task-setup/taskN/` subfolders |
| Dead root packages | `_archive/` (gitignored) |
| Pipeline build history | `korvin-merrow/_pipeline-history/` |
| Loose planning docs | `task-setup/taskN/design/` or `runs/` or `fa-ga/` — never at folder root |
| Dashboard + perf report | Update on every pilot gate clear or status change |

---

## Contribution hygiene rules (enforced on every commit)

1. **No .py files outside `tools/`** — ever. Live in `tools/build/` or `tools/verify/`; dead in `tools/archive/`.
2. **No loose .md files at folder roots** — planning docs go in `design/`, run records in `runs/`, annotations in `fa-ga/` or `preference-labeling/` or `handoff/`.
3. **No task artifacts outside `platform/taskN/current/`** — superseded sets move to `platform/taskN/archive/YYYY-MM-DD-reason/` immediately.
4. **No new root-level folders** — dead packages go in `_archive/` (gitignored).
5. **Dashboard + report updated on every pilot gate clear** — `dashboard/km-world-dashboard.html` and `task-setup/KM-WORLD-PERFORMANCE-REPORT.md` are always current.
6. **One canonical home per artifact type** — if you can't name the exact folder, check this file before creating.

---

## Active task status (6/11/2026)

Live status lives in `dashboard/km-world-dashboard.html`, `task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, and each `taskN/TASKN-STATE.md`; this table is a convenience snapshot - trust those if they disagree.

| Task | Status |
|---|---|
| KM01 | Delivered |
| KM02 | Delivered |
| KM03 | Delivered |
| KM04 | Delivered |
| KM05 | Delivered |
| KM06 | Delivered |
| KM07 | Under first human review (platform 2e5v8bf2, under Alexander). Fairness-corrected v3, nephrology referral; model completes the medication-reconciliation status from the record; fair mid-range (mean 0.525); golden-reachability check outstanding. `platform/task7/current/` |
| KM08 | Under first human review (platform 1l71a77d, under Alexander). Gabapentin-uptitration progress note; bimodal, mean ~0.67. `platform/task8/current/` |
| KM09 | Under first human review (platform 0zko93d5, under Abi O). Inpatient coding and DRG assignment; declines to anchor the principal diagnosis on sepsis; ~0.31. `platform/task9/current/` |
| KM10 | Reseed per Abi first review (6/11). CDI query response; the encephalopathy item needs rework across golden, FA, and grader, with the decline resting on clinical grounds rather than timing. Drafts at `task10/design/KM10-v2-reseed-plan.md`. (platform ixr0ddb9, under Abi O.) |

World target: **10 tasks** (Larry 6/10 pod announcement: over 8, preferably 10, before a new world; Alexander decision recorded in `reference/world-spec-guidelines/POD-ANNOUNCEMENT-2026-06-10-delivery-day-and-operating-rules.md`). Submit each task as it clears — no batching (pod rule 3).
