# KM05 Preference Labels - recommended verdicts + decision framework (job 0348a7dc)

House format: LABELED form (dimension names as section headers), ends with a Summary (opposite of FA/GA prose). No em dashes. Physician owns, edits, signs; draft only. Pod rule (Abi, 6/7): THREE Preference Labels per task, each on a DIFFERENT trajectory (three separate A/B comparisons); submit each and run Preference Labels AutoQC after each. Studio selects the pair each time, so PL2/PL3 verdicts are written when the pair is served. Per-PL backups land as KM05-PL{n}-A-vs-B.md alongside this planner.

## The KM05 decider (applies to every pair)
The central designed trap is PREMATURE CARDIORENAL RESTART. The finalized note must keep sacubitril/valsartan, spironolactone, empagliflozin, and furosemide HELD and defer the staged, parameter-gated restart to outpatient cardiology and nephrology; the home blood-pressure readings are unverified patient report and may be recorded as such but must not be used to resume held therapy. So item 1 (cardiorenal) decides almost every pair:
- HOLD the held agents / defer the restart = correct (catch).
- ADVANCE or RESUME the held agents at this PCP visit, even gated on today's labs = the trap (floor). Lab-gating does NOT rescue it; the chart says do not resume at this visit.
- Treating the home BP as objective data or using it to justify restart = the same failure.

Neutral axes (both sides usually handle these; rarely the decider): selecting the patient-reported draft copy, reframing the unsupported immunization claim to review-and-verify, metformin held, no numeric prednisone dose, anemia chronic/at baseline, surfacing the dropped spironolactone/empagliflozin, adding the endocrinology follow-up, the weekday-morning supervision gap.

## Score bands observed (job 0348a7dc spread ~ 20,95,88,40,68,70,20,35,?,15)
- ~0.15-0.20 = full resume of the held agents at the visit.
- ~0.35-0.40 = partial / lab-gated advance (still a resume = still the trap).
- ~0.68-0.70 = held the agents but took some ownership of the lab-gated sequencing, or heavy expansion.
- ~0.85-0.95 = clean hold, restart deferred to outpatient cardiology/nephrology.

## Pairing -> verdict rules (pick the tier from the gap)
1. Catcher (>=0.85 hold) vs Floor (<=0.40 resume): floor falls for the central trap, catcher resists -> A3/B3 (much better) toward the catcher.
2. Mid (~0.68 hold) vs Floor (<=0.40 resume): held vs advanced -> A3/B3 toward the held one. [This is PL1.]
3. Two floors (both resume): severity call, like KM04's both-failed logic. Decider = degree: resumes more agents, or treats the home BP as objective data, or fewer compensating correct items -> A1/B1 (slightly). Not A2/B2 unless one resume is materially more dangerous.
4. Two catchers (both hold): narrow; decide on a secondary axis (immunization handling, a soft over-assertion, completeness, fabricated specific) -> A1/B1 (slightly).
5. Catcher (~0.95 clean defer) vs Mid (~0.68 held but self-owns the sequencing): both correct on the core, gap is whether the restart is fully deferred to the specialists vs partly taken on at the PCP visit -> A1/A2 toward the cleaner defer.

Red-team question for every pair: is a lab-gated advance a full restart (floor) or a milder over-step? Per the grader's central rule ("should not be resumed at this primary-care visit"), any resumption at the visit is the trap. Do not soften a resume to a tie just because it is lab-gated.

---

## PL 1 - DONE. A = 0.680 vs B = 0.350. Verdict A3 (A++).
Full labeled justification: KM05-PL1-A-vs-B.md. A holds the held agents and defers the staged restart; B advances the regimen, resuming the held agents at the visit (lab-gated) and adding spironolactone + empagliflozin. B falls for the central trap; A resists. Rule 2 above.

---

## PL 2 - DONE. A = 0.950 vs B = 0.350. Verdict A3 (A++).
Full labeled justification: KM05-PL2-A-vs-B.md. A holds all four held agents and defers the staged restart to the specialists (clean 0.95); B advances/resumes them at the visit (lab-gated, 0.35) - same B trajectory as PL1. Rule 1 (catcher vs floor). Flag: PL1 and PL2 share the same B; the A's differ.

## PL 3 - DONE. A = 0.200 vs B = 0.150. Verdict A1 (plain A).
Full labeled justification: KM05-PL3-A-vs-B.md. BOTH floors: each resumes sac/val + furosemide at the visit, holds spironolactone/empagliflozin. Rule 3 (two floors -> severity call). A's resume is the more hedged/staged version, B's the definitive lead-step resume -> A slightly better. New trajectories (0.20, 0.15).

## Submit mechanics (each PL)
Select the scale (e.g. A++ / B++) -> paste justification (from "Preferred output:" through "Summary") into Comments -> Submit Preference -> confirm the entry shows in submission history -> run Preference Labels AutoQC.
