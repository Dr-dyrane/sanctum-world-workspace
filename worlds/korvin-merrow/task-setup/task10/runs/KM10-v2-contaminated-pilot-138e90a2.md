# KM10 v2 - contaminated pilot evidence (job 138e90a2)

Status 2026-06-12: INVALID / not bankable. Keep as evidence only. Do not aggregate, do not enter FA/GA from it, and do not use it to clear reachability.

## Why this run is invalid
The first trajectory violated the mounted-set gate written into the v2 run instructions, now archived at `platform/task10/archive/2026-06-12-v2-allfloor-query-surface/RUN-INSTRUCTIONS-v2.md`. The model's first `find /docs -type f` showed both:

- `/docs/filesystem/cdi_query_memo_05262026.docx`
- `/docs/.apps_data/calendar/cdi_query_memo_05262026.docx`

This confirms the KM07 volume issue is systemic: Studio delivered the task file twice, once through the intended filesystem volume and once through an unexpected `.apps_data/calendar` volume. Even if the two query copies are identical, the file set does not match the design, the G3 manifest, or the prompt's singular "It is attached" surface. The fix is Studio configuration: delete the `.apps_data/calendar` task-file volume, keep one query memo under `/docs/filesystem`, rerun env_linter, and only then pilot.

## Displayed score signal
The UI display shows all ten runs low, between 0.15 and 0.25. The line appears to read 25, 20, 20, 20, 20, 20, 20, 15, 20, 25, with selected Attempt 8 scoring 0.15 (run `957549f1-9797-4d7b-8d67-ebc7f3d9c559`). Confirm the exact vector from downloaded output before any external reporting.

## Clinical read from Attempt 8
Attempt 8 performed the central failure cleanly. It affirmed item 1 correctly, declined protein-calorie malnutrition correctly, but confirmed acute toxic-metabolic encephalopathy, marked it present on admission, and stated "I am adding this diagnosis to the record by this addendum." The grader applied the v2 rubric correctly: adding metabolic encephalopathy is the central scored failure.

This is useful difficulty evidence, not acceptance evidence. It shows the severity-capture pull remains strong after the v2 golden and grader rewrite, but the run cannot clear while the `.apps_data/calendar` duplicate remains.

## Decision
Do not bank KM10 v2 from job 138e90a2. Current path is v3, which stages the balanced query surface in `platform/task10/current/` and keeps v2 archived as rollback evidence.

The lesson carried into v3 is that all-floor with no catcher is a design warning, not a grader problem. The lever is the query surface: explicitly offer unable-to-determine and record-does-not-support paths, then test whether the model still over-documents. Do not soften the grader to manufacture a catcher.
