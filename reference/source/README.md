# Source Material - source-of-truth index

External and official Sanctum materials Alexander has authorized for local use. The Instruction Document and the Task Selection Categories are re-released roughly weekly, so this folder is organized by PURPOSE. Within each family the CURRENT version sits in its folder; prior versions live under `_superseded/`.

Rules:

- Cite the current file named below. Never cite a `_superseded/` file as current guidance. Stale reads are the dominant hallucination source here (`docs/anti-hallucination.md`, lever 2).
- Do not edit source artifacts in place. Derived guidance belongs in `reference/checklists/`, `reference/workflows/`, or `reference/world-spec-guidelines/`.
- When a new version arrives: drop it in the matching folder, move the prior file into `_superseded/<family>/`, and update this table.

## Folder map

| Folder | Holds | CURRENT source of truth (verified 2026-06-19) |
|---|---|---|
| `instruction-doc/` | The Project Sanctum instruction document (the weekly master guide) | `[EXP] Project Sanctum Instruction Document (06_09).md` |
| `task-selection-categories/` | Appendix A (approved list) + companions | Appendix A = `Sanctum_Task_Selection_Categories_Combined_06_19.docx` (237 workflows, tier + work product); pick the exact name and tier and match the deliverable to the work product. Companions: `Project_Sanctum_Task_Categories_with_Difficulty_Suggestions.docx` (difficulty levers), `Project_Sanctum_Resources_by_Category.docx`. Confirm against the latest Appendix A / live sheet (see below). |
| `phase-1-brainstorm/` | Current capture of the instruction doc's Part 1 (Brainstorm): World Setup + Rough Task Ideas writing standards, Common Mistakes, and the Studio upload/AutoQC/submit flow (2026-06-19 screenshots) | `phase-1-brainstorm-instructions-2026-06.md` |
| `phase-3-evaluating/` | Current capture of the instruction doc's Phase 3 (Evaluating): trajectories, TaigaQA, FA/GA, preference ranking, plus the 2026-06-19 "updated guidelines" screenshots | `phase-3-instructions-2026-06.md` |
| `autoqc-section-guides/` | Official AutoQC section writer-docs held locally (Sections 5-6; Sections 2-4 are in `reference/templates/`) | `AutoQC_Section_5_Golden_Response_v6.6_writer.docx.pdf`, `AutoQC_Section_6_Grader_Guidelines_v6.6_writer.docx` |
| `worked-examples/` | Filled reference instances + the difficulty worked example (not weekly-updated) | `FA_GA.md`, `FA_GA-2.md`, `FA_GA Template [05_14_26].docx`, `World 004 QA + Failure + Grader Analysis.docx`, `Raising_Task_Difficulty_Worked_Example.pdf`, `Grader Guidelines.md` |
| `media/` | Video walkthroughs | `How to Upload Your Clod Transcript.mp4` |
| `_superseded/` | Prior versions of the weekly families. Provenance only, never current. | see `_superseded/README.md` |

## The live sheet still wins

Even the current Task Selection Categories file is a local snapshot. The menu changes mid-flight, so per AGENTS.md guardrail 13, verify each task's workflow string against the LIVE sheet at Step 10, not against any saved copy. Appendix A (the approved list) is `task-selection-categories/Sanctum_Task_Selection_Categories_Combined_06_19.docx` (237 workflows, tier + work product). Pick the exact name and tier from it and match the deliverable to the stated work product. Quoted strings drift between the file and a reviewer's live view: Larry's 06/20 review recommends Specialist Referral Documentation and Discharge Medication Reconciliation (both P0) and treats Specialty Consultation Note as gone, but none appear verbatim or at that tier in the 06/18/19 files, so confirm the exact string and tier against the file or the live sheet before locking. The Difficulty-Suggestions doc adds the per-workflow difficulty levers.

## FA/GA worked examples are LIVE

`worked-examples/FA_GA.md` and `FA_GA-2.md` are the two official worked examples cited by `docs/fa-ga-canonical.md`. They are reference instances, not stale versions.

## Open follow-up for Alexander

Derived guidance under `reference/world-spec-guidelines/` (notably `11_transcript_requirements.md` and `12_required_upload_inventory.md`) still cites the archived 05_24 guide and 06_08 doc by line number. Those resolve to `_superseded/instruction-doc/` and stay accurate to those versions. Re-deriving them against 06_09 is a content task, not done in this reorg.
