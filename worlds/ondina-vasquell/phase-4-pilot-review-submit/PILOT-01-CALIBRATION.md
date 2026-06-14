# OV01 pilot-1 calibration and suite difficulty audit

Date: 2026-06-14. Source: OV01 pilot job 20965cc6 (10 trajectories) + task-difficulty-lessons.md + the OV01 grading transcript.

## OV01 pilot result: CEILING
Scores 96/92/92/82/92/95/95/95/92/92 (mean ~92). One 82, rest >=90, ZERO sub-70; the 82 is a strong answer, not a failure. No bankable miss. The 0.96 trajectory shows the model nailed every axis: renal-current dosing, the three held agents as explicit deferred restarts, deep-culture-over-swab, the sulfa exclusion, kept osteo/perfusion open, and CAUGHT the silent omissions (ferrous/cholecalciferol). This is a difficulty problem, not a grader problem (the grader scored an excellent answer correctly).

## Why (the model's profile, from the trajectory)
Reads all 35 files, cross-checks exhaustively, defaults to flagging rather than inventing, keeps open items open, excellent on every warm axis. So warm-axis + cautious-default = ceiling.

## The difficulty algorithm (apply to every task)
1. COLD - is the scored axis un-hunted (a background detail, not the deliverable headline or a loud world thread: osteo-not-established, perfusion-open, improving-but-unsafe, sulfa allergy, held agents)?
2. FORCED - one required wrong-able move (forced inventory / binding verdict / placeholder)?
3. AGAINST DEFAULT - does catching it require beating the model's reflex (caution, no-fabrication, systems-thinking, no-upcode) rather than being it?
4. VERIFICATION ASYMMETRY - a plausible wrong item inherited from a mounted doc that the model propagates without re-deriving?
5. FAIR + REACHABLE - floor is the model's own fault; a catcher is reachable (bimodal).

## Suite audit (predicted)
- CEILING / likely easy (warm + cautious-default): OV01 (confirmed), OV03 (osteo decline trivial), OV05 (sulfa allergy screaming-loud), OV08 (from-scratch warm perfusion), OV09 (systems-attribution IS the default; review genre anti-cold).
- MEDIUM: OV02 (forced inventory helps; osteo loud), OV04 (model integrates well), OV06 (forced verdict; not-safe well-supported), OV10 (completion+placeholder real if subtle).
- BEST FLOOR CANDIDATE as built: OV07 (quiet dated lookback/exclusion is a genuine cold axis).

Root cause: the world's central tensions are loud and the model is smart; we built the traps ON those tensions. Confirms the trap-correlation + warm-axis risk from PRE-PILOT-RECOMMENDATIONS.

## Recalibration: one COLD verification-asymmetry trap per task, distinct axis (all physician-ratified)
- OV01: VTE prophylaxis (enoxaparin) carried forward in the order set; correct = STOP at discharge (inpatient-only; bleeding risk with dual antiplatelet). Implemented for re-pilot.
- OV03: CDI presses a colder upcode than osteo (e.g., specifying AKI as ATN, unsupported).
- OV05: PBM offers a NON-sulfa substitute (fluoroquinolone) wrong for renal-dosing/not-culture-directed reasons - move the trap off the allergy.
- OV08: draft disposition table pre-fills "perfusion: adequate" (planted closure to catch).
- OV09: restructure to a forced-inventory with a cold contributor the model must surface.
- OV02/04/06/10: cold plant in the worksheet / denial / criteria / started draft.
- OV07: keep; verify the quiet date is truly missable.

## Other recalibrations to check after each pilot
1. Grader must FLOOR the cold miss (Section A/C name it a hard error), or even a floored run scores high (KM07 v3 noise).
2. Golden handles the cold trap (scores ~0.9 under its own grader = reachability anchor); physician-ratified.
3. Difficulty label + time estimate vs reality (OV01 spec said medium-high 25-35 min; actual 9.5 min / 0.96).
4. Prereg: lock a NEW prereg per re-pilot; reconcile the prior in a results record, do not edit the locked prereg.
5. Grader chart-access matched to mechanism (synthesis -> include_input_files=true); expect/justify the Self-Contained Guidelines flag.

## Sequence
Harden OV01 -> re-pilot -> confirm a bimodal spread with a real propagation (prove the cold-verification-asymmetry mechanism on this model) BEFORE re-centering OV02-10. Then replicate the validated pattern one task at a time, each re-piloted. Never batch-edit then pilot. OV07 may be piloted as-is in parallel.

## Codex addendum, 2026-06-14
Verdict: v2 enoxaparin is clinically fair, source-supported, and better than v1, but it is not a strong enough bet in its current surface. The task file still advertises the catch: "DRAFT - NOT RECONCILED," "pending reconciliation," "not yet reconciled against home medications or current renal function," and "MEDICATIONS CARRIED FORWARD." A careful model is being invited to audit every inherited row. VTE prophylaxis is also a familiar inpatient-only discharge-medication check, so the current package may still ceiling.

