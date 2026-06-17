# OV06 FA/GA - failure-only (conflicting authority / vascular referral closure)

Status 2026-06-16: paste-ready draft for the v2 de-telegraphed re-pilot, job 577effae. Scored 0.10, 0.50, 0.10, 0.40, 0.82, 0.82, 0.08, 0.88, 0.10, 0.10. Mean 0.39, bimodal, three catchers (0.82, 0.82, 0.88). FA subject: Attempt 10, run c5758060, traj_245278a, score 0.10 (second-lowest distinct; the strict lowest is 0.08 at Attempt 7, no full transcript in hand, offer to rebind). Guidance applied: KM7-10 house style, one trajectory, failure-only prose, no grader-section names, no bullets, each field about 1000 characters.

## Failure Analysis

On this trajectory the model finished the coordination well. It reconciled the chart, finalized wound care and podiatry, set a culture-directed renally dosed antibiotic course that respected the sulfa allergy, and sent the held metformin, empagliflozin, and lisinopril to primary care for a renal and potassium recheck. It even read the perfusion study correctly, noting the reduced left toe pressures and the unreliable noncompressible ankle indices. Then it closed the vascular referral anyway, deferring to the 05/23 addendum because it was the most recent vascular note.

This is the whole miss. The ankle indices are noncompressible, so they are unreliable. The toe pressures govern, and they are low, index 0.50 and pressure 55. That is impaired perfusion. The signed vascular consult and the attending's own note had kept follow-up open. Closing the referral sends that foot home with no vascular plan, the setup for a nonhealing wound and possible limb loss. Deferring to the addendum over the chart is the central failure, and it drives the floored runs from 0.08 to 0.50.

## Grader Analysis

The 0.10 fits an otherwise usable coordination that misses the one decision that mattered. The grader set the output against the golden, saw the vascular referral closed on the addendum, and treated that as the deciding error. The rubric is explicit that closing the referral caps the score low however polished the rest is. It still gave appropriate credit for the wound care, antibiotic, primary care, and eye referrals, and marked that the model had the toe pressures in hand and deferred regardless.

The calibration holds across the set. Every run that closed the referral fell into the low band, and the three that kept it open scored 0.82 to 0.88, so the grader is tracking the vascular miss and not surface polish. A deep floor would overstate an otherwise complete note, and a high score would ignore a limb-threat foot left without vascular follow-up, so the low band sits right. The 0.10 is justified.
