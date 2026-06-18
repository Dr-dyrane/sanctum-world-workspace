# World 3 Reference Audit

Date: 2026-06-18.

Purpose: explain what the example worlds and our KM/OV evidence add before World 3 planning begins.

## Sources Read

- `reference/templates/README.md`
- `reference/templates/WorldSpec_Quill.docx.md`
- `reference/templates/Task prompt.md`
- `reference/templates/Grader Guidelines.md`
- `reference/world-spec-examples/World_Spec_Document_Harold.docx`
- `reference/world-spec-examples/World_Spec_Document_Marcus.docx`
- Marcus task-level prompt, golden, and grader examples.
- Opus patient-safety RCA example.
- `docs/world-factory-playbook.md`
- `docs/task-structure-dossier.md`
- `docs/task-difficulty-lessons.md`
- `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`
- `worlds/ondina-vasquell/docs/WORLD-STATUS.md`
- `worlds/ondina-vasquell/docs/FLOOR-MECHANISM-LIBRARY.md`
- `worlds/ondina-vasquell/submission/Ondina_Vasquell_World_Spec_Claude_Transcript.md`
- `worlds/ondina-vasquell/docs/build-notes/phase-3-build-plan.md`
- `worlds/ondina-vasquell/docs/build-notes/PHASE-3-FILE-MANIFEST.md`
- `worlds/ondina-vasquell/cleanup-2026-06-18/CLEAN-HOUSE-SUMMARY.md`
- Local git history for `worlds/ondina-vasquell`.

## What We Were Missing

The strong example worlds do not start from a clever isolated trap. They start from source geometry.

Harold works because the same patient carries multiple incomplete, conflicting, and outdated source versions. Medication reconciliation is not hard because of rare pharmacology. It is hard because the output forces a per-line decision across discharge orders, family lists, pill bottles, consultant notes, and post-ICU physiology.

Marcus works because every task has a native forced output. The care plan forces problem ownership. Medication reconciliation forces home instructions. Referral letters force distinct urgency and consult questions. Risk stratification forces tiering and HCC judgment. The world is designed around the deliverables, not around a chart that later gets tasks pasted onto it.

Quill works because the spec names the central axis and then makes task files and task anchors do the hard work. It also shows a modern external-document pattern: a compliant CDI task is not a trick question. It asks the model to produce a real deliverable with balanced options and to avoid unsupported queries.

The Opus RCA example works because it separates proximate cause, root cause, contributing factors, and corrective actions. That is a structure-native forced distinction. A flat clinical diagnosis is not enough.

## What KM And OV Add

KM shows the model is strong at clean chart synthesis. It finds buried text, guards against fabrication, holds obvious meds, and handles standard clinical rules. It floors when a quiet forced move sits outside the task's reflex path.

OV shows the same thing in harsher terms. Planned traps often failed because the task surface itself primed the model to inspect the intended trap. OV05 made the bottle photo central to med rec, so it got read. OV09 made disposition the headline of post-acute coordination, so it got corrected. OV06 floored only after the telegraph was removed.

The third world must therefore be designed around these rules:

1. The task surface must not force the model to inspect the trap.
2. The wrong move must sit in a background line or external document, not the task headline.
3. The chart must contradict the wrong move.
4. The output schema must force a decision.
5. A correct answer must be reachable without private knowledge.

## OV Bootstrap Lesson From Git History

The git history changes the operating lesson. OV did not become reliable because the first trap slate was clever. It became reliable because the build system turned the world into a reproducible factory, then the pilots punished weak task geometry.

The OV sequence worth reusing:

