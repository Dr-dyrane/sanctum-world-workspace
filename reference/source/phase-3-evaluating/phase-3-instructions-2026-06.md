# Phase 3: Evaluating (official instruction-document transcription)

Source: Project Sanctum instruction document, Phase 3 "Evaluating", plus the "Phase 3: Evaluating Actions" operational tab. Transcribed from 16 screenshots shared 2026-06-19. This is a faithful content capture for internal reference, the source of truth our canon aligns to. Punctuation normalized to satisfy the repo no-dash rule (em and en dashes rendered as commas, hyphens, or periods); wording otherwise preserved. Visual source: screenshots/ (to be filed).

Status: this is the SOURCE capture (Stage 1). Reconciliation against fa-ga-canonical and any canon edits are Stages 2 and 3, done separately after sign-off.

---

## Context

In Phase 2 you created your task: a Task Prompt (plus optional Task Input Files), a Golden Response, and Grader Guidelines. In Phase 3 you have the agent attempt the Task Prompt and then evaluate how well it can actually produce a clinically ready deliverable.

The AI agent works under tight constraints. It will ONLY have access to:
- The set of clinical files (the "world") you built in Phase 1.
- The Task Prompt (and optional Task Input Files) you created in Phase 2.

To assess the agent fairly, the task is run as a batch of 10 attempts called trajectories. Each trajectory is one agent attempt to solve your task. When the batch is done, your job is to assess how well it did on ONE of those trajectories.

Suitability rule: for a task to be suitable for submission, the agent's output must contain a failure. If it doesn't, the prompt or task was too easy. Rule of thumb: if you would score most trajectories above 70%, the task is too easy to submit.

## Overview of Phase 3
1. Run the agent. Each run produces a batch of 10 trajectories, each a single agent attempt at your task prompt.
2. Run QC on the trajectories. Run [Trajectory] AutoQC, make fixes, and rerun until all flags are addressed.
3. Evaluate one trajectory and produce two analyses:
   - A failure analysis explaining why the agent's deliverable was flawed.
   - A grader analysis rating how well the grader scored that deliverable, both the score it gave and the reasoning behind it, on the Poor / Fair / Good / Great scale. You are evaluating the grader's performance, not critiquing the guidelines you wrote.
   - Run Failure and Grader Analysis AutoQC, make fixes, and rerun until all flags are addressed.
4. Complete preference rankings. Evaluate two trajectories and write an analysis of which deliverable is stronger, and why. Run Preference Ranking AutoQC, resubmit fixes, and rerun until all flags are addressed.

## Part 5: Running Trajectories (operational)

Click "Run Taiga Trajectories & QA". Up to 30 minutes. The batch of 10 appears as the most recent version (e.g., v2) in Task Submission History. Confirm all 10 trajectories completed with a percentage score assigned, then "Back to Task". If any trajectory failed (no percentage), do NOT proceed; ask in the tech-issues slack channel. Once the batch of 10 ran successfully, move to TaigaQA.

## TaigaQA

After the batch completes, two automated reports run: the Taiga QA Env Linter and the Data Quality Report. Up to 30 minutes. Expand each and check for flags. If there are no flags in both, proceed. If a report fails to complete, post in your pod for assistance; you cannot proceed until both reports complete.

Categories and action:
- EnvLinter: Taiga's QA agent, clinical and structural. Address every flag.
- Data Quality: Taiga's clinical data check. Address every flag.

For each audit item, decide:
- Agree, I will fix it. Thumbs up. Write a brief note on what you will do.
- Disagree, I will not change it. Thumbs down. Write a clear justification.
- Technical, not clinical. Thumbs down. Write "Defer to tech team. Does not impact clinical content." or similar.

Submit each response with the airplane icon.

