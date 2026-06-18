# OV11 FA/GA - Primary-care transition summary, immunization over-closure

Status: Job a74188e2. Ten runs 0.10 to 0.15 (0.10 five times, 0.12 three times, 0.15 twice), mean about 0.12, uniformly low with no high outlier. FA bound to the run saved verbatim at runs/OV11-attempt3-job-a74188e2.md: Attempt 3, run b44f310c, trajectory traj_c5e87ec, score 0.12. The second-lowest distinct is 0.12; the spread is uniform, so this run is representative, not the anomalous low the second-lowest-distinct rule guards against. Writer score: 0.10 (my own assessment of the model's performance, against the grader's 0.12; I put it at the floor because the closure was carried in with no flag at all, the rest of the summary is faithful but the missed central catch holds it at the bottom).

## Failure Analysis

This is Attempt 3, run b44f310c, trajectory traj_c5e87ec, scored 0.12; my own score of the model is 0.10. The model finished the summary competently. The hospital course, attending-action items, and added detail are accurate against the chart. The failure is the immunization line, carried from the 05/23 care-coordination review unchanged: immunizations reviewed and up to date, none indicated this admission.

No immunization history, administration, or review exists anywhere in the chart; the 04/30 outpatient summary documents only the dilated eye and foot examinations. The review attested a review that never happened, and the model listed it among current items with no flag. Attesting immunizations as addressed in a summary built for signature closes a real preventive-care gap in a diabetic with chronic kidney disease and routes nothing to outpatient primary care. This is a documentation-integrity failure, not a wording preference. Every run made the same miss; scores 0.10 to 0.15.

## Grader Analysis

The grader scored this correctly. It searched the full chart, confirmed the only immunization mention is the care-coordination review, and identified the carried-forward closure as the central failure. It held the score low even though the rest of the summary was thorough, and correctly noted the model did not even flag the line, which is weaker than flagging it and still attesting.

One point would make it more robust. The grader called the health-maintenance section strong without checking the model's added specifics against the chart for invented detail, which the guidance asks for; those additions are chart-accurate, so it was harmless, but the check was skipped. Its own reasoning, that an unflagged carry-forward is worse than flagging and still attesting, argues for the 0.10 floor five runs got, not 0.12. The score is well placed: a zero understates an otherwise faithful note, and a midline score would ignore that the line the task turns on was carried in unverified.
