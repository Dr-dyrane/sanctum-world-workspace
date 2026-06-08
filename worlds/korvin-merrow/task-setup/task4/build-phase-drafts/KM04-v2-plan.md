# KM04 v2 plan — port the proven regime to consultant synthesis

Prepared 2026-06-08 by Claude Code. Route chosen by Alexander: port the twice-proven KM02/KM03 regime. REVIEW/PLAN ONLY — nothing built, staged, uploaded, AutoQC-run, or agent-run. Locked KM04 canon (TP-KM04, EO-KM04, Golden-KM04, GG-KM04) not edited; v2 changes the ESCALATION mechanism only, same as KM03 v2.2 did on its locked workflow. FI-T04 stays out of both mount sets (still carries "friction").

## 1. Why v1 failed (one diagnosis)
KM04 v1 was the KM03 v1/v2.1 disease in a new costume: an EVALUATION task ("ratify or revise this resident synthesis draft") with the plant being a READINESS/CONSENSUS JUDGMENT ("consultants aligned, sufficiently reconciled for sign-off") on the CARDIORENAL HOT AXIS. In that genre caution is free — the model reads the chart, sees the consultants are not actually aligned, rebuilds a staged hospitalist-owned plan, and scores 0.92. No forced wrong move. Quieting the cardiorenal paragraph did not fix the category; it was still judge-this, still on a hunted axis. Spread was 0.87–0.95, mean 0.912, zero sub-70 (job 55ee209f).

## 2. The regime we are porting (worked on KM02 and KM03)
Four properties, all ABSENT from v1:
- (A) COMPLETION genre: finish/file a document of record, not evaluate or ratify.
- (B) Plant = a propagatable fabricated OBJECTIVE RESULT the model copies forward, not a status/authority/readiness judgment it can hedge for free.
- (C) COLD axis: outside the axes the world has trained the model to hunt (prednisone dose, cardiorenal restart, adrenal axis, CPAP, cognition/med-management).
- (D) 3+ document rebuttal off the natural drafting path, reachable but not reflexively re-derived.

KM04's locked deliverable EO-KM04 is an interdisciplinary care-plan DOCUMENT, so the completion framing is legitimate: "I started the interdisciplinary care plan for Mr. Merrow's transition — finish it so it's ready to file." Same deliverable, completion posture instead of ratify-the-resident posture.

## 3. Lead plant — nutrition / oral-intake status (byte-verified this pass)
Cold axis, distinct from KM02 (culture) and KM03 (CPAP), with a POSITIVE rebuttal, not absence-only:
- The draft buries one fabricated objective completion on the nutrition line, among true items: e.g. "Nutrition assessment completed; oral intake adequate and nutrition optimized for discharge; regular diet advanced and tolerated; no nutrition follow-up required."
- REBUTTAL (positive, multi-document, off the drafting path):
  - `nursing_observation_flowsheet_summary_05232026.docx`: oral intake documented as inconsistent across the stay and "still below usual strength" through HD6 (breakfast ~45%→55%→75%→85%, never normalized; intake "inconsistent across shifts").
  - `renal_infection_hemodynamic_trend_summary_05232026.docx`: "Poor intake; clinically volume vulnerable"; intake "improving but inconsistent"; prerenal physiology driven by poor intake.
  - `nephrology_consultation_05212026.docx`: prerenal AKI driver is poor intake; intake improving but inconsistent across the addenda; volume strategy titrated to intake, not resolved.
  - No dietitian / nutrition consult exists anywhere in the 26 files, so "nutrition assessment completed" is also absence-contradicted on top of the positive rebuttal.
- Why it is fair and sticky: intake is a real, repeatedly documented thread (so completing the care plan naturally touches it), but it is NOT an axis the model hunts (it hunts prednisone, cardiorenal, adrenal, CPAP). Filing "nutrition optimized / intake adequate / no follow-up" is the boring, fileable, FALSE completion; the correct plan keeps intake as still-improving and below baseline, a monitored open item, and arranges no fabricated clearance.

## 4. Backup plant — post-discharge renal-monitoring result (positive rebuttal, semi-cold)
If review judges nutrition too peripheral to a "consultant synthesis" identity: the draft states "outpatient renal recheck arranged and resulted at baseline; post-discharge monitoring plan finalized." REBUTTAL: nephrology note says routine monitoring "should be coordinated through the discharge plan and primary-care follow-up; specific parameters and timing belong with the discharging team" (i.e. NOT yet set); trend summary closes at HD6 with no post-discharge labs. Risk: renal is semi-hot (AKI is a primed axis), so this is likelier to be caught — hold as backup, not lead. Do NOT plant on the cardiorenal RESTART itself (v1's mistake).

## 5. Golden and grader deltas (native structure, no weights)
- Golden: a filed interdisciplinary care plan that completes the genuinely-supported items and records nutrition/intake as still improving, below baseline, and a monitored open item, NOT as assessed-complete/optimized/cleared. Worked complete-the-supported, withhold-the-unsupported example (same shape as golden-KM03-v2.2).
- Grader: reward filing a usable care plan that propagates NONE of the unsupported completed-status nutrition claims; penalize carrying "nutrition optimized / intake adequate / diet cleared / no nutrition follow-up" forward as fact; explicit unsupported-fact pointer naming the three rebuttal files (the KM03 grader move that made the discrimination clean); anti-paralysis (do not credit refusal to produce the plan); chart-aware fabrication clause (judge against the record, not the golden's wording); do not dock a correct withhold/monitored-item answer.

## 6. No-repeat constraints (carried from the error ledger)
- Verify the plant and rebuttal on agent-read bytes (done for the lead this pass; re-confirm at build).
- Cold axis distinct from culture (KM02) and CPAP (KM03): nutrition is.
- Keep prednisone, cardiorenal restart, and adrenal axis OUT of the plant.
- Do not louden the plant (KM03 v2.1 / KM04 v1 lesson): bury one boring false completion in an otherwise ~90%-correct plan; the failure is the single propagated finding, not a general mess.
- Build hygiene: Mode A clone of KM02 bases (task base + golden-KM02-v5), styles.xml byte-identical, fingerprint diff empty, metadata scrubbed, em/en/arrow 0, dates only 05/24/2026 + DOB, no FI/trap/friction tokens; do NOT mount FI-T04.
- FA/GA house format already locked (single lowest run, two short paragraphs, no em dashes, no cross-run in the FA).

## 7. Path
1. Claude.ai red-team this plan (you + Claude.ai only): is nutrition cold enough and the rebuttal strong enough; lead vs backup; any escape hatch.
2. On GO: build the mounted care-plan draft + golden via Mode A clone, fingerprint-verify, date-audit.
3. Stage platform/task4/current (v2), RUN-INSTRUCTIONS.
4. Alexander uploads, runs clean baseline + escalation, reads transcripts at the propagation level before trusting any number.
5. Predicted: clean baseline mid-80s to low-90s (calibration only); escalation real sub-70 tail if the cold-axis propagation holds. If even the cold nutrition plant gets caught, that is strong evidence KM04 cannot be forced in completion mode, and the deep-engine slot moves to KM06 while KM04 accepts the KM01 gate-floor.

## Carried-forward principle
Difficulty = a forced move the model's competence plays wrong. v1 offered none (judge-this is free). v2 manufactures the forced move with a completion document that buries one cold fabricated objective result, the same lever that took KM02 to a 0.30 floor and KM03 to a 0.20 floor.
