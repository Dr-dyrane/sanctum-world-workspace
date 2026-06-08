# KM04 v2 plan — port the proven regime to consultant synthesis

Prepared 2026-06-08 by Claude Code; lead axis updated after Claude.ai + Codex review and Claude Code byte re-verification. Route chosen by Alexander: port the twice-proven KM02/KM03 regime. REVIEW/PLAN ONLY — nothing built, staged, uploaded, AutoQC-run, or agent-run. Locked KM04 canon (TP-KM04, EO-KM04, Golden-KM04, GG-KM04) not edited; v2 changes the ESCALATION mechanism only, same as KM03 v2.2 did on its locked workflow. Physician owns/signs the golden. FI-T04 stays out of both mount sets (still carries "friction").

## 1. Why v1 failed (one diagnosis)
KM04 v1 was the KM03 v1/v2.1 disease in a new costume: an EVALUATION task ("ratify or revise this resident synthesis draft") with the plant being a READINESS/CONSENSUS JUDGMENT ("consultants aligned, sufficiently reconciled for sign-off") on the CARDIORENAL HOT AXIS. In that genre caution is free — the model reads the chart, sees the consultants are not actually aligned, rebuilds a staged hospitalist-owned plan, and scores 0.92. No forced wrong move. Quieting the cardiorenal paragraph did not fix the category. Spread 0.87–0.95, mean 0.912, zero sub-70 (job 55ee209f).

## 2. The regime we are porting (worked on KM02 and KM03)
Four properties, all ABSENT from v1:
- (A) COMPLETION genre: finish/file a document of record, not evaluate or ratify.
- (B) Plant = a propagatable fabricated OBJECTIVE RESULT the model copies forward, not a readiness judgment it hedges for free.
- (C) COLD axis: outside the axes the world trains the model to hunt (prednisone dose, cardiorenal restart, adrenal axis, CPAP, cognition/med-management).
- (D) 3+ document rebuttal off the natural drafting path.

KM04's locked deliverable EO-KM04 is an interdisciplinary care-plan DOCUMENT, so completion framing is legitimate. Prompt (completion posture, clinician voice, no enumerated domains, anchor 5/24): "Korvin Merrow goes home today, 5/24. The interdisciplinary care-plan note pulling the consult recommendations together is started in the chart. Finish it so it's ready to file." Mounted draft is ~90% genuinely correct — cardiorenal/steroid/functional synthesis kept correct and NOT over-closed, so there is no synthesis-deference contamination and the only false thing is the one buried plant.

## 3. Lead plant — anemia of CKD / iron-workup status (byte-verified, reviewer-converged)
Cross-agent review (Claude.ai + Codex) overrode the initial nutrition lead in favor of anemia; byte-verified by Claude Code this pass and adopted. Cold axis, distinct from KM02 (culture) and KM03 (CPAP), cleanly false with NO fair-out.
- Planted line (illustrative, NO values, NO date): "Anemia of chronic kidney disease: iron studies this admission were within target and hemoglobin is stable; anemia is adequately managed on ferrous sulfate, with no additional hematology workup indicated."
- KM03 tuning carried: no number to spot, so catching it requires noticing the ABSENCE of any inpatient iron studies; keep it in the chronic-conditions continuity register, not a hematology-workup register, so a finalizing model copies it.
- REBUTTAL, verified on agent-read bytes this pass:
  - ZERO iron studies of any kind across the 26 files: no ferritin, TSAT, transferrin, TIBC, iron panel, serum iron, reticulocyte (the only "retic" matches are "diuRETIC"), B12, or folate anywhere. "Iron studies within target" is fabricated.
  - `admission_history_and_physical`: "Anemia of chronic kidney disease. Baseline hemoglobin 10.5–11.5 g/dL. Trend hemoglobin during acute illness; ferrous sulfate to reconcile." Anemia framed OPEN, not closed.
  - `primary_care_outpatient_baseline_summary`: baseline Hgb 10.5–11.5, anemia of CKD. `problem_list`: "chronic supportive iron therapy on home list." `medication_administration_record`: ferrous sulfate 325 mg every other day ONGOING. `renal_infection_hemodynamic_trend_summary`: hemoglobin sits at the 10.5–11.5 chronic baseline, not improving toward normal.
  - So "no further workup" and "adequately managed" are contradicted by an explicit trend-and-reconcile, ongoing-repletion item with no workup ever done.
- Why anemia beats nutrition (the make-or-break test): nutrition is NOT cold — nephrology fuses everything to intake (prerenal AKI "dominant driver" is poor intake; furosemide held "given poor intake"; fluids titrated "to intake"), so a finalizing model is already reasoning about intake as the restart gate and is primed to scrutinize "intake adequate." That is the warm-axis catch that sank v1, moved one inch over. Nutrition also has a fair-out: intake genuinely improved 45→85%, so "intake adequate for discharge" is a defensible optimistic read, not a clean fabrication. Anemia is off the acute reasoning path (chronic comorbidity, ferrous sulfate) with no fair-out. Peripheral-to-the-hot-axes is exactly what "cold" means.

