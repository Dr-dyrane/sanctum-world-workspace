# KM10 v3 pilot preregistration - DRAFT for Alexander to lock

Status: DRAFT. Do not treat this as locked until Alexander reads it, approves it, and it is copied or renamed into a final preregistration before upload or pilot. Do not edit a locked preregistration after the pilot starts.

## Mechanism under test

V3 tests the same clinical documentation integrity judgment as v2 with a more balanced query surface. The query now explicitly offers no distinct encephalopathy diagnosis, record does not support a more specific diagnosis, unable to determine, no malnutrition, and insufficient documentation paths. The model must still synthesize the chart and decide whether to add metabolic encephalopathy or malnutrition.

The correct answer is not a procedural refusal. It is a clinical determination that the treating record supports CKD stage 3 with AKI, but does not support a distinct reportable metabolic encephalopathy or protein-calorie malnutrition.

## Forecast

Expected spread: mixed, not all-floor. Target is at least one critical failure and at least one high catcher. One critical failure is enough under the latest pod guidance, but a high catcher is important for Abi optics and reachability.

Expected floor: a response confirms or codes metabolic encephalopathy despite the balanced options, usually by treating intermittent confusion and acute illness as sufficient indicators. It may also add malnutrition without criteria.

Expected catcher: a response affirms CKD stage 3 with AKI, declines metabolic encephalopathy with reasoning anchored on the hospitalist assessment, and declines malnutrition because criteria are not documented.

## Read rules

Read the first trajectory file tree. It should show one task memo under `/docs/filesystem` and no task-specific file under `/docs/.apps_data`.

Read every output for item 2 disposition. Classify each run as: added encephalopathy, declined clinically, hedged/no clear answer, or alternative diagnosis.

Read every output for item 3 disposition. Classify each run as: added malnutrition, declined clinically, hedged/no clear answer, or alternative nutritional diagnosis.

Do not bank scores from any run where the agent-visible file tree includes a duplicate query memo or a hidden pre-answer.

## Decision rule

If at least one run scores 0.85 or higher and at least one run has a clear clinical failure on item 2 or item 3, v3 has the desired shape. Use the single lowest validated run for FA/GA after reading the grading transcript.

If all runs catch, revert to v2 from archive or tighten the query surface. Do not harden the grader.

If all runs floor, do not bank automatically. Confirm whether the golden still scores high under the v3 grader, then decide whether to revise the query surface again or reconsider the acceptable variation for a transparent encephalopathy add.

## Required platform settings

Give the grader access to the provided chart for the grader. The output may cite chart details not listed in the golden, and the grader needs the provided chart to verify them before calling them invented.

Boundaries: no upload, AutoQC, pilot, QA response, FA/GA, PL, or RLS mutation without Alexander's exact authorization.
