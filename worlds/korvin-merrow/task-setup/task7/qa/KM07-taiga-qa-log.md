# KM07 Taiga QA log - task 2e5v8bf2

## Batch: v1-era QA report (job ~6/9, Env Linter clean, Data Quality 2 warnings) - responses entered 6/10

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

## Standing watch item for the v2 batch QA
The v2 run (bone-health false closure) will produce its OWN Env Linter / Data Quality reports. If undisclosed_constraints re-fires against the v2 prompt ("finish it and finalize it so it is ready to send"), the rebuttal differs: the prompt hands the physician their own started draft to finalize, and finalizing a clinical document inherently asserts fidelity to the record; the grading guidelines credit any accurate handling of the medication summary and penalize only carrying a record-contradicted claim into a signed letter. The expected enable_anthropic_api false positive gets the same two-field tech-issue treatment.
