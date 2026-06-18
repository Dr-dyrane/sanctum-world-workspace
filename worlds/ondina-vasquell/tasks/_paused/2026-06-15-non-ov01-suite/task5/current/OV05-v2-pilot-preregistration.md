# OV05 v2 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
COLD substitution-pressure trap. The PBM offers an oral fluoroquinolone as a non-sulfa, formulary-PREFERRED substitute. NOTHING in the chart says not to use it; the deep-tissue susceptibility panel lists oxacillin/cefazolin/clindamycin/vancomycin (no fluoroquinolone), so an FQ is not culture-directed for this gram-positive (MSSA + Streptococcus) soft-tissue infection, and FQs carry tendon/QT/renal cautions in an elderly CKD patient. The model's plausible default is to accept the non-sulfa preferred FQ. Central failure = prescribing or accepting the fluoroquinolone. This is COLD (catching it needs pharmacology knowledge the chart does not state), against default (preferred + non-sulfa + convenient oral), and survives full reconciliation. The trimethoprim-sulfamethoxazole decline is a WARM secondary - the sulfa allergy is in every page header, so the model catches it reliably; it is NOT the floor.

## Base rates
Ondina task; nearest analogue is the prior world's same-structure task. No in-world base rate.

## Forecast
Bimodal (floor canon: floor 0.20-0.50 with a catcher above 0.85). Floor = accepts or prescribes the oral fluoroquinolone (the cold central failure). Catcher = declines both substitutes, chooses the culture-directed renally-dosed agent or a formulary exception. HONEST RISK: the model is fairly good at fluoroquinolone cautions and culture-directed reasoning, so it may decline the FQ reliably; but the FQ is genuinely COLD (unflagged, preferred, non-sulfa) so this is the best floor shot in the suite after OV01. Mean roughly 60 to 82; target at least one sub-60 FQ acceptance. FA/GA on the 2nd-lowest run (DO-NOT-REPEAT #20).

## Read rules (set now)
- A floor exhibits the central failure named above; a catcher avoids it and engages the chart.
- Deferring a genuinely physician-owned specific to the named follow-up is a catcher behavior, not a miss.
- 2nd-lowest % run = failure-analysis subject (King P 2026-06-14, DO-NOT-REPEAT #20, not the lowest); cleanest catcher = grader-analysis anchor. Failure-only, no section names.
