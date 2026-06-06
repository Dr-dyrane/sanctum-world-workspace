# Reasoning Discipline - the verification gate (workspace backbone)

Date: 2026-06-06. Status: BACKBONE doc. Cross-world, not Korvin-specific. Applies to every decision Claude makes in this workspace. Distilled from the Task 1 (KM01) retrospective and grounded in published sources (verified, not recalled). NO em dashes in any user-facing text remains a standing rule.

## LIVE CORRECTION (6/6) - I flipped THREE times on one fact; the transcript was the arbiter the whole time
Question: does the grader read the chart? My history on it: (1) said "golden-only" from a doc example; (2) Env Linter said "chart is mounted," I flipped to /docs-aware; (3) Abi (human reviewer) said "the grader does not go into the chart," I flipped again and edited THIS doc to say the Env Linter misled me. A cold-context review then pointed at the primary evidence I had held the entire time: the grading transcripts. VERIFIED GROUND TRUTH from the transcripts: include_input_files=true, the chart IS mounted, and the 0.78 grader (aef58074) ran `find /docs` and pandoc'd the med rec, handoff, cardiology, nephrology, endo, MAR, trend summary, and discharge snapshot directly from /docs/filesystem. The 0.72 grader (564d568d) instead worked from the golden + the model's embedded transcript. Both had chart access; they used it differently.
THE REAL LESSON (harder than the original): the failure was not "trusting the linter" or "trusting Abi." It was failing to anchor on the PRIMARY ARTIFACT (the transcript) I already possessed, and instead treating each new authoritative-sounding claim as ground truth. When a factual claim about system behavior is contested, go to the primary artifact, not the most recent authority. The transcript was the falsifier all along; I kept not reading it as the arbiter.
NOTE on deliverables: this changes none. For the GA, narrowing to the 0.72 run (per Abi) makes "scored from the golden + model transcript" both accurate and Abi-compliant - no "went into the chart" needed. The v5 grader guidelines are MECHANISM-AGNOSTIC (judge vs the golden; do not instruct the grader on how it verifies), which is correct regardless of chart access. Keep the chart-access fact in the back pocket only for any future Self-Contained-gate question; it does not belong in GA text.

## PROVISIONAL / STILL LEARNING (6/6) - not backbone yet; promote only if it holds across more tasks
Working hypothesis from the Task 1 round-2 retrospective. Flagged provisional on purpose: it comes from ONE task bouncing once for difficulty, n=1, so treat it as a lead to test on Tasks 2-6, not a settled rule. Do not let it harden into doctrine until the pattern repeats.

The observation: we sailed through brainstorm and world build, then the task "failed" at human review for being too easy (all 10 runs >=90). The likely cause is an OBJECTIVE-FUNCTION SHIFT we did not notice at the stage boundary. World stage grades realism (consistent, faithful, no leakage, reads like a real chart) and we are good at it. Task stage grades the opposite-ish thing: does a frontier model actually fail here. Cleaner and more realistic often means EASIER, so the two stages pull against each other in one place, and we carried world-stage momentum (make it clean and correct) into a stage that rewards making a strong model stumble.

The receipt: in round 1 we deleted the leaking task files and scores went UP (72-95 to 90-97). Those files were doing two jobs, leaking the answer AND giving the model surface to trip on, and we removed both as if they were one problem. Leakage and difficulty are different axes. A task file can be adversarial without leaking (the handoff-trap). We over-corrected cleanliness and stripped difficulty out with the leakage.

The deeper miscalibration: prednisone provenance, cardio/nephro staging, buried evidence are hard for a tired resident, not for a model that reads all 26 docs perfectly and never fatigues. We were designing HUMAN-traps. The model fails on different things: an authoritative voice telling it to do the wrong thing, rewards for over-helpfulness, ambiguity it should resist resolving. The handoff is the first real MODEL-trap.

The candidate rule to test (NOT yet adopted): design the failure FIRST. Decide what a strong model should get wrong and why it would genuinely fall for it, then wrap realism around that, instead of building realism first and hoping difficulty emerges. Invert the build order for tasks.

Structural caveat that makes this hard to catch early: AutoQC grades form (green/red), never difficulty. The first difficulty signal is a human running trajectories. So "too easy" is only knowable at human review, which is also why holding Tasks 2-6 until Task 1's pattern settles was correct. Watch whether Tasks 2-6 confirm or break this before promoting it above this line.

## The one rule
Before any commit that is expensive or irreversible to undo, or any claim about WHY a system did something, drop out of inductive guessing and read the ground truth (the config, the transcript, the output, the file). Everywhere else, stay fast. Falsification before commitment at the irreversible nodes; induction everywhere else.

