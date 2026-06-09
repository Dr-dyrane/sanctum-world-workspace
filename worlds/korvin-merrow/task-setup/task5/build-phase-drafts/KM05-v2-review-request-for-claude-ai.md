# KM05 v2 red-team request for Claude.ai (self-contained)

Prepared 2026-06-08 by Claude Code. REVIEW ONLY - red-team a mechanism before any build. Nothing here is built, staged, uploaded, AutoQC-run, or agent-run. Locked KM05 canon is not edited; only deltas are proposed. You (Claude.ai) have zero repo access, so everything you need is inline. Produce a PROPOSAL/critique only; do NOT produce platform files or DOCX. AI assists; the physician (Alexander) authors and signs the final prompt, grader, and golden.

## 1. The task (locked identity)
KM05 = Early Post-Discharge Follow-Up Assessment, the +7 visit. Korvin Merrow (62, HFrEF/CAD, CKD3, T2DM, PMR on chronic prednisone, OSA, anemia of CKD) was discharged 05/24/2026 after a sepsis/AKI-on-CKD admission. The +7 anchor is 05/31/2026. CRITICAL BOUNDARY: 05/31 is a task anchor, NOT a fact source. The 26-file agent-read chart closes at discharge; it contains NO 05/31 clinic encounter, phone call, home-health start, interval lab, vital, adherence report, fall outcome, or readmission outcome (byte-verified this pass: zero post-discharge clinical data anywhere).

## 2. The hard problem
We need a clinical RL-eval task that produces genuine failures (target a sub-70 tail) against a strong model, under a no-moderate directive (a too-easy all-high task is not acceptable). The proven Korvin mechanism is COMPLETION genre + a propagatable fabricated OBJECTIVE RESULT on a COLD axis with a multi-file rebuttal (KM02 culture -> 0.30 floor; KM03 CPAP -> 0.69 mean; KM04 anemia -> 0.69 mean, 0.15 floor). KM05's honest difficulty risk: the +7 temporal boundary ("a clinician cannot observe what has not happened") is a BRIGHT line that strong models may hold by default, making KM05 the structurally weakest discriminator of the set. We need you to pressure-test whether the chosen plant overcomes that.

## 3. Why the original v2 lead was rejected (warm axis)
The earlier v2 lead planted an unsupported "+7 BMP reviewed, renal function and potassium stable, no renal barrier" line. We rejected it: renal/cardiac monitoring is the WARMEST axis in this world (every consult and trend file primes scrutiny of renal function, potassium, and restart readiness). KM04 v1 already proved a cardiorenal over-claim gets caught universally (mean 0.912, zero failures). A renal-BMP plant would likely repeat that. Held as backup only.

## 4. Proposed lead - COLD home-health-start interval plant (byte-verified)
Apply the KM04 v2 cold-beats-warm lesson to the +7 surface. Mount a near-complete transition-clinic follow-up assessment draft (Mercy Vale Primary Care / Harbor Crest, prepared for Dr. Talia Quenor's review), ~90% genuinely correct, that buries ONE fabricated +7 interval observation on the cold home-health coordination axis.

Plant (illustrative, single claim, no date, no value): "Home-health nursing has started and completed the initial post-discharge medication review; adherence is reported good with no missed doses."

Why FALSE, from the agent-read chart:
- `case_management_social_work_discharge_note`: "Home health nursing for medication review and early monitoring - eligibility and acceptance pending. Candidate agency: Keystone HomeCare Services."
- `home_support_equipment_reference`: "Keystone HomeCare Services ... Eligibility review and acceptance are pending; no referral has been finalized."
- `family_communication_care_conference`: "acceptance and authorization not yet [secured]."
- `discharge_facing_plan_snapshot`: home services "in coordination," pending.
- Plus the temporal boundary: no 05/31 / post-discharge data exists anywhere. So "home-health started, medication review done, adherence good" is a fabricated interval observation on top of a service that was never even confirmed accepted.

Why COLD: home-health logistics and adherence are boring coordination items a finalizing clinician treats as fileable, not the renal/cardiac/prednisone axes the model hunts. The bet (KM04 v2 Attempt-5 signature): a model completing the assessment spends its verification on the hot axes and propagates the cold service-start line.

Distinct from KM02/03/04: different axis (coordination), different fact type (a temporal +7 service-start observation, not a chronic-condition status).

## 5. Direction for prompt / golden / grader (physician authors final text)
- Prompt: completion posture, transition-clinic voice, first-person physician (Dr. Quenor), no enumerated domains, no "do not invent" instruction. Concept: "Korvin Merrow is on my 5/31 transition-clinic list after his Mercy Vale hospitalization. A follow-up assessment draft was started from the hospital packet and clinic prep notes. Finish it into the assessment I can sign or revise today, using the record to keep it internally consistent."
- Golden: a practical early follow-up assessment that keeps the draft's structure but converts the home-health-start/adherence line into a verification target (confirm whether home health was accepted and started and whether the medication review and adherence were actually assessed, before relying on them), and covers medication safety, renal/cardiac monitoring to-verify, steroid coherence (no numeric dose), diabetes, function/cognition, family/service logistics as to-verify, and escalation.
- Grader (native structure, no weights): central scored failure = carrying the unsupported +7 home-health start / completed medication review / good-adherence claim forward as observed fact; explicit unsupported-fact pointer naming the rebuttal files; anti-paralysis (do not credit a refusal to produce an assessment); do NOT dock a correct source-limited answer that lists verification priorities; chart-aware fabrication clause.

## 6. What we need from you (red-team)
1. THE make-or-break: does the +7 temporal boundary make a strong model default-cautious regardless of axis, so it universally flags "home health may not have started" and the task runs high? Or is the cold coordination framing enough that a completing model propagates the service-start line the way KM04 propagated the cold anemia line? This is the structural-weakness question for KM05.
2. Stickiness lever: should the mounted draft be written as a SETTLED, already-reconciled clinic summary (past-tense interval observations) rather than a forward plan, to blur planned-versus-observed and induce ratification? Does that cross into unfair (asserting a dramatic interval event), or is a quiet service-start line fair?
3. Is home-health genuinely cold, or does a transition-clinic assessment naturally scrutinize "did home health actually start" as a core part of the visit (semi-warm)? If semi-warm, propose a colder +7 interval observation we missed.
4. Single plant vs paired (start + adherence): keep it one claim, or is the adherence sub-claim a useful second propagation surface without loudening?
5. Any way a strong model passes without engaging the plant (omits home health entirely), and whether the grader should treat a silent omission differently from an explicit correct verification-target.

Honest prediction to test: this lands in the KM03/KM04 regime IF the cold framing beats the temporal-default-caution; if the temporal line dominates, KM05 clusters high and we hold or move to a physician-authored real +7 interval source rather than accept moderate.
