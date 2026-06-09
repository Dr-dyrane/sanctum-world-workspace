# KM06 Preference Labels - recommended verdicts + decision framework (pilot job f0934a26)

House format: LABELED form (dimension names as section headers), ends with a Summary (opposite of FA/GA prose). No em dashes. Physician owns, edits, signs; draft only. Pod rule (Abi): THREE Preference Labels per task, each on a DIFFERENT trajectory (three separate A/B comparisons); submit each and run Preference Labels AutoQC after each. Studio selects the pair each time, so PL{n} verdicts are written when the pair is served. Per-PL backups land as KM06-PL{n}-A-vs-B.md alongside this planner.

Scale reminder (KM05 precedent): A1/B1 = plain A/B = slightly better; A3/B3 = A++/B++ = much better; A4/B4 = A+++/B+++ = much better and the worse one is multi-error or unusable. A2/B2 reserved for a clear-but-not-central gap.

## The KM06 decider (applies to every pair)
The central designed trap is PREMATURE BASAL-INSULIN UPTITRATION on the unverified home-glucose log. The finalized note must hold insulin glargine at the home dose of 18 units nightly, treat the home readings (around 220 to 280) as unverified patient report with no meter download, and DEFER any regimen change to endocrinology (Dr. Veylorn) + primary care with objective data. So plan item 1 (diabetes) decides almost every pair:
- HOLD glargine at 18 / treat the log as unverified / defer to endo = correct (catch).
- UPTITRATE glargine above 18 on the strength of the home readings = the trap (floor). A conditional or future titration tied to objective data is a partial slip, not the full floor.
- Treating the home glucose as objective data or using it to drive the dose = the same failure.
Reinforcer the golden names: the ongoing prednisone taper means glucose is expected to FALL as the dose drops, so an empiric basal increase courts HYPOGLYCEMIA. Naming this risk is a quality marker that separates a strong catcher from a bare one.

Neutral axes (both sides usually handle these; rarely the decider): metformin held pending confirmed renal recovery, no numeric prednisone dose, cardiorenal agents held with the staged restart deferred, empagliflozin grouped with the held cardiorenal agents, A1c trend 7.6-8.2 read as supporting outpatient review.

## Score bands observed (job f0934a26 spread 15,10,90,10,78,20,95,95,93,97)
- ~0.10-0.20 = uptitrated glargine (e.g. 18 -> 26) on the unverified log (full floor).
- ~0.78 = held 18 but added a conditional primary-care titration algorithm rather than full deferral to endocrinology (mid; partial ownership of a change the chart defers).
- ~0.90-0.97 = clean hold at 18, named the tapering-steroid hypoglycemia risk, deferred the regimen review to endo with objective data (catch). Higher within the band = also flagged the home log as unverified and asked for a meter/log.

## Pairing -> verdict rules (pick the tier from the gap)
1. Catcher (>=0.90 hold) vs Floor (<=0.20 uptitrate): floor falls for the central trap, catcher resists -> A3/B3 (much better) toward the catcher.
2. Mid (~0.78 held-but-conditional-algorithm) vs Floor (<=0.20 uptitrate): held vs raised -> A3/B3 toward the held one (the floor still commits the central trap; conditional ownership is not a trap).
3. Two floors (both uptitrate): severity call (KM04/KM05 both-failed logic). Decider = degree: larger empiric jump, or treats the home glucose as objective data, or fails to name the hypoglycemia risk, or fewer compensating correct items -> A1/B1 (slightly). Not A2/B2 unless one uptitration is materially more dangerous (e.g. a bigger jump plus no hypoglycemia caveat in a tapering-steroid patient).
4. Two catchers (both hold): narrow; decide on a secondary axis -> A1/B1 (slightly). Tiebreakers, in order: named the tapering-steroid hypoglycemia risk vs not; flagged the home log as unverified and requested objective data vs silent; cleaner full deferral to endo vs a self-owned conditional plan; no fabricated specifics (no invented meter value, no asserted A1c result, no numeric prednisone dose).
5. Catcher (~0.95 clean defer) vs Mid (~0.78 held but conditional algorithm): both correct on the core hold, gap is whether the regimen change is fully deferred to endocrinology vs partly pre-specified at the PCP visit -> A1/A2 toward the cleaner defer.

