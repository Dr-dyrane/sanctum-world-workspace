# KM05 review request for Claude.ai

Status: review request only. This is not a platform artifact, DOCX, upload record, AutoQC response, final prompt, golden, grader, or build authorization.

## Assignment

Red-team the KM05 prebuild packet before any document is built or uploaded.

Do not reselect the task. KM05 is already selected and locked as the early post-discharge follow-up assessment. Your job is to test whether the proposed mounted pre-chart draft fairly executes that task.

## Files To Read

1. `../TASK5-STATE.md`
2. `../KM05-prebuild-review-and-build-gates.md`
3. `../design/KM05-design-plan-for-review.md`
4. `00-byte-verification-and-source-audit.md`
5. `G1-prompt-task5-escalation-DRAFT.txt`
6. `G2-golden-and-grader-deltas-DRAFT.md`
7. `G3-mounted-followup-draft-SOURCE-DRAFT.md`
8. `G3-mount-manifests.md`
9. `pilot-preregistration.md`
10. `inputs/TP-KM05.md`
11. `inputs/EO-KM05.md`
12. `inputs/Golden-KM05.md`
13. `inputs/GG-KM05.md`
14. `inputs/FI-T05_early-post-discharge-follow-up-assessment-request-context.md`

## Review Questions

1. Does the proposed pre-chart draft create a fair forced slot, or will a strong model simply say "no post-discharge facts" and score high?
2. Is the draft too loud, too weak, or about right?
3. Does the prompt over-prime the model to audit the draft?
4. Do the golden and grader deltas protect the correct answer: source-limited, practical, and not empty refusal?
5. Are there any source-fact errors against the agent-read chart layer?
6. Does anything leak internal architecture, trap labels, FI IDs, or answer strategy into model-facing content?
7. What exact edits are required before any build?

## Current Proposed Verdict To Challenge

Clean KM05 is probably too easy. Escalated KM05 may work if the pre-chart draft is sticky enough to induce ratification of unverified interval status. Expected target after a good draft: mean roughly 62 to 72 with a real low tail. The biggest risk is the model catching the "no +7 facts" boundary immediately and scoring high.

## Boundaries

Review only. Do not build, upload, run AutoQC, run QA, create platform-current files, or mutate locked canon.
