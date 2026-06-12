# Workspace File Map
**Last updated: 2026-06-12 (KM07 ready for delivery after v4 true-placeholder pilot, FA/GA, and three PLs; KM08 v7 piloted in job 062652b2 with all-floor photo-miss pattern and FA/GA active from Attempt 1; KM09 v2 piloted cleanly in job 8ca908b5 with FA/GA active from Attempt 6; King P legitimate-failure-over-score guidance added and numeric score gates demoted; Raising Task Difficulty worked example added to sources and doctrine; KM10 v3 corrected GA after AO second review; A0.4/A0.5 draft-fairness gates and Abi review protocol added; macOS tooling/render notes added; internal medicine next-world planning canvas added; new-world 30 world-level file minimum indexed; next-world diabetic foot selection packet and hour prep packet indexed; Ondina Vasquell Brainstorm v1.1 indexed)**

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
  docs/                        ← lessons, playbooks, domain knowledge, tooling and DOCX render doctrine
  reference/                   ← Sanctum source docs, templates, guidelines
                                 reference/source/Raising_Task_Difficulty_Worked_Example.pdf is the
                                 difficulty-hardening worked example: remove answer-key world files,
                                 force reconciliation, add task-level format/noise, and use realistic
                                 off-text critical findings when clinically appropriate.
                                 reference/templates/ now holds the client's latest-guidance worked
                                 example (Quill CDI world+task: Brainstorm, WorldSpec, Task prompt,
                                 Golden Response, Grader Guidelines, FA_GA, Preferential Labeling) +
                                 README.md explaining it and its deltas vs KM conventions
                                 reference/workflows/internal-medicine-world-planning-canvas.md is the
                                 pre-brainstorm playground for the next internal medicine world: task
                                 surfaces, traps, source geometry, fairness routes, grader modes, and
                                 reachability before any build.
                                 reference/workflows/next-world-selection-proposal.md records the ten
                                 candidate internal medicine worlds and selection criteria.
                                 reference/workflows/next-world-candidate-scorecard.md scores those
                                 candidates and ratifies diabetic foot infection with limb threat as
                                 the primary planning candidate.
                                 reference/workflows/next-world-diabetic-foot-planning-canvas.md is
                                 the filled no-build cockpit for Candidate 1.
                                 reference/workflows/next-world-dfi-hour-prep-packet.md is the
                                 one-hour no-build preparation packet for Candidate 1: live-guidance
                                 gate (closed for Brainstorm scope 6/12 PM), workflow options, canvas
                                 gap audit, Phase 1 worksheets, decision pack, and verification log.
                                 reference/workflows/next-world-dfi-hour-prep-packet-review-2026-06-12.md
                                 is the independent handoff review (PASS, two non-blocking findings).
                                 reference/workflows/live-guidance-delta-memo-2026-06-12.md records the
                                 live (06/09) doc + live sheet verification: strings/priorities/claims
                                 unchanged for Brainstorm scope; 30-file minimum now in-doc; cutoff
                                 July 31 2025; residual open items for Phase 2+.
                                 reference/workflows/next-world-dfi-decision-record-2026-06-12.md holds
                                 Alexander's five Brainstorm-blocking decisions verbatim (identity,
                                 Pattern C snapshot, Option A workflows, SNF-denial payer axis,
                                 equivocal osteomyelitis).
                                 reference/workflows/next-world-dfi-brainstorm-draft-v1.1.md is the
                                 current four-element Brainstorm draft built from that record; it closes
                                 the patient-name, document-date, exact-snapshot, requester, task-anchor,
                                 and task-level-trap gates; markdown only, no DOCX or submission yet.
                                 reference/workflows/next-world-dfi-brainstorm-draft-v1.md is superseded
                                 local history.
  tools/                       ← all Python scripts (canonical home)
  worlds/
    korvin-merrow/             ← World #1 (delivered KM01-07; KM08-10 in review)
    ondina-vasquell/           ← World #2 (authorized 6/12 late): skeleton evolved to live
                                 cockpit. 00-START-HERE.md = world cockpit with decisions
                                 8-10 build doctrine (transcript from git hx; Custom Made
                                 origin + Mode A HIM/EMR; Codex imagegen delegation).
                                 phase-1 worksheets FILLED from the hour packet (1a slate,
                                 1c pairings + fairness gates, 1d forecasts). phase-2 holds
                                 2b-spec-prep-checklist.md (KM reviewer-correction
                                 inheritance: comorbidity expansion + med specificity
                                 OPEN FOR ALEXANDER) and 2c-autoqc-25-defense-notes.md
                                 (osteo, perfusion-conflict, borderline-stay defenses,
                                 drafted same-day per the KM lesson).
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
    build-docx-km07-draft-fairfix.py
    build-docx-km08-v7.py
    build-docx-km09-v2.py
    build-docx-km10-v3.py
  verify/                      ← substrate verification scripts
    verify-km08-substrate.py
    verify-km08-pain.py
  archive/                     ← dead/superseded scripts (reference only, never execute)
    build-docx-km05.py
    build-docx-km06-v1..v4.py
    build-docx-km07-v1.py
    build-docx-km08-physician-v2.py
    build-docx-km08-status-v3.py
    build-docx-km08-v6.py
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
    task7/current/             ← KM07 v4: nephrology referral letter, true placeholder; Ready for Delivery after db57dc63, FA/GA, and three PLs
    task8/current/             ← KM08 v7 discharge-day SOAP addendum plus night-float signout plus bedside photo; piloted job 062652b2, FA/GA active
    task9/current/             ← KM09 v2: coding attestation addendum plus HIM preliminary coding summary; piloted job 8ca908b5, FA/GA active
    task10/current/            ← KM10 v3: CDI query response with balanced query surface; pilot 62fc109e all-floor with no catcher
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
  task7/                       ← TASK7-STATE.md + design/ (v2-PLAN, v3-placeholder-plan, v4 true-placeholder
                                 plan), runs/ (v2 + v3 retired evidence), fa-ga/, preference-labeling/,
                                 qa/ (Abi-mode byte review),
                                 learnings/ (KM07-learnings.md: fairness, chart-aware grader, built-artifact gate)
  task8/                       ← TASK8-STATE.md + design/KM08-PLAN.md + fa-ga/, runs/
  task9/                       ← TASK9-STATE.md + design/ (KM09-PLAN, bite-risk-assessment), qa/ (v2 Abi-mode review), fa-ga/, runs/
  task10/                      ← TASK10-STATE.md + design/KM10-PLAN.md, design/KM10-v3-balanced-query-plan.md + fa-ga/, runs/
