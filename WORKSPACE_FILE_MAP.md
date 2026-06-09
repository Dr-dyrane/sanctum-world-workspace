# Workspace File Map
**Last updated: 2026-06-09 (post-hygiene audit)**

Single source of truth for repo structure, placement rules, and navigation.
Read this + `AGENTS.md` at the start of any new session before touching files.

---

## Root

```
sanctum-world-workspace/
  AGENTS.md                    ← operating instructions (always read first)
  README.md                    ← repo overview
  WORKSPACE_FILE_MAP.md        ← this file
  .gitignore                   ← updated 6/9
  _archive/                    ← dead root folders (gitignored); do not read for active work
  dashboard/                   ← km-world-dashboard.html (informational only)
  docs/                        ← lessons, playbooks, domain knowledge
  reference/                   ← Sanctum source docs, templates, guidelines
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
  active/                      ← brainstorm.md, clinical-logic.md, task-map.md
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
  KM-WORLD-PERFORMANCE-REPORT.md
  KM-World-Performance.xlsx
  platform/                    ← UPLOAD SETS (single source of truth per task)
    task1/current/             ← KM01: med-rec safety review (RFD)
    task2/current/             ← KM02: discharge summary (RFD)
    task3/current/             ← KM03: transition-of-care summary (RFD)
    task4/current/             ← KM04: interdisciplinary care plan (RFD)
    task5/current/             ← KM05: post-discharge transition note (post-Sang)
    task6/current/             ← KM06: post-discharge follow-up, insulin (RFD)
    task7/current/             ← KM07: nephrology referral letter (staged, not piloted)
    task8/current/             ← KM08 v4: gabapentin uptitration addendum (READY TO UPLOAD)
    task*/archive/             ← superseded platform sets (do not upload from archive)
  task1/                       ← fa-ga/, preference-labeling/, handoff/, trajectories/
  task2/                       ← TASK2-STATE.md + fa-ga/, runs/, learnings/, preference-labeling/
  task3/                       ← TASK3-STATE.md + fa-ga/, runs/, design/, preference-labeling/
  task4/                       ← TASK4-STATE.md + fa-ga/, runs/, design/, preference-labeling/
  task5/                       ← TASK5-STATE.md + fa-ga/, runs/, design/, preference-labeling/
  task6/                       ← TASK6-STATE.md + fa-ga/, runs/, design/, preference-labeling/
  task7/                       ← TASK7-STATE.md only (artifacts in platform/task7/current/)
  task8/                       ← TASK8-STATE.md + design/KM08-PLAN.md + fa-ga/, runs/
```

---

## platform/task8/current/ — KM08 v4 (READY TO UPLOAD)

```
prompt-task8-v4.txt                             ← one-sentence HD5 pain/sleep addendum prompt
neuropathic_pain_sleep_addendum_draft_05222026.docx  ← Mode A clone, byte-verified
golden-KM08-v4.docx                            ← Mode A clone, byte-verified
grader-guidelines-task8-v4.txt                 ← Sang five-block
RUN-INSTRUCTIONS-v4.md                         ← workflow type at top, pilot read guide
```

Build script: `tools/build/build-docx-km08-v4.py`
Design doc: `task8/design/KM08-PLAN.md` (single source of truth)

---

## Navigation ladder (read in this order for any new session)

1. `AGENTS.md` — operating instructions and guardrails
2. `WORKSPACE_FILE_MAP.md` — this file; structure + placement rules
3. `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md` — before any task-stage work
4. `worlds/korvin-merrow/task-setup/taskN/TASKN-STATE.md` — for the task you are working
5. `worlds/korvin-merrow/task-setup/platform/taskN/current/` — active uploadable set
6. `docs/grader-guidelines-lessons.md` — before editing any grader
7. `docs/reasoning-discipline.md` — before any one-way-door decision

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

---

## Active task status (6/9/2026)

| Task | Status |
|---|---|
| KM01 | RFD (Ready for Delivery) |
| KM02 | RFD |
| KM03 | RFD (post-Sang, FA/GA + 3 PLs submitted) |
| KM04 | Awaiting final human review |
| KM05 | Post-Sang rerun; FA/GA entered, AutoQC passed; PL pending |
| KM06 | Post-Sang rerun; FA/GA entered, AutoQC passed; PL pending |
| KM07 | Staged locally, not piloted yet |
| KM08 | v4 BUILT + BYTE-VERIFIED → ready to upload (render+visual confirm first) |
