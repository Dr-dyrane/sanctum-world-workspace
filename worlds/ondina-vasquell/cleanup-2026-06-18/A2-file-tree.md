# A2 - KM vs OV file-tree reconciliation + canonical pattern

Date: 2026-06-18. READ-ONLY audit. No files were moved, edited, or deleted. The only write is this report.

Scope: reconcile the directory structure of the two clinical-eval worlds so the project can lock one canonical pattern for both worlds and the next world.

- KM root: `worlds/korvin-merrow/`
- OV root: `worlds/ondina-vasquell/`

Bottom line up front. The two worlds use two different organizing principles. OV groups by **lifecycle phase** (`phase-3-build-task-artifacts/`, `phase-4-pilot-review-submit/`) with the Studio upload packet co-located per task at `platform/taskN/current/`. KM groups by **pipeline stage**, spraying ~20 sibling stage folders across the world root, splitting the per-task design work (`task-setup/taskN/`) from the per-task Studio packet (`task-setup/platform/taskN/current/`). OV is the cleaner of the two for a cold start. The recommended canonical pattern is OV's phase model with two refinements borrowed from KM (an explicit per-task design folder, and a single docs home).

---

## 1. Side-by-side: where each artifact type lives

| Artifact type | Korvin-Merrow (KM) | Ondina-Vasquell (OV) |
|---|---|---|
| World narrative / cockpit | `00-MASTER-NARRATIVE.md`, `README.md` (root) | `00-START-HERE.md` (root cockpit) |
| World status / running record | (folded into reviews + narrative) | `OV-WORLD-STATUS.md` (root) |
| Design source of truth | `active/clinical-logic.md`, `active/brainstorm.md`, `active/task-map.md` | `OV-FLOOR-MECHANISM-LIBRARY.md`, `WORKFLOW-MAP.md`, `OV-APPROACH-MEMO.md`, `OV-CANDIDATE-QUEUE.md`, `OV-FRESH-TASK-IDEAS.md`, `OV-TASK-IDEA-AUDIT-2026-06-17.md`, `EMR-TEMPLATE-FIDELITY-DIAGNOSIS.md` (all loose at root) |
| World files (shared chart) | `synthetic-files/locked/batch-1..5/`, plus `supplementary-files/locked/`, `task-context-files/locked/` | `phase-3-build-task-artifacts/world-files/` (34 docx/jpg, flat) |
| Supplementary files | `supplementary-files/locked/` (top-level dir) | `phase-3-build-task-artifacts/supplementary-files/` |
| Synthetic / image files | `synthetic-files/locked/batch-*` | `phase-3-build-task-artifacts/synthetic-files/` |
| Task deliverables (the "started_" drafts / task-level docx) | inside `task-setup/platform/taskN/current/` | inside `phase-3-build-task-artifacts/platform/taskN/current/`; loose build outputs also staged in `phase-3-build-task-artifacts/task-files/` |
| Goldens | `goldens/locked/Golden-KMNN.md` (top-level dir, markdown) AND `golden-response-taskN-vX.docx` inside each `platform/taskN/current/` | `phase-3-build-task-artifacts/goldens/` is an **empty `.gitkeep` stub**; the real goldens are docx inside each `platform/taskN/current/golden-OVNN.docx`. Goldens rendered via `build/build_goldens.py` |
| Graders | `task-setup/platform/taskN/current/grader-guidelines-taskN-vX.txt` (versioned in-packet) | `phase-3-build-task-artifacts/grader-guidance/` is an **empty `.gitkeep` stub**; real graders are `platform/taskN/current/grader-guidelines-OVNN.txt` |
| Prompts | `task-prompts/locked/TP-KMNN.md` (design markdown) AND `prompt-taskN-vX.txt` inside each `platform/taskN/current/` | `phase-3-build-task-artifacts/task-prompts/` is an **empty `.gitkeep` stub**; real prompts are `platform/taskN/current/prompt-OVNN.txt` |
| Preregistration | (not a distinct artifact; folded into runs/design) | `platform/taskN/current/OVNN-...-preregistration.md` (co-located in packet) |
| Run-instructions | (no standalone equivalent; closeout in `task-setup/taskN/handoff/`) | `platform/taskN/current/RUN-INSTRUCTIONS.md` (per task, the canonical Studio upload recipe) |
| FA/GA | `task-setup/taskN/fa-ga/FA-GA-*.md` (per-task design side) | `phase-4-pilot-review-submit/fa-ga/` |
| Preference labeling | `task-setup/taskN/preference-labeling/` | `phase-4-pilot-review-submit/preference-labeling/OVNN-PLx-A-vs-B.md` |
| Results / pilot logs | `task-setup/taskN/runs/` (e.g. `clean-pilot/`, `escalation-v2/`) | `phase-4-pilot-review-submit/results/OVNN-...-job-XXXX.md` (flat, job-id named) |
| Trajectories / recordings | `task-setup/taskN/trajectories/v1`, `v2`, `low-runs/` | `phase-4-pilot-review-submit/recordings/` |
| Status / planning / design docs | `planning/`, `active/`, `world-spec-prep/`, `reviews/`, `reference-file-design/` | loose at root (the OV-*.md set) + `phase-4-...` planning md (`OV-PATH-TO-8-...`, `OV-image-miss-lever-design-...`) |
| Reviewer sendbacks | `reviews/` (reviewer-go, reviewer-feedback, audits) | `reviews/2026-06-15-kathy-g-OV02-sendback.md` |
| Submission / spec provenance | `submission/Korvin_Merrow_Brainstorm.docx`; provenance folded into pipeline-history | `submission/` (World Spec, Brainstorm, transcripts, `STUDIO-PROVENANCE.md`) |
| Archive / history | `_pipeline-history/` (~25 stage subfolders, each with `locked/` + `ratifications/`) | `archive/2026-06-15-cleanup/` (phase-4-history, planning-history, root-history) |
| Build scripts | (none in-repo for KM; KM docx came through a different pipeline) | `phase-3-build-task-artifacts/build/` (`build_world_files.py`, `build_task_files.py`, `build_goldens.py`, `epic.py`, `clinical_data.py`, `task_data.py`, `build_ovNN.py`, `render_ov09_image.py`, `README.md`) |
| Stage-9 / file-review (RLS upload prep) | `file-review/` (pipeline-output, revision, upload, holdback, protocol, logs) | `file-review/` (STAGE-9-REVISION-RECORD.md, revision/filesystem/ = the 34-file chart, zips) |
| Per-pipeline-stage scaffolds | `file-inventory/`, `world-spec-prep/`, `final-submission-resolution/`, `goldens/`, etc., each `locked/`+`ratifications/` | (not used; OV collapsed these into phase folders) |

