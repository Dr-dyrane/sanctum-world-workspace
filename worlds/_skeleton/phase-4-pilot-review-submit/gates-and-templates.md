# Phase 4 - Pilot, review, submit

Order: lock the prereg, pilot, read by rule, bank or reshape, then FA/GA, three preference labels, Abi-mode review, AutoQC, submission. Nothing here proceeds without the writer's explicit authorization for that exact step.

## Preregistration (before every pilot, never edited after)

Lock a prereg per task in `phase-4-pilot-review-submit/` with: the mechanism under test, the honest forecast (mean, bimodal split), and the READ RULES (what counts as FLOOR vs CATCH per trajectory, the legitimate-failure bar, and the all-floor and all-catch branches). The KM lesson: a pilot run under a -DRAFT prereg forces a post-hoc reconciliation; title it locked before the run.

## Reading the pilot

- Verdict by per-trajectory disposition, not the headline mean (King 6/12: the score is evidence, not the verdict).
- A task banks on at least one LEGITIMATE failure that materially degrades the deliverable or creates patient-harm, compliance, or malpractice exposure. Cosmetic misses do not count.
- Difficulty gate: every task needs at least one genuine sub-90 clinical failure; all >=90 is too easy and cannot bank.
- Reachability (Abi Lens 7): a bankable deep task is bimodal, real floors plus a catcher near 0.85 to 0.95, OR a structural proof that the golden self-scores high under its own grader. All-floor with no catcher is an unfair gotcha unless reachability is proven.
- Mount-coherence gate on trajectory 1: exactly the intended task files under /docs/filesystem, nothing task-specific under /docs/.apps_data. The calendar-volume duplicate invalidated KM07 v4 and KM10 v2; fix the Studio volume, do not rename around it.

## FA / GA (failure-only, natural prose)

- FA: the single lowest genuine-failure run; what the MODEL did poorly. GA: what the GRADER did right or wrong in scoring that output against the golden (descriptive, not prescriptive; do not tell the grader what to do). Each part under about 1000 characters, complete sentences, no bullets, no headers, no section names. Template: `reference/templates/FA_GA.md` and `reference/source/FA_GA Template [05_14_26].docx`.

## Preference labels (three per task, each a different trajectory)

- Compare A and B against the golden on five dimensions (prompt adherence, correctness, completeness, methodology, quality and clarity). Scale A4-B4: tier 4 overwhelmingly better, tier 3 falls for a central designed trap or misses a critical finding, tier 2 avoids an error the other makes, tier 1 both close on a narrow point. Both-floor pairs are severity comparisons, tier 1 when the difference is degree, tier 2 only when one output is materially safer. Confirm the rating and paragraph tell the same story. Template: `reference/templates/Preferential Labeling.md`.

## Abi-mode pre-review (catch it in-house first)

Run the nine-lens protocol in `docs/abi-review-protocol.md` against the built packet before declaring it ready: model's-seat fairness and the built-artifact rule, genre purpose, answer-the-why, voice anchor, structural realism, answer-giving scaffolding, difficulty and symmetric spread, alignment-after-change, mechanism precision. Output to the task's `qa/`.

## AutoQC and submission

- Self-QC with the AutoQC writer templates (`reference/templates/AutoQC_Section_*`) before upload: Blockers, then Majors, then Minors.
- Resolve or dispute every finding before the next gated step; rerun N failing only, never full reruns.
- Submission package requirements: `reference/world-spec-guidelines/10_submission_package_requirements.md`, `12_required_upload_inventory.md`, `11_transcript_requirements.md`.

## Standing boundary

No upload, AutoQC, agent run, QA response, FA/GA, preference label, or platform mutation without the writer's explicit authorization for that exact step.
