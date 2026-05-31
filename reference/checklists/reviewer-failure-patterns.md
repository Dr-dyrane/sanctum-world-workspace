# Reviewer Failure Patterns

Source indexed: `reference/source/New Writers Version - Instruction Guide (05_24).md`

Use this as a pre-review audit list.

## Phase And Scope Failures

- Continuing past onboarding Step 6 without explicit approval.
- Starting synthetic file generation before World Spec approval.
- Drafting task prompts, golden responses, or grader guidelines with AI.
- Treating future pipeline steps as current deliverables.
- Curating templates or files during onboarding unless explicitly instructed.

## AI Usage Failures

- Letting AI drive scenario, task, or trap decisions.
- Accepting AI clinical judgment over physician judgment.
- Submitting AI-sounding generic prose without critical review.
- Allowing LLM-generated wording, timeline inconsistencies, or typos to remain.
- Clearing self-QA too quickly without meaningful review.
- Asking AI to write task prompts, golden responses, or grader guidelines from scratch.

## Brainstorm Failures

- Scenario is too generic or too rare-disease driven.
- Setting, specialty, encounter type, or timeline is unclear.
- Patient profile does not fit the encounter.
- Frictions are information gaps rather than stakeholder conflicts.
- Stakeholders are not named or their positions are not clear.
- Traps are too obvious, too vague, or not clinically meaningful.
- Traps do not require cross-document synthesis.
- Rough tasks do not map to approved workflow categories.
- Task ideas lack concrete deliverables.
- Self-containment risks are ignored.

## World Spec Failures

- Required sections are incomplete.
- Placeholder text remains in the document.
- Dates, names, medication doses, lab values, or diagnoses conflict across sections.
- Key dates are referenced outside the Key Milestones table.
- Clinical history is not detailed enough to build files from.
- Clinical Complexity Overview restates the problem list instead of explaining reasoning difficulty.
- Task expected outputs are too vague to grade consistently.
- Failure design lacks plausible wrong answers and clear remediation paths.
- Task prompts reveal traps or use test-question language.
- Blueprint metadata leaks into the prompt.

## File Plan Failures

- Files are designed before tasks.
- Essential files lack detailed descriptions or reference origins.
- Supplementary files contain trap content or answer-critical facts.
- A single file resolves a task.
- File count is too thin to support chart navigation.
- File count is so large that review becomes unwieldy.
- File naming is inconsistent or missing dates.
- No explicit source-of-truth hierarchy exists despite conflicting records.
- Over-authoritative summaries remove the need for cross-document reasoning.

## Trap Design Failures

- Trap can be solved from one or two files.
- Trap can be solved by general medical knowledge without chart synthesis.
- Trap feels artificially inserted rather than arising from the clinical story.
- Plausible wrong answer is absurd rather than realistically tempting.
- Trap is not fair game for a seasoned clinician.
- Trap is so obvious that it does not differentiate model performance.
- Trap content disappears from its planned source file.

## Reviewer Response Failures

- Ignoring reviewer comments or resolving them only superficially.
- Failing to rerun AutoQC after revisions.
- Not documenting disagreement with an AutoQC item or reviewer comment.
- Moving forward before Human Review gives GO.
- Keeping official feedback outside RL Studio.