Key structural facts confirmed by inspection:
- OV's Studio upload packet is **`phase-3-build-task-artifacts/platform/taskN/current/`** and it is self-contained: prompt, golden (docx), grader (txt), the task-level deliverable docx, the preregistration, and RUN-INSTRUCTIONS all sit together. This matches what `STUDIO-PROVENANCE.md` and each `RUN-INSTRUCTIONS.md` describe as the upload set.
- OV's top-level `goldens/`, `grader-guidance/`, `task-prompts/`, `task-context-files/` under `phase-3-build-task-artifacts/` are **empty placeholders (`.gitkeep` only)**. The live artifacts of those types live inside the per-task `current/` packets. These four stubs are dead scaffolding inherited from the KM-style layout.
- KM keeps two parallel per-task trees: `task-setup/platform/taskN/` (the Studio packet, `current/` + `archive/`) and `task-setup/taskN/` (the design side: `design/`, `fa-ga/`, `preference-labeling/`, `runs/`, `trajectories/`, `qa/`, `learnings/`, `handoff/`). OV split these by phase instead: build packet in phase-3, all pilot/FA/GA/PL/results in phase-4.
- OV builds every docx in-repo through `build/` (canonical rule in `build/README.md`: never a bare `Document()`). KM has no build scripts in the tree.

---

## 2. Concrete inconsistencies between the two trees