1. Create from skeleton into a live cockpit. Commit `2bc6a35` made World 2 a real workspace with doctrine, decisions, worksheets, and AutoQC defenses.
2. Lock the brainstorm, then build the submission copy. Commits `b9aaab8` through `dcd181d` show the early value: clean reviewer-facing copy, exact Brainstorm DOCX structure, and render verification before the spec.
3. Run Phase A before the spec. Commit `b19846f` created a substrate proposal pack with identity, meds, labs, studies, roster, and milestones, with every derived number flagged for physician ratification.
4. Run Phase B as task architecture plus file plan. Commit `748c6c6` assembled the 4-section spec, 10 task blocks, 43-file plan, data hierarchy, friction table, and defended ambiguities.
5. Audit before DOCX. Commit `7f40709` removed task telegraphs and marked shared-trap substrate before the package hardened.
6. Build DOCX by Mode A clone, then keep polishing against the approved world style. Commits `9487864` through `53ee024` show several passes on template parity, content completeness, leak removal, and KM-style visual fidelity.
7. Build files through the canonical Epic renderer, not by hand. Commits `da468c3`, `92338eb`, and `3893d15` created the Phase 3 plan, built 29 world files, 3 supplementary files, and 9 task files, then caught a header or footer prior-world leak.
8. Make deterministic rebuilds and one-command gates. Commit `fd024c0` pinned document output. Later commits wired `build_all.py`, `verify_ondina.py`, and the task gates into the routine.
9. Separate world and task files at upload. Commit `ee1ab7a` put each E1-T file only in its task packet. That is the mount lesson paid for by OV01.
10. Pilot, retire, and recenter by evidence. The later history is a search over mechanisms. Coding restraint ceilinged. Telegraphed conflict ceilinged. De-telegraphed conflict floored. Off-text image worked when the deliverable did not force the image open. Background-line med resume floored where headline disposition ceilinged.

World 3 should copy that conveyor. Do not start by writing 30 files. Start with the task slate and source geometry, then ratify substrate, then build deterministic documents.

## Exact OV Tooling Found

There is no finished generic `tools/new_world.py` in the repo. That was only proposed in `docs/world-factory-playbook.md`.

The existing working toolchain is world-local:

- `worlds/ondina-vasquell/build/build_all.py` - one-command deterministic rebuild.
- `worlds/ondina-vasquell/build/build_world_files.py` - core Mode A world and supplementary file builder.
- `worlds/ondina-vasquell/build/build_task_files.py` - task-file builder, delegating to the same renderer.
- `worlds/ondina-vasquell/build/build_goldens.py` - golden builder through the same renderer.
- `worlds/ondina-vasquell/build/build_task_packages.py` - prompt, grader, run-instructions, prereg, task-file copy, and workflow-map emitter.
- `worlds/ondina-vasquell/build/epic.py` - canonical Epic renderer and banned-character guard.
- `worlds/ondina-vasquell/build/clinical_data.py` - single source of truth for world substrate.
- `worlds/ondina-vasquell/build/task_data.py` - single source of truth for task-level files.

Git confirms the origin:

- Commit `92338eb` introduced the Phase 3 build pipeline: 29 world files, 3 supplementary files, 9 task reference files, manifest, `clinical_data.py`, `task_data.py`, `epic.py`, `build_world_files.py`, and `build_task_files.py`.
- Commit `fd024c0` made it deterministic with `build_all.py`, pinned timestamps, deterministic docx output, `requirements.txt`, and the rebuild gate.
- Commit `d75b171` moved the build tools into the flattened canonical OV tree and repointed paths after clean-house.

World 3 should clone and generalize this exact toolchain, not invent a new renderer. That wrapper is now canonical at `tools/build/bootstrap_world_factory.py`. It copies the world-local factory pattern, creates blank `clinical_data.py` and `task_data.py` physician-gated stubs, and refuses to overwrite an existing world. Generic mechanical verification lives at `tools/verify/verify_world_factory.py`.

## World 3 Implication

The third world should not be "HF exacerbation." That is a textbook task and will ceiling.

The third world should be a transition-readiness world where the apparent clinical improvement is real but discharge is unsafe because oxygen, DME, exertional physiology, renal status, anticoagulation, and handoff ownership are not resolved.

The first task family should be oxygen and DME because it has not been spent in KM or OV, it supports realistic off-text evidence, and it naturally creates payer, post-acute, and discharge-readiness conflicts.

## Avoid As Primary Levers

- Generic diuresis.
- Generic restart of RAAS inhibitors, SGLT2 inhibitors, or diuretics.
- CPAP adherence as the headline.
- Vitals as the hidden clue.
- Pure CDI restraint.
- Pure coding restraint.
- Buried text without off-text or forced schema.
- Same-author draft falsehood without placeholder or correction duty.

## Best Early Floor Candidates

1. Oxygen qualification denied because resting saturation is acceptable, while an off-text exertional test qualifies the patient.
2. DME delivery marked complete in a routine handoff, while a vendor note shows the portable concentrator or home oxygen setup failed.
3. Anticoagulation plan embedded in an external SNF or pharmacy sheet, with the chart contradicting the dose, duplication, or hold timing.
4. Discharge summary or post-acute handoff inherits a background closure of "no oxygen need" or "equipment delivered" that the chart contradicts.
5. Patient safety RCA after readmission, where the tempting answer is patient nonadherence but the source chain shows a system failure.
