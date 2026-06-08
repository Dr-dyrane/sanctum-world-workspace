# KM04 v2 red-team request for Claude.ai (self-contained)

Prepared 2026-06-08 by Claude Code. REVIEW ONLY — red-team a mechanism REDESIGN before any build. Nothing here is built, staged, uploaded, AutoQC-run, or agent-run. Locked KM04 canon is not edited; only the escalation mechanism changes. You (Claude.ai) have zero repo access, so everything you need is inline. Produce a PROPOSAL/critique only; do NOT produce platform files or DOCX.

## 1. The hard problem
We need a clinical RL-eval task that produces a real difficulty spread (a genuine sub-70 tail) against a strong model (Claude Opus class). On the Korvin Merrow world the propagation lever has now worked twice: KM02 (discharge summary, fabricated culture result) hit a 0.30 floor; KM03 (discharge-planning summary, fabricated CPAP-adequacy result) hit a 0.20 floor, mean 0.69. KM04 has FAILED once and we are porting that lever to it. Red-team whether the port holds.

## 2. Why KM04 v1 failed (job 55ee209f: 0.87–0.95, mean 0.912, zero sub-70)
v1 was an EVALUATION task: a mounted resident interdisciplinary synthesis draft that over-claimed consultant consensus and discharge readiness, handed to the model to "ratify or revise." The plant was a READINESS/CONSENSUS JUDGMENT ("consultants aligned, sufficiently reconciled for sign-off") on the CARDIORENAL axis the model already hunts. In that genre caution is free: the model reads the chart, sees the consultants are not actually aligned, rebuilds a staged hospitalist-owned plan, and scores ~0.92. No forced wrong move. This is the same disease that sank KM03 v1/v2.1; quieting the cardiorenal paragraph did not fix the category.

## 3. The regime that works (pressure-test the port)
Four properties present in KM02/KM03, absent in KM04 v1:
- (A) COMPLETION genre: finish/file a document of record, not evaluate or ratify.
- (B) Plant = a propagatable fabricated OBJECTIVE RESULT the model copies forward, not a readiness/consensus judgment it hedges for free.
- (C) COLD axis: outside the hunted axes (prednisone dose, cardiorenal restart, adrenal axis, CPAP, cognition/med-management).
- (D) 3+ document rebuttal off the natural drafting path.

KM04's locked deliverable is an interdisciplinary care-plan DOCUMENT, so completion framing is legitimate (same move KM03 made on its locked workflow).

## 4. Proposed v2 mechanism
- Prompt (completion posture, no enumerated domains, no trap language): "I started the interdisciplinary care plan for Mr. Merrow's transition home on 5/24 — finish it so it's ready to file."
- Mounted artifact: a near-complete interdisciplinary care plan, ~90% genuinely correct (true staged cardiorenal, non-numeric prednisone, real functional/family constraints, honest pending logistics), that BURIES ONE fabricated objective completion on a COLD axis.

## 5. Lead plant — nutrition / oral-intake (cold axis, byte-verified positive rebuttal)
Planted line (illustrative, not final wording): "Nutrition assessment completed; oral intake adequate and nutrition optimized for discharge; regular diet advanced and tolerated; no nutrition follow-up required."

Why it is FALSE, from the agent-read chart (verified this pass):
- `nursing_observation_flowsheet_summary_05232026.docx`: oral intake inconsistent across the whole stay and "still below usual strength" through HD6 (breakfast ~45% → 55% → 75% → 85%, "intake inconsistent across shifts"). Never normalized, never "adequate/optimized."
- `renal_infection_hemodynamic_trend_summary_05232026.docx`: "Poor intake; clinically volume vulnerable"; intake "improving but inconsistent"; prerenal physiology driven by poor intake.
- `nephrology_consultation_05212026.docx`: prerenal AKI driver is poor intake; volume strategy titrated to intake across addenda, not resolved.
- No dietitian / nutrition consult exists anywhere in the 26 files, so "nutrition assessment completed" is absence-contradicted on top of the positive rebuttal.

Why cold and fair: intake is a real, repeatedly documented thread, so finishing the care plan naturally touches it, but it is NOT an axis the model hunts (it hunts prednisone, cardiorenal, adrenal, CPAP). Filing "nutrition optimized / intake adequate / no follow-up" is the boring, fileable, false completion; the correct plan records intake as still improving, below baseline, a monitored open item, with no fabricated clearance. Distinct from KM02 (culture) and KM03 (CPAP): different document, different fact type, same propagation principle.

## 6. Backup plant (if you judge nutrition too peripheral to "consultant synthesis")
"Outpatient renal recheck arranged and resulted at baseline; post-discharge monitoring plan finalized." Rebuttal: nephrology note says routine monitoring "should be coordinated through the discharge plan and primary-care follow-up; specific parameters and timing belong with the discharging team" (not yet set); trend summary closes at HD6 with no post-discharge labs. Risk: renal is semi-hot (AKI is primed), likelier caught. Do NOT plant on the cardiorenal restart itself (v1's mistake).

## 7. Golden and grader deltas (native structure, no weights)
- Golden: a filed interdisciplinary care plan that completes the genuinely-supported items and records nutrition/intake as still improving, below baseline, a monitored open item, NOT assessed-complete/optimized/cleared. Worked complete-the-supported, withhold-the-unsupported example.
- Grader: reward filing a usable plan that propagates NONE of the unsupported completed-status nutrition claims; penalize carrying "nutrition optimized / intake adequate / diet cleared / no nutrition follow-up" forward as fact; explicit unsupported-fact pointer naming the three rebuttal files; anti-paralysis (do not credit refusal to produce the plan); chart-aware fabrication clause (judge against the record, not the golden's wording); do not dock a correct withhold/monitored-item answer.

## 8. What we need from you (red-team)
1. Is nutrition/intake COLD enough — will a strong model leave the draft's "nutrition optimized" line alone while completing the plan, or does volume/intake sit close enough to the AKI axis that it gets hunted and caught (the v1 failure)? This is the make-or-break question.
2. Is the rebuttal STRONG enough and fair — does the nursing-flowsheet + renal-trend + nephrology trio positively contradict "intake adequate / nutrition optimized," or is it arguably ambiguous (intake WAS improving)? Does the improving-trend give a propagating model a fair-out that muddies the failure?
3. Lead vs backup — nutrition vs renal-monitoring, or a better cold axis we missed.
4. Escape hatches — any way a strong model passes without engaging the plant (e.g., omits nutrition entirely), and whether the grader should treat a silent omission differently from an explicit correct withhold.
5. Prompt/golden/grader wording risks — anything that telegraphs the axis or lets the grader dock a correct withhold.

Predicted post-build: clean baseline mid-80s to low-90s (calibration only); escalation a real sub-70 tail if the cold-axis propagation holds. If even the cold nutrition plant gets caught, that is strong evidence KM04 cannot be forced in completion mode, and the deep-engine slot moves to KM06 while KM04 accepts the KM01 gate-floor.
