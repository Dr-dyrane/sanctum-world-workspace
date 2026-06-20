# QC dispositions - paste-ready justifications for borderline AutoQC findings

Two kinds of QC finding. REAL-BUG classes (boilerplate, missing upload, wrong-task grader, metadata, undocumented chart edits) are caught by the local gates and you FIX them; they live in docs/qc-error-class-register.md. BORDERLINE classes are findings where the artifact is correct and the QC is over-reading; you JUSTIFY them in the Notes or dispute field and do NOT re-run or re-pilot. This file holds the paste-ready justifications for the borderline ones, on both QC layers (task AutoQC and trajectory AutoQC).

Standing rule: do not re-pilot a healthy, correctly-graded task to appease a borderline QC reading. A re-pilot is a fresh sample that can thin the floor or ceiling, and it forces an FA/GA rebind. Dispute instead.

## D1. Trajectory floor flagged as output-constraint non-compliance
Layer: Trajectory AutoQC, "Compliance with Output Constraints". When: a floor trajectory, the run where the model fails or refuses the deliverable, is flagged for violating the prompt's output constraint (e.g. "finalize it for submission").

> This trajectory is the task's intended failure mode, not a trajectory-quality defect. The task is an adversarial difficulty evaluation. The deliverable is a physician-advisor continued-stay determination, and a known way for a model to fail is to refuse to enter the determination and hand it back to a physician advisor. The grading rubric names this exact failure ("refusing to enter a determination earns no credit, anti-paralysis"), and the grader correctly capped this run low. The agent's non-compliance with "finalize it for submission" is the measured failure the batch exists to capture, confirmed by the grader, not a defect in the run. The batch is bimodal and healthy: other trajectories enter the determination and score 0.70 to 0.95, so the constraint is reachable, and this run is the floor that proves the task discriminates. Flagging a correctly-graded floor as non-compliant would make any adversarial difficulty task impossible to pass. The trajectory is valid and is retained.

Adapt the named deliverable and failure to the task. The shape holds for every floor trajectory: the non-compliance IS the measured failure, the grader confirms it, and the catchers prove the constraint is reachable.

## D2. Grader reasoning lists "what was done well" (read as the FA dwelling on positives)
Layer: Task AutoQC, the failure-analysis criterion. When: the authored FA field is failure-only, but the selected model grader's per-trajectory reasoning enumerates positives ("what was done well", "there are some positives").

> The authored failure analysis is failure-only, which this finding confirms. The cited "what was done well" and "positives" sections (name the flagged trajectories) are not part of it. They are the selected model grader's own scoring rationale, written at runtime as it weighs each response, and the writer neither authors nor edits a grader's reasoning. A grader acknowledging genuine improvement before naming the capping failure is correct behavior; the rubric directs it to weigh that improvement as the restraint to credit. The criterion governs the authored failure analysis, which lists no strengths. The grader's transient rationale is out of scope. We request the finding be waived.

(Name the specific flagged trajectories in the paste, e.g. traj_3603df058c2d, traj_3a69f35cdbb8, traj_5abe7cf086c1.)

To reduce recurrence on future runs, avoid grader-guideline phrasing that invites a strengths list, then re-pilot; the writer cannot edit a grader's runtime reasoning, so for the current run the dispute is the path.

## D3. Chart medication discrepancy (MAR vs H&P supplements)
Layer: Task AutoQC, "Medication List Consistency". World-specific. The paste-ready dispute lives with the disclosure at worlds/ondina-vasquell/docs/KNOWN-CHART-DISCREPANCIES.md (the OV MAR omits ferrous sulfate and cholecalciferol while the H&P marks them continued; benign, immaterial, the chart is frozen).
