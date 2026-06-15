# OV02 v6 (image-miss lever) - RUN-INSTRUCTIONS

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot. The image does not exist yet (Codex to generate from codex-image-prompt-OV02-v6.md).

## Workflow type (DECISION + verify at Step 10)
Content is an SNF transfer/admission note, so the approved workflow is "Referral Intake, Triage, and Scheduling Coordination" OR "Medical Transcription and Clinical Documentation Completion" - NOT the old OV02 "Inpatient Medical Coding and DRG Assignment" string. Verify the exact name on the live Task Selection Categories sheet. Also confirm OV02-id reuse versus a fresh id (OV02 coding was earlier marked do-not-build-on).

## Mechanism under test
IMAGE-MISS (worked-example Change 3; KM08-proven). The critical finding - an infected IV line site - lives only in the task-level photo plus one low-grade temperature in the intake note; prose is silent. The physician completing the transfer note must catch and act on it. Floor = misses or does not act on the line infection. Catcher = identifies it from the photo + temp and acts.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- THREE task-level files: snf_transfer_note_template_05242026.docx, transfer_day_nursing_intake_05242026.docx, iv_line_site_photo_05242026.jpg. Upload all three; confirm UPLOADED, not staged.
- FIRST-TRAJECTORY MOUNT GATE (DO-NOT-REPEAT #16): inspect the first trajectory's `find /docs`. Require exactly these three task files under `/docs/filesystem`, no `/docs/.apps_data`, no stale filename or collision with a world file.
- VISION GATE (KM08, REQUIRED before trusting any score): confirm the photo is AGENT-VISIBLE (the model opens and sees it) AND GRADER-VISIBLE (the grader can see it to score the miss). A floor riding on an image not visible to one side is broken.

## Self-QC before RLS upload (CANONICAL)
Run the writer-edition AutoQC against the Task Prompt, Golden, and Grader, one per upload; every numbered check PASS or justified N/A. Grader is the KM five-block with NO scoring bands.

## Order of operations (do not skip)
1. Codex generates the photo from codex-image-prompt-OV02-v6.md; scrub metadata; render-verify.
2. Vision gate: confirm agent- and grader-visible.
3. Cold bench red-team screen (docs/red-team-screen-prompt.md): does a fresh strong model finishing the transfer note CATCH the infected line or MISS it? A reviewer MISS is the floor signal. Upload only on a FLOORS or BORDERLINE (reviewer-miss) verdict.
4. RLS upload, Task AutoQC, first-trajectory mount + vision gate, then Trajectories.

## Expectation
See OV02-v6-pilot-preregistration.md for the locked forecast and read rules. One re-roll only (#19); if it ceilings, OV closes at one floor (OV01).
