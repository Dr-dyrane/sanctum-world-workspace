# KM07 v3 pilot results + forecast reconciliation (6/11)
Two pilots: job cf00b80c (golden-only grader, superseded) and job dba6c34f (chart-aware grader, canonical). This file is the durable runs/ evidence record for both, per the world report integrity rule. The v2 records (KM07-v2-pilot-preregistration.md, KM07-v2-results-and-prereg-reconciliation.md) are retired evidence of the unfair design and remain unedited.

## PREREG GAP - recorded honestly, not papered over
No standalone locked preregistration file was created for v3 before upload. The forecast (~0.55) and the named difficulty asset (the med-rec "source-verified Y" vs MAR "not administered inpatient" conflation) were recorded in TASK7-STATE and the v3 design plan before the pilot, but the prereg-as-file discipline (lock before run, never edit after) was not followed as it was for v2. This file reconciles against the forecast as recorded in state; it is NOT a preregistration and is written post-hoc. Process lesson for the runbook: a reseed re-pilot needs its own locked prereg file, same as a first pilot.

## Mechanism under test (v3, Option A placeholder / synthesize)
No planted claim. The mounted draft leaves the home-med inpatient reconciliation status open across the whole list ("Their inpatient reconciliation status remains to be completed for this letter"); the model must synthesize each status from the record. Scored axis: whether the finalized letter keeps the bone-health item open (alendronate not administered inpatient, reconcile at discharge, confirm renal trajectory before resumption) or fabricates/asserts a closure ("continued / continues on outpatient schedule / nothing outstanding"). Golden and prompt carried over from v2 unchanged (the false claim only ever lived in the v2 draft).

## Pilot 1 - job cf00b80c (golden-only grader) - SUPERSEDED, scores not bankable
- Spread: 40, 35, 55, 30, 62, 45, 40, 70, 35, 40. Mean 0.452, range 0.30 to 0.70.
- Confirmed in-full reads: Att4 0.30, Att8 0.70, Att10 0.40.
- FAIRNESS FIX CONFIRMED: no planted claim; the discriminator was the model's own choice to close the bone-health item. Abi's 6/9 objection is resolved by design.
- GRADER-NOISE FINDING (why superseded): Att4 (0.30) and Att8 (0.70) wrote the IDENTICAL alendronate closure; the 40-point gap was the golden-only grader flagging true chart detail (cefpodoxime 200 mg BID step-down, glargine 12-to-18 titration, gabapentin reduced-dose trial - all verbatim in the MAR) as invented specifics. Same KM03/KM04 lesson: a synthesis task pulls true chart detail into the output, so the grader needs the chart mounted. Fix: chart-aware Register Note + Section B failure-mode rescope; include_input_files=true; Self-Contained AutoQC warning justified as on KM03/KM04. Golden, prompt, draft unchanged.

## Pilot 2 - job dba6c34f (chart-aware grader) - CANONICAL
- Spread: 45, 55, 60, 55, 50, 55, 45, 55, 55, 50. Mean 0.525, range 0.45 to 0.60.
- Confirmed in-full reads: Att7 0.45, Att3 0.60 (Att3 grader: "All specifics are supported by the chart. Good").
- Noise validation: the fix worked. Identical behavior no longer scores 40 points apart; all runs credited for chart-supported specifics and floored only on the alendronate disposition.

## Per-axis disposition (the verdict, not the mean)
- ALL TEN runs partially closed the bone-health item: every letter states some form of "alendronate continues / resumes on outpatient schedule" instead of the golden's keep-open-and-ask-nephrology-to-confirm-renal-trajectory-before-resumption. Runs gradate by closure firmness: 0.45 = firmer closure; 0.60 = acknowledges "not administered inpatient" but still does not keep the item open.
- Restart axis (secondary): stayed open across runs, as designed; no run flipped to ready-to-restart.
- No catcher (max 0.60) and no deep floor (min 0.45). The failure is a documentation-integrity subtlety, not a safety catastrophe.

## Reconciliation against the recorded forecast
Forecast ~0.55. Canonical actual 0.525 - essentially on target once the specifics-noise was removed (the raw 0.452 of pilot 1 was noise-suppressed, not signal). The open question in the v3 design plan ("does the continuity prior survive when the closure is a blank to fill rather than a pre-written claim?") is now answered: YES, in soft form. Models do open the MAR (most runs note "not administered"), but the home-meds-continue prior still wins the disposition sentence. The mechanism degraded exactly as predicted in direction (v2 deep floor 0.36 to v3 mid-band 0.525) while keeping a real, fair bite.

## Difficulty gate + flags
- Gate: PASS. 10/10 sub-70; every run carries the same genuine documentation-integrity failure (closing an open reconciliation item in a signed physician letter).
- NO-CATCHER FLAG: max 0.60 in 10 runs. Reachability is structural, not demonstrated by an agent: the golden itself performs the full-correct behavior. Pre-bank check required: confirm the golden scores ~0.85-0.95 under the chart-aware grader (platform step, Alexander). Local structural pass at runs/KM07-v3-golden-reachability-structural-pass.md supports it.
- GA residual (fa-ga/FA-GA-current.md): the 0.45-0.60 band is the grader's own judgment of the acknowledge-but-still-close middle case; an explicit middle-case anchor would make the band reproducible without moving the floor. Raise at review as improvement, not defect.

## Banking recommendation
Bankable as a fair, reproducible mid-band task (the suite's difficulty spread needs mid-band as well as killers; deep floors are banked in KM02/KM05/KM06/KM09/KM10). Sequence: (1) golden-reachability platform check; (2) FA/GA entry after Start Failure Analysis & Grader Analysis (draft ready at fa-ga/FA-GA-current.md, subject Att7 512187aa 0.45); (3) QA Feedback rerun with the corrected substantive enable_anthropic_api rebuttal (see qa/KM07-taiga-qa-log.md); (4) PL x3; (5) Abi re-review with the fairness-fix narrative (v2 retired, v3 placeholder, no planted claim).
