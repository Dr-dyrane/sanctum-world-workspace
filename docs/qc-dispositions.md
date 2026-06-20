# QC dispositions - paste-ready justifications for borderline AutoQC findings

Two kinds of QC finding. REAL-BUG classes (boilerplate, missing upload, wrong-task grader, metadata, undocumented chart edits) are caught by the local gates and you FIX them; they live in docs/qc-error-class-register.md. BORDERLINE classes are findings where the artifact is correct and the QC is over-reading; you JUSTIFY them in the Notes or dispute field and do NOT re-run or re-pilot. This file holds the paste-ready justifications for the borderline ones, on both QC layers (task AutoQC and trajectory AutoQC).

Standing rule: do not re-pilot a healthy, correctly-graded task to appease a borderline QC reading. A re-pilot is a fresh sample that can thin the floor or ceiling, and it forces an FA/GA rebind. Dispute instead.

Voice: write every disposition to be read aloud first. It should sound like the writer making a point, not a legal brief. Vary the rhythm, one idea per breath, no semicolons, no compressed jargon ("transient rationale", "the restraint to credit"). Same flow rule as the FA/GA voice.

## D1. Trajectory floor flagged as output-constraint non-compliance
Layer: Trajectory AutoQC, "Compliance with Output Constraints". When: a floor trajectory, the run where the model fails or refuses the deliverable, is flagged for violating the prompt's output constraint (e.g. "finalize it for submission").

> This is the failure the task is built to catch, not a defect in the run. The task is an adversarial difficulty evaluation, and one of the ways a model fails it is exactly this: it gets cold feet, leaves the determination blank, and hands the call back to a physician advisor instead of finalizing. The rubric names that move and caps it, which is why the grader scored this run low. The other trajectories enter the determination and score up into the nineties, so the constraint is plainly reachable, and this run is the floor that proves the task separates a model that finalizes from one that flinches. Re-running it would only discard a valid, correctly-graded failure. The trajectory stands.

Adapt the named deliverable and failure to the task. The shape holds for every floor trajectory: the non-compliance IS the measured failure, the grader confirms it, and the catchers prove the constraint is reachable.

## D2. Grader reasoning lists "what was done well" (read as the FA dwelling on positives)
Layer: Task AutoQC, the failure-analysis criterion. When: the authored FA field is failure-only, but the selected model grader's per-trajectory reasoning enumerates positives ("what was done well", "there are some positives").

> The failure analysis here is already failure-only, and the finding says as much. The praise it points to isn't in the failure analysis at all. Those "what was done well" and "positives" lists, in [the flagged trajectories], are the model grader's own scoring notes, written as it reasons through each run, and that reasoning is the grader's, not ours. A grader that weighs the genuine improvement before it lands on the failure is doing exactly what the rubric asks of it. So the strengths sit in the grader's thinking, never in the failure analysis, which names only what went wrong. That places them outside what this criterion checks, and we ask that the finding be waived.

Name the specific flagged trajectories where bracketed (e.g. traj_3603df058c2d, traj_3a69f35cdbb8, traj_5abe7cf086c1).

To reduce recurrence on future runs, avoid grader-guideline phrasing that invites a strengths list, then re-pilot; the writer cannot edit a grader's runtime reasoning, so for the current run the dispute is the path.

## D3. Chart medication discrepancy (MAR vs H&P supplements)
Layer: Task AutoQC, "Medication List Consistency". World-specific. The paste-ready dispute lives with the disclosure at worlds/ondina-vasquell/docs/KNOWN-CHART-DISCREPANCIES.md (the OV MAR omits ferrous sulfate and cholecalciferol while the H&P marks them continued; benign, immaterial, the chart is frozen).