### Valid reasons to dispute a flag (only these)
- Factual inaccuracy in the TaigaQA flag. Example: the flag says two values are inconsistent but misses the real clinical reason for the difference (a creatinine that legitimately changed between admission and discharge, or two facilities reporting the same lab against different reference ranges). Valid to dispute. NOT acceptable to merely state the inconsistency does not affect the analysis or is "minor".
- Clinical inaccuracy in the TaigaQA flag. Example: the flag says a guideline or dosing standard applies, but that guidance has since been superseded or withdrawn. Valid to dispute. NOT acceptable to dismiss a judgment call you disagree with but another clinician would agree with; in that case defer to the flag and address it.
- Intentional task design. TaigaQA may say your prompt did not specifically request an aspect of your Golden. In limited cases this flag is invalid: if you ask for a discharge medication reconciliation, a clinician is assumed to know they must review the home medication list, identify every relevant change across notes and consults, and produce a reconciled list in an acceptable format; none of these need to be specified if they would be known to all competent clinicians. The test is universal agreement. If the flagged aspect is a matter of personal preference, or not something other clinicians would agree with, the flag cannot be disputed.
- Technological issue. Separated within the report as "Technological Issues". Respond with the exact text string "tech issue" (no additional characters, capitalization, or punctuation) and engineering will action it later.

You must not dispute flags for reasons not shown above. For any flag ineligible to be disputed, address it by editing your task or world. If it cannot be addressed because it is inherent in the task's design or content, the task may need to be discarded; consult your pod lead. If you dismiss a finding, make the explanation clear, specific, and professional, as these responses are reviewed externally alongside the task submission.

### Re-run the agent if you made changes
If any response was "thumbs up, I will fix X": make the changes to the task, files, golden, or grader; save the new version in RL Studio; re-run the external agent with the same settings. New trajectories and a new QC report generate. Repeat EnvLinter, Data Quality, and AutoQC until every item is resolved.

Common pitfalls: clicking the arrow beside Fetch QC Report instead of the button itself; forgetting to re-run the agent after fixes, so the QC report never updates.

---

## Failure Analysis

You are explaining the failures you identified in the agent's deliverable for your prompt. The AI output may look polished and complete; your job is to look past that and judge whether the actual clinical work holds up. Ask: is this a deliverable a clinician could present to the intended audience? Often the answer is yes. Sometimes no, because the AI still struggles with deep domain knowledge or reasoning. If no, the diagnosis of what is flawed is the heart of the failure analysis.

### What is an acceptable failure
Clinical errors on the core questions of the prompt, extraction errors, or errors in tone, style, and formatting that cannot be easily corrected under an hour.
- Clinical errors: misstatements of medical fact, hallucinated findings or references, faulty clinical reasoning, incorrect management decisions.
- Extraction errors: misreading or misattributing chart information (a lab value, dose, or date) in a way that materially affects the assessment.
- Errors in tone, style, formatting: e.g., a patient-facing letter when the task calls for a clinician-to-clinician note, that cannot be quickly corrected.

### What is not an acceptable failure
- Spelling, grammar, punctuation. Rarely brings the output below 70% and is easily remedied. If the style error can be fixed in under an hour, it is not a valid failure.
- Subjective choice between multiple viable answers. If the output is validly reasoned but relies on different evidence or reaches a different defensible conclusion than your Golden, that disagreement of opinion is not a failure.
- Non-inclusion of ancillary or corollary points. If the point is not required to respond to the prompt, its absence is not a valid failure.

### Ancillary or corollary points
The test is the task prompt. If the deliverable fully answers what the prompt asked without the missing point, the omission is ancillary. Examples: a discharge summary prompt where the output gets the core assessment right but does not suggest an optional outpatient referral the prompt never asked for; the Golden cites six supporting findings and the output cites three that fully carry the assessment; the output omits a "next steps" section the prompt never requested.

By contrast, an omission is a valid failure if it is required by the prompt or necessary to the conclusion: a contraindication that flips the management plan, a major risk left out when the prompt asks for the risks of proceeding, or an unaddressed element of the differential the assessment must cover. The dividing line: if a supervising attending could not sign off on the deliverable without the missing point, the omission is core; if it could go out the door without it, it is ancillary.

### Self-scoring bands
A failure analysis requires your independent assessment. Read the output carefully, identify why it falls short, and compare it against the Golden. Assign a percentage score using the bands below. Ignore the score the grader assigned (it is notoriously inaccurate and gives unreasonably high scores) and assess the output independently. Write the analysis in structured plain language a non-clinician could understand.

