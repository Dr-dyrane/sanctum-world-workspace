# KM07 Taiga QA log - task 2e5v8bf2

## CURRENT: v3 batch (chart-aware re-pilot dba6c34f) - dispositions decided 6/11, ONE CORRECTION OUTSTANDING

### Flag 1 (Technical): enable_anthropic_api False - thumbs DOWN, but the bare "tech issue" annotation FAILED Feedback review
The Taiga QA Feedback review rejected the two-word "tech issue" annotation as dismissive deflection (does not engage the finding's substance). The old two-field rule (KM03-era) is CORRECTED: a tech-issue disagree needs a substantive, fact-referenced rebuttal. Replacement reasoning to enter, then rerun the Taiga QA Feedback AutoQC:

"The grader did not fail or fall through on this task. The selected grader is the model grader, and on the trajectory pilot (job dba6c34f) it executed normally and returned valid, discriminating per-run scores across all ten runs (0.45 to 0.60). enable_anthropic_api=False is a static configuration-preflight signal that does not reflect the actual grading run; the completed pilot empirically contradicts the predicted cannot-call-the-model / will-fail-or-fall-through. No grading failure occurred, so the finding does not apply to this task."

### Flag 2 (Non-technical): undisclosed_constraints - thumbs DOWN, substantive rebuttal ALREADY PASSES review
Accurate but intended; justified, not fixed. The required stances (keep bone-health open, staged restart, held agents not restarted) are disclosed by the chart the agent reads (MAR: alendronate not administered inpatient, reconcile at discharge; held agents charted restart-not-ordered). The prompt is intentionally a minimal in-role completion instruction per pod prompt guidance; restating the stances would telegraph the judgment the task tests (the KM06 reconcile-clause difficulty-killer). Do NOT add stance instructions to the prompt.

### Expected on any re-run: Self-Contained Guidelines warning
The chart-aware grader requires include_input_files=true, so expect the Self-Contained AutoQC warning; justify with the include_input_files evidence exactly as on KM03/KM04.

---

## HISTORICAL: v1-era batch QA report (job ~6/9, Env Linter clean, Data Quality 2 warnings) - responses entered 6/10
NOTE 6/11: the two-field "tech issue" treatment recorded below was the standard at the time but FAILED the 6/11 Feedback review; see CURRENT section for the corrected substantive approach. Kept for history.

### Flag 1 (Technical): "Agentic grader configured but enable_anthropic_api is False"
Disposition: thumbs DOWN. The recurring false positive (Task 1 / KM02 / KM03 / KM06 precedent).
TWO-FIELD RULE (KM03 correction, mandatory): the annotation/comment field takes EXACTLY the two words below, nothing else - any narrative there fails the Feedback AutoQC. The reasoning sentence goes ONLY in the dedicated dismissal-reasoning field.

Annotation field (exact):
tech issue

Dedicated dismissal-reasoning field (one sentence):
The agentic grader executed and returned scores on all ten trajectories in this batch, so the enable_anthropic_api setting did not affect grading for this task; the flag reflects an environment configuration outside the task definition.

### Flag 2 (Non-technical): "undisclosed_constraints - prompt asks only to state the reason for the referral with no warning [that the staged-restart framing is required]"
Disposition: thumbs DOWN + substantive rebuttal (client-visible). Chart citations byte-verified against the agent-read nephrology consultation and discharge-facing plan.

Response field (paste as one block):
We respectfully disagree that the staged-restart framing is an undisclosed constraint. The required stance is disclosed by the source record itself rather than by the prompt: the nephrology consultation states it verbatim across signed entries ("Do not interpret a single favorable creatinine value as sufficient grounds for simultaneous restart"; "Coordinate restart sequencing with Cardiology; nephrology does not declare Korvin ready for full simultaneous restart"), and the discharge-facing plan carries the same position. Representing a consultant's documented position accurately in a physician-to-physician referral letter is baseline clinical documentation practice, not a hidden grading rule; misstating a consultant's recorded stance would be a substantive clinical error in any real chart. The grading guidelines apply that fidelity standard against the golden response rather than enumerating clinical stances in the prompt, consistent with the project guidance that prompts read like a real clinician request rather than a test question. The batch results confirm the framing was discoverable in good faith from the chart alone: all ten trajectories in this run framed the restart as an open, staged question and scored 90 or above without any prompt hint.

### Operator mechanics (every flag)
1. Respond to BOTH flags in BOTH reports if they appear in each view.
2. Save each with the paper airplane, then refresh and confirm the responses persisted.
3. NEVER thumbs up (thumbs up = Go Back to Task Writing).
4. After both saved: run Taiga QA Feedback AutoQC (step 5) and address any 5.2 items by copying the exact flagged line before responding.
5. Do NOT write FA or GA until the Start Failure Analysis & Grader Analysis button is clicked.

## RETIRED: standing watch item for the v2 batch QA (obsolete 6/11)
Written for the v2 planted-closure design, which Abi retired as unfair on 6/9; v3 has no planted claim, so the "penalize only carrying a record-contradicted claim" rebuttal frame no longer matches the task. The undisclosed_constraints rebuttal for v3 is in the CURRENT section above (chart-discloses-the-stance + minimal completion prompt). The two-field tech-issue treatment referenced here is also corrected per the CURRENT section.
