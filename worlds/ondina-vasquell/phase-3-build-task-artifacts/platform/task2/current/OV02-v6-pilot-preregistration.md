# OV02 v6 PILOT PREREGISTRATION - locked before any upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

OV02 latest version (v6). This re-purposes the OV02 slot away from the retired coding mechanism (v1-v5, all ceilinged) to the IMAGE-MISS lever. NOTE for Alexander: this reuses the OV02 task identity that was earlier marked "do not build on it"; confirm the OV02 id reuse is intended versus a fresh id, and note the workflow is no longer Inpatient Coding (see Workflow below).

## Mechanism under test
IMAGE-MISS (the sixth class, untested here; "Raising Task Difficulty: Worked Example #1", Change 3; KM08 banked all-floor on a photo-miss). A critical finding - an infected intravenous line site - lives ONLY in a task-level photograph plus one buried low-grade temperature in the transfer-day intake note. It appears nowhere in prose. The physician completing the SNF transfer note must catch the line infection and act on it. The model fails because it reads images poorly, not because the finding is hidden in text. Floor = the completed transfer note does not identify or act on the infected line. Catcher = it catches it from the photo and the temperature and acts (remove, culture, hold IV antibiotics through the line, defer transfer).

## Base rate
KM08 banked as an all-floor photo-miss on this model. The worked example moved a SNF-note task from all 95-98 percent (ceiling) to 15-40 percent (deep bimodal) primarily via this image change.

## Forecast
Bimodal. Floor below 0.30 if the response misses the line infection or notes it without acting. Catcher above 0.85 if it identifies the infection from the photo and temperature and acts while completing the transfer note. Mean target 45 to 75. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

## Read rules (set now)
- A floor MISSES the line-site infection (or notes it without acting / transfers on the line as-is). A catcher IDENTIFIES it from the photo plus the low-grade temperature AND acts.
- Identifying but not acting = incomplete (partial), not a full catch.
- FA/GA subject = 2nd-lowest % run; pull the grading transcript before writing. Failure-only, no section names, no dashes.

## Substrate / freeze gate - PASSED
No world file describes the IV/PICC line site (the chart is foot-only), so the finding is prose-silent: nothing in text states or contradicts it (this is what avoids the prose wall). IV antibiotics are documented, so a line exists and the finding is clinically grounded. All additions are task-level (template + intake note + photo); no world file is edited. The worked example's Change 1 (remove a leaking world file) is skipped because no world file leaks this finding.

## VISION GATE (KM08 precedent) - REQUIRED before any pilot
The image does not exist yet (Codex to generate from codex-image-prompt-OV02-v6.md). Before any pilot, confirm the infection is AGENT-VISIBLE (the model under test can open and see the photo) AND GRADER-VISIBLE (the grader can see it to score the miss). A floor that rides on an image not visible to one side is broken.

## Bench rule (decisive)
Cold screen AFTER the image exists: does a fresh strong model, finishing the transfer note, CATCH the infected line or MISS it? Because models read images poorly, a reviewer MISS is the FLOOR signal here - the inverse of the prose levers. Proceed to pilot ONLY on a floor (reviewer-miss) verdict. If the cold reviewer reliably catches it, the image lever ceilinged; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).

## Workflow
RESOLVED: "Medical Transcription and Clinical Documentation Completion" (the deliverable is completing a clinical documentation template, the SNF transfer note). Fallback if a unique string is required: "Referral Intake, Triage, and Scheduling Coordination". NOT "Inpatient Medical Coding and DRG Assignment" (the old OV02 string). Verify the exact name live at Step 10.

## Mount
Three intended task-level files (per the worked-example noise + format design): snf_transfer_note_template_05242026.docx, transfer_day_nursing_intake_05242026.docx, iv_line_site_photo_05242026.jpg, plus the world chart. First-trajectory find /docs must show exactly these three task files under /docs/filesystem, no /docs/.apps_data, no stale/collision.

## Stopping rule (pre-registered)
One embedded re-roll only (DO-NOT-REPEAT #19). If the cold screen says WILL CEILING or the pilot ceilings, this mechanism class is exhausted; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).
