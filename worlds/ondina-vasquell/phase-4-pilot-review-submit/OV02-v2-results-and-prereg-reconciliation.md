# OV02 v2 results and prereg reconciliation - PROVISIONAL (transcript pending)

Date: 2026-06-14. Reconciles the locked `platform/task2/current/OV02-v2-pilot-preregistration.md` against the first clean-mount pilot. Locked prereg not edited.

## Job
afa44ac7-72b5-4166-a73a-17c96a7d2fc8. Scores: 93, 92, 93, 88, 83, 62, 92, 82, 95, 90. Mean 87.0. One sub-70 (0.62, attempt 6, run 9b415de9). No hard floor.

## Mount gate: CLEAN
First-trajectory `find /docs`: one worksheet `him_preliminary_coding_worksheet_05212026.docx` under `/docs/filesystem`, no `/docs/.apps_data`, no duplicate. Mount hygiene held (DO-NOT-REPEAT #16 applied from the start).

## Verdict: NOT BANKABLE (near-ceiling); the cold anemia plant ceilinged
The lowest run (0.62) EXPLICITLY rejected the acute-blood-loss-anemia plant (Hgb flat 9.8, no bleeding -> D63.1 anemia of CKD), and also declined osteo and pressure-injury. If the lowest run caught the plant, the higher runs did too: no run floored on the designed mechanism. The cold plant is not cold enough for this genre.

Root cause = the KM06 fully-reconciling lesson. A coding attestation is an inherently line-by-line "verify every proposed code against the chart" genre, so a fabrication-style plant (a code contradicted by a value already in the chart) is checked and rejected almost every time. Only a JUDGMENT trap (a binding call that stays wrong-able after full reconciliation) survives this genre - the same reason OV01's reconcile-and-correct prompt was a difficulty-killer.

## The single sub-70 is NOISE, not signal - CONFIRMED via the attempt-6 grading transcript
The 0.62 grading transcript (read 2026-06-14) shows the grader judged the content "excellent," "would have merited ~0.9+ against the golden," and credited the correct anemia (D62->D63.1), osteo, and pressure-injury calls. It scored 0.62 SOLELY because the run answered inline and did not save a file to /tmp/outputs (the harness instruction). Not a clinical miss; not the designed mechanism. (My earlier over-specification hypothesis was wrong; the actual driver was the missing saved file.)

## Cross-cutting finding: file-output noise affects the whole suite
The task prompt is conversational ("give me your attestation line by line") but the platform harness says "Output files MUST be saved in /tmp/outputs/." Runs that answer inline get docked regardless of clinical quality. This also nicked OV01's 0.40 run (noted in FA-GA-OV01-current.md GA) but did not dominate there because OV01 had a real clinical floor. On OV02 it IS the only sub-70. This noise can fake or mask floors across every task and should be addressed world-wide (standardize the deliverable expectation, or have graders not weight output location for a conversational deliverable).

## Verdict: NOT bankable; mechanism ceilinged
Coding attestation is strong-for-this-model and fully-reconciling; the anemia fabrication plant ceilinged. Real clinical spread is all >=0.82. The 0.62 is a file-save artifact. Do NOT tighten or loosen the grader to manufacture/erase spread without a deliberate decision.

## Decision put to Alexander 2026-06-14 (pending)
Option 1: re-center OV02 on a JUDGMENT trap that survives full reconciliation (the only thing that floors this genre; risks KM09 overlap; coding-judgment traps historically land ~0.86 mean). Option 2: set OV02 aside as a medium/competence task and pursue the next hard floor on OV07 (genuine cold lookback). Either way: address the file-output noise suite-wide.