- 91-100%: Perfect. Every domain expert would agree, without exception, that the output is ready to deliver to a client and is of the highest possible quality.
- 71-90%: Good enough to use in your clinical setting. The analysis and everything in the output holds up. Defects limited to non-impactful points, defensible choices between viable answers, or minor errors that do not affect the analysis or its conclusions. A self-assessed score in this band means the output succeeded and you would put your name on it and send it to your client; your task was too easy and cannot be submitted.
- 51-70%: Minor flaws preventing sharing in your clinical setting. At least one significant error on a core question of the prompt: a misstatement, a faulty conclusion, or an information error that affects the analysis. The deliverable needs real rework before a domain expert could send it.
- 31-50%: Noticeable core errors. Multiple core errors, or a single error that flips the bottom-line conclusion.
- 21-40%: Fundamentally defective. Errors are pervasive; the analysis cannot be trusted at any point without independent verification. Potentially needs re-writing from scratch.
- <20%: Unusable. The output misunderstands the assignment, rests on hallucinated authority, or fails to produce the requested deliverable.

If the score you assigned is above 70%, the task is too easy and you may not proceed with it.

[Transcriber note: the 31-50% and 21-40% bands overlap in the source document. Captured verbatim; flag for clarification before this drives any gate.]

### Required FA headings and content
- What the Agent Got Wrong. Lead with the most consequential flaw; discuss failures in order of materiality. Identify all other notable flaws. Anchor each flaw to what the Golden Response does instead; do not critique in the abstract, explain what the right answer would have looked like.
- Why the Failure Matters. State explicitly that the output would not be deliverable by any competent practicing clinician. If you cannot make this statement, the failure is insufficient. Explain what the errors mean in real clinical practice and what a competent clinician would have done differently.
- Output Score. Assign a percentage per the bands. If above 70%, you may not proceed. State a brief justification.

### Never include in a failure analysis
- Commentary like "overall, the output is great". This is a failure analysis; we argue the output is not good enough to be sent.
- Drafting preferences framed as failures. A wrong clinical conclusion is a failure. Choosing "BID" over "twice daily" is a style preference, not a failure.

---

## Grader Analysis

In addition to the failure analysis, submit a grader analysis for the SAME trajectory. In the failure analysis you judged the AI's deliverable. In the grader analysis you judge the grade assigned in the platform to that deliverable. A summary of why the grade was assigned is in the grading transcript. Check its work and evaluate whether you agree with how it scored the output. Think of it as grading the grader, confirming whether it marked the deliverable accurately.

### Three important rules
1. Your grader analysis must agree with your failure analysis. You already assigned a score of 70% or below based on failures; that is locked in. If the grader said the output is "overwhelmingly correct" or similar, it would be illogical to agree; a work product cannot have a critical failure and be nearly flawless at once. Vigorously refute any grader statement contradicting your failure analysis. Point out what the grader missed and any judgment calls you disagree with.
2. If the grader's score is above 70%, you cannot rate its performance as "Great". A score that contradicts the critical failure you found means the grader misjudged the work, and a grader that misjudged the work does not earn the top rating no matter how polished its rationale.
3. The score gap is not the whole story; reasoning matters more. Start with the score gap to find the highest rating you could award (chart below), then downgrade from there. Example: a 10-point gap is a Good, but if the reasoning is flawed you move down to Fair or Poor. With a 10-point gap it can never be higher than Good. You can only downgrade for reasoning, never upgrade.

### Required GA headings and content
- Suggested Score. Restate the score you assigned during the failure analysis, briefly restating your explanation for it.
- Score Comparison. Compare your score to the score the output was assigned. You must reference the grading summary, citing specific parts of it. Did the grader arrive at its score the same way you would have? Quote or point to the exact places where it got something right, or where it misread, missed, or misapplied judgment. This is the crux: you are judging whether the grader's rationale is accurate, not just whether its final number was close to yours.

