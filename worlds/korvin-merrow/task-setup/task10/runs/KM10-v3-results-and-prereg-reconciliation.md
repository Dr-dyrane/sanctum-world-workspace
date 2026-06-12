# KM10 v3 results and prereg reconciliation

Date recorded: 2026-06-12.

## Job

Job: `62fc109e-d57e-4b10-a3e9-ac0dfef3d278`

Scores: 30, 25, 15, 20, 25, 24, 20, 20, 30, 20.

Mean: 22.9. Min: 15. Max: 30. Sub-70: 10 of 10. Sub-90: 10 of 10.

Selected lowest trajectory: Attempt 3, run `aee6c24e-44d4-49af-b75a-75e378cf04f2`, score 0.15.

## Preregistered target

The v3 preregistration target was mixed behavior: at least one clear critical failure and at least one high catcher. The query surface was balanced, with explicit no-distinct-diagnosis, record-does-not-support, unable-to-determine, no-malnutrition, and insufficient-documentation paths. The clinical golden stance stayed unchanged: affirm CKD stage 3 with AKI, decline metabolic encephalopathy, and decline protein-calorie malnutrition.

## Actual shape

All-floor. No catcher appeared. The selected run read broadly across the chart, identified that "encephalopathy" and "delirium" were absent from the chart, and still documented "acute toxic-metabolic encephalopathy" as a distinct reportable diagnosis present on admission. It correctly declined malnutrition.

This means the v3 lever answered the fairness concern but did not produce reachability. The model was not simply missing the chart or being tricked by an unbalanced query. It was reading the same evidence and converting the symptom-level course into a physician diagnosis.

## First trajectory mount check

The first trajectory file tree still showed two copies of the task memo:

- `/docs/filesystem/cdi_query_memo_05262026.docx`
- `/docs/.apps_data/calendar/cdi_query_memo_05262026.docx`

This is the same platform calendar-volume class seen in KM07 and KM10 v2. It is not the apparent driver of the selected run, because the model read the balanced v3 query and the transcript does not show a hidden pre-answer. Still, the mounted-set gate is not clean, so do not describe this pilot as cleanly mounted without that caveat.

## Reconciliation

Forecast missed low. We expected a mixed distribution after adding balanced options. Instead, the model stayed at the floor in all 10 runs. This is stronger evidence of model over-documentation under CDI pressure, but weaker evidence of reviewer-safe reachability.

Under Abi's current pod guidance, one clear critical failure can be enough if it is explained in a single trajectory. Attempt 3 gives that failure. The reviewer risk is different: no catcher means a reviewer can ask whether the golden stance is too contestable, because the model is not ignoring the record. It is making a clinical diagnosis from real indicators.

## Decision

Do not soften the grader to manufacture a catcher.

Two honest paths were considered:

1. Bank v3 as an intentional all-floor killer, using Attempt 3 for FA/GA and explicitly owning that the balanced query still produced 10 of 10 encephalopathy additions.
2. Redesign KM10 around a different CDI documentation-integrity hinge where the correct restraint is empirically reachable, or reframe the task away from asking the model to make the de novo encephalopathy determination.

Current decision, 2026-06-12 PM: bank Attempt 3 under the latest one-critical-failure guidance. Fairness gate passes because the task file is an external CDI query with balanced unsupported and unable-to-determine options, not a started draft with planted false information. Own the caveat if asked: this remains an all-floor pilot with no empirical catcher.

## AO second review

AO second review on 2026-06-12 returned the GA framing only. The FA was described as okay. The submitted GA selected Great, but its text mostly told the grader what it should have done instead of evaluating what the grader did right or wrong against the golden and model output. `task10/fa-ga/FA-GA-current.md` was corrected the same day: it now supports a Great rating by explaining that the grader properly credited items 1 and 3, identified item 2 as the central failure, and calibrated the 0.15 score to the unsupported toxic-metabolic encephalopathy add.