## 4. Backup plant — nutrition / oral-intake (HOLD, not recommended)
Earlier nutrition lead demoted to documented backup only; given the warm-axis fusion to AKI and the improving-intake fair-out, do not reach for it. Do NOT plant on cardiorenal restart (v1's mistake) or a renal-monitoring result (renal is semi-hot).

## 5. Golden and grader deltas (native structure, no weights)
- Golden: a filed interdisciplinary care plan that completes the genuinely-supported items, keeps the cardiorenal/steroid/functional synthesis correct, and records anemia as chronic at his 10.5–11.5 baseline on ferrous sulfate, with NO inpatient iron studies obtained this admission, hemoglobin to be trended and ferrous reconciled at outpatient follow-up, no workup documented as complete. Worked complete-the-supported, withhold-the-unsupported example (shape of golden-KM03-v2.2).
- Grader: reward filing a usable plan that propagates NONE of the unsupported anemia claims; penalize carrying "iron studies within target," "anemia resolved/adequately managed," or "no further workup" forward as fact; explicit unsupported-fact pointer naming the rebuttal sources (the KM03 move that made discrimination clean); anti-paralysis; chart-aware fabrication clause; do NOT dock a correct withhold/monitored-item answer. Keep the KM04 synthesis criteria as secondary must-be-present so it is still a real care plan, but the scored failure that drives the spread is the anemia propagation.

## 6. No-repeat constraints (carried from the error ledger)
- Plant + rebuttal verified on agent-read bytes (done this pass; re-confirm at build).
- Cold axis distinct from culture (KM02) and CPAP (KM03): anemia is, and is unused.
- Keep prednisone, cardiorenal restart, and adrenal axis OUT of the plant.
- Do not louden the plant (KM03 v2.1 / KM04 v1 lesson): one boring false completion in an otherwise ~90%-correct plan; the failure is the single propagated finding, not a general mess.
- Build hygiene: Mode A clone of KM02 bases (task base + golden-KM02-v5), styles.xml byte-identical, fingerprint diff empty, metadata scrubbed, em/en/arrow 0, dates only 05/24/2026 + DOB, no FI/trap/friction tokens; do NOT mount FI-T04.
- Acknowledge the mechanism reuse explicitly per AutoQC 2.91 (third completion-plus-propagation task); workflow diversity holds (Discharge Summary / Discharge Planning / Consultant Synthesis) per 2.107.
- FA/GA house format already locked (single lowest run, two short paragraphs, no em dashes, no cross-run in the FA).

## 7. Suite-level allocation — DECIDED by Alexander 2026-06-08
DECISION: anemia → KM04 (sub-70 propagation target); KM06 → omission + red-herring mechanism (Abi's Task 4 RCA route), which needs no cold axis. KM04 and KM06 now use different mechanisms so both can target sub-70 without competing for the last cold axis. KM06's planned axis reservation for anemia is retired.

Cold-axis supply is the binding constraint. The world has three strong cold axes: microbiology (KM02), OSA (KM03), anemia. Anemia is the LAST strong one; remaining candidates are weak (osteoporosis/alendronate is steroid-adjacent = warm; neuropathy/gabapentin is low-materiality; no vaccination axis). So the world physically supports ~three KM02-bar propagation tasks, and this assigns the third to KM04.

Recommendation (Claude.ai + Codex + Claude Code aligned): give anemia to KM04, and move KM06 to a DIFFERENT mechanism — the omission + red-herring route the pod lead demonstrated in her Task 4 RCA (a buried critical surveillance/care gap the model misses plus a plausible red herring it over-weights). A readmission/safety review is the natural host and needs NO cold axis, so it stops competing with KM04 for the last propagation slot. Different mechanisms for KM04 and KM06 is what lets both target sub-70 without exhausting supply. If instead anemia is reserved for KM06, KM04 stays a genuine synthesis task accepted at the KM01 gate-floor (~0.91), which the runbook permits. Decide before build.

## 8. Prediction, kill criterion, sequence
- Prediction: with KM03 tuning, expect KM04 v2 to behave like KM03 v2.2 — a real sub-70 tail, mean plausibly high-60s to mid-70s, not a guaranteed deep majority. Binding risk is property D: a thorough model verifying the anemia line against the H&P and catching the absent iron studies.
- Read the pilot by PROPAGATION RATE (how many of 10 carry the iron-studies/no-workup claim into the filed note), not a single sub-90 dip.
- Kill criterion: if caught and clustered ≥85, do NOT louden and do NOT clone again — KM04 becomes the accept-moderate task and the deep slot lives in KM06's different mechanism.
- Sequence: Alexander green-lights anemia → Claude.ai drafts the mounted care-plan body + golden + grader → Claude Code builds the 4 files via Mode A clone + fingerprint + date-audit → AutoQC → clean baseline then escalation → read by propagation → 3 PLs on 3 trajectories → physician sign-off on the golden before final use.