1. **Top-level organizing principle differs.** KM = pipeline-stage folders at the world root (~20 siblings: `goldens/`, `task-prompts/`, `supplementary-files/`, `task-context-files/`, `synthetic-files/`, `file-inventory/`, `world-spec-prep/`, `final-submission-resolution/`, `reference-file-design/`, `task-setup/`, `file-review/`, `planning/`, `active/`, `reviews/`, `submission/`, `_pipeline-history/`). OV = phase folders (`phase-3-build-task-artifacts/`, `phase-4-pilot-review-submit/`) plus a few siblings (`file-review/`, `reviews/`, `submission/`, `archive/`).

2. **Studio packet lives at a different path.** KM: `task-setup/platform/taskN/current/`. OV: `phase-3-build-task-artifacts/platform/taskN/current/`. Same `current/` + `archive/` convention inside, different parent.

3. **Goldens, prompts, graders, context-files have a different home.** KM materializes them BOTH as top-level design markdown (`goldens/locked/Golden-KMNN.md`, `task-prompts/locked/TP-KMNN.md`, `task-context-files/locked/...`) AND as in-packet files. OV has only the in-packet files; the matching top-level dirs are empty `.gitkeep` stubs.

4. **Naming conventions for the same file type diverge.** Goldens: KM `Golden-KM01.md` / `golden-response-task1-v6.docx` vs OV `golden-OV01-v1.docx`. Prompts: KM `TP-KM01.md` / `prompt-task1-v5.txt` vs OV `prompt-OV01.txt`. Graders: KM `grader-guidelines-task1-v10.txt` vs OV `grader-guidelines-OV01.txt`. KM versions in the filename (`-v10`); OV mostly drops the version suffix on the current file and keeps versions in `archive/`.

5. **Design-vs-pilot artifacts are split differently.** KM co-locates all per-task design + pilot work under one `task-setup/taskN/` tree (fa-ga, preference-labeling, runs, trajectories, qa, learnings, design, handoff). OV scatters by phase: deliverable/prereg/RUN-INSTRUCTIONS in phase-3 packet, but FA/GA + preference-labeling + results + recordings in `phase-4-pilot-review-submit/`. So for one OV task, design lives in two top-level trees.

6. **Results/logs naming.** KM groups runs into named subfolders per task (`runs/clean-pilot/`, `runs/escalation-v2/`). OV uses a single flat `phase-4-.../results/` directory with job-id-stamped filenames (`OV03-pilot-2026-06-16-job-cb628a70.md`). OV's is flatter and easier to scan; KM's is nested per task.

7. **Retired/paused task handling.** OV has dedicated `platform/_retired/` and `platform/_paused/` sibling dirs (dated, descriptive) at the same level as `taskN/`. KM keeps retired versions inside each task's own `archive/` (e.g. `task6/archive/2026-06-08-orthostatic-v1-tooeasy/`). OV's `_retired`/`_paused` is clearer for whole-task retirement; KM's per-task `archive/` is clearer for version retirement. They are not mutually exclusive.

8. **Build scripts exist only in OV.** `phase-3-build-task-artifacts/build/` is OV-only. KM has no in-repo build pipeline.

9. **Archive shape differs.** KM uses `_pipeline-history/<stage>/{locked,ratifications}` (per-stage, ratification-driven). OV uses one dated `archive/2026-06-15-cleanup/{phase-4-history,planning-history,root-history}` snapshot folder. OV's is a single cleanup epoch; KM's is a continuous stage ledger.

10. **Status / planning docs placement.** KM puts these in named folders (`active/`, `planning/`, `reviews/`, `world-spec-prep/`). OV leaves the design/status/idea docs loose at the world root (eight OV-*.md / 00-*.md / EMR-*.md files), plus two planning md stranded inside `phase-4-pilot-review-submit/`. OV's root is noisier; KM's is tidier at the root but heavier overall.

11. **Cockpit/entry-point filename differs.** KM `00-MASTER-NARRATIVE.md` + `README.md`; OV `00-START-HERE.md`. Both serve as the "read first" file but are named differently.

