# Ondina Vasquell - pre-pilot recommendations (HOLD until live)

Date: 2026-06-13. Status: **DO NOT ACT YET.** The spec is in human review. These are staged for the Step-10 task-setup phase and are actionable only after a spec GO. Nothing here changes a shipped artifact today; it is the plan for when tasking opens.

Source basis: a top-down audit of the KM run against this world, grounded in `docs/task-difficulty-lessons.md`, `docs/world-pipeline-playbook.md`, `DO-NOT-REPEAT.md`, and the OV spec + task data.

## The framing this rests on
Two independent axes govern every task: DIFFICULTY (does the idea floor a strong model on a cold, chart-contradicted, forced, anti-default axis) and FAIRNESS (is the floor the model's own fault). A task ships only when it is BOTH. KM was bounced from both directions: too-easy ceilings (KM05-NSAID 95, KM06-orthostatic 93, KM08v3 96) AND unfair floors (KM05v4-pilot1 20, KM07v2 36). A high score is not the goal and a low score is not the goal; a fair, bankable, legitimate failure is.

Where OV stands: structurally ahead of KM (structures-first variety across 10 distinct workflows, mostly wrong-by-genre external task files that are fair without a fix, single-source-of-truth + determinism against canon drift) but empirically unproven (zero pilots) and trap-correlated (osteo / perfusion / renal-current-dosing recur across many tasks).

## The governing principle
Never bank a task on a contestable verdict. An equivocal judgment trap (osteo "cannot exclude," perfusion "genuinely uncertain") drifts to the TOO-EASY quadrant if the golden makes the call obvious, or to the UNFAIR quadrant if the golden floors the defensible opposite. Bank instead on what the chart contradicts or mandates; keep the equivocal item genuinely open in the golden and CREDIT that restraint in the grader.

## Recommendations, in priority order

1. **Pilot OV01 before replicating OV02-10.** Difficulty is the one axis that cannot be eyeballed; KM measured all ten. Lock the prereg first, run, read the trajectory content (not the mean), confirm a real bankable failure. Replicate only if the pattern holds. Saves nine rebuilds if it does not.

2. **De-correlate the traps.** Give each task ONE distinct primary axis the chart contradicts; demote the shared world traps (osteo / perfusion / renal) to secondary texture. In piloting, confirm tasks fail INDEPENDENTLY - high cross-task score correlation means one task built ten times (KM monotony in disguise).

3. **Convert judgment traps into forced moves on chart-contradicted axes.** Per task, force the move where the record actually contradicts or mandates: renal-dosed regimen off the CURRENT creatinine (not the admission peak), deep-culture-over-swab hierarchy, the dated quality-measure finding, or the wrong-by-genre external document (agree-or-rebut). Score the consequence, not the osteo/perfusion verdict; keep those open.

4. **Rebuild Task 9's (safety review) trap placement.** A review genre is anti-cold - reviewing is verifying, so a headline trap is caught universally (KM06-orthostatic, 93, killed). Either move the scored miss to a cold background section, or use the fair safety-review structure that forces system-cause vs individual-blame rather than a headline catch.

5. **Split golden-authorship from grader scrutiny; Alexander owns the contestable calls.** Same author wrote golden and grader, so the grader fits the golden. Stress-test each grader against an adversarial-but-correct trajectory (does a differently-worded correct answer still score full?). Confirm the golden scores ~0.85-0.95 under its own grader (proves a catcher is reachable -> bimodal, not an all-floor gotcha). Make the grader explicitly credit keeping the trap item open.

6. **Match grader chart-access to mechanism; verify task-file fairness on built bytes.** Synthesis-from-chart -> chart-aware grader (chart-readable grading); planted-artifact catch -> golden-only. Confirm every task-level draft is a TRUE placeholder (asserts nothing about the scored item), exactly one visible task file per task, verified on extracted bytes - no leak via filename or duplicate mounted volume.

## Platform-guidance items deferred (added 2026-06-14)

Decision (Dyrane, 2026-06-14): OV already satisfies both current hard rules - no future-dated material (latest date 06/11/2026, before today) and English-only (patient is Spanish-preferred as a profile attribute; no Spanish-language file content). Two pieces of new pod guidance are parked, each at its CORRECT layer (clarified 2026-06-14: the date shift hits the TEMPLATE/WORLD files, which lock at world generation; the TASK files are the flexible layer, rebuilt at tasking):

1. Pre-July-2025 date shift (Abi, 2026-06-13; soft preference for not-yet-tasking worlds) - TEMPLATE / WORLD-FILE LAYER, do BEFORE world generation, NOT at tasking. The world files (EW1-EW31, WS1-WS3) carry the dates and lock when the world is generated (Stage 7), so if we pursue the shift it must happen on these owned files first: apply a UNIFORM delta to the clinical_data milestone dates so every interval holds, rebuild all world files + the spec + filenames deterministically, then re-verify the T7 HEDIS measure window and the EW28 eye-exam lookback in the new window (the one physician checkpoint - the rest is mechanical). The task-level files (E1-T*) carry dates too but are rebuilt at tasking, so they inherit the shifted window then - no separate now-action. This is OPTIONAL: the hard no-future-date rule is already met; this is only the soft pre-cutoff preference. If pursued, sequence it after spec approval and before Stage-7 generation.

2. Workflow remaps for the four closed workflows (Ed/Abi, 2026-06-13) - TASK LAYER, at Step 10. Re-pick each from the LIVE Task Selection Categories sheet (our 06/10 snapshot is stale - priorities already drifted). Affected and candidate open swaps: T1 Discharge Med Recon -> Medication Reconciliation at Care Transitions; T3 CDI Query Response Review -> CDI-Coding DRG Reconciliation Review or CDI Query Response Tracking & Follow-up; T8 Specialist Referral Letter -> Care Coordination Referral Tracking & Closure or Referral Intake/Triage; T9 Patient Safety Event -> Patient Safety Indicator (PSI) Analysis or NPSG Compliance Monitoring. T8 and T9 swaps shift task framing slightly. Keep the unsubmitted designs (Ed: do not delete closed-workflow drafts; they may reopen).

## Through-line
2-4 tighten the design before any run; 1 is the only step that tells you whether it worked; 5-6 are the fairness and grader gates KM paid for. Do none of it until the spec clears review and tasking is authorized.