Guidance:
- If you disagree with the assigned score or rationale: say exactly what the grader got wrong; name the specific points it misjudged; tie the mistake to whether the score was too high or too low. Do not give "Great" or "Good" if you disagree with most of the rationale.
- If you agree with the assigned score or rationale: the analysis can be shorter; confirm alignment and note any areas of improvement.
- Always emphasize what the grader could have done better. It is very rare that an AI grades flawlessly, so focus on areas of improvement.
- DO NOT reference the scoring bands in your actual write-up.

### Grader Rating (entered in Studio, scale Poor to Great)
Based on one core question: how much do you agree with the grading agent, both its rationale and the score it landed on?

| Rating | How close the grader's score is to yours |
|---|---|
| Great | Within 5 points |
| Good | Within 10 points |
| Fair | Within 15 points |
| Poor | More than 15 points off |

---

## Templates

Failure Analysis template headings: What the Agent Got Wrong / Why the Failure Matters / Output Score (content per the FA section above).

Grader Analysis template headings: Suggested Score / Score Comparison (content per the GA section above). [Transcriber note: the doc's "Grader Analysis Template" image repeats the FA headings, a copy-paste error; the true GA structure is Suggested Score / Score Comparison, confirmed by the GA format section and the worked example below.]

### Worked Grader Analysis example (from the doc)
Suggested Score: 50%. The deliverable contains two core medication-management errors: failing to restore apixaban to the appropriate dose after renal recovery, and failing to identify and restart finerenone as the appropriate MRA for advanced heart failure with diabetic nephropathy, compounded by a failure to follow the one-page length instruction (it ran to four). Multiple core errors plus the instruction miss place it at the seriously-deficient to minor-flaws boundary, well below the 70% threshold.

Score Comparison: The grader assigned 55%, a gap of 5 points from my 50%. The grader got two things right. It correctly flagged that the agent never makes the finerenone restart recommendation, which aligns with my most material finding. And it correctly reasoned that apixaban should not be stopped given the patient's stroke risk, sound clinical logic that matches the direction of my apixaban concern. But its rationale has gaps that pushed its score higher than the output earns. First, it grades non-medication items, which are out of scope for a medication reconciliation and should not factor into the score; crediting them inflates the result. Second, it makes an inappropriate concession, accepting at face value the agent's claim that a library version mismatch did not affect any extracted content; the grader should independently verify the output, not adopt the agent's own reassurance. Third, and most consequentially, it misses the length and format failure entirely; rather than checking the output against the one-page expectation, it calls the four-page render clean and complete, which both overlooks the instruction violation and certifies a reconciliation as complete and verified against every source despite the two medication recommendations it failed to surface.

So while the grader's final number and mine are close, its path there is unreliable: it rewards out-of-scope content, defers to the agent's self-assessment, and certifies the output as complete and clean when two core recommendations are missing and a clear length instruction was broken.

---

## Phase 3: Evaluating Actions (operational tab)

Two items to fill out: Failure Analysis (what was the main reason for failure? what did the model output do well on?) and Grader Analysis (what did the grader get wrong? what did the grader get right?).

- Step 1, complete Failure + Grader Analysis. In Section 6.0 under task submission history, click the trajectory. Select the SECOND LOWEST scoring trajectory to analyze. Read the agent trajectory and grading transcript. Treat the automated grader scores as a starting point only; your clinical judgment is the authority, not the grader, which may miss errors, over-penalize formatting, or misattribute partial credit.
- Step 2, download and read the full output. Actions menu, Download Output Directory (.tar.gz). Read the full output end to end against your golden. Non-negotiable: errors the grader missed surface only from your own reading.
- Step 3, complete the Failure Analysis on the right side, then "Add finding"; confirm it shows in submission history. Fill the Grader Analysis, select Poor to Great, add the detailed explanation, submit, confirm it shows in submission history. If submission errors, save responses to a Google Sheet and upload to the shared drive as a temporary measure, and report in the technical channel.
- Step 4, AutoQC Failure + Grader Analysis (10 to 15 minutes). Open the report, review all feedback, and add notes in Section 7.2 addressing every point; provide reasoning for any disagreement. Then "Submit for First Human Review".
- Wait on First Human Review. The reviewer either approves (status moves to "Ready for Preference Labels", Move Forward becomes "Start Preference Labels", Part 4), or returns the task with notes to address and rerun from the relevant stage.
