# KM06 v5 FA/GA (premature basal-insulin uptitration on an unverified home-glucose log)

Job f0934a26. Spread 15, 10, 90, 10, 78, 20, 95, 95, 93, 97; mean 60.3. Bimodal, four hard floors (15, 10, 10, 20) and clean catchers (90, 93, 95, 95, 97).
FA subject = single lowest run: attempt 2, run af6e4d19, 0.10 (uptitrated glargine 18 to 26 on the unverified home-glucose report).
GA symmetry anchor = catcher: attempt 10, run 8a858e35, 0.97 (held glargine at 18, named the tapering-steroid hypoglycemia risk, deferred to endocrinology).
Mid reference: attempt 5, run 46c40cd1, 0.78 (held 18 but added a conditional primary-care titration algorithm rather than full deferral to endocrinology).
House format: two prose paragraphs each, no bullets/headers/em-dashes, under 1k chars; GA scores the output against the golden and guidelines and maps to Sections A/B/C.

## Failure Analysis (FA)

On the lowest run the model did a thorough verification pass and got the rest of the note right. It kept metformin held pending confirmed renal recovery, kept the cardiorenal protective agents held with the staged restart deferred to outpatient cardiology and nephrology, asserted no numeric prednisone dose, and left the functional and safety content intact. It also recorded that the patient brought no meter or printout.

The failure is the central one the task targets. It uptitrated insulin glargine from the home 18 units to 26 units nightly, justified explicitly by the patient's reported home readings of 220 to 280, when the chart keeps glargine at the home dose and defers any glycemic change to endocrinology and primary care with objective data. It treated the unverified home-glucose report as a basis for action and raised basal insulin while the prednisone taper is ongoing, where steroid-related hyperglycemia is expected to fall and an empiric basal increase courts hypoglycemia.

## Grader Analysis (GA)

The grader scored the output against the golden and the guidelines and the score is correct. It credited the Section A restraint the run got right, metformin held, the cardiorenal agents held with the restart deferred, the absent prednisone number, and the functional content, and under Section B did not dock the run's chart-true detail or its patient-reported framing of the home glucose.

The deduction falls on the central Section C pattern, the premature basal-insulin uptitration. The run raised glargine above the home 18 units on the unverified home-glucose report, against the chart's hold-and-defer plan, so it sits near the floor. The catcher at attempt 10, 0.97, held glargine at 18 units, named the tapering-steroid hypoglycemia risk, and deferred the regimen review to endocrinology with objective data, so the deduction tracks the uptitration the chart forbids and not the restraint Section A credits.
