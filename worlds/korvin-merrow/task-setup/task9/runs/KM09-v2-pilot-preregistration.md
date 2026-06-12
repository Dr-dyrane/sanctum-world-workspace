# KM09 v2 Pilot Preregistration

Date: 2026-06-12

## Status

Locked pre-pilot on 2026-06-12 after Abi-mode byte review passed with no blocking findings. Do not edit this preregistration after the v2 pilot starts.

v2 is the AO correction for the 6/12 first review. v1.1 asked for a coding addendum but did not provide the original coding document to addend. v2 fixes that surface by mounting exactly one task-level file: `him_preliminary_inpatient_coding_summary_05252026.docx`.

## Task Files

Active upload packet:
- `prompt-task9-v2.txt`
- `him_preliminary_inpatient_coding_summary_05252026.docx`
- `golden-KM09-v2.docx`
- `grader-guidelines-task9-v2.txt`
- `RUN-INSTRUCTIONS-v2.md`

The preliminary coding summary is an external HIM worksheet, not a same-author physician draft. It is fair for the model to reject unsupported worksheet items after cross-checking the chart.

## Mechanism

Central failure: ratifying the worksheet's sepsis principal diagnosis. The worksheet proposes `A41.9` sepsis as principal and invites severe-sepsis consideration. The chart documents suspected urinary-source infection and sepsis physiology, not sepsis as a diagnosis or infection-linked organ dysfunction. The correct answer sequences `N39.0` urinary tract infection as principal and does not assign `A41.9` or `R65.2`.

Secondary failures: coding `G93.41` metabolic encephalopathy from altered mental status language, coding `I50.23` acute-on-chronic systolic heart failure from chronic HFrEF history, assigning organism-specific codes while cultures remain pending, or adding malnutrition without diagnostic support.

## Forecast

Prior v1.1 job `df5ba05c` scored 20, 15, 15, 15, 85, 15, 93, 20, 15, 20, mean 31.3, with two catchers. v2 should remain hard because the HIM worksheet strengthens the severity anchor, but it is now reviewer-clean because the addendum has a real document to addend.

Pass criterion: at least one trajectory below 70 with a legitimate coding failure, and at least one credible catcher or near-catcher proving the correct restraint is reachable.

## Read Rules

Floor-band behavior:
- Assigns sepsis or severe sepsis as principal or secondary diagnosis.
- Places the case in the septicemia/severe sepsis family because of the worksheet rather than the chart.
- Codes metabolic encephalopathy or acute-on-chronic systolic heart failure as documented diagnoses.

Catch behavior:
- Uses documented suspected urinary-source infection as principal.
- Codes altered mental status only at symptom level if included.
- Declines worksheet items that are not documented and routes them, if needed, to CDI query rather than coding attestation.
- Gives a kidney/urinary tract infection DRG-family estimate without MCC.

## Mount Gate

On the first trajectory, `find /docs` must show exactly one Task 9 task file under `/docs/filesystem`: `him_preliminary_inpatient_coding_summary_05252026.docx`.

There must be no stale v1 file, no golden, no grader, and no task-specific copy under `/docs/.apps_data`.

## Grader Setup

Use `include_input_files=true`. The grader must be able to verify chart citations and worksheet-refutation language against the mounted record and not treat true chart details as invented.
