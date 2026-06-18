# Marva Lydell - World Status

Status: pre-brainstorm scaffold. No platform world exists.

Last updated: 2026-06-18.

## Current State

Marva Lydell is approved as the patient-world name. Candidate 3 is selected from the internal medicine candidate list, with the post-audit product thesis: cardiorenal respiratory transition readiness.

There are no finalized patient-specific clinical values, dates, files, tasks, prompts, goldens, graders, or trajectories. The current demographic direction is a Black older adult woman. The only current work is source review, task architecture, trap source geometry, and Brainstorm drafting.

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

## Open Decisions

1. Patient profile and setting beyond Black older adult woman.
2. World snapshot date.
3. Five or more task structures.
4. First three floor candidates.
5. Which source documents must exist to arm each task without answer-key synthesis.
6. Which off-text evidence is realistic and peripheral enough to be missed.
7. Whether the Brainstorm draft should stay transition-readiness first, or narrow harder around oxygen and DME.
8. Which OV Brainstorm and transcript builder rules become mandatory for Marva.

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
