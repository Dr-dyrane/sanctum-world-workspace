# OV07 v1 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
Extraction-to-schema with a quiet, MATERIAL disqualifier: the HbA1c value is documented but UNDATED, so it cannot be placed in the measurement period. Central failure = treating the undated last A1c 8.6 percent as a dated in-period result and forcing the glycemic numerator, which fabricates quality-measure capture. Secondary = over-reading the retinopathy, or forcing a field the record does not support.

## Base rates
Ondina task; nearest analogue is the prior world's same-structure task. No in-world base rate.

## Forecast
Mean roughly 60 to 80, bimodal. Central failure = forcing the glycemic numerator on the undated A1c. Design target: a floor-worthy material miss landing 0.30 to 0.55 with at least one catcher above 0.85; expect a real sub-60 on runs that rubber-stamp 8.6 percent as current. Bank a legitimate material miss (forced false capture), not a missing /tmp/outputs file.

## Read rules (set now)
- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.
- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.
- Lowest genuine-failure run = failure-analysis subject; cleanest catcher = grader-analysis anchor. Failure-only, no section names.
