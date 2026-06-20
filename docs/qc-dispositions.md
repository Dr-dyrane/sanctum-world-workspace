# QC dispositions - paste-ready justifications for borderline AutoQC findings

Two kinds of QC finding. REAL-BUG classes (boilerplate, missing upload, wrong-task grader, metadata, undocumented chart edits) are caught by the local gates and you FIX them; they live in docs/qc-error-class-register.md. BORDERLINE classes are findings where the artifact is correct and the QC is over-reading; you JUSTIFY them in the Notes or dispute field and do NOT re-run or re-pilot. This file holds the paste-ready justifications for the borderline ones, on both QC layers (task AutoQC and trajectory AutoQC).

Standing rule: do not re-pilot a healthy, correctly-graded task to appease a borderline QC reading. A re-pilot is a fresh sample that can thin the floor or ceiling, and it forces an FA/GA rebind. Dispute instead.

Voice: write every disposition to be read aloud first. It should sound like the writer making a point, not a legal brief. Vary the rhythm, one idea per breath, no semicolons, no compressed jargon ("transient rationale", "the restraint to credit"). Same flow rule as the FA/GA voice.

## Dispute discipline: stay inside the sanctioned reasons

Disputing is bounded, and the boundary matters. When the TaigaQA Env-Linter or Data-Quality report raises a flag, the only moves the report accepts are the ones shown on the flag: agree and fix it, disagree for a reason that is actually in the offered list, or mark it technical and not clinical. You cannot invent a reason that is not offered. A flag you agree with has to be fixed in the task or the world, not argued away, and if it genuinely cannot be addressed the task may have to be discarded rather than shipped over it. Every dismissal is reviewed externally, so a disagree is never a one-liner; it is a substantive, fact-referenced rebuttal (AGENTS.md guardrail 4) that maps to one of the offered reasons.

So the dispositions below are disagree rebuttals for genuine over-reads only, and each one still has to be framed inside a sanctioned reason when you paste it. When you are not sure whether a flag is a borderline over-read or a real bug, treat it as a real bug and fix it; the fixable classes live in docs/qc-error-class-register.md. The full dispute rules are in the Phase-3 evaluation guidelines at reference/source/phase-3-evaluating/ (read phase-3-instructions-2026-06.md; the 2026-06-19 updated-guidelines screenshots are the raw source).

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

## D4. Preference-label structure read as AI prose (Human-Written criterion)
Layer: Preference Labels AutoQC, the "Human-Written (Preference Label)" criterion. When: the label set is flagged as machine-written for carrying the labeled subsections (Prompt adherence, Correctness, Completeness, Methodology, Quality and clarity, Summary), for the balanced A-versus-B framing, or for dash and hedge tells that belong to a superseded draft.

PRECONDITION (do this before you dispute): the dash and hedge half of the finding is a REAL fix, not an over-read, if those tells are actually in the submitted text. Confirm the current cleaned labels are what is submitted, re-paste if the old draft is still in Studio, and run `python3 tools/verify/lint_pl.py <all of the task's PL files>` until it is clean (no dashes, no hedge phrases, no opener shared across labels). Only the structural half below is disputable.

> The structure this finding reads as an AI tell is the preference-label format itself. The platform's own Preference Label template prescribes exactly these labeled parts, Prompt adherence, Correctness, Completeness, Methodology, Quality and clarity, and Summary, and instructs us to paste from the Scale Selection line through Summary into the Comments box. Every label in the set carries them because the format requires them, and a preference label is by its nature a side-by-side read of A against B on each of those points. That is the assignment, not a generated pattern. Holding the labels to the template and then citing the template as proof of machine writing reads the required form as a defect.
>
> The specific prose the finding quotes is not in these labels. The stacked hedge it cites, the "plain A, slightly better, not a full step" line, belongs to an earlier draft that has since been rewritten. The current labels open differently from one another, state the margin once, and use plain hyphens, not the dashes or the piled qualifiers described. If the report is reading a prior version, the current submission supersedes it. We ask that the finding be waived against the labels as they now stand, each of which is the writer's own, follows the prescribed format, and names its preference and reasoning in the writer's own words.

Frame it inside the offered reason: this is a disagree (the structure is the mandated format) and can be tagged technical-not-clinical (a format and house-style matter, not a clinical-accuracy defect). Name the format source (references/pl-format-template.md, which prescribes the six subsections and the paste-from-Scale-Selection-through-Summary rule). Do NOT dispute the dash or hedge tells if they are genuinely present, fix those by submitting the cleaned, lint-clean version first.