```

---

## platform/task8/current/ - KM08 v7 off-text bedside-photo SOAP addendum (ready locally; upload/pilot not authorized)

```
prompt-task8-v7.txt                             ← discharge-day SOAP placeholder prompt, 5/24
discharge_day_soap_addendum_started_05242026.docx  ← attending draft; true placeholder, no gabapentin decision or wound interpretation
night_float_pain_sleep_signout_05242026.docx   ← external signout suggests gabapentin TID, fair handoff temptation
bedside_photo_05242026.png                      ← nursing bedside photo; off-text diabetic foot wound signal
golden-KM08-v7.docx                            ← Mode A clone, declines signout escalation and addresses photo wound
grader-guidelines-task8-v7.txt                 ← chart-aware and photo-aware; include_input_files=true required
RUN-INSTRUCTIONS-v7.md                         ← workflow = Progress Note Daily Rounding Documentation
```

Prior v5 and v6 sets archived at `platform/task8/archive/2026-06-12-v5-placeholder-allcatch/` and `platform/task8/archive/2026-06-12-v6-signout-allcatch/`.
Design doc: `task8/design/KM08-PLAN.md` (single source of truth; v7 fair off-text bedside-photo route and gates 0-3)
KM07 v4 build script: `tools/build/build-docx-km07-draft-fairfix.py` (genre-true PCP base; alendronate absent from draft)
Pilot preregistrations: `task7/runs/KM07-v2-pilot-preregistration.md`, `task8/runs/KM08-v7-pilot-preregistration.md` (locked pre-pilot, never edited after)

---

## platform/task9/current/ - KM09 v2 coding attestation addendum (piloted 8ca908b5; FA/GA active)

```
prompt-task9-v2.txt                             ← addendum prompt, asks for final code set, principal sequencing, rationales, DRG family
him_preliminary_inpatient_coding_summary_05252026.docx  ← task-level HIM worksheet to addend; external preliminary coding surface
golden-KM09-v2.docx                             ← Mode A signed physician coding attestation addendum
grader-guidelines-task9-v2.txt                  ← chart-aware; include_input_files=true required
RUN-INSTRUCTIONS-v2.md                          ← Studio upload and first-trajectory mount gates
```

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
9. `reference/workflows/internal-medicine-world-planning-canvas.md` - before drafting a new internal medicine Brainstorm; this is the task/trap/source/fairness playground and no-build gate
10. `reference/workflows/next-world-selection-proposal.md`, `reference/workflows/next-world-candidate-scorecard.md`, `reference/workflows/next-world-diabetic-foot-planning-canvas.md`, and `reference/workflows/next-world-dfi-hour-prep-packet.md` - current next-world planning packet; planning only, no build authority
11. `reference/checklists/world-spec-checklist.md` - before drafting a new World Spec; includes the 06/10 minimum of 30 world-level files for new worlds
12. `docs/task-difficulty-lessons.md` - before designing any task mechanism (the cold/forced/contradicted difficulty rule AND the fairness doctrine in sections 5-6: never floor a planted claim with no correction instruction). Companion: `docs/abi-review-protocol.md` (Abi mode: the nine lenses + the A0.5 built-artifact fairness gate; run before declaring any completion task staged)
13. `docs/clinical-voice-lessons.md` - before authoring any world file, golden, or reference template (the World #1 pipeline voice standard)
14. `reference/templates/README.md` - the client's latest-guidance worked example (CDI world+task) and its deltas vs KM conventions
15. `docs/git-workflow.md` - before any git work (the sandbox delete-grant lesson: git is blocked until `mcp__cowork__allow_cowork_file_delete` is approved, then full git works)
16. `docs/tooling-verification.md` + `docs/tooling-audit.md` + `docs/docx-generation-method.md` - before diagnosing DOCX render/tool failures, especially on macOS where bundled LibreOffice can be dependency-blocked

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

## Active task status (6/12/2026)

Live status lives in `dashboard/km-world-dashboard.html`, `task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, and each `taskN/TASKN-STATE.md`; this table is a convenience snapshot - trust those if they disagree.

