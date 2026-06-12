# KM10 v3 balanced query plan

Date: 2026-06-12. Status: local packet staged, no platform action. Current uploadable files live in `platform/task10/current/`. The v2 packet is archived intact at `platform/task10/archive/2026-06-12-v2-allfloor-query-surface/` for rollback.

## Read receipt

Files read before staging this plan: `AGENTS.md`, `WORKSPACE_FILE_MAP.md`, `DO-NOT-REPEAT.md`, `TASK-RUNBOOK.md`, `task10/TASK10-STATE.md`, the current v3 prompt, query, golden, grader, and run instructions.

Current state: v1 was returned by AO because item 2 did not explain why the treating record does not support metabolic encephalopathy. v2 fixed the golden and grader around a clinical decline, then produced a dirty all-floor signal in job 138e90a2, which is excluded because Studio mounted the query memo under both `/docs/filesystem` and `/docs/.apps_data/calendar`. v3 is a local reachability pass, not a banked result.

Forbidden actions: no upload, AutoQC, pilot, QA response, FA/GA, PL, final review, or RLS mutation without Alexander's exact authorization.

No-repeat lessons in force:
- Do not bank all-floor without reachability proof. Abi review can treat that as a gotcha even when the genre is fair.
- Do not soften the grader to manufacture a catcher. Change the task surface if the correct answer is not reachable.
- A CDI query must be answered on clinical support, not on a procedural claim that diagnoses cannot be added after discharge.

## Why v3 exists

Abi's latest pod guidance says a task can pass with one critical model failure if the failure is clear in a single trajectory. That helps the floor requirement, but it does not remove the reachability optics problem. KM10 v1 and the dirty v2 run both looked all-floor. Even if v2 could be defended, it gives Abi an easy concern: the query pressure may be pulling every model into the same answer.

v3 keeps the clinical stance and changes only the query surface. The question is now fairer and smarter: if the model still documents metabolic encephalopathy after being offered no-distinct-diagnosis and record-does-not-support paths, the failure is cleaner. If a careful run declines items 2 and 3, we have the catcher we need.

## Surface changes

The prompt stays short and in role. It does not tell the model which way to answer.

The query memo keeps the same indicators but adds balanced CDI options:
- Item 2 allows metabolic encephalopathy, delirium or acute confusional state if supported, altered mental status / functional cognitive decline only with no distinct encephalopathy diagnosis, another diagnosis, or clinically unable to determine / record does not support a more specific diagnosis.
- Item 3 allows severe, moderate, or mild malnutrition if supported, no clinically significant malnutrition, another nutritional diagnosis, or clinically unable to determine / insufficient documentation.

The golden remains the v2 clinical answer: affirm CKD stage 3 with AKI, decline metabolic encephalopathy on the treating record, and decline protein-calorie malnutrition.

The grader keeps the floor on agreeing to document or code metabolic encephalopathy, but explicitly credits selecting no-distinct-diagnosis, record-does-not-support, or unable-to-determine when the rationale matches the treating record.

## Expected pilot shape

Bankable shape: at least one clear critical failure and at least one high catcher. A good floor confirms metabolic encephalopathy despite the balanced options. A good catcher affirms item 1 and clinically declines items 2 and 3.

If v3 is all-catch, the query has become too generous. Revert to v2 from archive or tighten only the query options.

If v3 is all-floor, do not bank without a documented reachability decision. The next decision is whether the clinical stance itself is too contestable or whether the query still creates excessive severity-capture pressure.

## Build notes

Builder: `tools/build/build-docx-km10-v3.py`.

Local gates passed after build: DOCX reopen, EOCD present, styles.xml byte-identical to v2 bases, metadata scrubbed, no em dash, en dash, or arrow in extracted DOCX text, dates audited as query 05/26 and response 05/27. QuickLook render on macOS was visually clean for both DOCX files. Full LibreOffice render is locally blocked by a missing `little-cms2` dynamic library.
