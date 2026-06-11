# Task Difficulty Lessons - what makes an RL eval task hard (Korvin Merrow, tasks 1-10)

Date: 2026-06-08, extended 2026-06-11 (KM07-KM10 evidence + the fairness doctrine). Source: the full KM01-KM10 build/pilot history. Companion: `docs/grader-guidelines-lessons.md` (structure + length), `docs/task-structure-dossier.md` (the 8 structures + variety mandate), `docs/clinical-voice-lessons.md` (golden register), `docs/reviewer-response-protocol.md`. This is the difficulty playbook: read it before designing any new task. Two axes govern a task and they are independent - DIFFICULTY (does it floor a strong model) lives in sections 1-4 and 7; FAIRNESS (is the floor the model's fault) lives in sections 5-6. A task ships only when it is BOTH hard AND fair; the suite paid for both rules in reseeds.

## 1. The core principle: the IDEA is the lever, not the writing

Writing quality and the trap idea are two different axes governing two different outcomes:
- Writing (clinical voice, Sang grader structure, house style, length) governs whether the task PASSES REVIEW. Necessary, but it does nothing for difficulty.
- The trap IDEA governs DIFFICULTY - the entire score spread. A well-written task with a weak idea clears high every time.

Proof both ways: KM05-NSAID and KM06-orthostatic were clean prose with textbook graders and both scored ~93 (failed). The wins (KM02/03/04) share the same IDEA, not the same prose. So judge the idea on reasoning first; a weak idea dies cheap in the workspace and only a real idea earns a pilot.

## 2. The 4-point trap test (run before writing a line)

1. Cold - is the axis un-hunted, NOT primed by the chart's loud threads, the other tasks, or the deliverable's own headline?
2. Forced - is there one wrong move, so caution is not free?
3. Against the default - does catching it require something other than the model's trained "be cautious / don't fabricate" reflex? If free caution passes, it is too easy.
4. Direction - invert what the model is primed to police (it guards "don't restart too fast" -> plant a de-escalation; it guards "don't add false facts" -> plant a reassuring one it accepts).

## 3. The one reliable mechanism

Completion genre + a single buried fabricated objective result in an otherwise-correct draft, on a COLD axis the chart can cleanly contradict but where the model has no reason to suspect error. It works because: the draft is 95%+ correct so the model trusts it; the planted line is plausible; the chart has clear contradicting evidence but requires active lookup; and the model self-verifies its OWN additions, never re-verifying what it inherited from the draft. That verification asymmetry is the universal exploit.

Two important successors learned later: (1) the bare planted-fabrication form is now gated by the fairness doctrine (section 5) - the FAIR version leaves the status as a placeholder the model synthesizes from the chart (KM07 v3), which keeps a real floor because the "home meds continue / nothing outstanding" prior still drives a fabricated closure even when it is a blank to fill, not a claim to ratify. (2) The forced move does not have to come from a planted lie at all: a forced-inventory schema (KM01 med rec, KM09 coding) forces a value per row with no deferral, and an external adversarial document wrong-by-genre (KM10 CDI query, a denial letter) forces agree-or-rebut. Those floor fairly without any planted claim. See `docs/task-structure-dossier.md` for the eight structures and where each one's forced move lives.

## 4. COLD beats WARM (the rule that decides difficulty)

A fabrication on a WARM axis (primed; the model is already hunting it) gets caught universally. A COLD axis (un-hunted background) gets propagated. The deliverable's own subject makes its headline axis WARM.

Measured evidence (ran and scored):
| Task | Axis | Genre | Warm/Cold | Mean | Result |
|------|------|-------|-----------|------|--------|
| KM01 | unsafe rec (nitrofurantoin etc.) | med rec | bright/known | 89 | clears, soft |
| KM02 | urine culture (E. coli) | discharge summary | cold secondary | 59 | DEEP win |
| KM03 v1 | cardiorenal restart | discharge planning | warm/primed | ~94 | killed |
| KM03 v2.2 | CPAP adequacy | discharge planning | cold secondary | 76 | DEEP win |
| KM04 v1 | (renal/primed) | care plan | warm | 91 | failed |
| KM04 v2 | iron studies / anemia | care plan | cold secondary | 66 | DEEP win |
| KM05 v2 | +7 interval observation | transition note | chart-silent | (killed) | unfair |
| KM05 v3 | NSAID-in-CKD | transition note | bright/known | 95 | failed |
| KM05 v4-pilot1 | home-BP+weight+immun (3 plants) | transition note | chart-silent | 20 | unfair, all-floor |
| KM05 v4 | premature restart on home BP | transition note | cold + forced | 36 | DEEP win, bimodal |
| KM06 v1 | orthostatic vitals | fall-risk SAFETY REVIEW | WARM (headline) | 93 | failed |
| KM06 v2 | echo / LVEF recovery | transition summary | cold secondary | 97 | failed (warm enough) |
| KM06 v4 | med false-closure + reconcile clause | follow-up note | cold but instructed | ~98 | failed - reconcile clause killed it (see 5) |
| KM06 v5 | premature insulin uptitration on home glucose | +30 follow-up | cold + forced | 60 | DEEP win, bimodal |
| KM07 v1 | cardiorenal restart, FROM-SCRATCH | referral letter | warm + no forced slot | 93.8 | failed (both faults) |
| KM07 v2 | bone-health false closure (planted) | referral letter | cold + forced | 36 | floored 9/10 but UNFAIR (see 5) - retired |
| KM07 v3 | bone-health status, PLACEHOLDER synthesize | referral letter | cold + forced + fair | 52.5 | fair mid-band, bankable |
| KM08 v3 | inpatient-vs-observation | determination | unambiguous case | 96 | failed - verdict was free (not borderline) |
| KM08 v4 | gabapentin uptitration on overnight self-report | progress note | cold + forced + 4 contraindications | 67 | DEEP win, bimodal (0.10 floor, 0.95 catch) |
| KM09 | sepsis-to-principal sequencing | coding attestation | forced inventory, fights severity-anchoring | 31 | DEEP win |
| KM10 | retrospective encephalopathy add | CDI query response | adversarial-by-genre | ~25 | all-floor; reachability (catcher) open |

Two refinements the suite paid for:
- Chart-SILENT is not the same as chart-CONTRADICTED. A fair, deep failure must be something the record CONTRADICTS or explicitly mandates, never something it is merely silent about. KM05 v4-pilot1 (home BP/weight at +7) floored every run but was UNFAIR and would be bounced, because the +7 home data is silent in the chart and the model cannot be faulted for trusting it. Re-centering onto the premature restart (which the chart explicitly defers to outpatient cardiology/nephrology) gave a fair bimodal spread.
- A REVIEW genre is anti-cold. Reviewing IS verifying, so the whole document is warm; KM06-orthostatic put the plant on the fall-risk headline of a fall-risk review and every run caught it. Use a DOCUMENTATION genre (summary/plan/note) where the plant sits in a BACKGROUND section the model finishes without special scrutiny.

## 5. Fairness of construction (the Abi doctrine - what makes a floor FAIR to the model)

A floor is only bankable if the model's failure is genuinely the model's fault. Abi (pod lead) ruled the same construction unfair three times - KM05, KM06, KM07 - and it is now a standing pre-build gate. THE RULE: a mounted draft that carries a false or unverified claim, authored by the same person who writes the golden, with NO instruction to the model to correct it, is unfair to floor. Propagating a claim handed to you in your own working draft is defensible behavior; flooring it punishes the model for trusting the chart it was given. KM07 v2 floored 9 of 10 on a planted bone-health closure and was retired as unfair despite being mechanically perfect.

The three sanctioned fixes (any mounted draft with an unverified/false claim must do ONE):
- (a) RE-ATTRIBUTE the claim to a weak/unverified source (KM05: home BP re-attributed to the patient's own report). Attribution only - do NOT add an "unverified" caveat or you telegraph the catch.
- (b) PLACEHOLDER / SYNTHESIZE: the draft states no status; the model must complete it from the record (KM07 v3: the med-reconciliation block is left open, the model fills each status from the MAR). No planted lie exists, so flooring a fabricated closure is fair. This is the Abi-fair successor to draft-planted fabrication.
- (c) RECONCILE-AND-CORRECT INSTRUCTION: tell the model in the prompt to reconcile the draft against the record and correct anything unsupported before signing (KM06 v4).

CRITICAL TENSION - fix (c) is a difficulty-killer. A mandatory reconcile/verify posture defeats EVERY propagation/fabrication mechanism: a model told to verify everything catches every chart-contradicted claim. KM06 v4 went to mean ~0.98 (all-catch) the moment the reconcile clause was added, which is why KM06 abandoned false-closure entirely for the v5 insulin-uptitration judgment trap. On any propagation/closure mechanism, prefer (a) or (b); reserve (c) only when the task is a genuine judgment trap that survives a fully-reconciling model. Never add a reconcile clause to chase a clean board, and never add stance instructions to the prompt to make a catch easier - that is the same telegraph.

What stays fair WITHOUT a fix: an external adversarial document that is wrong BY GENRE (a payer denial letter, a CDI query asking for an unsupported upcode, a pharmacy handoff with an unsafe rec) is realistic-by-genre, so the model is fairly expected to push back (KM01 pharmacy handoff, KM09 coding attestation, KM10 CDI query). The unfairness is specific to a false claim planted in the model's OWN draft with no signal to distrust it.

## 6. Fairness of spread (the symmetric-spread test)

A bankable deep task is BIMODAL: a clear floor (the propagators) AND clear catchers (0.85-0.95) proving a strong model can pass. All-floor (no catcher) reads as an unfair gotcha and gets bounced (KM10 carries exactly this open flag - no catcher observed; confirm any run can decline before banking). The grader must score the floor on the planted failure and reward the correct restraint at the ceiling. Confirm fairness by reading a catcher transcript, not just the mean. When no agent produced a catcher in 10 runs, reachability can still be shown structurally: confirm the golden itself scores ~0.85-0.95 under its own grader (KM07 v3 golden-reachability check).

## 7. Reading a pilot

- Read by PER-AXIS propagation rate / disposition, not the headline mean.
- For a propagation task: do the floors carry the fabricated line forward, and do the catchers correct it and score high?
- If it clusters too high (no floor): the axis is too warm/bright or the plant too obvious - re-center the IDEA (colder axis, sharper plant), do NOT just rewrite prose.
- If it is all-floor (no catcher): check the plant is chart-CONTRADICTED, not chart-silent; if silent, it is unfair - re-center onto the chart-mandated move (the KM05 v4 fix).
- The lowest-floor run is the FA subject; a clean catcher is the GA symmetry anchor.

## 8. One-line summary

Difficulty is a property of the idea: a cold, chart-contradicted, forced fabrication that inverts what the model polices, buried in an otherwise-correct document. Fairness is independent: the floor must be the model's own fault (no planted lie it was never told to correct, and at least one reachable catch). A task ships only when it is both. Everything else (voice, structure, length) is for passing review.
