# Task 1 First Human Review - AO 2026-06-05

Status: SEND BACK / REWORK REQUIRED

Reviewer: Abimbola O, pod lead Abi

Scope: Task 1 Discharge Medication Reconciliation / Medication-Safety Review after batch v2 trajectories, FA/GA submission, and FA/GA AutoQC.

## Reviewer Summary

Abi recognized strong process progress: Task AutoQC errors were cleared, Env Linter and Data Quality were clean, and the lower trajectories showed a real clinical failure. The task was still not ready to advance because the platform-facing task design contained structural realism problems, over-helpful task-file scaffolding, golden-response format gaps, and FA/GA scope errors.

This review is now the governing learning record for Task 1 rework and for Tasks 2-6. Do not mass-produce task setup materials from the pre-AO Task 1 pattern.

## Findings

### 1. Task Files Were Structurally Unrealistic

Finding: Both Task 1 task files were dated 05/24/2026 even though the task prompt is anchored to 05/23/2026. A medication reconciliation request cannot be dated after the task it is requesting.

Forward rule: Every task-context file must pass a date-anchor scan before upload. Check every header, footer, table field, signature line, and embedded date, not just the filename.

Finding: The medication-safety handoff contained project-planning artifacts such as "Date / Anchor" and "discharge anchor." These are not realistic clinical-document fields.

Forward rule: Platform-facing clinical documents must never expose architecture words, source-package words, anchor labels, trap language, or project metadata. If a phrase would not appear in the chart, it does not belong in a task file.

### 2. Task Files Were Too Answer-Giving

Finding: Abi questioned whether both task files needed to exist. The discharge medication reconciliation request should be deleted entirely because it unrealistically tells the receiving hospitalist exactly how to perform the reconciliation and likely inflates model scores.

Finding: Abi recommended deleting the medication-safety handoff as well, while deferring the final decision to Alexander. If kept, it should be signed only by Pharmacy and minimized.

Alexander ruling: Delete both Task 1 task files. Task 1 should rely on the prompt plus the world chart, not answer-shaped task scaffolding.

Forward rule: Task-context files must frame the task, not teach the answer. A file is allowed only if it is realistic, necessary, and not duplicative of the reasoning the model is supposed to perform.

### 3. Prompt Must Follow File Decisions

Finding: If task files are deleted, the prompt must stop referring to attached task files.

Forward rule: Prompt/file alignment is a hard gate. Any uploaded-file deletion, addition, or rename requires a prompt scan before Task AutoQC.

### 4. Golden Response Needed Real Chart Format

Finding: The golden response read like a clinical answer but not like a realistic clinical document. It lacked DOB, MRN, allergies, date, and signature blocks for the attending and pharmacist.

Forward rule: Golden responses must preserve physician-owned clinical reasoning and also look like the requested deliverable. For clinical documents, include chart-appropriate demographics, date, relevant identifiers, allergies/code status when appropriate, and signature blocks.

### 5. FA/GA Scope Was Too Broad

Finding: Grader Analysis should analyze one trajectory run only, usually the single lowest-scoring run. It should not analyze "the two lowest runs" or describe what Alexander/Codex missed. It should use two to three sentences on what the grader got right and two to three sentences on what the grader got wrong.

Finding: Failure Analysis should also analyze one trajectory run only, usually the single lowest-scoring run. It should use two to three sentences on what the model failed and two to three sentences on what the model did well.

Forward rule: FA/GA is single-run, compact, and reviewer-facing. It is not a retrospective of our internal debugging process.

### 6. Grader Mechanism Claim Must Be Removed From GA

Finding: Abi corrected the GA claim that "the grader went into the chart." Her instruction: the grader scores the model output against the golden and grader guidelines.

Reconciliation: Local transcript evidence indicates the chart may be mounted and may be used differently across grader runs. That mechanism debate does not belong in the reviewer-facing GA. Future grader guidance and GA wording should be mechanism-agnostic: evaluate whether the grader correctly scored the model output against the golden and grader guidelines.

Forward rule: Do not put platform-mechanism claims in GA unless the platform explicitly asks for them. If a system-behavior claim matters for an AutoQC response, verify from the primary transcript/config and label verified vs inferred.

## Rework Direction

Task 1 rework should proceed only under explicit Alexander/platform authorization.

Required platform-facing changes:

- Delete both Task 1 task files.
- Replace the prompt with `prompt-task1-v2.txt`, which no longer references attached task files.
- Replace the golden with `golden-response-task1-v3.docx`, which restores clinical chart format.
- Replace grader guidelines with `grader-guidelines-task1-v5.txt`, which removes task-file references and uses mechanism-agnostic grading language.
- Rerun Task AutoQC.
- Rerun trajectories.
- Rewrite FA and GA against the new single lowest run after rerun, not against stale batch v2 trajectories.

## Future-World Lessons

- Waiting for review before Tasks 2-6 was correct. Abi caught a structural pattern that would have propagated into every task.
- Task files are dangerous when they become hidden instruction manuals. They should be sparse, realistic, and necessary.
- Golden responses need both clinical reasoning quality and deliverable realism.
- FA/GA should be short, single-run, and platform-facing.
- Mechanism claims require primary-artifact verification. Reviewer-facing text should not litigate platform internals.