12. **The 34-file chart is duplicated in OV** (intentionally, for Stage-9 upload): `phase-3-build-task-artifacts/world-files/` (the build outputs) and `file-review/revision/filesystem/` (the RLS upload snapshot, 34 files). KM keeps the analogous split as `synthetic-files/locked/batch-*` vs `file-review/.../filesystem/`.

---

## 3. Proposed single canonical tree pattern

The canonical pattern is OV's phase model, cleaned up. Rationale per choice favors least-surprise for a cold start: a reader should be able to open the world root and know, without tribal knowledge, where the Studio upload packet is, where the design lives, where pilots landed, and what is frozen.

```
worlds/<name>/
  README.md                         # cockpit: status, lanes, what-to-test-next, gates. Single entry point.
  docs/                             # ALL world-level design + status + planning + ideas (no loose md at root)
    WORLD-STATUS.md                 #   running record (the canonical state log)
    FLOOR-MECHANISM-LIBRARY.md      #   design source of truth
    WORKFLOW-MAP.md
    CANDIDATE-QUEUE.md
    <other design / approach / audit md>
  build/                            # in-repo docx pipeline (clinical_data.py, epic.py, build_*.py, README.md)
  world-files/                      # shared chart the model reads (frozen after world gen)
  supplementary-files/              #   (optional split; or fold into world-files/)
  synthetic-files/                  #   images / non-Epic assets
  tasks/
    taskN/
      current/                      # THE Studio upload packet (frozen once shipped):
                                    #   prompt-<TASK>.txt, golden-<TASK>.docx,
                                    #   grader-guidelines-<TASK>.txt, <deliverable>.docx,
                                    #   <TASK>-pilot-preregistration.md, RUN-INSTRUCTIONS.md
      archive/                      # dated retired versions of THIS task's packet
      design/                       # per-task design notes, grounding, bench
      pilot/                        # per-task pilot results, FA/GA, preference-labeling, trajectories
    _retired/<dated-task>/          # whole tasks retired from the suite
    _paused/<dated-task>/
  file-review/                      # Stage-9 RLS upload prep (revision/, logs, the upload snapshot)
  submission/                       # World Spec, Brainstorm, transcripts, STUDIO-PROVENANCE.md
  archive/<dated-cleanup>/          # frozen history snapshots
```

Justification, top level by top level:
- **`README.md` as the only cockpit.** Both worlds already have a "read first" file; standardize the name to `README.md` (KM `00-MASTER-NARRATIVE` and OV `00-START-HERE` both map to this). One entry point, conventional name, no guessing.
- **`docs/` for all world-level design/status/planning.** OV's biggest cold-start cost is eight design md loose at the world root. A single `docs/` folder collects them, and the cockpit links into it. KM already proves named design folders work (`active/`, `planning/`); `docs/` is the least-surprising name.
- **`build/` at world root.** OV's build pipeline is a real asset and the canonical rule (never a bare `Document()`) depends on it being findable. Keep it top-level and adopt it for the next world.
- **`world-files/` + `supplementary-files/` + `synthetic-files/` at root.** Flat, obvious, matches OV today and what `STUDIO-PROVENANCE.md` calls the shared chart. Drop the empty `goldens/`/`grader-guidance/`/`task-prompts/`/`task-context-files/` stubs entirely; those artifact types live in the task packet, not at world root.
- **`tasks/taskN/` (rename from `phase-3-build-task-artifacts/platform/taskN/`).** The phase-3/phase-4 prefix and the `platform/` layer add depth without adding meaning at cold start. `tasks/taskN/` is shorter and self-explanatory. Inside it:
  - **`current/` = the frozen Studio packet** (unchanged from both worlds; this is the one path Studio uploads from, keep it stable).
  - **`archive/` = retired versions of this task** (KM convention, better than nothing).
  - **`design/` and `pilot/` = the per-task design and pilot work** that OV currently strands in `phase-4-pilot-review-submit/`. Co-locating design and pilot under the task they belong to is KM's one clear win; pulling FA/GA, preference-labeling, results, and recordings back next to the task removes the "one task, two top-level trees" problem.
