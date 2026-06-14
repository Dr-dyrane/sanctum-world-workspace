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