| Task | Status |
|---|---|
| KM01 | Delivered |
| KM02 | Delivered |
| KM03 | Delivered |
| KM04 | Delivered |
| KM05 | Delivered |
| KM06 | Delivered |
| KM07 | Ready for Delivery as of 2026-06-12 per Alexander. v4 true-placeholder pilot job `db57dc63` produced spread 55,60,78,55,55,62,45,85,55,40. Trajectory Quality passed on rescore after an initial severity-calibration false alarm; Taiga QA and Feedback AutoQC passed. FA/GA used Attempt 10, score 0.40. Three PL backups drafted with recommendations A+, A+, plain B. Records: `task7/qa/KM07-v4-trajectory-quality-qcaud-3bd4de.md`, `task7/fa-ga/FA-GA-current.md`, `task7/preference-labeling/`. |
| KM08 | v7 piloted in job `062652b2`: 15,15,30,20,20,20,15,30,30,20, mean 22.0. The agent and grader both saw the PNG; Attempt 1 safely declined gabapentin escalation but falsely documented no wound on a visible plantar lesion. FA/GA active from Attempt 1 at `task8/fa-ga/FA-GA-current.md`. Because v7 was all-floor, keep the golden/catcher reachability watch before final banking if the platform allows. |
| KM09 | AO first review returned v1 on 6/12 because the task asked for a coding addendum without mounting an original coding document. v2 fixed that by adding one external HIM preliminary inpatient coding summary as the task-level attachment. Job `8ca908b5` piloted cleanly at 20, 20, 15, 15, 92, 15, 20, 15, 85, 25, with first trajectory showing the HIM file once under `/docs/filesystem` and no task-specific `.apps_data` copy. FA/GA is active from Attempt 6, score 0.15; prior v1.1 job `df5ba05c` is retired difficulty evidence only. |
| KM10 | v3 balanced CDI query surface piloted in job `62fc109e`: 30,25,15,20,25,24,20,20,30,20, mean 22.9, no catcher. Selected low run Attempt 3 / `aee6c24e` adds toxic-metabolic encephalopathy despite the balanced unsupported and unable-to-determine options, while declining malnutrition. Fairness gate passes because this is an external CDI query, not a started draft with planted false information. AO second review said the FA is okay and returned only the GA framing; corrected GA is in `task10/fa-ga/FA-GA-current.md`. First trajectory still showed duplicate query memos under `/docs/filesystem` and `/docs/.apps_data/calendar`, so own the mount caveat if asked. Evidence: `task10/runs/KM10-v3-results-and-prereg-reconciliation.md`. (platform ixr0ddb9, under Abi O.) |

World target: **10 tasks** (Larry 6/10 pod announcement: over 8, preferably 10, before a new world; Alexander decision recorded in `reference/world-spec-guidelines/POD-ANNOUNCEMENT-2026-06-10-delivery-day-and-operating-rules.md`). Submit each task as it clears — no batching (pod rule 3).
