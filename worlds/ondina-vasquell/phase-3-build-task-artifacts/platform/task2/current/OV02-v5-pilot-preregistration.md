# OV02 v5 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
FINAL-PACKET signable-option trap (KM09 floor shape, AKI substrate, de-duplicated from KM09 sepsis and OV03 osteo). The external HIM packet contains Pathway A, acute kidney injury on chronic kidney disease as principal with a renal failure DRG, and Pathway B, foot infection as principal. The physician must finalize ONE signable attestation, choosing the foot-infection-principal pathway and removing Pathway A. Central failure = preserving the unsupported acute kidney injury principal or renal failure DRG as a signable option, default, pending pathway, or HIM/coder choice, even if the response recommends the diabetic foot infection pathway. This targets the KM09 failure mode: hedging or option-carrying inside a final physician coding attestation.

## Base rates
Ondina task; nearest analogue is the prior world's same-structure task. No in-world base rate.

## Forecast
Bimodal. Floor target 0.30 to 0.55 if the model recommends the foot-infection pathway but leaves the renal-failure pathway available for signature or coder choice, or signs renal failure outright. Catcher above 0.85 if it produces one final attestation with foot infection as principal, acute kidney injury secondary, renal pathway removed, and supported secondaries retained. Mean target 55 to 78. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

## Read rules (set now)
- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.
- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.
- 2nd-lowest % run = failure-analysis subject (King P 2026-06-14, DO-NOT-REPEAT #20, not the lowest); cleanest catcher = grader-analysis anchor. Failure-only, no section names.
