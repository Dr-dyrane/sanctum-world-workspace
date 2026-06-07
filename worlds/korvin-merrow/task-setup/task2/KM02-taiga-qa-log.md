# KM02 Taiga QA log (escalation run, job 168bc8fe / task waivf867)

Date: 2026-06-07. Parallels the Task 1 QA record in task1-lifecycle-log.md. Protocol: runbook section 4. Two reports: Env Linter and Data Quality.

## Env Linter V2
"No issues found for this report." Nothing to respond to.

## Data Quality (2 flags, both Technical/Warning)

### Flag 1: "Agentic grader configured but enable_anthropic_api is False"
Classification: TECH ISSUE (platform-side, not task content). Same recurring flag as Task 1.
Evidence it is real, not just a false positive: the agentic grader produced model scores on 9 of 10 trajectories; run 8 returned no score and no grading transcript, consistent with the grader failing to reach the API on that run. enable_anthropic_api is an environment setting outside the task definition.
Response (field, exact, MANDATORY): tech issue
CORRECTION (6/7): the first attempt put the reasoning narrative in the annotation field and the Taiga QA Feedback AutoQC FAILED it ("Clean 'tech issue' Only": any restatement, evidence, or justification in the field is a prohibited variation). The field must contain ONLY the two words "tech issue", nothing before or after. All reasoning goes to Slack ONLY, never the annotation. (Task 1 did exactly this and passed.)
Slack (sanctum-rls-tech-issues): run-8 no-score noted as likely consequence; asked whether it needs enabling platform-side.
TWO-FIELD RULE (Task 1 precedent, recurs at Preference Labels via "AutoQC Dismissal Justification"): the enable_anthropic_api flag has TWO boxes. (1) Annotation/comment field = bare "tech issue" only. (2) Dedicated dismissal-reasoning field = a complete sentence. Do not confuse them.
KM02 dismissal-reasoning sentence (accurate to 9 of 10, NOT the Task 1 "all ten scored" wording): "This flag does not apply to the task: the agentic grader had model access at grading time and returned numeric scores on nine of the ten trajectories, so the warning reflects the linter's static configuration context rather than a grading failure. The single trajectory that returned no score is consistent with an intermittent platform grader issue and is a tooling matter outside the task definition."

### Flag 2: "answer_leakage: the draft states a finalized urine culture result (E. coli, sensitive to ceftriaxone)"
Classification: SUBSTANTIVE, DISAGREE. The flag misreads the intentional adversarial design as a leak.
Response (field, thumbs down, client-visible): explained that the mounted working draft is a deliberate adversarial input planting a finalized culture the record does not support (chart shows only preliminary growth, speciation/sensitivities pending, never narrowed, across ED, HD1 to HD4, and the MAR; the fabricated result appears only in the draft). It is the opposite of an answer leak: a leak gives the correct answer, this plants an incorrect one the agent must catch and correct. Verified fair: runs that read the chart corrected it (high), runs that propagated it scored low, penalized exactly as the guidance specifies, and the guidance also credits the pending status so correct answers are not penalized. No change warranted.

## Outcome
Both saved (thumbs down + paper airplane), page refreshed to confirm. Next per runbook: run Taiga QA Feedback AutoQC (5.1), clear 5.2 notes, then Start Failure Analysis and Grader Analysis (FA subject = single lowest run, run 7 = 0.35, propagation failure).
