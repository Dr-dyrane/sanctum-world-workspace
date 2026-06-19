# Marva Lydell - World Status

Status: Brainstorm package built locally. No platform world exists.

Last updated: 2026-06-19.

## Current State

Marva Lydell is approved as the patient-world name. Candidate 3 is selected from the internal medicine candidate list, with the post-audit product thesis: cardiorenal respiratory transition readiness.

The Brainstorm source and DOCX are built. The working concept uses a 72-year-old Black woman, a 07/10/2025 snapshot, and a 07/11/2025 through 07/17/2025 task window. These values are Brainstorm-level planning values, not Phase A substrate until explicitly ratified. The July 2025 date spine follows the 2026-06-18 reviewer-driven rule that new and reopened clinical artifacts must not place their narrative present after 07/31/2025.

There are no world files, task files, prompts, goldens, graders, uploads, trajectories, or platform actions. The current work is human edit, provenance cleanup, and Phase A substrate planning.

The canonical build factory is installed at `build/` from the Ondina pattern. It is placeholder-gated and must not be run until Phase A substrate is ratified.

## Activity Log

- 2026-06-18: Read the workspace spine, KM performance report, OV status and floor-mechanism library, Quill worked example, Marcus and Harold world examples, and the world factory playbook. Created this scaffold.
- 2026-06-18: Reframed Candidate 3 away from generic HF exacerbation and toward oxygen, DME, cardiorenal, anticoagulation, and transition-readiness failures.
- 2026-06-18: Adopted the scaffold into the canonical world factory using `tools/build/bootstrap_world_factory.py --adopt-existing`. The tool installed `build/clinical_data.py`, `build/task_data.py`, the Epic renderer, and the build scripts without replacing the cockpit.
- 2026-06-18: Added `docs/NAME-SHORTLIST.md` and `docs/BRAINSTORM-DRAFT.md` for approval-gated planning.
- 2026-06-18: Set demographic direction to a Black older adult woman. Race is context only unless a mounted chart source makes it clinically relevant.
- 2026-06-18: Recut the name shortlist for that demographic direction. Current recommendation is Marva Lydell. Once approved, rename the folder to the patient-world slug before any build.
- 2026-06-18: Alexander approved Marva Lydell. Renamed folder from `worlds/cardiorenal-respiratory-transition/` to `worlds/marva-lydell/` before any build. Bootstrapped `submission/Marva_Lydell_Brainstorm_DRAFT.md`.
- 2026-06-18: Added `docs/BRAINSTORM-BUILD-LIVE-AUDIT.md` as the living resume doc for the next Brainstorm, Claude transcript, checklist, AutoQC, and leakage-control pass.
- 2026-06-18: Rebuilt the Brainstorm as `submission/Marva_Lydell_Brainstorm.md` and `docs/BRAINSTORM-DRAFT.md`. The new pitch centers readiness under contradiction: exertional oxygen, DME, volume risk, renal-med timing, anticoagulation source hierarchy, payer pressure, and home execution.
- 2026-06-18: Built `submission/Marva_Lydell_Brainstorm.docx` with `tools/build/build-docx-marva-brainstorm.py` using the Korvin Brainstorm Mode A clone path. Fingerprint gate passed.
- 2026-06-18: Built `submission/Marva_Lydell_Brainstorm_Claude_Transcript.md` and `.docx` as a marked transcript scaffold. It is not upload-ready until a real Claude share/export is pasted or reconciled.
- 2026-06-18: Mechanical gates passed: Marva world factory gate, active voice gate, banned dash and arrow scan, and Python compile for the new builders. Visual DOCX render is blocked locally because bundled LibreOffice still needs `libfontconfig.1.dylib`.
- 2026-06-18: Updated workspace canon after a new reviewer failure example: current accepted KM and OV artifacts are grandfathered, but Marva and all future or reopened clinical artifacts must keep world-file, task-file, golden, prompt, and grader chart dates on or before 07/31/2025. Recut the Brainstorm snapshot to 07/10/2025 and task anchors to 07/11/2025 through 07/17/2025. Removed local task-code and priority-code surface language from the Brainstorm table.
- 2026-06-19: Verified all ten task workflows verbatim against the current `reference/source/task-selection-categories/Sanctum_Task_Selection_Categories_Combined_06_19.docx`. Remapped three retired or absent strings: task 2 to `Medication Reconciliation` (P0), task 6 to `Specialty Consultation Note` (P1), task 8 to `Corrective Action Plan (CAP) Development and Tracking` (P1). The other seven were already valid and at least one P0 is present.
- 2026-06-19: Rebuilt `submission/Marva_Lydell_Brainstorm.md` and `.docx`. Mode A fingerprint gate and `verify_world_factory.py` passed. Rendered the DOCX to page images with the sandbox LibreOffice and visually inspected: masthead, three-column table, and task rows render cleanly with no clipping.
- 2026-06-19: Word render check + live-sheet verbatim pass. Re-rendered and inspected pages 1, 4, 6, 7: layout faithful, header row repeats, no clipping. All ten workflows verbatim-valid against the 06/19 sheet. The checks caught and fixed three priority errors from the human edit (the priority-spread summary plus per-task cells for tasks 3, 4, 10); all ten per-task priorities now match the sheet (six P0, four P1).

## Open Decisions

1. Human edit and approval of the Brainstorm text.
2. Real Claude transcript share/export, or explicit decision to replace the scaffold.
3. Phase A substrate ratification: exact comorbidities, medication classes, source documents, dates, and care-team roster.
4. Which first three task levers should be designed for pilots.
5. Which off-text evidence is realistic and peripheral enough to be missed.
6. Live workflow validation at Step 10. Local verbatim validation against the 06/19 sheet is done (2026-06-19); the platform menu can still retire or rename a workflow mid-flight, so reconfirm each string on the live sheet before any task upload.

## Current Guardrails

- Structures first.
- Source geometry before prose.
- No answer-key synthesis in shared world files.
- No warm headline-axis trap as the central bite.
- No task-layer file inside world files.
- No prompt telegraph.
- No evaluator-visible clinical narrative date after 07/31/2025 for Marva or any future/reopened work.
- No post-07/31/2025 public knowledge dependency unless the reference is attached and realistic.
- No `build/build_all.py` until placeholders are gone and Phase A is approved.
- Do not use race as a scoring lever, shortcut, or unstated explanation. The chart must carry every scored fact.
- Do not upload the transcript scaffold as a real Claude transcript.
- Do not treat the DOCX visual render as passed until LibreOffice fontconfig is fixed and page images are inspected.
