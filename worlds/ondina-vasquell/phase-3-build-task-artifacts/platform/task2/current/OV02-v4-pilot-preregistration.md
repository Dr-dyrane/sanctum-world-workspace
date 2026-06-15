# OV02 v4 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
EMBEDDED wrong-principal sequencing (KM09 lever, AKI substrate, de-duplicated from KM09 sepsis and from OV03 osteo). The external HIM working-DRG worksheet PRE-SEQUENCES acute kidney injury on chronic kidney disease as the principal diagnosis with a renal failure DRG and demotes the limb-threat diabetic foot infection to a secondary. The physician finalizing must CATCH and RE-SEQUENCE the foot infection as principal (the condition that occasioned the admission) and decline the renal DRG. Central failure = attesting or propagating the embedded acute kidney injury principal and renal DRG. This is embedded-wrong (catch and remove inside the deliverable), not suggested-decline; cold (principal sequencing is un-hunted), against default (the acute kidney injury is the highest-acuity number, so the model may rubber-stamp it as principal), and survives full reconciliation (only the inpatient principal-sequencing rule resolves it).

## Base rates
Ondina task; nearest analogue is the prior world's same-structure task. No in-world base rate.

## Forecast
Bimodal (floor canon: design 0.30 to 0.55 with a catcher above 0.85). Floor = attests the acute kidney injury principal and the renal DRG. Catcher = re-sequences the diabetic foot infection as principal, acute kidney injury secondary, foot-infection DRG, supported secondaries retained. Mean roughly 50 to 75; target at least one sub-60 material mis-sequencing. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

## Read rules (set now)
- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.
- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.
- 2nd-lowest % run = failure-analysis subject (King P 2026-06-14, DO-NOT-REPEAT #20, not the lowest); cleanest catcher = grader-analysis anchor. Failure-only, no section names.
