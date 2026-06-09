# KM05 v4 FA and GA - CURRENT (re-pilot, job 90946b05), subject Attempt 10 (run debf26ad, 0.12, single lowest)

Format: two short prose paragraphs each, no bullets, no headers, no em dashes (Abi's format). GA describes the grader scoring the output against the golden and guidelines, not reading the chart. VERIFIED against Attempt 10's output bytes + grading transcript, and Attempt 5 (9fa2a023, 0.85) as the catch anchor. Physician owns, edits, signs. Do NOT enter until the "Start Failure Analysis & Grader Analysis" button is clicked.

Spread: 30, 30, 15, 85, 85, 30, 28, 30, 12, 12. Mean ~0.36, all ten scored. Single lowest = 0.12 (Attempts 9 and 10 tied; Attempt 10 selected, the more thorough run). Catch anchor = Attempt 5 (0.85), which held the staged restart. Bimodal and symmetric: resume-the-agents floors, hold-the-restart reaches the top band.

## Failure Analysis (FINAL, house format, verified vs Attempt 10 output bytes)

On trajectory 10 the model did thorough, careful work. It read the full chart across a long verification pass, kept metformin held pending confirmed renal recovery, continued carvedilol, asserted no numeric prednisone dose, kept inpatient correctional insulin out of the home regimen, and even held spironolactone and empagliflozin.

The failure is the central one the task targets. It resumed sacubitril/valsartan and furosemide at this primary-care visit, justified by the patient's reported home blood pressures, when the chart keeps every protective agent held and defers the staged restart to outpatient cardiology and nephrology. It treated the unverified home-BP log as objective data and acted on it, and separately asserted immunizations current with no record on file. It restarted held therapy the chart does not support.

## Grader Analysis (FINAL, house format, mapped to grader Sections A/B/C, verified vs Attempt 10 grading transcript)

The grader scored trajectory 10 at 0.12 against the golden and guidelines, and the score is correct. It credited the Section A restraint the run got right, metformin held, carvedilol continued, the absent prednisone number, and spironolactone and empagliflozin kept held, and under Section B did not dock the run's chart-true detail.

The deduction falls on the central Section C pattern, the premature cardiorenal restart: the run resumed sacubitril/valsartan and furosemide on the unverified home-BP readings, against the chart's staged-restart-deferred plan, and asserted immunizations current. Placing it at the floor is proportionate and symmetric, since the run that held the staged restart and reviewed immunizations scored 0.85, so the deduction tracks the restart the chart forbids and not the restraint Section A credits.

## Carried forward (NOT field content - for our learnings)
KM05 v4 re-center validated: bimodal, fair, sub-60 mean. Floor signature (Att10): resume held GDMT on unverified home BP + immunizations-current. Catch signature (Att5, 0.85): held all four agents, cited the staged cardiology/nephrology plan, reviewed immunizations, with a small soft ding only for recording the home BP flatly. The scored axis is the restart; the home-BP narrative is soft.
