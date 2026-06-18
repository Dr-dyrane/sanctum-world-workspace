# OV02 Path A PILOT PREREGISTRATION (synthesis recut) - locked before re-upload, AutoQC, re-pilot
Rule: this file does not change after the re-pilot lands. Post-pilot reconciliation goes in a results record citing this file. Supersedes OV02-v6-pilot-preregistration.md (image-miss lever), which is retained as the historical record of pilot job fe95a8a0.

OV02 deliverable filenames stay v6 (golden-OV02-v6.docx, grader-guidelines-OV02.txt, same three task files); the LEVER is recut from image-miss to off-text synthesis. Same OV02 task identity and workflow as the v6 pilot.

## Why recut (from the v6 image pilot)
v6 (image-miss) piloted job fe95a8a0 = UNIFORM floor 0.08-0.15, ZERO catchers. Diagnosis: the Studio harness is bash-only on both sides; neither agent nor grader can view the photo, and the grader REQUIRED identification "from the photograph", so the floor was a broken-vision artifact, not a clinical-judgment failure, and it punished correct restraint identically to negligent overclaiming. Records: tasks/task2/pilot/OV02-v6-pilot-2026-06-15-job-fe95a8a0.md.

## Mechanism under test (recut)
OFF-TEXT SYNTHESIS (vision-independent). The central finding - a new intravenous line-site infection - appears in NO chart prose. It must be ASSEMBLED from three documented transfer-day signals, all readable as text: (1) a line-site photograph was specifically obtained on transfer day and added to the chart; (2) a new low-grade temperature of 38.0 appeared in the transfer-day intake vitals, where the patient had been afebrile (36.8 on 05/21); (3) intravenous antibiotics are running through that same line. The physician completing the SNF transfer note must connect these into a line-site concern and act (inspect/hold/qualify the transfer, remove and culture the catheter, do not run IV antibiotics through a possibly infected line). The photograph is corroboration, not a requirement.

## Key evidence this floors independent of vision
In the v6 pilot the representative run (Attempt 10) had ALL THREE text signals in front of it - it explicitly noted the 38.0 temp (and compared it to the 36.8 afebrile baseline), referenced the "line-site photo taken and added to the chart" line, and stated IV antibiotics were infusing - and STILL wrote "No line complication documented" with only "recheck temp per protocol". 10/10 runs missed the synthesis. The miss is real at the current intake calibration without any reliance on the image. The intake note is therefore UNCHANGED from the v6 pilot (pilot-calibrated); only the grader and golden were recut to credit the text path.

## Forecast
Bimodal. Floor below ~0.30 if the response misses the line, affirmatively dismisses it ("no line complication"), or notes it without acting / transfers on the line as-is. Catcher above 0.85 if it assembles the line concern from the three signals AND acts. Mean target ~0.40-0.70. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

HONEST RISK: this is now a PROSE/off-text lever, and five prose-reasoning levers ceilinged on this chart. The saving grace is that this finding is genuinely OFF-TEXT (no chart prose states or contradicts it), which is the same cold-gap shape that made OV01 the one floor - not the "catch a wrong line contradicted by loud chart prose" shape that ceilinged the other five. The bench decides before any spend.

## Bench rule (decisive) - REVERTED to the prose-lever rule
Cold screen: a fresh strong model finishing the transfer note from the SAME inputs the bash agent had (template + intake note text + chart facts; the photo is referenced but not provided as viewable). Does it assemble the line concern and act, or finish a clean note that ignores/dismisses the line? Because this is now a text-synthesis lever (NOT an image lever), a cold reviewer-CATCH is a CEILING signal (do not pilot); only a genuine reviewer-MISS is a floor candidate. This is the inverse of the v6 image-prereg rule.

## Read rules (set now)
- A floor MISSES the line concern, affirmatively dismisses it, or notes it without acting / transfers on the line as-is. A catcher ASSEMBLES it from the three transfer-day signals AND acts (inspect or remove+culture, hold/qualify transfer, do not run IV abx through the line).
- Crediting the correct hedge: a response that says it cannot fully assess the line from the record but flags the new fever + the specifically-obtained line-site photo + the IV route and directs inspection and holding/qualifying the transfer HAS caught and acted; credit it (this is the v6 fairness fix).
- FA/GA subject = 2nd-lowest % run; pull the grading transcript before writing. Failure-only, no section names, no dashes.

## Substrate / freeze gate - PASSED
No world file describes the IV/PICC line site (chart is foot-only), so the finding is off-text: nothing in prose states or contradicts it. IV antibiotics are documented, so a line exists and the finding is clinically grounded. All inputs are task-level (template + intake note + photo); no world file edited.

## Mount
Same three task-level files: snf_transfer_note_template_05242026.docx, transfer_day_nursing_intake_05242026.docx, iv_line_site_photo_05242026.jpg (retained as corroboration; harmless if the harness cannot render it), plus the world chart. First-trajectory find /docs must show exactly these three task files under /docs/filesystem, no /docs/.apps_data, no stale/collision. The grader no longer requires the image as a grader input.

## Stopping rule (pre-registered)
One re-roll only (DO-NOT-REPEAT #19). If the cold bench says WILL CEILING, or the re-pilot ceilings, the OV02 synthesis lever is exhausted; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).
