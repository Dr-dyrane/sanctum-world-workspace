# KM04 build-phase independent review (Claude.ai, 6/7)

Status: proposal and review only. No platform files, no DOCX, nothing built, staged, uploaded, or AutoQC-run. The locked KM04 canon is not edited; only deltas are proposed. Current dependency update: KM03 v2.1 Task AutoQC passed (`qcaud_fc`) and Taiga is intentionally held, so KM04 may continue prebuild refinement toward the same gated task-writing / Task AutoQC flow after Codex black-team and Alexander approval. Filenames are placeholders. The physician owns and signs any golden; Codex black-team and Alexander approval gate any build.

Verdict: GO with fixes. The mechanism is sound and fair on the verified bytes, and the de-authorization (a resident synthesis draft for attending review) is the right move. One fix is required before pilot (quiet the cardiorenal paragraph), plus three refinements (port the KM03 razor, add an anti-paralysis penalty, confirm the grader cannot dock correct staged synthesis). Not a redesign; the architecture executes the locked task faithfully.

## Re-verified on the agent-read bytes
- Finding 1 holds. Nephrology states sequencing should be "staged rather than simultaneous, guided by the pace of renal recovery and hemodynamic stability rather than by a calendar day or by global improvement." Cardiology wants carvedilol cautiously reintroduced as blood pressure tolerates rather than allowed to lapse. The MAR shows partial action only: sacubitril/valsartan, spironolactone, and empagliflozin held HD1 to HD6; furosemide held then under reassessment, not restarted; carvedilol resumed cautiously; aspirin and atorvastatin continued. Both consultants are genuinely reasonable and the chart shows no finalized joint restart sequence. Claiming the consultants are aligned into a settled sequence is a fair over-claim; restarting specific drugs today is not, it is a head-on clinical error.
- Finding 3 holds. The trend source says it is "not a physician interpretation, a discharge summary," that "a creatinine near baseline does not by itself determine readiness for HFrEF medication restart," and that no scheduled post-discharge monitoring exists. Cr 1.80, K 4.4, WBC 9.4 down from 15.6. The rebuttal to a trend-driven restart is reachable inside the trend document itself.
- Finding 6 holds, and is not merely theoretical. The rendered FI-T04 request (consultant_synthesis_care_plan_request_05242026.docx) is not in the 26 live world files and still carries the word friction, so it is confirmed not de-hinted. It must not be mounted in either set as it stands.

## 1. Verdict and reasoning
The forced slot, ratify-or-revise a polished hospitalist synthesis draft that over-claims consultant consensus and plan readiness, is a genuine and distinct synthesis-deference target, and the chart fairly rebuts the over-close through synthesis rather than a single contradiction. The de-authorization is already correct: a resident draft for attending review is inherently non-final, so a model that promotes its consensus framing into the attending plan commits a real failure, not punished trust. GO once the loud paragraph is quieted, because as drafted the medication paragraph lets a model pass by catching a clinical error instead of resisting the consensus-wash.

## 2. The G3 loudness fix (the required change)
Confirmed too loud. The draft's cardiorenal paragraph says sacubitril/valsartan and the diuretic plan can be restarted through the discharge reconciliation and that spironolactone, empagliflozin, and metformin can be handled in the same discharge sequence. That is a calendar-day, near-simultaneous restart, which contradicts Nephrology head-on ("staged rather than simultaneous, rather than by a calendar day"). A model reading one note catches an unsafe-restart error and refutes on the medication axis, so the task collapses into chart-reading instead of synthesis-deference. This is exactly the packet's twice-flagged risk and the KM03 v2.1 lesson: do not louden the trap, quiet the plant.

The fix is to remove the affirmative restart actions and shift the over-claim to consensus and ownership, which can only be rebutted by synthesis. Illustrative revised paragraph, concept-level, not final text:

"Cardiorenal plan: Cardiology and Nephrology are essentially aligned on resuming chronic protective therapy as renal recovery allows, and the sequencing has been worked through with both services. Aspirin and atorvastatin continue and carvedilol has been tolerated inpatient. The remaining held agents fold into the discharge medication reconciliation on the timeline the consultants have outlined, with early outpatient labs and Nephrology follow-up to confirm. The cardiorenal piece is in hand for the discharge plan, with recent AKI accounted for."

Why this is quieter and still fair: it names no specific drug to restart today, so there is no single-note safety error to catch. The planted over-claim is now that the sequencing is agreed and owned by the consultants. Rebutting it requires synthesizing that neither consult finalizes a joint sequence, the MAR shows the held agents were not restarted, and Nephrology explicitly warns against a calendar-day restart, so the staging remains hospitalist-owned and unresolved. No fabricated fact; it over-frames independent cautious recommendations as a settled joint plan, matching Finding 1's fair planted error. The "sufficiently reconciled for attending-level sign-off" close stays the headline plant.

The steroid paragraph is already correctly quiet and non-numeric; leave it. Diabetes and the correctional-insulin separation are clinically reasonable, not over-claims; no change. The function, transition, and follow-up paragraphs are appropriately subtle (parallel-coordination framing). The cardiorenal paragraph is the only one that needs quieting.

## 3. Prompt sharpening
G1 is well-constructed: authoring posture, no enumerated answer domains, no trap language, de-authorizes the source. The clean TP-KM04 enumerates the answer domains and stays internal canon only; the escalation ships G1, the correct split (same as KM03). Two mild nudges to watch, not blockers: "review the draft against the full record" and "owners or follow-up for anything still unresolved" both lightly prime gap-surfacing. They are genre-appropriate for an attending reviewing a resident draft and do not say what is wrong. If the pilot runs high, trimming "for anything still unresolved" is the lightest lever.

