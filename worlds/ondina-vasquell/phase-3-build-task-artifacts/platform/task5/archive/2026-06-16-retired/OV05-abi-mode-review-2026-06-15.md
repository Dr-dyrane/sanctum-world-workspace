# Abi-mode review: OV05 v1 packet - 2026-06-15 (run against the BUILT bytes, not the plan)
Scope read cold: prompt-OV05.txt, medication_reconciliation_snf_transfer_draft_05242026.docx, transfer_day_nursing_note_05242026.docx, golden-OV05-v1.docx, grader-guidelines-OV05.txt, home_medication_bottles_05242026.jpg (image passes its spec: legible IBUPROFEN, others texture).
Posture: read the prompt + draft from the model's seat before opening golden/grader. Local-only file (not uploaded).
VERDICT: PASS. No blocking findings.

## Lens 1 + 1a - Model's-seat fairness / built-artifact rule (the OV04 class, the reason for this review)
PASS. Extracted the draft's verbatim lines about the scored item:
- Only NSAID line: "Acetaminophen 650 mg oral three times daily as needed (knee osteoarthritis; NSAIDs avoided given chronic kidney disease)." This is a TRUE statement of the care plan (the team avoids prescribing NSAIDs), NOT a pre-asserted "the patient takes no NSAIDs."
- The two scored sections - "RECONCILIATION: DISCREPANCIES AND MEDICATIONS TO STOP" and "ATTENDING VERIFICATION" - are both "To be completed" TRUE PLACEHOLDERS, not a pre-asserted "no discrepancies."
So there is NO planted false claim the model must correct under a finish-only prompt. This is NOT the OV04-v1 propagation pattern; fairness comes from the placeholder + an off-text finding the model integrates (the home-med-bottle photo). Gate 0 (AO 6/11) satisfied by construction; the plain prompt is fair.
NOTE (difficulty, not fairness): the "NSAIDs avoided given CKD" annotation mildly primes the NSAID concept. It does not telegraph the unlisted ibuprofen or point to the photo, and the floor still rides on whether the model opens the image, but it could nudge the catch rate up. If the pilot ceilings, quiet that line first.

## Lens 2 - Genre purpose
PASS. A medication reconciliation exists to cross-check the documented list against what the patient actually takes; integrating the brought-in bottles is the instrument's purpose, not a gotcha.

## Lens 5 - Structural realism
PASS. DOS 05/24/2026: after the 05/21 HD6 snapshot, before today (06/15), pre-July-2025 is a soft preference only. Realistic SNF-transfer med-rec form; daughter-brought-bottles + a chart photo is true to practice.

## Lens 6 - Grader
PASS. Chart-aware Register Note ("verify any drug, dose, date, lab, or name against the mounted chart"); five-block; names golden-OV05-v1.docx in the Preamble; Section B verbatim two-failure-mode clause; Section C verbatim opener + credit-correct-restraint; 540 words (<=540). Does not penalize what the golden does; credits the catch in any form (Section B). Grader scores the response text vs the known finding and does not need to read the image (de-risks grader vision).

## Lens 7 - Difficulty / reachable catcher
Cold design-bench = plausibly bimodal (off-text image, OV04-v3 proven engine: floors do not open the photo, catchers do). Reachable by construction (the IBUPROFEN label is legible). CONFIRM on the pilot by reading a catcher transcript (Abi: read a catcher, not just the mean).

## Lenses 8/9 + mechanical pass
Plain prompt, 32 words, no meta-guidance (presubmit clean). 3-file mount with a first-trajectory find /docs gate in RUN-INSTRUCTIONS. A0.5 on file. Banned chars none, metadata scrubbed, template parity, no synthetic/prior-world tokens (verify_ondina green). Prereg locked. FA/GA to be drawn from the 2nd-lowest distinct run after the pilot.

## Residual to watch
Difficulty only: the NSAID annotation could compress the floor. Read the pilot by mechanism (floor = never opened the photo; catcher = opened it and stopped the ibuprofen), not just the mean.
