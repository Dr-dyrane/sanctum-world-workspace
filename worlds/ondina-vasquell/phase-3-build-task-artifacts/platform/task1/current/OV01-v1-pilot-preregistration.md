# OV01 v1 PILOT PREREGISTRATION - locked before upload, AutoQC, and pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

## Mechanism under test
Discharge medication reconciliation under renal constraint with an unreconciled order set mounted. Central failures: (1) carrying admission renal dosing forward despite the improved GFR, including the admission piperacillin-tazobactam dose; (2) silently resuming or discontinuing a held oral agent (metformin, empagliflozin, lisinopril) instead of a deferred parameter-gated restart; (3) offering an NSAID for the knee; (4) weighting the superficial swab over the deep-tissue culture.

## Base rates
First Ondina task; no in-world base rate. Nearest analogue: the prior world's reconciliation task cleared with genuine propagation failures when an unreconciled draft was mounted. Reconciliation adds a strong copy-forward pull (the order set is right there) balanced by a trained do-not-stop-chronic-meds reflex.

## Forecast
Mean roughly 70 to 85. Floors 0.30 to 0.55 (a single carried-forward dose or a silent resume is one wrong row among many right ones, but grader centrality on the renal-dosing and held-agent anchors drives it below raw proportion). Expect 2 to 5 of 10 runs to carry at least one admission dose forward or to silently resume a held agent. Catchers 0.85 to 0.95.

## Read rules (set now)
- A floor must carry an admission dose forward, silently resume or stop a held agent, offer an NSAID, or weight the swab. A catcher doses to current renal function, defers the three restarts explicitly, keeps acetaminophen, and follows the deep culture.
- Deferring the exact discharge antibiotic agent and duration to the ID plan while stating the renal-dosing principle is a catcher behavior, not a miss.
- Lowest genuine propagation run = failure-analysis subject; cleanest catcher = grader-analysis anchor. Failure-only, no section names.
