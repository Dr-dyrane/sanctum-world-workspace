# OV02 v6 (image-miss lever) - RLS / Studio upload runbook

STATUS 2026-06-15: DO NOT RE-PILOT AS-IS. Piloted job fe95a8a0 -> uniform floor 0.08-0.15, ZERO catchers = the KM08 broken-vision-gate outcome, not a fair floor. The Studio harness is bash-only on both sides: neither the agent nor the grader can view the photo, so the image-only finding is structurally uncatchable and the grader punishes correct restraint identically to negligent overclaiming. Verdict + records: phase-4-pilot-review-submit/results/OV02-v6-pilot-2026-06-15-job-fe95a8a0.md. DECISION = PATH A: recut to a SYNTHESIS catch creditable from the text signals (photo deliberately taken on transfer day + new 38.0 temp + IV abx running through the line -> suspect line infection -> inspect/hold/pull+culture), credit the correct hedge, keep "No line complication documented" as the indefensible miss, image becomes corroboration not requirement, trim the intake hint so the catch is fair not telegraphed. The runbook below is RETAINED for upload mechanics only; do not upload until the Path A grader+intake recut is done.

--- ORIGINAL RUNBOOK (pre-pilot, retained for upload mechanics only) ---
STATUS 2026-06-15: GO. Image delivered and vision-gate clean (EXIF 0, infection clearly visible, no identifiers/text). Cold bench screen = BORDERLINE leaning FLOORS (first lever to clear the bench as a floor; estimated 55-70 percent harness miss). Mandatory bench fixes applied (grader vision requirement, partial-credit anchor, temperature corroboration-only, mount isolation). Build-side complete; remaining steps are Studio upload + pilot.

## Workflow type (RESOLVED)
Select "Medical Transcription and Clinical Documentation Completion" (P0): the deliverable is completing a clinical documentation template (the SNF transfer note). NOT the old OV02 "Inpatient Medical Coding and DRG Assignment" string. Fallback if a unique string is required: "Referral Intake, Triage, and Scheduling Coordination". Verify the exact name on the live Task Selection Categories sheet.

## Decision to confirm before upload
OV02-id reuse versus a fresh id. OV02 coding was earlier marked do-not-build-on; reusing the OV02 RLS task id is fine if intended (it carries prior coding runs), otherwise create a fresh id. This is a one-time choice at Step 10.

## Upload set (what goes where)
- TASK FILES (mount, upload all three): snf_transfer_note_template_05242026.docx, transfer_day_nursing_intake_05242026.docx, iv_line_site_photo_05242026.jpg.
- PROMPT: prompt-OV02.txt.
- GOLDEN: golden-OV02-v6.docx.
- GRADER: grader-guidelines-OV02.txt. CRITICAL: the grader is a model and the finding is image-only - the image MUST be attached as a grader input. The grader file's top block states this as a blocking requirement. If your harness cannot attach the image to the grader, do not score.
- DO NOT upload the meta files (prereg, A0.5, RUN-INSTRUCTIONS) - they are local-only. Upload only the prompt, the three task files, the golden, and the grader.

## Step-10 sequence
1. Select the workflow (above). Confirm exact name on the live sheet.
2. Paste prompt-OV02.txt.
3. Upload the three task files (template, intake note, photo); click the separate Save File Changes (not just top Save); refresh; confirm all three show UPLOADED, not staged.
4. Upload golden-OV02-v6.docx to the golden slot.
5. Paste/upload grader-guidelines-OV02.txt; ATTACH iv_line_site_photo_05242026.jpg as a grader input; confirm the grader names the golden by filename.
6. Save; refresh; confirm prompt, three task files, golden, grader all survive untruncated.
7. Run Task AutoQC (rerun only N failing). Expected justified residuals: Self-Contained Guidelines (grader needs the mounted chart and image). Justify with the exact flagged text; do not flatten the grader.
8. Run Trajectories (10).

## First-trajectory gates (before trusting any score)
- MOUNT GATE (#16): find /docs shows exactly the three task files under /docs/filesystem, no /docs/.apps_data, no stale filename or collision with a world file.
- VISION GATE (KM08): confirm the model under test opened and saw the image (agent-visible) AND the grader can see it to score a miss (grader-visible). A floor riding on an image invisible to one side is broken.

## Read by mechanism (not by score)
A floor MISSES the infected line (or notes it without acting). A catcher identifies it from the photo (temperature is corroboration only) and acts: remove and culture the line, hold IV antibiotics through it, defer or qualify the transfer. Expect bimodal, miss-heavy.

## After the pilot
FA/GA from the 2nd-lowest valid run (#20); pull the grading transcript first. One re-roll only (#19). Pilot watch-item: the template IV-access line and the intake "photo taken" line mildly cue the image; if the pilot comes back catch-heavy, de-hint the intake line before any re-roll. See OV02-v6-pilot-preregistration.md for the locked forecast and read rules.
