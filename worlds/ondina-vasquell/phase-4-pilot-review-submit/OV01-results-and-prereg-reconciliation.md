# OV01 results and prereg reconciliation - clean-mount bankable pilot

Date: 2026-06-14. This reconciles the locked v2 prereg (`platform/task1/current/OV01-v2-pilot-preregistration.md`) against the clean-mount result. The locked prereg is not edited; this is the results record.

## The bankable job
Job `741ba52f-bae9-4594-a25c-ef5ae0e8bcdc` (clean mount). Scores: 68, 72, 40, 70, 72, 72, 50, 65, 78, 93. Mean 68.0. Sub-70: four (40, 50, 65, 68). Hard floors: 0.40 (attempt 3) and 0.50 (attempt 7). Catcher: 0.93 (attempt 10).

## Mount verified clean (the gate that matters, per DO-NOT-REPEAT #16)
First-trajectory `find /docs`: one order set `discharge_medication_orders_05212026.docx` in `/docs/filesystem/`; 34 world files; NO `/docs/.apps_data/`; NO `preliminary`. 35 files total. The two prior jobs (20965cc6 ceiling; 9765ba91 bimodal-but-invalid) are superseded: the first ceilinged pre-trap; the second carried the duplicate stale order set and is not bankable.

## Forecast vs outcome
v2 prereg forecast: bimodal, floor 0.30 to 0.55 = continues the enoxaparin, catcher 0.85 to 0.95, mean roughly 60 to 80, at least one sub-70. Outcome: bimodal, floors 0.40 and 0.50 both continuing or soft-pedaling enoxaparin, catcher 0.93, mean 68.0, four sub-70. Forecast hit. The cold verification-asymmetry mechanism (propagating the carried-forward inpatient VTE prophylaxis without re-deriving it) is validated on this model on a clean mount.

## Read by rule
King P's 2026-06-14 rule changed FA/GA subject selection to the second-lowest run, not the lowest. For the original clean job `741ba52f`, that would have been Attempt 7, score 0.50, run `b105b942`; Studio exports attached 2026-06-15 confirmed it had visible saved output. That read is now superseded by Larry E's review return and Alexander's post-cleanup rerun below. The old Attempt 3 score 0.40 analysis and the interim Attempt 7 text are historical only and must not be pasted into the live FA/GA box.

Cleanest catcher = attempt 10 (0.93): explicit held-agent holds, explicit vanc/cefepime stops, files saved. Reachability proven; golden Section-A items all reachable (confirmed locally pre-pilot).

## Review-return rerun, 2026-06-15
Larry E returned OV01 for two fixable issues: grader wording that looked like platform language and FA/GA being tied to the wrong run-selection process. The grader wording was scrubbed locally. Alexander then reran trajectories. Current FA/GA evidence is job `aa949641-e849-4d84-8a60-4d4642eb61ed`, Attempt 6, run `28a61869-fdee-465f-a59a-ca65cf8f4bd0`, score 0.50. Attempt 6 has visible saved output at `/tmp/outputs/Vasquell_discharge_med_review.md`. The failure is the same banked enoxaparin miss: the output leaves enoxaparin as a confirmation item, asks for home injection planning, and describes the shot in patient instructions instead of stopping inpatient-only prophylaxis at discharge.

Current paste rule: select Attempt 6 in Studio and confirm the FA/GA text box is bound to run `28a61869`. The Attempt 7 text from job `741ba52f` is now superseded and should not be pasted.

## Difficulty verdict
BANKABLE. Real floors that are the model's own fault, a reachable catcher, mean in band, four sub-70. Clears the Abi two-sided gate (not all >=90, not all-floor). The de-telegraph plus the renamed/refiled clean mount held; no OV07 pivot needed.

## Next steps (writer-authorized, one at a time)
1. Alexander selects Attempt 6 in Studio and confirms the FA/GA text box is associated with run `28a61869`.
2. Paste the corrected FA/GA for Attempt 6 only.
3. Three preference labels, each a different trajectory.
4. Abi-mode review pass on the final packet.
5. Confirm Task AutoQC green on the clean task if the platform requires it.
6. Submit. Do not re-run trajectories after banking unless a reviewer specifically requires it.
