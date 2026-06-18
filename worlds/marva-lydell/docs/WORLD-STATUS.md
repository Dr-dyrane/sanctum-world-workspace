# Marva Lydell - World Status

Status: Brainstorm package built locally. No platform world exists.

Last updated: 2026-06-18.

## Current State

Marva Lydell is approved as the patient-world name. Candidate 3 is selected from the internal medicine candidate list, with the post-audit product thesis: cardiorenal respiratory transition readiness.

The Brainstorm source and DOCX are built. The working concept uses a 72-year-old Black woman, a 06/10/2026 snapshot, and a 06/11/2026 through 06/17/2026 task window. These values are Brainstorm-level planning values, not Phase A substrate until explicitly ratified.

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

## Open Decisions

1. Human edit and approval of the Brainstorm text.
2. Real Claude transcript share/export, or explicit decision to replace the scaffold.
3. Phase A substrate ratification: exact comorbidities, medication classes, source documents, dates, and care-team roster.
4. Which first three task levers should be designed for pilots.
5. Which off-text evidence is realistic and peripheral enough to be missed.
6. Live workflow validation before any task upload.

## Current Guardrails

- Structures first.
- Source geometry before prose.
- No answer-key synthesis in shared world files.
- No warm headline-axis trap as the central bite.
- No task-layer file inside world files.
- No prompt telegraph.
- No post-July-2025 public knowledge dependency unless the reference is attached and realistic.
- No `build/build_all.py` until placeholders are gone and Phase A is approved.
- Do not use race as a scoring lever, shortcut, or unstated explanation. The chart must carry every scored fact.
- Do not upload the transcript scaffold as a real Claude transcript.
- Do not treat the DOCX visual render as passed until LibreOffice fontconfig is fixed and page images are inspected.
