# KM07 v3 pilot results + forecast reconciliation (6/11) - RETIRED EVIDENCE
Status 2026-06-11 PM: RETIRED as unfair after AO's second review. The chart-aware pilot remains useful for grader-noise and partial-placeholder lessons, but its banking recommendation is void. The built v3 draft still listed alendronate under current medications beside a held list, so runs were ratifying a same-author planted assertion rather than freely synthesizing the item from the chart.

Two pilots: job cf00b80c (golden-only grader, superseded) and job dba6c34f (chart-aware grader, retired evidence). This file is the durable runs/ evidence record for both, per the world report integrity rule. The v2 records (KM07-v2-pilot-preregistration.md, KM07-v2-results-and-prereg-reconciliation.md) are retired evidence of the unfair design and remain unedited.

## PREREG GAP - recorded honestly, not papered over
No standalone locked preregistration file was created for v3 before upload. The forecast (~0.55) and the named difficulty asset (the med-rec "source-verified Y" vs MAR "not administered inpatient" conflation) were recorded in TASK7-STATE and the v3 design plan before the pilot, but the prereg-as-file discipline (lock before run, never edit after) was not followed as it was for v2. This file reconciles against the forecast as recorded in state; it is NOT a preregistration and is written post-hoc. Process lesson for the runbook: a reseed re-pilot needs its own locked prereg file, same as a first pilot.

## Mechanism under test (v3, Option A placeholder / synthesize)
No planted claim. The mounted draft leaves the home-med inpatient reconciliation status open across the whole list ("Their inpatient reconciliation status remains to be completed for this letter"); the model must synthesize each status from the record. Scored axis: whether the finalized letter keeps the bone-health item open (alendronate not administered inpatient, reconcile at discharge, confirm renal trajectory before resumption) or fabricates/asserts a closure ("continued / continues on outpatient schedule / nothing outstanding"). Golden and prompt carried over from v2 unchanged (the false claim only ever lived in the v2 draft).

## Pilot 1 - job cf00b80c (golden-only grader) - SUPERSEDED, scores not bankable
- Spread: 40, 35, 55, 30, 62, 45, 40, 70, 35, 40. Mean 0.452, range 0.30 to 0.70.
- Confirmed in-full reads: Att4 0.30, Att8 0.70, Att10 0.40.
- OLD READ, NOW WRONG: this was initially called fair because the design plan described a placeholder. AO's later byte-level review showed the built draft still asserted alendronate as a current medication, so this fairness conclusion is retired.
- GRADER-NOISE FINDING (why superseded): Att4 (0.30) and Att8 (0.70) wrote the IDENTICAL alendronate closure; the 40-point gap was the golden-only grader flagging true chart detail (cefpodoxime 200 mg BID step-down, glargine 12-to-18 titration, gabapentin reduced-dose trial - all verbatim in the MAR) as invented specifics. Same KM03/KM04 lesson: a synthesis task pulls true chart detail into the output, so the grader needs the chart mounted. Fix: chart-aware Register Note + Section B failure-mode rescope; include_input_files=true; Self-Contained AutoQC warning justified as on KM03/KM04. Golden, prompt, draft unchanged.

## Pilot 2 - job dba6c34f (chart-aware grader) - RETIRED EVIDENCE
- Spread: 45, 55, 60, 55, 50, 55, 45, 55, 55, 50. Mean 0.525, range 0.45 to 0.60.
- Confirmed in-full reads: Att7 0.45, Att3 0.60 (Att3 grader: "All specifics are supported by the chart. Good").
- Noise validation: the fix worked. Identical behavior no longer scores 40 points apart; all runs credited for chart-supported specifics and floored only on the alendronate disposition.

## Per-axis disposition (the verdict, not the mean)
- ALL TEN runs partially closed the bone-health item: every letter states some form of "alendronate continues / resumes on outpatient schedule" instead of the golden's keep-open-and-ask-nephrology-to-confirm-renal-trajectory-before-resumption. Runs gradate by closure firmness: 0.45 = firmer closure; 0.60 = acknowledges "not administered inpatient" but still does not keep the item open.
- Restart axis (secondary): stayed open across runs, as designed; no run flipped to ready-to-restart.
- No catcher (max 0.60) and no deep floor (min 0.45). The failure is a documentation-integrity subtlety, not a safety catastrophe.

## Reconciliation against the recorded forecast
Forecast ~0.55. Canonical actual 0.525 - essentially on target once the specifics-noise was removed (the raw 0.452 of pilot 1 was noise-suppressed, not signal). The open question in the v3 design plan ("does the continuity prior survive when the closure is a blank to fill rather than a pre-written claim?") is now answered: YES, in soft form. Models do open the MAR (most runs note "not administered"), but the home-meds-continue prior still wins the disposition sentence. The mechanism degraded exactly as predicted in direction (v2 deep floor 0.36 to v3 mid-band 0.525) while keeping a real, fair bite.

## Difficulty gate + flags - superseded
- Gate verdict void. The numerical spread is not bankable because the construction was later ruled unfair on the built bytes.
- NO-CATCHER FLAG remains useful as a warning: max 0.60 in 10 runs, and the golden self-score was never run. Current v4 must prove reachability by catcher or golden self-score before any banking.
- GA residual (fa-ga/FA-GA-current.md): the 0.45 to 0.60 band is historical grader evidence only; do not enter the v3 FA/GA.

## Retired banking recommendation
The prior recommendation to bank v3 was wrong. Correct sequence is v4 only: read-and-own the built packet, lock a fresh v4 preregistration, run the authorized pilot, prove reachability, then draft any FA/GA from the v4 result.
