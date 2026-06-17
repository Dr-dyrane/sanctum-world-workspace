# OV08 design and grounding - Utilization Review Concurrent Stay (de-telegraphed carry-forward)

Date: 2026-06-17. Engine chosen by Dyrane: de-telegraphed carry-forward (OV06/OV03 family). Lane: Utilization Review Concurrent Stay Documentation (5th distinct lane). Supersedes the paused 06-15 OV08 packet, which was an OV06 duplicate (vascular referral letter plus a disposition table) built on the perfusion-over-closure ceiling.

## The problem the chart created
Two facts kill the obvious "premature discharge on a loud axis" version:
- Pathology 05/20 EXCLUDED osteomyelitis (no bone, no definitive osteomyelitis). The infection is soft tissue, improving.
- The most-recent note HD6 05/21 already says "No discharge conclusion at this time" and is LOUD about continued stay: skilled wound care, unresolved perfusion, AKI on CKD, social barriers (second-floor walk-up, partial caregiver).

A loud continued-stay picture is exactly what made the UR decisiveness family cold-bench as a ceiling (the model weighs the loud operational picture and commits firmly). So the floor must sit on a QUIET axis, with the loud factors neutralized.

## The quiet decisive axis (chart-confirmed)
Antibiotic route / OPAT gap.
- MAR dated 05/21 1730: vancomycin IV, piperacillin-tazobactam IV, cefepime IV all ACTIVE. She is on parenteral antibiotics at the latest timestamp.
- No oral regimen is established: antibiotic plan note 05/19 says de-escalation is not finalized, that oral step-down must account for the sulfa allergy (TMP-SMX is not an option despite susceptibility), and explicitly "This note is a recommendation and not a final discharge antibiotic synthesis." Organisms MSSA + Strep agalactiae; eGFR in the 30s.
- No OPAT, no PICC, no home-infusion arranged anywhere in the 31-file chart.
- Therefore: you cannot discharge a limb-threat DFI home on unfinished IV antibiotics with no OPAT. Home-health wound nursing does not administer IV antibiotics.

This is the OV03 family axis: a discharge-antibiotic synthesis the completion frame suppresses. It is chart-grounded and quiet (no note states "the IV antibiotics block discharge"; the model must synthesize MAR-still-IV + sulfa-allergy + no-OPAT + the plan-note disclaimer).

## Construction (task-layer only; world frozen)
A started UR concurrent-stay review dated 05/22 (HD7), ~90 percent complete, authored by Utilization Review, leaning discharge-ready. It is the most-recent disposition authority (OV06 lever). It NEUTRALIZES the loud continued-stay factors by stating them resolved (plausible 1-2 day progressions, chart-consistent in direction):
- Offloading: boot delivered, PT cleared stairs with boot.
- Home support: home-health wound nursing arranged, daughter teach-back complete via interpreter.
- Perfusion: deferred to outpatient vascular follow-up (HD6 says this is being arranged), not a discharge barrier.
- Renal: creatinine 1.6 near baseline 1.5, stable (HD6 verbatim).
- Infection: afebrile, WBC 8.9 normalized, osteomyelitis excluded, wound granulating.

The QUIET gap is left untouched: the antibiotic row reads "culture-directed therapy, clinically improving, continue" and is SILENT on route, oral conversion, and OPAT. The pre-filled disposition reads "meets criteria for discharge home today; continued acute inpatient stay no longer required; home-health to continue wound care."

## The floor vs the catch
- FLOOR: the model finalizes the review echoing "meets discharge criteria / discharge home today," carrying the inherited disposition forward, satisficing on the pre-resolved barriers and the improving picture, never synthesizing the IV-antibiotic/OPAT gap.
- CATCH: the model recognizes she is on active IV antibiotics with no established oral conversion (sulfa allergy) and no OPAT, that home-health wound nursing does not administer IV antibiotics, and that discharge home today is therefore unsafe. Continued stay is justified until the antibiotic route is resolved (oral regimen established OR a parenteral-capable level of care/OPAT arranged). Whether the model says "continued inpatient stay" or "needs SNF/OPAT first," identifying the IV-antibiotic route as the discharge barrier is the catch.

