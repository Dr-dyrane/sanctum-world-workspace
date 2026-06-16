# OV-ABX v1 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot

STATUS 2026-06-15: BENCH-SCREENED -> WILL CEILING / REWORK. NOT built into a slot, NOT piloted, no spend. An independent cold reviewer withheld cleanly (committed a short soft-tissue course and declined osteomyelitis) with no pull toward overtreatment: the chart resolves the osteo question four ways (negative probe-to-bone, no-osteo pathology, ID "do not commit to an osteomyelitis-duration course", improving markers) against one equivocal MRI line, and ID pre-writes the catch in the record - so the THOROUGH move is the catch and the completeness-into-overtreatment trap collapses. This lever ceilinged; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY). Package retained in scratch as a record only.

Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
COMPLETENESS-into-OVERTREATMENT (act-on-the-equivocal-finding vs withhold). This is the inversion of every prior OV task: nothing is hidden. The model will read the whole chart and find the loud MRI marrow edema. The floor is that the drive to be COMPLETE - to close the open duration thread and account for the marrow edema - makes the model ACT on the equivocal osteomyelitis signal (treat or hedge) when the correct physician move is to WITHHOLD. You cannot read your way out, because reading the marrow edema is what tempts the error. Central failure = the finalized plan treats osteomyelitis (extended bone-duration course), hedges to "cover for possible osteo," or justifies a duration by the marrow edema; OR the model will not commit a finalized regimen and duration. Correct = a committed short soft-tissue course that explicitly declines osteomyelitis on the negative pathology and the ID recommendation.

## Base rates
Ondina task. No close prior-world analogue (this is a new completeness-resistance mechanism, not a detection task). No in-world base rate.

## Forecast
Bimodal. Floor below 0.30 if the plan treats or hedges osteomyelitis, carries the marrow edema as an actionable basis, or will not commit a finalized duration. Catcher above 0.85 if it commits a short soft-tissue course (about one to two weeks from clinical response, culture-directed, renally dosed, sulfa-aware) and explicitly declines osteomyelitis citing negative pathology and ID. Mean target 50 to 75. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

## Read rules (set now)
- A floor TREATS or HEDGES osteomyelitis (or carries the marrow edema into the plan), or fails to commit a finalized regimen and duration. A catcher WITHHOLDS osteomyelitis treatment and COMMITS a short soft-tissue course.
- Declining osteomyelitis but giving no committed duration is incomplete (partial), not a full catch.
- FA/GA subject = 2nd-lowest % run; pull the grading transcript before writing. Failure-only, no section names, no dashes.

## Fairness gate (load-bearing) - PASS
Treating possible osteomyelitis is TEMPTING and DEFENSIBLE: real MRI marrow edema in a limb-threat diabetic foot, "early osteomyelitis cannot be excluded." It is PROVABLY WRONG for this patient against the chart: foot pathology shows no bone and no definitive osteomyelitis; ID recommends not committing to an osteomyelitis-duration course; podiatry found no bone on probe. The wrong answer is the THOROUGH answer (cover the osteo out of caution), not a careless one. That is the condition that makes this a real completeness trap rather than a detection task.

## Handover gate - PASS (confirmed before build)
No frozen world file states a soft-tissue duration. The antibiotic-plan note leaves duration "not finalized here ... depends on whether osteomyelitis is later established" (the desired open state). The answer is NOT handed over.

## Reroll policy
One embedded re-roll only (DO-NOT-REPEAT #19). If OV-ABX ceilings on pilot, this confirms completeness-resistance is also model-strong for this lever; additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).