Recommended stronger version before re-pilot: keep the enoxaparin mechanism, but change the surface, not the grader. Make the task file look like a routine "Discharge medication orders, pending signature" document. Remove all "not reconciled" and "carried forward" language. Let the enoxaparin row blend with the continuation rows, for example: "Enoxaparin 40 mg SC daily, continue until mobility back to baseline." The prompt should force a row-level disposition: sign, revise, stop, or confirm before sign. Correct answer stops it. Floor run signs or continues it.

If that still all-catches, retire OV01 as the first floor probe and pilot OV07 next. OV07's quiet lookback or exclusion logic is colder than any obvious medication-reconciliation row in this world. Do not tighten the OV01 grader to manufacture spread; the next move is colder source geometry.

## De-telegraph implemented, 2026-06-14
Order set rewritten to a routine "DISCHARGE MEDICATION ORDERS" pending-signature surface: removed all DRAFT / NOT RECONCILED / pending-reconciliation / carried-forward language. Enoxaparin blended into the continuation rows as "continue until mobility returns to baseline"; the three held agents now read "Resume" (affirmative wrong, chart-contradicted). Prompt reframed to force a row-level disposition (sign / change / stop each, with a why). Grader and golden untouched (golden still discontinues enoxaparin; grader still floors continuing it). World MAR enoxaparin row unchanged from the prior revision. Filename initially kept, then de-telegraphed in the AO review pass (2026-06-14): renamed preliminary_discharge_order_set_05212026.docx -> discharge_medication_orders_05212026.docx because the path itself re-advertised the catch (AO lens 1a). That re-pilot step is now closed by the clean-mount rerun recorded below.

## AO/Abi-mode review pass, 2026-06-14
Ran the full nine-lens + mechanical Abi-mode review on the de-telegraphed v2 packet (record: abi-mode-review-OV01-2026-06-14.md). Fairness PASS (external order set + correction-licensing prompt). Two residuals caught and fixed: (1) the filename still read "preliminary" -> renamed; (2) golden source/rationale still called it "preliminary unreconciled" -> neutralized. Difficulty verdict UNPROVEN: the row-level reconcile-and-correct prompt is a known difficulty-killer (KM06), so a re-pilot ceiling remains plausible; OV07 fallback stands. Open before banking: golden self-score under its own grader (reachability anchor); first-trajectory mount-hygiene gate (find /docs, no .apps_data dup, no "preliminary" in path).

## Clean-mount rerun and final OV01 calibration, 2026-06-14

The clean rerun banked the v2 mechanism. Job `741ba52f-bae9-4594-a25c-ef5ae0e8bcdc` scored 68, 72, 40, 70, 72, 72, 50, 65, 78, 93. Mean 68.0. Four runs were sub-70, with hard floors at 0.40 and 0.50 and a catcher at 0.93.

Mount gate: first-trajectory `find /docs` showed one order set, `discharge_medication_orders_05212026.docx`, under `/docs/filesystem`, 34 world files, no `/docs/.apps_data`, and no `preliminary` file. The prior bimodal job `9765ba91` is excluded from shipping evidence because it mounted two same-purpose task files. The old ceiling job `20965cc6` remains historical pre-v2 evidence.

Disposition: OV01 is now bankable. The validated floor is the model carrying inpatient-only enoxaparin into discharge, or leaving it alive as confirm, despite the chart supporting only inpatient prophylaxis and the patient already taking aspirin plus clopidogrel. Use `OV01-results-and-prereg-reconciliation.md` as the clean results record and `fa-ga/FA-GA-OV01-current.md` as the current FA/GA draft.

## Suite recalibration status, 2026-06-14 (workspace recalibration)
OV01 banked, so the suite recalibration now proceeds one task at a time, each re-piloted, never batch-edited. The VALIDATED TEMPLATE to replicate on OV02 to OV10: one cold verification-asymmetry plant on a distinct axis (physician-ratified, coding/clinically accurate, chart-grounded as wrong, not a KM duplicate), kept off the loud world threads; a de-telegraphed routine surface on the task file; a single plain Filesystem task file with a clean filename and the first-trajectory `find /docs` mount gate; grader floors the cold miss; golden self-scores high; a NEW locked prereg per pilot; and a two-paragraph failure-only FA/GA. Warm secondary misses may remain, but the cold plant is the floor lever.
- OV01: DONE (banked).
- OV02: IN PROGRESS. Decision: recalibrate-now (v1's osteo-POA and pressure-injury steers are both warm -> predicted ceiling). Cold-plant candidates drafted in `OV02-recalibration-plan.md` (lead = acute-blood-loss-anemia upcode vs the stable Hgb 9.8 trend); awaiting Alexander ratification before any build.
- OV03 to OV10: queued; recalibration axes pre-assigned in the Recalibration section above; OV07 may be piloted as-is in parallel.

## Workflow remap status (verify live before Step 10, per DO-NOT-REPEAT #13)
Canonical source: `WORKFLOW-MAP.md` / build_task_packages.py WORKFLOW. Four originals were retired 2026-06-13 and remapped: task1, task3, task8, task9. OV01's remap is CONFIRMED LIVE - the Studio task screen showed Workflow = "Medication Reconciliation at Care Transitions". OV02's workflow is "Inpatient Medical Coding and DRG Assignment" (P0, unchanged, not on the retired list); still verify it on the live Task Selection Categories sheet at Step 10 before selecting, since the menu is volatile.
