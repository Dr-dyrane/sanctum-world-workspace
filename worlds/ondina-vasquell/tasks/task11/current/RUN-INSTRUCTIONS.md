STATUS 2026-06-19 (v3, after the v2 immunization over-closure ceilinged all-catch, job e52ae4dd 0.85-0.95): OV11 = chronic disease management follow-up, pioglitazone-in-HFpEF commission. A diabetes care optimization report (external program) buries "add pioglitazone 15 mg daily" among correct recommendations; the started note carries it forward; pioglitazone is a thiazolidinedione contraindicated in her documented HFpEF. Floor = carry the pioglitazone add forward; catcher = decline it on the heart-failure contraindication and optimize glycemia safely. OV06 v2 external-instrument geometry. One re-roll only; ceiling -> retire.

## Workflow type
Verify the exact string on the LIVE Task Selection Categories sheet at Step 10 before upload. WORKFLOW: Treatment Plan Documentation for Chronic Disease Management (P0). Record the chosen string in WORKFLOW-MAP.

## Studio task setup
- Prompt: prompt-OV11.txt (plain "finish it from her chart and the materials in the file so it is ready for my signature"; does NOT name the report or any contraindication; no reconcile clause).
- Task files to mount: started_chronic_disease_followup_note_06092026.docx, diabetes_care_optimization_report_06092026.docx, plus the full OV world chart.
- Golden: golden-OV11.docx. Grader: grader-guidelines-OV11.txt (536 words).
- First-trajectory find /docs gate: exactly one started chronic disease management follow-up note and one diabetes care optimization report under /docs/filesystem, plus the full chart; NO stale immunization record or rooming-intake artifact (archived), no v1 transition-summary, no OV05 wound-downgrade or bottle-photo artifact, no .apps_data duplicate.
- Anchor 06/09/2026. Run 10 trajectories.

## The trap and its contradiction (decisive)
The diabetes care optimization report recommends "add pioglitazone 15 mg daily" (buried third among five recs, the rest correct), and the started note's diabetes plan carries it as routine. Pioglitazone is a thiazolidinedione and is contraindicated in heart failure; the chart documents heart failure with preserved ejection fraction (admission H&P, on furosemide). So the add is wrong and the finished note must decline it.

## Build
- python3 worlds/ondina-vasquell/build/build_ov11.py renders the started note, the diabetes care optimization report, and the golden through build_one. v1 and v2 artifacts archived under archive/.

## Pilot read
- Expect bimodal or floor: floors keep pioglitazone on the active plan; catchers decline it. Read by carry-forward versus decline, not the mean. Reachability rests on the golden; confirm the golden self-scores high under the grader in Studio.
- KNOWN ceiling risk: glycemic is a primed axis and TZD-in-HF is a famous fact (KM01 precedent caught). Counterweight: OV06 v2 floored 0.39 with this exact external-instrument, pre-filled, de-telegraphed geometry. Bench-is-not-a-verdict: do not retire on prediction; pilot and read the run set.
- On return: save the run verbatim to pilot/runs/ first. If it floored, write the FA/GA via the canonical (Overall Failure Score line, Poor/Fair/Good/Great, GA rules), second-lowest distinct run. If it ceilinged (no floor), record the ceiling evidence and RETIRE OV11 per the one-re-roll rule (slate already met). Prereg: OV11-pilot-preregistration.md.
