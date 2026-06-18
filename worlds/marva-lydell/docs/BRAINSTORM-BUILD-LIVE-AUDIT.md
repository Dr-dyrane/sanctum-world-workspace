# Marva Lydell Brainstorm Build Live Audit

Status: living resume doc. Brainstorm package built locally, pending human edit and provenance cleanup.

Date opened: 2026-06-18.

## Current Checkpoint

Marva Lydell is the approved patient-world name. The repo folder is `worlds/marva-lydell/`.

Current phase: post-local Brainstorm build. The only authorized work is human edit, provenance cleanup, and Phase A planning. No AutoQC, Studio action, task artifact, world file, prompt, golden, grader, image generation, or trajectory is authorized from this checkpoint.

Current product thesis: a Black older adult woman with a cardiopulmonary admission that improves at rest but remains unsafe at transition unless oxygen, DME, exertional physiology, renal recovery, anticoagulation, and handoff ownership are reconciled.

## Source Of Truth Now

- Cockpit: `worlds/marva-lydell/00-START-HERE.md`
- Live status: `worlds/marva-lydell/docs/WORLD-STATUS.md`
- Planning canvas: `worlds/marva-lydell/docs/PLANNING-CANVAS.md`
- Brainstorm draft and audit copy: `worlds/marva-lydell/docs/BRAINSTORM-DRAFT.md`
- Canonical Brainstorm markdown: `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm.md`
- Brainstorm DOCX: `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm.docx`
- Transcript scaffold markdown: `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm_Claude_Transcript.md`
- Transcript scaffold DOCX: `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm_Claude_Transcript.docx`
- Draft pointer: `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm_DRAFT.md`
- Factory: `worlds/marva-lydell/build/`
- Repo spine: `WORKSPACE_FILE_MAP.md`

## OV Build Path To Reconstruct Before Editing

Read these before any serious Brainstorm rewrite:

- `worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm.md`
- `worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm.docx`
- `worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm_Claude_Transcript.md`
- `worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm_Claude_Transcript.docx`
- `worlds/ondina-vasquell/submission/STUDIO-PROVENANCE.md`
- `tools/build/build-docx-ondina-brainstorm.py`
- `tools/build/build-docx-ondina-brainstorm-claude-transcript.py`
- `worlds/ondina-vasquell/docs/WORLD-STATUS.md`
- `worlds/ondina-vasquell/docs/REFERENCE-AUDIT.md`
- `worlds/ondina-vasquell/docs/build-notes/phase-3-build-plan.md`

Questions to answer from the OV path:

1. How did the Brainstorm MD become the DOCX?
2. Which builder controlled style, footer, metadata, and banned characters?
3. How did the Claude transcript avoid benchmark language, tooling leakage, and prior-world identifiers?
4. Which checklist ran before Studio upload?
5. Which human-review or AutoQC issues did OV catch early?
6. Which facts were deferred to substrate ratification rather than asserted in the Brainstorm?

## Brainstorm Quality Target

This Brainstorm should beat the published examples by making the task architecture obvious and the chart synthesis invisible.

The Brainstorm must show:

- Typical clinical world declared in the first paragraph.
- A patient identity that is synthetic, stable, and non-searchable.
- A coherent hospital snapshot where the patient improves but remains transition-unsafe.
- At least five distinct task structures, with completion capped at one to two tasks.
- Ten rough task ideas with requester, deliverable, workflow family, forced slot, quiet wrong move, and post-snapshot anchor.
- Frictions that arise from real clinical and operational conflict, not generic complexity.
- Traps that are source-geometry mechanisms, not clever labels.
- Raw world files as substrate, not answer-key synthesis.
- Race as demographic context only.
- No public post-July-2025 knowledge dependency.

## Parallel Audit Lanes For Next Session

Use parallel agents or parallel read passes if available. Every lane writes findings back here before edits harden.

| Lane | Focus | Required output |
|---|---|---|
| OV build lane | Reconstruct the exact OV Brainstorm and transcript build path. | Builder steps, leak gates, and reusable command list. |
| Template lane | Read Brainstorm templates, examples, AutoQC guidance, and reviewer patterns. | Required Brainstorm shape and send-back risks. |
| KM and OV difficulty lane | Extract what ceilinged and what floored. | World 3 trap design rules, with spent levers marked. |
| Clinical lane | Stress-test cardiorenal respiratory transition realism. | Proposed patient profile, source set, and unsafe-transition axes. |
| Voice and leakage lane | Check all draft text for clinical cadence and platform-language leaks. | Banned phrases, rewrite notes, and verification command list. |
| Repo hygiene lane | Ensure every new artifact has one canonical home. | Updated file map and no loose planning files. |

