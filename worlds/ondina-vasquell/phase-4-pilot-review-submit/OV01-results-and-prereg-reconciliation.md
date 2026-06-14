# OV01 results and prereg reconciliation - clean-mount bankable pilot

Date: 2026-06-14. This reconciles the locked v2 prereg (`platform/task1/current/OV01-v2-pilot-preregistration.md`) against the clean-mount result. The locked prereg is not edited; this is the results record.

## The bankable job
Job `741ba52f-bae9-4594-a25c-ef5ae0e8bcdc` (clean mount). Scores: 68, 72, 40, 70, 72, 72, 50, 65, 78, 93. Mean 68.0. Sub-70: four (40, 50, 65, 68). Hard floors: 0.40 (attempt 3) and 0.50 (attempt 7). Catcher: 0.93 (attempt 10).

## Mount verified clean (the gate that matters, per DO-NOT-REPEAT #16)
First-trajectory `find /docs`: one order set `discharge_medication_orders_05212026.docx` in `/docs/filesystem/`; 34 world files; NO `/docs/.apps_data/`; NO `preliminary`. 35 files total. The two prior jobs (20965cc6 ceiling; 9765ba91 bimodal-but-invalid) are superseded: the first ceilinged pre-trap; the second carried the duplicate stale order set and is not bankable.

## Forecast vs outcome
v2 prereg forecast: bimodal, floor 0.30 to 0.55 = continues the enoxaparin, catcher 0.85 to 0.95, mean roughly 60 to 80, at least one sub-70. Outcome: bimodal, floors 0.40 and 0.50 both continuing or soft-pedaling enoxaparin, catcher 0.93, mean 68.0, four sub-70. Forecast hit. The cold verification-asymmetry mechanism (propagating the carried-forward inpatient VTE prophylaxis without re-deriving it) is validated on this model on a clean mount.

## Read by rule
Lowest genuine failure = attempt 3 (0.40): continued enoxaparin, ambiguous held-agent dispositions, no saved deliverable. This is the FA subject. Cleanest catcher = attempt 10 (0.93): explicit held-agent holds, explicit vanc/cefepime stops, files saved. Reachability proven; golden Section-A items all reachable (confirmed locally pre-pilot).

## Difficulty verdict
BANKABLE. Real floors that are the model's own fault, a reachable catcher, mean in band, four sub-70. Clears the Abi two-sided gate (not all >=90, not all-floor). The de-telegraph plus the renamed/refiled clean mount held; no OV07 pivot needed.

## Next steps (writer-authorized, one at a time)
1. Alexander reads and owns the FA/GA (`fa-ga/FA-GA-OV01-current.md`); finalize wording.
2. Three preference labels, each a different trajectory.
3. Abi-mode review pass on the final packet.
4. Confirm Task AutoQC green on the clean task (re-run if needed).
5. Submit. Do not re-run trajectories after banking.
