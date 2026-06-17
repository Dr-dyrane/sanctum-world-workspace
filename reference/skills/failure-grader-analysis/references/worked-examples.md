# Worked FA/GA examples

Two examples of the same shape on different tasks. Read these when a draft feels
off-format or you are unsure how much detail to carry. Both are failure-only, two
paragraphs each, about 1000 characters, in Alexander voice.

## Example 1: OV03 discharge insulin (gate-clean; FA shape PARTLY SUPERSEDED)

Note (2026-06-16): this example's FA opens with a competent-baseline paragraph ("the model completed the discharge medication plan competently. It reconciled..."). Pod lead Ahmad cut that for the OV world: the FA is now FAILURE-ONLY (see SKILL.md). Keep this example's GA shape and clinical voice; in the FA, drop the baseline paragraph, lead with the failure, and carry more detail on the consequences.

The lever: the started draft pre-fills the inpatient insulin in the home list as
continue; the golden discontinues the mealtime sliding scale for home. The model
floored on every run by carrying it forward. This is the exemplar to match.

What it shows: paragraph one leads with the competent baseline then the one central
failure; paragraph two carries the clinical mechanism, the secondary errors, and
the across-trajectory line a reviewer asks for. The GA walks how the grader reached
the score, then the calibration close.

Status 2026-06-16: paste-ready draft for the v2 re-pilot, job 048aa8eb. Scored
0.12, 0.10, 0.15, 0.20, 0.05, 0.20, 0.10, 0.15, 0.15, 0.10. Mean about 0.13, all
ten low, no catcher. FA subject: Attempt 1, run 1332c3b6, traj_8585aac, score 0.12
(lowest run with a full transcript in hand; rebind to a 0.05 or 0.10 run if strict
second-lowest-distinct binding is required).

Failure Analysis

On trajectory 1, the model completed the discharge medication plan competently. It
reconciled the home medications, framed the soft-tissue foot infection correctly,
kept the held agents in view, and documented offloading and follow up. The failure
is the discharge insulin. The started draft pre-filled the inpatient regimen,
glargine 26 units and a mealtime aspart sliding scale, both marked continue. The
model carried both home unchanged and repeated the sliding scale in the patient
instructions.

A mealtime sliding scale is an inpatient tool, and the golden stops it for home:
this patient lives alone, eats variably, and has falling insulin needs as the
infection resolves, so a home scale is a hypoglycemia hazard. The model added no
hypoglycemia precautions, named an antibiotic that Infectious Disease had deferred,
and restarted lisinopril and metformin before renal recovery. The inpatient insulin
carry-forward is the central failure pattern, and it drives the low band across all
ten runs, 0.05 to 0.20.

Grader Analysis

The 0.12 is appropriate for an otherwise usable plan that misses the central insulin
decision. The grader compared the output to the golden, found the inpatient sliding
scale carried into both the discharge medications and the patient instructions, and
made that the deciding error. It applied the rubric instruction that carrying the
inpatient insulin home caps the score low however complete the rest is. It flagged
the unsupported cephalexin and the early restart of the held agents, and gave
appropriate credit for the accurate infection management, reconciliation, and follow
up.

The same calibration holds across the run set. Every trajectory that sent the scale
home landed in the low band, which shows the grader is keying on the safety miss and
not surface quality. A deep floor would overstate an otherwise complete plan, and a
high score would ignore a hypoglycemia hazard sent home to a patient who lives
alone, so the low band is well placed. The 0.12 is justified.

## Example 2: KM7 nephrology referral (same shape, different task)

The lever: a held bone-health agent (alendronate) was not given inpatient and the
golden keeps it open for nephrology review; the model instead continues it on its
home schedule, turning a specialist question into routine continuation. Same shape
as OV03: complete deliverable, one central reconciliation miss.

Note: KM7 predates the current both-sides rule and wrote "it also appropriately
credited the correct renal course." Under the present gate that phrase trips the
both-sides check; reword to "it also noted the correct renal course." Everything
else is the standard to copy.

Failure Analysis

On trajectory 10, the model produced a nephrology referral letter that was not
adequate for the central medication-reconciliation purpose of the task. It correctly
framed the AKI on CKD course, preserved the staged restart question for the
cardiorenal and diabetes agents, and did not invent a prednisone dose. It also found
the alendronate detail and correctly noted it was not administered in the hospital.
The failure is that it then says alendronate continues on its Sunday schedule at
home, grouping it with routine medications rather than leaving it open for
nephrology.

The MAR says alendronate was not administered inpatient and should be reconciled at
discharge, and the golden asks nephrology to confirm renal trajectory before
resumption after AKI on CKD. This turns a required specialist question into routine
continuation, which is the central failure pattern, and it is what places the run in
the low band.

Grader Analysis

The 0.40 is appropriate for an otherwise usable referral that misses the central
bone-health reconciliation item. The grader recognized that the letter did not keep
alendronate open the way the golden does, despite the preserved restart framing for
the other held agents. It also noted the correct renal course, the one to two week
nephrology follow up, and the absence of unsupported prednisone dosing.

The calibration is sound. "Not administered inpatient" does not rescue the answer
once the letter says alendronate continues on its home schedule, because the record
requires nephrology confirmation before resumption. A deep floor would overstate an
otherwise good letter, and a high score would ignore a closure the golden leaves
open, so the mid-band 0.40 is well placed.
