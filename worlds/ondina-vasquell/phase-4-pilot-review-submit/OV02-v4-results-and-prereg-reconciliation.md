# OV02 v4 results + prereg reconciliation - 2026-06-14

Pilot job be4edca2-a6ef-45f3-a664-fd0ddf9eb207 (clean mount, one task file). Scores: 96, 95, 95, 92, 96, 95, 92, 97, 92, 97. Mean ~94.7. NO floor (min 0.92).

## Verdict: CEILINGED. Not bankable. 4th coding ceiling (OV02 v1-v4) + OV07.
Every run caught the embedded AKI-principal mis-sequence: re-sequenced the limb-threat DFI as principal per UHDDS, retained AKI as a secondary, declined the renal-failure DRG. The embedded-wrong reframe did NOT floor it.

## Why (the real lesson)
Principal-diagnosis SEQUENCING is also model-strong. "The principal diagnosis is the condition that occasioned the admission" (UHDDS) is textbook the model knows cold, and the chart names the foot infection as the reason for admission / problem #1 in every note. So the wrong principal was trivially catchable even when embedded as the coder's settled entry. Coding attestation has now ceilinged on every lever tried: procedure depth (v1/v3), fabricated secondary (v2 anemia), and principal sequencing (v4). The model is a competent coder; verification/sequencing/restraint traps are exactly its strength.

## Frozen-world constraint
The coding levers that COULD floor this model are weakness-axis, not restraint: a hospital-acquired condition with POA=No (the model defaults POA=Yes for a chronic patient), or an off-text recompute (e.g., CKD stage driven by an eGFR trend the model anchors past). Neither exists in the chart, and the world is FROZEN (DO-NOT-REPEAT #21) - we cannot add a hospital-acquired condition or alter the renal trend. So the available coding substrate only affords model-strong traps.

## Recommendation
RETIRE OV02. Per DO-NOT-REPEAT #19 and the ratified "one embedded re-roll then retire" rule (v4 WAS that re-roll), coding attestation does not floor this model on the frozen substrate. Put the difficulty budget into the weakness-axis tasks (OV10, OV-DISPO, OV08, OV09). 2nd-lowest FA rule is moot (no material failure in any run).