## Known Do-Not-Repeat Rules For This Brainstorm

- Do not begin by writing a narrative chart. Task architecture comes first.
- Do not make oxygen or DME the task headline every time. A model inspects the headline.
- Do not let world files state the final readiness conclusion.
- Do not use race as a clue or disease explanation.
- Do not mount task files as world files.
- Do not call a trap fair unless the chart contradicts the wrong move.
- Do not use a same-author false draft claim without a true placeholder or correction duty.
- Do not allow workflow labels to drift from live platform categories at Step 10.
- Do not leave transcript text sounding like a benchmark, eval, agent, or internal build log.

## Working Inferences

| Date | Inference | Status |
|---|---|---|
| 2026-06-18 | World 3 should not be generic heart failure. It should be transition readiness under cardiopulmonary and renal constraints. | Active |
| 2026-06-18 | Best first floor family is oxygen and DME readiness, especially off-text exertional data or vendor failure hidden from the obvious deliverable. | Active |
| 2026-06-18 | Female patient is locked. Marva Lydell is the approved name. | Active |
| 2026-06-18 | The repo slug must match the patient-world name. This is already done: `worlds/marva-lydell/`. | Done |
| 2026-06-18 | The Brainstorm should stay task-first, then substrate, then spec. | Active |
| 2026-06-18 | Brainstorm values now proposed: 72-year-old Black woman, snapshot 06/10/2026 at 18:00, task window 06/11/2026 through 06/17/2026. These are planning values until Phase A ratifies them. | Active |
| 2026-06-18 | Transcript is a scaffold, not a true Claude export. It cannot be uploaded as a real Claude transcript until Alexander provides or confirms the share/export. | Active |

## Build Record - 2026-06-18

Built artifacts:

- `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm.md`
- `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm.docx`
- `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm_Claude_Transcript.md`
- `worlds/marva-lydell/submission/Marva_Lydell_Brainstorm_Claude_Transcript.docx`

Build tools:

- `tools/build/build-docx-marva-brainstorm.py`
- `tools/build/build-docx-marva-brainstorm-claude-transcript.py`

Verification:

- Brainstorm DOCX Mode A fingerprint gate passed: styles, fills, borders, palette, metadata, banned dash/arrow, synthetic token, and banner checks.
- `tools/verify/verify_world_factory.py worlds/marva-lydell` passed for 2 DOCX files and 12 text files.
- `tools/verify/verify_voice.py worlds/marva-lydell/submission worlds/marva-lydell/docs` passed active deliverables. Existing older archived warnings elsewhere in the repo remain non-blocking.
- Python compile passed for both new Marva DOCX builders.
- Banned dash and arrow scan passed on Marva submission and docs markdown.

Render status:

- Visual DOCX render attempted with the documents render helper.
- First blocker was `liblcms2.2.dylib`; local user-cache patch redirected that and bundled freetype successfully.
- Render is still blocked on missing `libfontconfig.1.dylib` in the bundled LibreOffice runtime.
- Page-image QA is not passed. Do not claim rendered visual approval until fontconfig is installed or a working LibreOffice renderer is available.

## Next Authorized Work When Resuming

1. Human edit the Brainstorm text.
2. Replace or reconcile the transcript scaffold with a real Claude share/export.
3. Fix local LibreOffice fontconfig or render on a machine with a working DOCX renderer.
4. Inspect rendered pages before upload.
5. Only after Alexander authorizes it, run Brainstorm AutoQC or upload.

## Mechanical Gates Before Any Brainstorm DOCX

- Run `tools/verify/verify_world_factory.py worlds/marva-lydell`.
- Run the relevant voice scan before upload-facing text leaves markdown.
- Confirm no banned dash or arrow characters in active Marva docs.
- Confirm no old slug, old name, or prior-world patient identifier remains.
- Confirm every future DOCX build uses the correct Mode A or document builder path, not ad hoc Word construction.
- Confirm the transcript source is real before any platform upload.