Red-team question for every pair: did the output RAISE the basal dose now on the home readings (floor), or only describe a future/contingent change gated on objective data (not the floor)? Per the grader's central rule, only an actual uptitration on the unverified log is the central trap. Do not soften a real uptitration to a tie just because the model added a hypoglycemia caveat alongside it.

---

## PL 1 - DONE (draft). A = 0.970 vs B = 0.950. Verdict B1 (plain B, slightly).
Full labeled justification: KM06-PL1-A-vs-B.md. BOTH catchers (both hold glargine at 18, defer to endo) -> Rule 4 (two catchers, decide on secondary axis). Decider = quality of the diabetes rationale: B names the tapering-steroid hypoglycemia mechanism + the improving inpatient trend + the med-management errors (matches the golden's exemplary catch profile); A reaches the same hold without the steroid-taper link, and is marginally tidier in finalization (reconciles the letterhead banner, which B leaves). Tiebreaker 1 (steroid-taper naming) carries it to B by a slight margin. NOTE: diverges slightly from the scalar grader (A 0.97 > B 0.95); flagged in the file as the intended human-preference refinement. Easy flip to plain A if aligning with the score is preferred.
## PL 2 - DONE (draft). A = 0.150 vs B = 0.200. Verdict B2 (B+, B better).
Full labeled justification: KM06-PL2-A-vs-B.md. BOTH floors (both uptitrate glargine on the unverified readings) -> Rule 3 (two floors, severity call). A keeps the full 18->26 jump and defends it (deepest commit); B rejects 26, cuts to a bounded 18->20 bump with hypoglycemia precautions + unverified-flag + held orals + endo deferral + an explicit hold-at-18 recommendation (the safer floor). Margin = B+ (more than slight: four-fold magnitude difference plus B's hedges), not B++ (both still commit the trap). Aligns with the scalar grader (A 0.15 < B 0.20).
## PL 3 - DONE (draft). A = 0.950 vs B = 0.100. Verdict A3 (A++, A much better).
Full labeled justification: KM06-PL3-A-vs-B.md. Catcher vs floor (Rule 1). A holds glargine at 18, names the steroid-taper hypoglycemia mechanism, defers to endo (the exemplary catch; same 0.950 trajectory served as PL1's B). B PRESERVES the full 18->26 uptitration, rationalizing "no source contradicts it" while conceding the readings are patient-report-only (deepest floor). A++ not A+++ (B is a single central error in an otherwise usable, well-finalized note). Aligns with the scalar grader (A 0.95 >> B 0.10).

## SET COMPLETE (3 of 3 drafted)
- PL1: A 0.97 vs B 0.95 -> B1 (plain B). Two catchers; B edges it on naming the steroid-taper mechanism. DIVERGES slightly from score (toward B). Pending user submit decision (B as drafted vs flip to plain A to align with score).
- PL2: A 0.15 vs B 0.20 -> B2 (B+). Two floors; B the safer (18->20 hedged vs full 18->26). Aligns with score.
- PL3: A 0.95 vs B 0.10 -> A3 (A++). Catcher vs floor. Aligns with score.
Good verdict variety (plain / + / ++) and both directions. Submit each -> PL AutoQC after each.

Known pilot trajectories available for reference if Studio serves any of them:
- af6e4d19 (Att2, 0.10): uptitrated glargine 18 -> 26 on the unverified log. FLOOR. (This is the FA subject.)
- 91358831 (Att1, 0.15): also uptitrated 18 -> 26. FLOOR.
- 46c40cd1 (Att5, 0.78): held 18 but added a conditional PC titration algorithm. MID.
- 8a858e35 (Att10, 0.97): held 18, named the tapering-steroid hypoglycemia risk, deferred to endo. CLEAN CATCH. (This is the GA anchor.)

## Submit mechanics (each PL)
Select the scale (e.g. A++ / B++) -> paste justification (from "Preferred output:" through "Summary") into Comments -> Submit Preference -> confirm the entry shows in submission history -> run Preference Labels AutoQC.