- **`tasks/_retired/` and `tasks/_paused/`.** Adopt OV's whole-task retirement dirs; clearer than burying a dead task inside a live task's `archive/`.
- **`file-review/`, `submission/`, `archive/` at root.** Both worlds already converge here; keep as-is.

Net effect: a cold reader opens `README.md`, finds design in `docs/`, the upload packet in `tasks/taskN/current/`, and the build pipeline in `build/`. Nothing is stranded loose at the root, and no empty placeholder dirs mislead.

---

## 4. OV path classification: MUST-NOT-MOVE vs SAFE-TO-REORG

This section is advisory only. **No moves were executed.** All paths are relative to `worlds/ondina-vasquell/`.

### 4a. MUST-NOT-MOVE (Studio-referenced or frozen)

These are the live Studio upload packets, the frozen world chart, the RLS upload snapshot, and two design docs that packets reference by name. Moving any of these breaks a Studio upload path or a documented cross-reference.

- `phase-3-build-task-artifacts/platform/task*/current/` - **all 10 live task packets.** Each is the exact set Studio uploads (prompt, golden, grader, deliverable, prereg, RUN-INSTRUCTIONS). RUN-INSTRUCTIONS files name these by filename. Frozen.
- `phase-3-build-task-artifacts/platform/task*/archive/` - retired packet versions referenced from cockpit and RUN-INSTRUCTIONS (e.g. OV05 archive is called out in `00-START-HERE.md`). Leave in place.
- `phase-3-build-task-artifacts/platform/_retired/` and `.../_paused/` - dated retired/paused tasks referenced by cockpit and status. Leave in place.
- `phase-3-build-task-artifacts/world-files/` - the 34-file shared chart. Frozen ("world files are frozen and must not change" - cockpit). MUST-NOT-MOVE.
- `phase-3-build-task-artifacts/supplementary-files/` - part of the shared chart per RUN-INSTRUCTIONS ("world-files/ plus supplementary-files/"). Frozen.
- `phase-3-build-task-artifacts/synthetic-files/` - task/world image assets referenced by packets. Frozen.
- `phase-3-build-task-artifacts/build/` - canonical builder; `build/README.md` and CLAUDE.md require builds to run through it. Moving it would break the documented build path. Treat as fixed.
- `phase-3-build-task-artifacts/task-files/` - build outputs that feed the packets; some are the source of the `current/` deliverables. Leave with build/ until a deliberate consolidation.
- `OV-FLOOR-MECHANISM-LIBRARY.md` (root) - referenced by name in 4 platform/submission files and named in CLAUDE.md as a governing doc. If reorganized into `docs/`, every reference must be updated in the same commit. Do NOT move loosely.
- `WORKFLOW-MAP.md` (root) - referenced by a platform file and by `STUDIO-PROVENANCE.md` ("Workflow remaps in WORKFLOW-MAP.md"). Same caveat: move only with reference updates.
- `submission/STUDIO-PROVENANCE.md` and the World Spec / Brainstorm / transcript docx in `submission/` - Studio lineage record. Leave in place.
- `file-review/revision/filesystem/` (34 files) + `file-review/STAGE-9-REVISION-RECORD.md` + the two zips - the RLS Stage-9 upload snapshot. Leave in place.
- `phase-4-pilot-review-submit/` packets that RUN-INSTRUCTIONS cite by relative path (e.g. `phase-4-pilot-review-submit/OV01-results-and-prereg-reconciliation.md`, and the `OV02-pathA-pilot-preregistration.md` reference). The directory is cross-referenced from live packets, so do not rename the directory or move cited files without updating the citing packet in the same change.

### 4b. SAFE-TO-REORG (loose planning / status / history; not Studio-referenced)

These are world-level design, status, idea, and audit docs with no Studio path dependency and no inbound reference from the frozen packets (verified: 0 references from `platform/`/`submission/` for each). They can be consolidated into a `docs/` folder to de-noise the root. The new `cleanup-2026-06-18/` folder is the natural staging point if you prefer to land them there first.

