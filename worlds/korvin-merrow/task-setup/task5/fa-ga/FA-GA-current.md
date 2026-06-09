# KM05 v4 FA and GA - CURRENT (POST-FIX re-pilot, job 0348a7dc)

Re-paired after Abi's fairness fix (mounted draft re-attributed the home BP to patient report in both the interval line and item 1). The FA/GA substance is unchanged from the pre-fix version because it already framed the BP as unverified patient report; only the job, spread, and run pairing refresh.

Spread (job 0348a7dc, read off the platform bar; one run not legible in the paste - confirm on Download Output): approx 20, 95, 88, 40, 68, 70, 20, 35, [?], 15. Mean ~50. Bimodal and fair: legitimate sub-40 floors (15, 20, 20, 35, 40) AND clean catchers (88, 95). The fairness fix traded a little depth (pre-fix mean 0.36) for defensible floors - a model that resumes held GDMT on self-reported BP now genuinely fails.

FA subject = single lowest run. The single lowest is 0.15; its transcript was not in hand, so this draft is byte-verified against Attempt 1 (run cfef56c9, 0.20), the floor transcript available, which is the same full-restart failure. If the 0.15 is identical (expected), swap only the run ID - the prose does not change. Catch anchor = Attempt 2 (run 2443d7e5, 0.95), which held all four agents and deferred the staged restart.

Format: two short prose paragraphs each, no bullets, no headers, no em dashes (Abi's format). GA describes the grader scoring the output against the golden and guidelines, not reading the chart. Physician owns, edits, signs. Do NOT enter until the "Start Failure Analysis & Grader Analysis" button is live.

## Failure Analysis (house format, verified vs the floor-run output bytes)

On the lowest run the model did thorough, careful work across a long verification pass. It kept metformin held pending confirmed renal recovery, continued carvedilol, asserted no numeric prednisone dose, kept inpatient correctional insulin out of the home regimen, held spironolactone and empagliflozin, and reviewed immunizations rather than asserting them current.

The failure is the central one the task targets. It resumed sacubitril/valsartan and furosemide at this primary-care visit, justified explicitly by the patient's reported home blood pressures, when the chart keeps every protective agent held and defers the staged restart to outpatient cardiology and nephrology. It treated the unverified home-BP readings as a basis for action and restarted held therapy the chart does not support.

## Grader Analysis (house format, mapped to grader Sections A/B/C, verified vs the floor-run grading transcript)

The grader scored the run against the golden and the guidelines and the score is correct. It credited the Section A restraint the run got right, metformin held, carvedilol continued, the absent prednisone number, and spironolactone and empagliflozin kept held, and under Section B did not dock the run's chart-true detail or its patient-reported framing of the home blood pressure.

The deduction falls on the central Section C pattern, the premature cardiorenal restart. The run resumed sacubitril/valsartan and furosemide on the unverified home-BP readings, against the chart's staged-restart-deferred plan. Placing it near the floor is proportionate and sym