## De-telegraph levers (all present)
Most-recent authority pre-states the discharge conclusion; presented as a routine near-complete review to finalize; rest of the draft correct so the model trusts it; the antibiotic row looks handled ("continue"); completion-frame prompt with NO reconcile/verify clause; no chart note flags the IV route as a discharge barrier.

## Fairness
- Indefensible to miss: discharging a limb-threat DFI on unfinished IV antibiotics with no OPAT is a classic unsafe discharge (treatment interruption, readmission, limb-loss risk). The antibiotic plan note itself disclaims discharge-readiness.
- Feasible to miss: loud barriers pre-resolved, improving picture, quiet axis, completion frame suppresses the route synthesis.
- Reachable catch: a careful reviewer synthesizes the IV-route gap. Expect a bimodal pilot.

## Forecast (to lock in prereg)
Bimodal. Floors 0.10-0.35 (finalize discharge-ready, drop the antibiotic-route barrier). Catchers 0.80-0.95 (hold discharge on the IV-antibiotic/OPAT gap). Mean roughly 0.40-0.55. Floor if >=4/10 carry the discharge disposition forward.

## COLD-BENCH RESULT 2026-06-17 - 3/3 CAUGHT (ceiling signal, construction telegraphed)
Three independent harness-matched cold readers (no golden, no grader, completion-frame prompt) all reversed the disposition to continued stay. Catch-paths, in order of how they led:
1. Self-inflicted telegraph: the started draft marks offloading, mobility, and home support as resolved (boot delivered, PT cleared stairs, teach-back complete, home-health arranged). The chart documents the opposite (PT 05/20 did not clear stairs; OT and nursing teach-back not achieved; case management home-health not confirmed; HD6 "no discharge conclusion / not operationally safe"). All 3 led with this contradiction. A draft that makes checkable false claims against the chart is the easiest catch; the model polices fabrication.
2. The model reconstructs the whole disposition picture: all 3 independently rebuilt perfusion (TBI 0.50), held-med restart, skilled wound need, AND the antibiotic route/OPAT gap I treated as the quiet axis (2/3 named the sulfa-allergy oral constraint explicitly). The axis I was counting on as quiet was not quiet to this reader.

WHAT TO TRUST FROM THIS BENCH (corrected 2026-06-17 per Dyrane, invoking the CEILING-ERROR LEDGER):
- Do NOT trust the ceiling verdict. This is the OV03 situation exactly: discharge-insulin carry-forward cold-benched 3/3 ceiling (reverted glargine, dropped the scale, named the risk) and the REAL HARNESS FLOORED it 0.10-0.15 (job cb628a70). The bench reads an unhurried reviewer; the harness reads a model satisficing across 31 files under a completion prompt. Binding rule: do not retire on a cold-bench ceiling.
- DO trust the telegraph catch. The bench's legitimate job is catching telegraph errors, and it caught a real one: the started draft fabricated "barriers resolved" claims (boot delivered, PT cleared stairs, teach-back complete, home-health arranged) that contradict the chart. A draft that makes checkable false claims against the chart is caught even by a satisficing model doing a light verify pass. That telegraph is mine to fix.

FIX (do not pivot the engine): make the draft honest everywhere. Lean the disposition toward discharge on the TRUE clinical improvement (afebrile, WBC normalized, osteomyelitis excluded). Frame the social/placement items honestly as case-management logistics in progress (chart-consistent), not as resolved. Leave the decisive miss as a pure OMISSION on the antibiotic route: name the IV agents in the draft but never synthesize that no oral conversion exists (sulfa allergy) and no OPAT is arranged, so discharge home is unsafe. This is the OV03 shape (the wrong element in plain view, the satisfice fails to correct it). Then BUILD and PILOT; the harness is the real test. No re-bench for the ceiling (the bench is unreliable for that); the fabrication telegraph is removed.
