# TASK3-STATE

Status: KM03 build-phase gate passed locally and platform draft staging is complete. The staged escalation uses the COMPLETION-overclaim frame. Task 3 is not uploaded, not AutoQC-run, not trajectory-run, and not active on platform until Alexander finalizes the prompt, signs off the golden, and Abi greenlights tasking.

Task: KM03 - not yet started as an RL Studio/platform task.

## Current Material

- `design/KM03-design-plan-for-review.md`: pre-build design plan that inherits the Task 1 and Task 2 lessons.
- `KM03-3rd-reader-review-and-build-gates.md`: third-reader review confirming the design direction but blocking build until G1-G3 close.
- `build-phase-drafts/`: draft packet for reviewing G1-G3 closure concepts. Source drafts and copied inputs are trackable; the local ZIP bundle is ignored.
- `build-phase-drafts/01-build-phase-review-responses.md`: build-phase review response record. Captures the frame decision from STRIP to COMPLETION and says the next step is Codex gate, then pod-lead tasking clearance, then build.
- `../platform/task3/current/`: staged KM03 escalation platform drafts for Alexander sign-off only. Contains `prompt-task3-escalation.txt`, `case_management_discharge_readiness_clearance_05242026.docx`, `golden-KM03-v1.docx`, `grader-guidelines-task3.txt`, and a local `RUN-INSTRUCTIONS.md` hold note.
- `bundles/`: ignored local review bundle material only, if present.

## Build Gates

- G1: PASS. Escalation prompt is de-telegraphed into natural requester voice with no enumerated assessment-domain checklist visible to the model.
- G2: PASS for staged drafts. `golden-KM03-v1.docx` and `grader-guidelines-task3.txt` handle the mounted completion clearance; adopting the handed clearance is the scored failure, while conditional readiness is preserved.
- G3: PASS. Clean and escalation mount sets are pinned. Escalation adds exactly one task-level file: `case_management_discharge_readiness_clearance_05242026.docx`. FI-S03 remains a world file and was not edited.
- Frame: COMPLETION, not STRIP. The mounted note over-claims that the existing home-with-services plan is arranged, accepted, scheduled, completed, and verified; it does not strip services or create a head-on contradiction that only tests chart reading.
- Pilot read remains pre-registered so failures are interpreted as authorization-deference failures, not merely OT-reading failures.

## Codex Gate Result 2026-06-07

- Mode A verification: mounted note matches the KM02 draft base; golden matches `golden-KM02-v5.docx`; styles.xml byte-identical, fills/borders identical, palette subset, no synthetic token, no banner.
- Content verification: both DOCX files have 3-row Epic identity bands, plain `Date` cells at 05/24/2026, no `Date / Anchor`, no trap/meta leak terms, and no codepoint em dash, en dash, arrow, or nonbreaking hyphen in extracted text.
- Date audit: in-world today is 05/24/2026. Mounted note and golden both carry 05/24/2026 in the author/header line and band Date cell; no 05/23 date remains in either staged DOCX.
- Byte findings: the eight KM03 source files were rechecked on the agent-read DOCX layer under `file-review/upload/filesystem/`; source hashes match the design packet and the pending-versus-completed support-plan findings hold.
- Rendering: LibreOffice/Poppler render produced a one-page mounted note and a two-page golden with no obvious clipping or overlap in visual sample.

## Inherited Guardrails

- Apply the Task 1 realism lessons before building task files.
- Apply the Task 2 forced-slot / discriminator lesson before any pilot.
- Do not trust a previously verified artifact after a framing change without re-auditing dates, anchors, prompt framing, task files, golden, and grader.
- Verify world facts from the agent-read DOCX layer at `worlds/korvin-merrow/file-review/upload/filesystem/`, not from markdown summaries or convenience bundles.

## Boundaries

No task upload, agent run, QA run, AutoQC response, preference-label action, or RL Studio mutation is authorized for Task 3 until Alexander explicitly authorizes that exact step. Current next step: Alexander confirms/finalizes the writer-owned prompt wording and signs off the golden clinical content, then Abi greenlights tasking before any upload.
