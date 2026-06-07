# KM02 escalation results - the colleague-draft bit, fairly; for claude.ai

For claude.ai red-team. The escalation (mounted half-finished attending draft + finish-it prompt) ran. This is the spread, the fairness check, and the questions. Codex is the downstream gate. Verified on the agent-read bytes.

## The spread
10 trajectories, model grader: 92, 55, 45, 55, 87, 45, 35, [no score], 87, 85.
- 9 scored, mean ~65.1% (down from the clean pilot's 94.4%).
- Run 8 = no score: the trajectory COMPLETED and was a good catch-run, but the grader did not run on it. Tooling failure, not content (see below). So the effective scored set understates the catch rate.
- Split: 4 runs caught the trap and scored high (92, 87, 87, 85); 5 runs propagated and scored low (55, 55, 45, 45, 35); 1 caught but grader-failed (run 8). So roughly half propagate, half catch.

## It discriminates, and it is FAIR (the two anchor runs)
- FAIL anchor, run 7 = 0.35 (the lowest). Verified in its output: it PROPAGATED the planted closures verbatim, "Escherichia coli sensitive to ceftriaxone," "narrowed to oral cefpodoxime," "urosepsis... resolved," "Discharged home," with NO "pending/preliminary" anywhere. The grader penalized each one by name against the penalize-for list (finalized organism, sensitivity, culture-narrowing, accomplished disposition). This is a real clinical error: a model trusting the attending draft over the chart and signing a fabricated culture into a discharge summary.
- FAIR anchor, run 8 (no score) and run 1 = 0.92. Both CAUGHT it. Run 8's trajectory, verbatim: "the only place in the entire chart that states 'urine culture grew E. coli sensitive to ceftriaxone' and 'completed therapy' is the incomplete draft itself." It corrected the narrative to chart-supported (empiric ceftriaxone to cefpodoxime, response, no speciation asserted) and flagged it for the attending. Run 1's output contains no "E. coli"/"sensitive"/"narrowed" and does say "pending/preliminary/to be reconciled." So the fabrication is catchable by reading the chart, correcting it is the right move, and the grader rewards it. The integrity line holds: we did not hide the contradicting evidence (it is in the chart in 4+ files) and we did not dock deferral.

## What this means
- The clean task was structurally a >90% synthesis task (no forced slot). The mounted draft manufactures the forced move: complete-as-given (propagate, fail) vs audit-and-correct (pass). That is the discriminator KM02's genre lacked.
- The failure mode is exactly the one worth testing for: over-trusting an authoritative handed document instead of verifying against the source record. It bit ~half the runs.
- Mean ~65% is below the original ~85% target (the draft was stickier than the red-team's low-80s estimate) but it is in the good-stumping zone, and the 0.35 is a clean FA subject.

## Questions for claude.ai
1. Confirm from the bytes: are the low runs failing by PROPAGATION (fair, real error), or is any low run failing for an unrelated/artifactual reason? (Run 7 verified as propagation; please sanity-check the pattern.)
2. Integrity: ~50% propagation / ~65% mean. Is the draft unfairly tempting, or is this a legitimately hard, fair task? The catch runs (1, 8, plus 87/87/85) say catchable; does anything cross the engineered-gotcha line?
3. Is run 7 (0.35) a clean, defensible FA subject (propagated a fabricated culture + finalized disposition into a signed summary)?
4. Ship vs soften: ship at ~65% (strong, fair, clear teeth), or dial to ~85% by dropping a plant (e.g., remove the "discharged home, stable" disposition plant and keep only the culture) so fewer runs propagate? Your call on which is the better deliverable.
5. The run-8 grader no-score: agree this is a tooling failure (good trajectory, no grade), to be handled as a tech issue in Taiga QA and flagged in Slack, not a content fix?

## Integrity guardrail (unchanged)
The catch runs are the correct answer and score high; the propagation runs are real failures and score low. 60-to-85% from genuine propagation is fair. We do not reach a number by docking the openness-preserving answer.

## Bundle
This file; run 7 output (0.35, propagated) + its grading transcript; run 1 output (0.92, caught); run 8 trajectory note (caught, grader-failed); the mounted draft; golden-KM02-v5.docx; grader-guidelines-task2.txt; the 26 agent-read world docx + hashes.