## What this fixes (the Task 1 evidence)
The day's costly errors all shared one shape: reasoning from a confirming instance or a plausible pattern when the ground truth was available to check, and not checking it before committing.
- The golden-only grading-config error: inducted from ONE instruction-doc example ("grades golden-only") to "this task's grader grades golden-only," committed a fix on it, and it triggered an irreversible Go Back to Task Writing + a full AutoQC + 10-trajectory rerun. The falsifier (include_input_files=true) was sitting in the grading transcript the whole time.
- The "grader underscore" / "near-perfect 0.78 run" call: assessed the trajectory from my own read (which missed metformin exactly as the model did) instead of reading the grader transcript first.
- The guessed low-run failure modes (restart specificity, antibiotic stop-date, supervision gap): all wrong; the real miss was metformin, visible by a 10-second grep of the output.
Every one was caught by switching into verification mode (pull transcript, grep output, read config). Verification never failed once it was used. The problem was using it AFTER the wrong call, not before.

## The mirror (why this world specifically)
Task 1 is built to punish this exact error. The model dropped metformin because it inducted "I reconciled everything" from a confident self-count ("18 of 19 verified") and never did the deterministic check (count the list against the chart). The grader scored it correctly because it did the one thing the model and my first read both skipped: it went into the chart and verified. The discriminator that separated the 90s from the 70s is the same discriminator that separated my good calls from my costly ones: trust the reassuring surface, or check the buried ground truth.

## The five published anchors (verified quotes; paraphrases marked)
1. PROBLEM OF INDUCTION / FALSIFICATION - Karl Popper (paraphrase of his established position, per Stanford/IEP): no number of confirming instances can establish a universal claim as true, while a single disconfirming instance refutes it; the rational move is to seek the falsifier, not pile up confirmations. -> Don't stop at the confirming instance. Look for the one thing that could prove you wrong.
2. CONFIRMATION BIAS - Peter Wason, 2-4-6 task (1960): subjects tested only positive examples of their hypothesis, never the disconfirming ones; every time the hypothesis "worked" their confidence grew, and only ~20% found the real rule. -> "It worked 90% of the time" is the documented trap: confidence rises precisely while you are wrong. The confirmations are not proof.
3. SELF-DECEPTION - Richard Feynman, "Cargo Cult Science," Caltech 1974 (verbatim): "The first principle is that you must not fool yourself, and you are the easiest person to fool." -> Trust the artifact over my own surface impression. (The "evidence-based medicine" creed, stated for science.)
4. MEASURE, DON'T GUESS - Rob Pike, "Notes on Programming in C" (verbatim, Rule 2): "Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest." -> Do not guess where the truth is. Read it. (Pulling the transcript / grepping the output IS the measurement.)
5. ONE-WAY vs TWO-WAY DOORS - Jeff Bezos, 2015 Amazon shareholder letter (verbatim): "Some decisions are consequential and irreversible or nearly irreversible, one-way doors, and these decisions must be made methodically, carefully, slowly... We can call these Type 1 decisions. But most decisions aren't like that, they are changeable, reversible, they're two-way doors... Type 2 decisions can and should be made quickly." -> The calibration trigger: verify at the one-way doors; stay fast at the two-way doors. The failure was walking through a one-way door (a recommendation that forces a rerun) at two-way-door speed.

## The operating gate (apply every task, every world)
At each decision, ask: is this a one-way door (expensive/irreversible to undo) OR a causal claim about why a system behaved a certain way?
- If YES: switch to verification mode. Read the actual config/transcript/output/file before committing. State plainly which parts of the recommendation are verified vs inferred.
- If NO: stay in fast inductive mode. Being wrong here costs a cheap retry; do not over-verify (Bezos warns that Type 1 process on Type 2 decisions is its own failure).

The proactiveness is the two-way-door engine and stays fast. The gate is a single question added at the expensive nodes, not a brake on everything.

## Synthesis
Feynman is WHY (you are the easiest person to fool). Wason is the WARNING (you will feel confident regardless). Popper is the LOGIC (confirming instances do not license the conclusion; seek the falsifier). Pike is the METHOD (measure, do not guess). Bezos is the TRIGGER (do it at the one-way doors, stay fast at the two-way doors).

## Sources (verified 2026-06-06)
- Feynman, "Cargo Cult Science," Caltech 1974: https://people.cs.uchicago.edu/~ravenben/cargocult.html ; https://speakola.com/grad/richard-feynman-caltech-1974
- Popper (problem of induction / falsification): https://plato.stanford.edu/entries/popper/ ; https://iep.utm.edu/pop-sci/
- Wason 2-4-6 task / confirmation bias: https://en.wikipedia.org/wiki/Peter_Cathcart_Wason ; https://explorable.com/confirmation-bias
- Pike, "Notes on Programming in C" (Rule 2, Measure): https://www.lysator.liu.se/c/pikestyle.html ; https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html
- Bezos one-way/two-way doors, 2015 shareholder letter: https://www.founderstribune.org/p/10-passages-from-jeff-bezos-s-shareholder-letters ; https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/