Proposed `from -> to` (DO NOT EXECUTE; reference updates in the cockpit would be needed because `00-START-HERE.md` links some of these):

```
OV-WORLD-STATUS.md                      -> docs/WORLD-STATUS.md
OV-APPROACH-MEMO.md                     -> docs/APPROACH-MEMO.md
OV-CANDIDATE-QUEUE.md                   -> docs/CANDIDATE-QUEUE.md
OV-FRESH-TASK-IDEAS.md                  -> docs/FRESH-TASK-IDEAS.md
OV-TASK-IDEA-AUDIT-2026-06-17.md        -> docs/TASK-IDEA-AUDIT-2026-06-17.md
EMR-TEMPLATE-FIDELITY-DIAGNOSIS.md      -> docs/EMR-TEMPLATE-FIDELITY-DIAGNOSIS.md
```

Two design/planning md currently stranded inside the phase-4 tree are also safe to relocate into `docs/` (they are notes, not pilot results, and are not cited by packets):

```
phase-4-pilot-review-submit/OV-PATH-TO-8-km-ported-2026-06-15.md        -> docs/history/OV-PATH-TO-8-km-ported-2026-06-15.md
phase-4-pilot-review-submit/OV-image-miss-lever-design-2026-06-15.md    -> docs/history/OV-image-miss-lever-design-2026-06-15.md
```

Empty placeholder dirs that are safe to delete outright (they hold only `.gitkeep`, the live artifacts of these types are in the task packets):

```
phase-3-build-task-artifacts/goldens/.gitkeep            (delete dir)
phase-3-build-task-artifacts/grader-guidance/.gitkeep    (delete dir)
phase-3-build-task-artifacts/task-prompts/.gitkeep       (delete dir)
phase-3-build-task-artifacts/task-context-files/.gitkeep (delete dir)
```

Held back from the move list on purpose:
- `OV-FLOOR-MECHANISM-LIBRARY.md` and `WORKFLOW-MAP.md` - listed under MUST-NOT-MOVE because packets reference them by name. They belong in `docs/` under the canonical pattern, but only via a deliberate move that updates all references in the same commit, not as a loose reorg.
- `00-START-HERE.md` - the cockpit. Rename to `README.md` only as a deliberate, reference-aware change.
- Anything under `phase-4-pilot-review-submit/fa-ga|preference-labeling|results|recordings/` - these are the real pilot artifacts. Under the canonical pattern they move to `tasks/taskN/pilot/`, but that is a phase-2 structural migration, not a safe loose move, because RUN-INSTRUCTIONS cite the directory.

---

## Appendix - raw structure reference

KM top-level dirs: `_pipeline-history/`, `active/`, `file-inventory/`, `file-review/`, `final-submission-resolution/`, `goldens/`, `planning/`, `reference-file-design/`, `reviews/`, `submission/`, `supplementary-files/`, `synthetic-files/`, `task-context-files/`, `task-prompts/`, `task-setup/`, `world-spec-prep/`. Root files: `00-MASTER-NARRATIVE.md`, `README.md`.

OV top-level dirs: `archive/`, `file-review/`, `phase-3-build-task-artifacts/`, `phase-4-pilot-review-submit/`, `reviews/`, `submission/`. Root files: `00-START-HERE.md`, `EMR-TEMPLATE-FIDELITY-DIAGNOSIS.md`, `OV-APPROACH-MEMO.md`, `OV-CANDIDATE-QUEUE.md`, `OV-FLOOR-MECHANISM-LIBRARY.md`, `OV-FRESH-TASK-IDEAS.md`, `OV-TASK-IDEA-AUDIT-2026-06-17.md`, `OV-WORLD-STATUS.md`, `WORKFLOW-MAP.md`.

OV Studio upload packet (canonical example, `platform/task1/current/`): `prompt-OV01.txt`, `golden-OV01-v1.docx`, `grader-guidelines-OV01.txt`, `discharge_medication_orders_05212026.docx` (deliverable), `OV01-v2-pilot-preregistration.md`, `OV01-A0.5-fairness-check.md`, `RUN-INSTRUCTIONS.md`.
