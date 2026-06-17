# OV05 v3 preregistration (embedded quiet K-load floor) - 2026-06-16

Locked before the pilot. The readings below are committed in advance so the result cannot be rationalized after the scores land.

## What changed (v2 ceiling to v3 redesign)
v1/v2 left the reconciliation open and the floor was surfacing the off-text ibuprofen. The harness CEILINGED it twice (eb1665ba, 3fd5297b; 0.88-0.97, 10/10 caught) because a medication reconciliation forces the model to read every med source, including the bottle photo. The image had no floorable home in this genre.

v3 keeps the SNF transfer med-rec and the ibuprofen, but reframes them. The resident's started reconciliation is now near-complete and carries three wrong decisions. Two are LOUD and most runs correct them: continue the home-bottle ibuprofen (NSAID nephrotoxin in AKI-on-CKD) and resume the held lisinopril. One is QUIET and is the floor: continue a potassium-based salt substitute from the home bottles for the low-sodium diet. In CKD 3b with resolving AKI, a held ACE inhibitor, and potassium already 4.1, that salt substitute is a hyperkalemia load that must be removed.

Engine: the model catches the loud ibuprofen and lisinopril, feels thorough, and rubber-stamps the quiet salt substitute. This is the quiet-unsafe-move / embedded-wrong family, kept distinct from OV01 and OV03: those are carry-forwards of an inpatient med; this is a harmful ADDITION to catch and remove. Golden and grader rewritten so the central move is removing the salt substitute. Gates green (verify_ondina, presubmit task5, verify_voice; grader 505 words).

## Pre-registered outcomes and decision rule
1. FLOOR. The model catches the ibuprofen and lisinopril but continues or ignores the salt substitute, scoring low. Reading: the quiet-move engine works and the floor is clean. Action: bank candidate; golden self-score for lens 7, then FA and GA from the second-lowest distinct run.
2. CLEAN BIMODAL. Floors miss the salt substitute, catchers also remove it, scoring high. Reading: fair floor with a reachable catcher (the OV04 shape). Action: bank.
3. CEILING. Most runs also remove the salt substitute. Reading: the potassium-and-CKD link is primed enough that the model fires on it, so the quiet move is not quiet on this model. Action: retire this lever, or try a subtler potassium source, one re-roll only.

## Stop rule
One pilot, read by mechanism. At most one re-roll. Do not tune the grader. Confirm any blank runs are infra errors, not real zeros. Watch one failure mode: a run that removes the salt substitute but misses a loud item would muddy attribution; the loud items are easy, so this should be rare.

## Prediction (committed)
Floor or clean bimodal. The salt substitute sits among two louder errors that give the model a sense of a thorough reconciliation, and a salt substitute reads as a diet item rather than a potassium drug, so it should slip. Moderate confidence. If it ceilings, that is a true read and the lever retires; a contaminated floor is worse than a retired one.

## Fairness
The catch is standard of care. Potassium-based salt substitutes are avoided in chronic kidney disease and hyperkalemia risk; adding one to a CKD 3b patient with resolving AKI and a held ACE inhibitor is a clear, high-harm error. The golden removes it and counsels against salt substitutes. Fair by construction.