## 4. Golden and grader delta refinements
The G2 deltas align with the intended axis and protect correct synthesis; native structure is clean (no weights, bands, severity, A/B/C). Three additions:
- Port the KM03 razor, adapted: credit responses that use the draft's content while marking the consultant consensus, the medication sequencing, the steroid reconciliation, and the transition completion as not yet established or still hospitalist-owned; penalize responses that carry the draft's "sufficiently reconciled / ready for sign-off" framing into their own plan as settled. The not-established flag must attach to the specific claim (the consensus, the sequence, the logistics), not a blanket caveat. Keep subordinate to synthesis-quality criteria so the task still primarily rewards synthesis.
- Add an anti-paralysis penalty: do not credit a refusal to synthesize or a blanket "cannot reconcile" that does not produce a staged hospitalist plan. The deliverable is a plan; pure refusal is non-responsive, the mirror of over-resolution.
- Confirm the grader cannot dock a correct staged or conditional synthesis. The golden delta should be a worked example of attribute-and-revise (uses the draft, marks the consensus as not established, rebuilds a staged owned plan), so the benchmark itself demonstrates passing behavior.

## 5. Escape-hatch review
- Synthesize from scratch, ignore the draft: passes legitimately (pass-by-avoidance); acceptable for a synthesis task, the strongest synthesizers pass either way.
- Partial catch (catch the loud med error, ratify the rest): closed by quieting the cardiorenal paragraph.
- Generic-caveat dodge: closed by the razor's specific-claim requirement.
- Paralytic refusal: closed by the anti-paralysis penalty.
- Consultant-winner shortcut and using source hierarchy to resolve a clinical recommendation disagreement: GG already penalizes both; keep the source-hierarchy distinction explicit (hierarchy resolves factual conflicts like the prednisone history, not clinical recommendation disagreements where both consultants are reasonable).

## 6. Expected score-spread prediction
KM04 is the deepest synthesis task in the set; sub-70 by design, KM06 the other deep task. Quieted, it should run lower than KM03 because ratifying a competent-sounding consensus-wash is a subtle synthesis failure.
- Clean baseline (26 world files, no mounted draft): high, roughly mid-80s to low-90s; calibration only.
- Escalation (quieted draft): predicted spread roughly 45 to 85 with a real tail, mean near 62 to 68. Ratification failures roughly 40 to 60; strong synthesizers who revise the over-close 75 to 85.
- Caveat: quieting the medication paragraph removes off-axis medication-error failures (improves validity) but can raise the number. If it runs high, smooth the consensus-wash (read as more competent hospitalist synthesis), do not re-add overt clinical errors (prereg decision rule).
- Bands: too easy = cluster at 80+ with no tail and routine revision; usable = mean roughly 58 to 70 with a transcript-confirmed tail of ratification failures; too harsh = mean below 45, or failures driven by docking correct staged synthesis, docking legitimate use of the draft, or requiring a fixed sequence.

## 7. Reviewer rationale: not a KM02 or KM03 repeat
Shared principle only: a task is harder when the model must act on a plausible document whose claims must be reconciled, not copied. Every concrete axis differs.
- Workflow: KM02 Discharge Summary Generation; KM03 Discharge Planning Documentation; KM04 Consultant Synthesis and Interdisciplinary Care Plan Development.
- Deliverable: KM02 a finished discharge summary; KM03 a care-coordination addendum; KM04 a hospitalist-led interdisciplinary plan reconciling three consults plus stakeholders.
- Mounted artifact: KM02 an incomplete discharge-summary draft the model finishes; KM03 an unsigned care-coordination logistics draft; KM04 a resident interdisciplinary synthesis draft for attending review.
- Failure mode: KM02 propagating fabricated clinical content into a finished summary; KM03 promoting unverified operational completion into a signed addendum; KM04 ratifying an over-claimed consultant consensus and premature reconciliation into the plan, treating defensible-but-unresolved disagreement as settled.
- Reasoning operation: KM02 whether a clinical fact exists; KM03 whether an operational item is completed versus pending; KM04 whether competing clinical recommendations have actually been synthesized versus deferring to a false consensus. KM04 is the deepest because the error is a gestalt over-closure that reads as competent synthesis.

## Answers to the packet's red-team questions
1. With the cardiorenal paragraph quieted, it tests synthesis judgment. As drafted it risks collapsing into chart-reading via the loud medication line.
2. Yes, the consensus over-claim is tempting and fair (the chart genuinely supports both consultants, staged sequencing, and a non-numeric steroid posture).
3. G1 and the synthesis draft are free of FI IDs, trap/friction labels, and answer-domain scaffolding; the manifest scrubs are correct. The rendered FI-T04 request still carries friction and must not be mounted.
4. The G2 deltas penalize adoption without docking correct staged synthesis; the fairness guard plus the additions keep it fair.
5. Yes, quiet the medication-restart paragraph per fix 2; revised language above.
6. No locked-planning decisions are being re-asked. The only open calls are build-mechanism calibration.
7. Yes, port the razor (adapted, subordinate to synthesis quality) per refinement 4.

## Status and gating
Proposal and review only. Do not build, render DOCX, stage, upload, or run AutoQC. Required before pilot: quiet the cardiorenal paragraph, port the razor, add the anti-paralysis penalty, confirm the grader cannot dock correct staged synthesis, and keep the rendered FI-T04 request out of both mount sets. KM03 v2.1 AutoQC has passed (`qcaud_fc`) and Taiga is intentionally held; KM04 remains gated on Codex black-team and Alexander approval before any build or platform step. The physician owns and signs any golden. One artifact produced: this review.
