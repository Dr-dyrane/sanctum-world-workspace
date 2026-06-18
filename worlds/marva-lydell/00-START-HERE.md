# Marva Lydell World - Cockpit

Status: pre-brainstorm scaffold, renamed to approved patient-world slug 2026-06-18.

Approved patient-world name: Marva Lydell.

Working product thesis: Cardiorenal respiratory transition readiness.

Candidate source: Candidate 3 from `reference/workflows/next-world-selection-proposal.md`, originally "HF exacerbation, CKD, AFib, COPD/OSA." Post-KM and post-OV audit reframes it as a transition-readiness world, not a generic heart-failure world.

No platform action is authorized from this folder. No world files, task files, goldens, graders, prompts, uploads, trajectories, preference labels, or reviewer actions have started.

## Current Product Thesis

This world tests whether a clinician can determine whether a medically improving cardiopulmonary patient is actually safe to leave the hospital.

The core is not heart-failure treatment. The core is discharge readiness under cardiorenal and respiratory constraints: oxygen qualification, DME delivery, exertional hypoxemia, anticoagulation safety, renal recovery, diuretic handoff, conflicting specialty notes, and payer or post-acute pressure.

## Read-In Receipt

Files read before this scaffold:

- `AGENTS.md`
- `WORKSPACE_FILE_MAP.md`
- `DO-NOT-REPEAT.md`
- `docs/world-factory-playbook.md`
- `docs/world-pipeline-playbook.md`
- `docs/task-structure-dossier.md`
- `docs/task-difficulty-lessons.md`
- `reference/templates/README.md`
- `reference/templates/WorldSpec_Quill.docx.md`
- `reference/world-spec-examples/World_Spec_Document_Harold.docx`
- `reference/world-spec-examples/World_Spec_Document_Marcus.docx`
- `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`
- `worlds/ondina-vasquell/docs/WORLD-STATUS.md`
- `worlds/ondina-vasquell/docs/FLOOR-MECHANISM-LIBRARY.md`
- `worlds/ondina-vasquell/docs/CANDIDATE-QUEUE.md`
- `worlds/ondina-vasquell/docs/TASK-IDEA-AUDIT-2026-06-17.md`
- `worlds/ondina-vasquell/submission/Ondina_Vasquell_World_Spec_Claude_Transcript.md`
- `worlds/ondina-vasquell/docs/build-notes/phase-3-build-plan.md`
- `worlds/ondina-vasquell/docs/build-notes/PHASE-3-FILE-MANIFEST.md`
- `worlds/ondina-vasquell/cleanup-2026-06-18/CLEAN-HOUSE-SUMMARY.md`
- Local git history for `worlds/ondina-vasquell`.

No-repeat receipt:

1. Choose 5 or more task structures before building any patient chart. Completion is capped at 1 to 2 tasks.
2. Do not floor on a same-author false draft claim unless the draft uses true placeholders or the prompt explicitly asks for correction.
3. A planned trap is not a trap. It becomes a task only after source geometry makes the wrong move forced, fair, quiet, and chart-contradicted.

## Working Decisions

- Candidate 3 is selected for World 3 planning.
- Patient demographic direction: Black older adult woman. Use as documented demographic context, not as a trap or substitute for chart facts.
- Repo folder renamed to approved patient slug: `worlds/marva-lydell/`.
- The build starts with task architecture and source geometry, not a narrative patient dump.
- Oxygen and DME readiness are the first-priority trap family because KM and OV have not spent them as the central floor.
- CPAP adherence, generic held-med restart, generic diuresis, vitals, pure CDI, and pure coding are not primary levers. They are warm or already spent.
- Every proposed task must name its forced slot, source route, fairness route, and reachability plan before it enters the brainstorm.
- World 3 should reuse the OV bootstrap conveyor: skeleton cockpit, Brainstorm, Phase A substrate ratification, Phase B task architecture and file plan, Phase C deterministic file build, then pilots. Do not start from narrative chart drafting.

## Active Files

- `docs/WORLD-STATUS.md` - running status and activity log.
- `docs/REFERENCE-AUDIT.md` - what the example worlds and local source docs changed in our understanding.
- `docs/PLANNING-CANVAS.md` - World 3 task-first canvas.
- `docs/BRAINSTORM-BUILD-LIVE-AUDIT.md` - living resume doc for Brainstorm, transcript, checklist, and leak-control work.
- `docs/NAME-SHORTLIST.md` - deterministic name shortlist for approval.
- `docs/BRAINSTORM-DRAFT.md` - draft Brainstorm content, not a submission artifact.
- `submission/Marva_Lydell_Brainstorm_DRAFT.md` - Brainstorm bootstrap copy, not a DOCX and not upload-ready.
- `build/` - canonical OV-style factory installed by `tools/build/bootstrap_world_factory.py --adopt-existing`; placeholders block any build.

## Forbidden Until Explicit Authorization

- No patient-specific clinical values are final.
- No DOCX build.
- No image generation.
- No world file generation.
- No task prompt, golden, or grader drafting.
- No Mercor Studio action.
- No trajectory run.
- No external upload.

## Current Factory State

The local factory is installed. `build/clinical_data.py` and `build/task_data.py` are placeholder-only and must remain that way until Alexander approves the name, source geometry, and Phase A substrate.

Do not run `build/build_all.py` yet. It is intentionally not runnable until the approved substrate and task plans exist.

## Next Eligible Step

Alexander approves or edits:

1. Task architecture in `docs/PLANNING-CANVAS.md`.
2. Live audit findings in `docs/BRAINSTORM-BUILD-LIVE-AUDIT.md`.
3. Brainstorm direction in `docs/BRAINSTORM-DRAFT.md`.
4. Bootstrap Brainstorm copy in `submission/Marva_Lydell_Brainstorm_DRAFT.md`.

After that, build the Brainstorm submission artifact only with explicit authorization.
