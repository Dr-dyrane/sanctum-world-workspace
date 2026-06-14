# Task Difficulty Lessons - what makes an RL eval task hard (Korvin Merrow, tasks 1-10)

Date: 2026-06-08, extended 2026-06-12 (KM07-KM10 evidence + the fairness doctrine, including AO's KM08 draft-fairness rule + the Raising Task Difficulty worked example + King P's legitimate-failure score guidance). Source: the full KM01-KM10 build/pilot history plus `reference/source/Raising_Task_Difficulty_Worked_Example.pdf`. Companion: `docs/grader-guidelines-lessons.md` (structure + length), `docs/task-structure-dossier.md` (the 8 structures + variety mandate), `docs/clinical-voice-lessons.md` (golden register), `docs/reviewer-response-protocol.md`. This is the difficulty playbook: read it before designing any new task. Two axes govern a task and they are independent - DIFFICULTY (does it floor a strong model) lives in sections 1-4 and 7; FAIRNESS (is the floor the model's fault) lives in sections 5-6. A task ships only when it is BOTH hard AND fair; the suite paid for both rules in reseeds.

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

Two important successors learned later: (1) the bare planted-fabrication form is now gated by the fairness doctrine (section 5). A fair placeholder must assert nothing about the scored item in the built draft, and the uploaded file tree must not leak the correction by filename or duplicate mounted copies. KM07 v3 failed because the draft still listed alendronate under current medications beside a held list. KM07 v4 job 6b687360 then failed Studio hygiene because the agent saw two mounted drafts from two volumes: a stale old draft under `/docs/filesystem` and a pre-corrected copy under `/docs/.apps_data/calendar`. The `v4_clean` name added a telegraph, but the root cause was the extra calendar volume. The corrected v4 staging requires one filesystem volume with exactly one visible started draft. (2) The forced move does not have to come from a planted lie at all: a forced-inventory schema (KM01 med rec, KM09 coding) forces a value per row with no deferral, and an external adversarial document wrong-by-genre (KM10 CDI query, a denial letter) forces agree-or-rebut. Those floor fairly without any planted claim. See `docs/task-structure-dossier.md` for the eight structures and where each one's forced move lives.

## 3a. Worked Example #1 hardening pattern: remove the answer key, force reconciliation, add off-text signal

Source: `reference/source/Raising_Task_Difficulty_Worked_Example.pdf`. The example moved an SNF admission-note task from near-universal high scores to repeated clinical failures by changing the information geometry, not by making the prose louder. The transferable pattern:

1. Pull the answer key out of world files. A world-level discharge summary or consultant synthesis that states the conclusion turns the task into transcription. World files should provide raw material, not the completed synthesis. If a later task truly needs the summary, mount it as a task-level file scoped to that task, and make the prompt explain why the user does not already have it.
2. Force reconciliation. No single source should be complete. The model should have to cross-check vitals, MAR, consults, nursing notes, imaging, photos, forms, and templates to get the non-negotiables right.
3. Add realistic task-level noise and required format. A template, intake form, or extra nursing note can be fair if it mirrors practice and does not pre-answer the task. The model then has to sieve relevant from irrelevant information while fitting the answer into a required structure.
4. Bury one critical finding off the text when clinically realistic. Images are fair game and often harder for the model than prose. A task-level photo, handwritten list, medication bottle, preliminary imaging capture, or downtime note can carry a decisive finding, especially if the prose only contains indirect hints such as a low-grade temperature or "photo taken."
5. Match the grader to the stakes. If missing the off-text finding would be indefensible in real care, make it a hard error. Do not let a polished note with the central clinical miss score as merely incomplete.

Guardrail: off-text and multimodal traps must still be fair. The image or audio must be visible to the agent, realistic for the workflow, temporally anchored, and supported by at least a minimal chart clue. The model should fail because it did not integrate available evidence, not because the file was hidden, post-cutoff, illegible, or impossible to interpret. For guideline-timing traps, the needed rule must match the world's date, or the dated guideline source must be attached.

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
| KM07 v3 | bone-health status, partial placeholder | referral letter | cold + forced but unfair | 52.5 | retired 6/11; built draft still asserted alendronate as current |
| KM07 v4 | true placeholder, alendronate absent from neutral-named draft | referral letter | cold + forced + fair pending clean pilot | pending | first v4 job invalid due extra `.apps_data/calendar` volume plus stale filesystem draft; Studio volume cleanup needed |
| KM08 v3 | inpatient-vs-observation | determination | unambiguous case | 96 | failed - verdict was free (not borderline) |
| KM08 v4 | gabapentin uptitration on overnight self-report | progress note | cold + forced + 4 contraindications, unfair draft | 67 | DEEP but returned; draft pre-wrote the scored uptitration order with finalize-only prompt |
| KM09 | sepsis-to-principal sequencing | coding attestation | forced inventory, fights severity-anchoring | 31 | DEEP win |
| KM10 | retrospective encephalopathy add | CDI query response | adversarial-by-genre | ~25 v1; v2 dirty all-floor excluded; v3 pending | v1 returned by AO; v2 job 138e90a2 invalid due duplicate `.apps_data/calendar` query memo. v3 balanced query surface staged to seek catcher plus critical failure, not grader softening |

Two refinements the suite paid for:
- Chart-SILENT is not the same as chart-CONTRADICTED. A fair, deep failure must be something the record CONTRADICTS or explicitly mandates, never something it is merely silent about. KM05 v4-pilot1 (home BP/weight at +7) floored every run but was UNFAIR and would be bounced, because the +7 home data is silent in the chart and the model cannot be faulted for trusting it. Re-centering onto the premature restart (which the chart explicitly defers to outpatient cardiology/nephrology) gave a fair bimodal spread.
- A REVIEW genre is anti-cold. Reviewing IS verifying, so the whole document is warm; KM06-orthostatic put the plant on the fall-risk headline of a fall-risk review and every run caught it. Use a DOCUMENTATION genre (summary/plan/note) where the plant sits in a BACKGROUND section the model finishes without special scrutiny.

## 5. Fairness of construction (the Abi doctrine - what makes a floor FAIR to the model)

A floor is only bankable if the model's failure is genuinely the model's fault. Abi (pod lead) ruled the same construction unfair repeatedly - KM05, KM06, KM07, then KM08 - and it is now a standing pre-build gate. THE RULE: a mounted draft that carries a false, unsupported, or judgment-bearing claim, authored by the same person who writes the golden, with NO instruction to the model to correct it, is unfair to floor. Propagating a claim handed to you in your own working draft is defensible behavior; flooring it punishes the model for trusting the draft it was given. KM07 v2 floored 9 of 10 on a planted bone-health closure and was retired as unfair despite being mechanically perfect. KM08 v4.1 had real catchers but still failed the same class because the draft pre-wrote the gabapentin uptitration order and the prompt only said to finalize it.

Canonical AO 6/11 rule for finalize-the-draft tasks: before turning it in, either prompt the model to correct errors in the draft, or use placeholders in the draft for the model to complete in the finalized version. That is the whole gate. For our purposes:
- TRUE PLACEHOLDER / SYNTHESIZE: the built draft asserts nothing about the scored item. "Nothing" means no current list membership, no held list membership, no dose, no plan order, no schedule, no routine-looking placement, and no pre-written plan order. The uploaded file tree must also assert nothing: no duplicate old/new drafts, no hidden pre-corrected `.apps_data` copy, no extra task-file volume, and no meta-answer filename such as clean, fixed, corrected, reviewer, or v4_clean. KM07 v3 proved that a generic status disclaimer does not un-assert a current-medication listing; KM08 v4.1 proved that a pre-written plan order is an assertion; KM07 v4 job 6b687360 proved that an extra `.apps_data/calendar` volume can pre-answer or destabilize a task even when the local current/ folder is clean.
- RECONCILE-AND-CORRECT INSTRUCTION: tell the model in the prompt to reconcile the draft against the record and correct anything unsupported before signing (KM06 v4). This passes fairness but usually kills propagation difficulty.
- RE-ATTRIBUTION is not a same-author draft fix. It belongs to external or weak-source documents where the model is fairly expected to evaluate the source, such as patient-reported home BP or an external handoff. Do not use re-attribution to justify false content inside the model's own started draft.

CRITICAL TENSION - fix (c) is a difficulty-killer. A mandatory reconcile/verify posture defeats EVERY propagation/fabrication mechanism: a model told to verify everything catches every chart-contradicted claim. KM06 v4 went to mean ~0.98 (all-catch) the moment the reconcile clause was added, which is why KM06 abandoned false-closure entirely for the v5 insulin-uptitration judgment trap. On any propagation/closure mechanism, prefer (a) or (b); reserve (c) only when the task is a genuine judgment trap that survives a fully-reconciling model. Never add a reconcile clause to chase a clean board, and never add stance instructions to the prompt to make a catch easier - that is the same telegraph.

What stays fair WITHOUT a fix: an external adversarial document that is wrong BY GENRE (a payer denial letter, a CDI query asking for an unsupported upcode, a pharmacy handoff with an unsafe rec) is realistic-by-genre, so the model is fairly expected to push back (KM01 pharmacy handoff, KM09 coding attestation, KM10 CDI query). The unfairness is specific to a false claim planted in the model's OWN draft with no signal to distrust it.

## 6. Fairness of spread (the symmetric-spread test)

A bankable deep task is BIMODAL: a clear floor (the propagators) AND clear catchers (0.85-0.95) proving a strong model can pass. All-floor (no catcher) reads as an unfair gotcha when the clinical stance itself is contestable, so prove reachability with a catcher run when possible. When no agent produced a catcher in 10 runs, reachability can be supported structurally by confirming the golden itself scores ~0.85-0.95 under its own grader, but that is weaker than an actual catcher. Do not confuse this with the separate difficulty gate: King P's 6/12 guidance says the content of the trajectory matters more than the percentage. If at least one trajectory shows legitimate model failure that materially lowers deliverable quality or creates patient-harm or malpractice risk, the task can be acceptable even when the score is noisy or high. If all the evidence is cosmetic, such as a missing clinic logo, it is not a legitimate failure. The grader must score the floor on the real failure and reward the correct restraint at the ceiling. Confirm fairness and bankability by reading the output and transcript, not just the mean.

## 7. Reading a pilot

- Read by PER-AXIS propagation rate / disposition, not the headline mean.
- Read the content before trusting the percentage. The score is evidence, not the verdict. A 0.90 can hide a legitimate clinical failure, and a low score can be unusable if the only defect is cosmetic.
- Do not require a sub-70 score for approval. One trajectory with a critical clinical or material deliverable failure can be bankable if the construction is fair and the FA can explain the miss.
- For a propagation task: do the floors carry the fabricated line forward, and do the catchers correct it and score high?
- If it clusters too high (no floor): the axis is too warm/bright or the plant too obvious - re-center the IDEA (colder axis, sharper plant), do NOT just rewrite prose.
- If it is all-floor (no catcher): check the plant is chart-CONTRADICTED, not chart-silent; if silent, it is unfair - re-center onto the chart-mandated move (the KM05 v4 fix).
- The FA subject must be a legitimate model failure: clinically meaningful omission, inaccurate synthesis, unsafe recommendation, or material degradation of the deliverable. Do not bank a task on cosmetic misses.
- The lowest-floor run is usually the FA subject; a clean catcher is the GA symmetry anchor. If the lowest score is only cosmetic but another run contains the real failure, escalate the selection rationale instead of writing a weak FA.

## 8. One-line summary

Difficulty is a property of the idea: a cold, chart-contradicted, forced move that inverts what the model polices. Fairness is independent: the failure must be the model's own fault, not a planted lie it was never told to correct, and the correct answer must be reachable. A task ships when the trajectory content shows a legitimate clinical or material deliverable failure and the construction is fair. Everything else (voice, structure, length) is for passing review.

## Floor depth: separate the APPROVAL bar from the DESIGN target (canon, 2026-06-14)
Two different things, do not conflate them:
- APPROVAL (platform rule): a task does NOT need a trajectory below 70 (or below 60). It needs ONE legitimate critical clinical or material (signability) failure in a trajectory. The bar is the QUALITY of the failure (real, material, the model's own fault - King P), never a numeric score threshold. Do not gate approval on <60 or <70.
- DESIGN (our Sanctum build target): design the intended floor so a fair bad run lands ~0.30 to 0.55, with at least one catcher above 0.85. That band is the practical canonical target because it forces a real signability failure rather than a soft miss, and it gives margin to survive review.

CANON (one line): Do not require <60 to approve a task. But when designing a task, target a floor-worthy failure below 60, with at least one catcher above 85.

Why design low: a deep floor requires the missed item to be CENTRAL and material AND Section A to floor it hard. Evidence: OV01 banked on its 0.40/0.50 runs (material enoxaparin safety failure); OV02's only sub-70 was a 0.62 that was file-output NOISE; KM's bankable tasks floored 0.15-0.40 (the one that limped to 0.55, KM09, was the weakest). A miss that only grazes (0.62-0.68) is usually partial-credit, lenient grading, or noise - so if the best the mechanism can force is a graze, it is too soft: re-center or retire, never tune the grader to manufacture depth.
Read rule: judge a run by whether its failure is legitimate and material, not by the number. A 0.60-0.74 run still counts IF it reflects a real critical/material miss (that satisfies the platform bar); it is noise only when the drop is an artifact (missing /tmp/outputs, partial credit on a non-material point). We design for 0.30-0.55 so the material failure is reliable and clears review with margin.
