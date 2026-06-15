# KM02 (Hospital Discharge Summary) - design plan for 3rd-party review

Status: PRE-BUILD design. No prompt, golden, or grader written yet. This is the discriminator design, sent to claude.ai to red-team BEFORE we build, so we build slowly and right. Governed by docs/reasoning-discipline.md "THE LAW" (build real; build the task with the world's rigor; reason from the full context to outsmart the model, not feed it; difficulty is empirical and adversarial, not architectural).

Note: old drafts in platform/task2/ predate the law and are SUPERSEDED. We build from this read, not from them.

## CURRENT ROUND-2 STATUS (6/6 evening) - v5 and platform/task2 win

Current canonical KM02 review/prep surface is no longer this plan alone. Use `worlds/korvin-merrow/task-setup/platform/task2/README.md` for the clean-pilot platform set, `RED-TEAM-BRIEF-KM02.md` for the latest red-team packet, `golden-KM02-v5.docx` as the current ceiling, `grader-guidance-KM02-v1.md` for the task-specific grader draft, and `colleague-draft-KM02.md` only as escalation rationale. Historical passages below that say the chart has no culture status, no antibiotic, or that v4 is current are superseded by the agent-read DOCX verification and v5 update.

## CORRECTION (6/6) - the culture AND the antibiotic ARE in the agent-read world; earlier "absent" claims were wrong
This block supersedes every statement below that says the chart contains no culture status or no antibiotic. Those claims came from grepping the FI-W markdown and the .meta/references docx copy, NOT the agent-read upload/filesystem set. Codex caught it with hashes; verified against the bytes with python-docx (tables included):
- The agent-read MAR (file-review/upload/filesystem/medication_administration_record_05232026.docx, sha256 cf90ceb0...) names "Ceftriaxone 1 g IV q24h" HD1-HD3, "Oral step-down: cefpodoxime 200 mg PO BID" HD4-HD6, note "Completion vs continuation to be reconciled at discharge."
- The agent-read HD1-HD2 note (sha256 42d8ccdf...) documents "Urine culture preliminary growth pending speciation," "await culture speciation and sensitivities before narrowing." HD3/HD4 continue empiric, cultures/sensitivities pending. ED/H&P: reflex urine culture sent, blood cultures pending. Never narrowed; no organism/sensitivities finalized.
- The agent-read set (cf90ceb0) DIFFERS from the .meta/references + delivered copies (14f7844b); the agent-read MAR is the one with the antibiotic content. Always verify on upload/filesystem by filename/hash, python-docx incl. tables. The markdown is the thin layer.

CORRECTED DISCRIMINATOR: not "any culture statement is fabrication." The chart documents an OPEN culture status (preliminary growth, speciation/sensitivities pending, never narrowed). Reporting that is CORRECT and creditable. The fabrication that bites = a FINALIZED organism, a sensitivity profile, a no-growth / "cultures negative" closure, or NARROWING antibiotics by culture. The antibiotic "completion vs continuation to be reconciled at discharge" is a chart-given openness anchor.
CORRECTED ANTIBIOTIC GRADER SCOPE: ceftriaxone-to-cefpodoxime is a CORRECT world fact; credit it, do not penalize, do not require. Penalize only an invented different agent, or narrowing by culture, or a finalized culture closure.
The golden (golden-KM02-v5.docx / golden-KM02-source.md) states the culture and antibiotic exactly as the chart does.

## VERIFIED AGAINST FILES (6/6, after claude.ai red-team)
claude.ai red-teamed v1 of this plan and flagged two factual claims as load-bearing. Both checked against the live world; the reviewer is right on both, and the discriminator is revised accordingly. claude.ai should still verify independently from the attached files.

1. FI-W22 self-flags as incomplete (CONFIRMED, stronger than v1 said). FI-W22 contains a literal "## Items To Complete Before Final Discharge Order" section, the line "No final discharge order has been entered in this snapshot," an "Anticipated Disposition Frame," and a Guardrails block stating it "is not a completed discharge summary, final disposition decision, final medication reconciliation, final prednisone taper plan." So OVER-CLOSURE BROADLY IS CHART-COACHED: a careful model reads "anticipated / items to complete" and writes an open synthesis, the same way KM01's coached traps cleared >=90. Over-closure is therefore DEMOTED from the discriminator to a fair anchor. The reviewer's core objection stands: the FI-W22 language I leaned on to justify the trap is the same language that defuses it.

2. The chart never finalizes a culture (CONFIRMED). grep across all 22 world files: no organism, no speciation, no "no growth," no sensitivities anywhere. Infection is "suspected urinary-source" from ED through HD6. FI-W12 only quietly notes culture "is not summarized here as a definitive single-cause answer," buried in a trend-source file, and nothing anywhere says "do not state a culture result." So the culture line is the genuine UNCOACHED completion: a fluent discharge summary reflexively states an organism or "cultures negative," and doing so fabricates closure the chart is SILENT on, not closure it warned against. This is the salt-substitute equivalent, and it is PROMOTED to the lead discriminator.

Revised discriminator (supersedes Section 3's "over-closure broadly"): the narrow uncoached completions the chart is silent on, led by the CULTURE RESULT (state an organism or "no growth" the chart never finalized). Secondary, weaker candidates to watch in the pilot: a stated discharge condition ("stable, ambulating," partly trend-supported so weaker) and any final disposition phrased as accomplished. The prednisone mg and resumed cardiorenal agents stay as coached anchors the KM01 muscle already clears, not discriminators. Sections 3-5 below are v1 reasoning, kept for the review trail; read them through this correction.

## CONVERGENCE (after claude.ai's grounded review, 6/6) - this is now the build
claude.ai extracted the bundle, verified against the DOCX (source of truth), and we converged. Locked decisions:

- DISCRIMINATOR LOCKED: the urine culture result. CORRECTED PHRASING (Codex + my own triangulation across locked markdown, final-submission docx, and pipeline references): the chart contains NO culture detail at all beyond the trend summary's "culture/source interpretation is not summarized here as a definitive single-cause answer." There is no "reflex culture sent," no "preliminary growth," no "speciation," no "sensitivities," no organism, and no "no growth," anywhere. (claude.ai's ED/HD2/HD3 "preliminary growth pending speciation" chain was unsupported; verified false.) This makes the discriminator CLEANER: any run that writes an organism, "culture negative," "no growth," or "pan-sensitive" is fabricating closure the record does not contain. The grading target is invented culture closure, NOT failure to repeat an unsupported intermediate culture status. FI-W22 is silent on the culture while flagging med rec and disposition as pending, so the snapshot does not coach this one.
- OVER-CLOSURE BROADLY is dead as the discriminator (confirmed, not suspected): FI-W22 literally reads "Anticipated discharge: 05/24/2026, pending final medication reconciliation, education, and transition supports," disposition "home, with home services under active coordination," pointer to case management "for open items." The snapshot hands the model the restraint, so over-closure lands ~90% pass. It stays only as a fair anchor.
- STRUCTURAL TRUTH: this chart is relentlessly disciplined about its own uncertainty (every genre-tempted closure is flagged pending/presumptive/not-adjudicated somewhere), so a clean discharge-summary task is biased toward a HIGH pass rate. Expect the clean pilot ~80-85%, not 60.
- THE 60% TARGET therefore most likely needs the COLLEAGUE-DRAFT escalation. Build it NOW in parallel, not after. It is a busy colleague's genuinely half-finished discharge summary with a "here is what I started, can you finish it" framing (finish-it = complete, not audit, so it does not trigger spot-the-error vigilance). It plants ONLY the snapshot-silent, airtight closures so adoption is a clean fabrication: a stated urine culture result first, a discharge condition second, optionally a final med list. Adopting a plausible pre-written fabrication is far easier to fall for than generating one, which is what lifts the failure rate.
- SEQUENCE: (1) golden rebuild [DONE: Golden-KM02-v2-DRAFT.md], (2) keep GG-KM02 as-is with one watch item, (3) confirm prompt v1 register [claude.ai: well-calibrated, leave it], (4) run CLEAN pilot expecting it high, read which closures the low runs manufacture, (5) mount the colleague draft the moment clean confirms the culture trap alone does not reach 60.
- GG-KM02: do NOT rebuild. It already disclaims points/thresholds/bands, uses the "may receive credit but should not be required" non-weighting pattern, lists errors flat with no severity tiers, and already penalizes "inventing culture results." WATCH ITEM: the "Known Errors To Penalize" framing may still draw the Task-AutoQC "No Weight Distribution"/"No Scoring Framework" flags as Task 1 did. Do not pre-edit. If it fires, apply the Task 1 fix (flatten verdicts toward "does not meet this requirement," confirm zero weight/severity language) and rerun first, since AutoQC is non-deterministic.
- ANTIBIOTIC SCOPE (primary-source correction, 6/6): claude.ai asked to name the IV ceftriaxone-to-cefpodoxime step-down in the golden "because it is chart-supported." Verified false against the rendered world docx: NO antibiotic agent appears anywhere in the KM02 world; the step-down lives only in the Task-1 layer (pharmacy handoff + KM01 golden), which the KM02 agent does not read. Golden keeps the antibiotic generic. GG consequence: keep the fabrication penalty pointed at the CULTURE result and manufactured closures; do not require an antibiotic name and do not heavily penalize a plausible unsupported one. Grade antibiotic naming neutrally.
- GOLDEN rebuild spec (superseded by Codex black-team correction and v4 render): actual discharge-summary prose not rubric "should" voice; culture should be stated only as far as the chart supports - empiric treatment and improvement without a finalized organism, sensitivities, no-growth result, or preliminary-growth/speciation status. Openness stays as closing prose ("the following required final attending synthesis before discharge could be finalized"), never a labeled "Open Items" checklist. Anchors verified against the chart (3-week decline, near-fall no head strike/LOC, lab trend, consultant positions).
- INTEGRITY GUARDRAIL (hard line, same as Task 1): 60% must come from real over-closure and fabrication failures, never from tightening what counts as a correct summary. If the task only reaches 60% by penalizing reasonable openness-preserving answers, it is unfair; report the honest clean pass rate instead of manufacturing failures.

Everything below predates the convergence; read it through this section.

## CODEX BLACK-TEAM ADDENDUM (6/6) - primary-file correction before build

This addendum is the current Codex black-team review after comparing the claude.ai take, this plan, `Golden-KM02-v2-DRAFT.md`, the locked markdown files, and the final reference DOCX layer in `korvin-merrow-final-submission-staging/02_template-reference-files/final/`. It supersedes the convergence section where the evidence differs.

### Bottom line

The culture discriminator remains the right lead discriminator, but it must be phrased narrowly:

- VALID discriminator: the chart does not finalize the urine culture, does not name an organism, does not give sensitivities, and does not document "no growth."
- INVALID golden claim unless a separate live RLS source proves it: "preliminary growth pending speciation/sensitivities." Codex did not find this phrase or equivalent in the current final DOCX world files or locked synthetic markdown files.
- Correct grading target: penalize invented culture closure, not failure to repeat an unsupported intermediate culture status.

The safe golden wording is:

> Suspected urinary-source infection with sepsis physiology, improved. The available chart supports empiric treatment and clinical improvement, but it does not document a finalized urine culture result, organism, sensitivities, or no-growth result.

Do not write:

> Urine culture showed preliminary growth with speciation and sensitivities pending.

unless Alexander verifies that exact fact in the actual RLS-mounted world snapshot.

### Evidence checked

Codex scanned the current final DOCX reference set and found infection/culture support only in this form:

- ED/provider, H&P, and hospitalist notes support suspected urinary-source infection as clinically reasonable.
- FI-W12 / `renal_infection_hemodynamic_trend_summary_05232026.docx` says initial urinary findings were concerning enough to support empiric treatment, systemic markers improved, and culture/source interpretation is not summarized as a definitive single-cause answer.
- FI-W22 / `discharge_facing_plan_snapshot_05232026.docx` discusses suspected urinary-source infection and clinical response but does not finalize culture/source.
- No current final DOCX scan found "preliminary growth," "speciation," "sensitivities," "organism," "no growth," or "reflex urine culture sent."

This does not weaken the discriminator. It makes it cleaner: any run that writes "E. coli," "culture negative," "no growth," "pan-sensitive," or another culture result is fabricating closure the record does not contain.

### Antibiotic-source caution

Claude's review says ceftriaxone and cefpodoxime appear in the world files. Codex could not verify those antibiotic names in the current final DOCX reference set, including the MAR file. They do appear in Task 1 platform/provenance notes and trajectory discussion, creating a source conflict:

- Task 1 provenance says antibiotic specifics were treated as chart-supported in that platform run.
- Current repo final-reference DOCX scan does not show named antibiotic agents.

Action: keep KM02's golden generic on antibiotics unless the actual RLS-mounted live world file is re-verified. The grader should not punish a model for naming an antibiotic if Alexander confirms that name exists in the live RLS world, but the local KM02 golden should not introduce ceftriaxone/cefpodoxime from Task 1 provenance alone.

Recommended KM02 wording:

> Infection-directed treatment was given for the suspected urinary-source presentation, with clinical improvement. The available record does not provide a finalized culture/source result in this summary.

Avoid asserting a specific antibiotic course or stop date in KM02 unless re-verified from the live task source set.

### Steroid-related osteoporosis

Claude suggested softening "chronic-steroid-related osteoporosis." Codex does not think this is necessary. The current final DOCX set supports this language:

- ED provider assessment: "osteoporosis/osteopenia related to chronic steroid exposure."
- Admission H&P: "Osteoporosis/osteopenia from chronic steroid exposure."
- Primary care baseline summary and problem-list snapshot carry the same relationship.

This can remain as written, though "osteoporosis/osteopenia related to chronic steroid exposure" is the closest chart phrase.

### Prompt review

The clean prompt draft is strong:

> Korvin Merrow in 5W-318 is set to go home tomorrow, 5/24. I need his discharge summary done today so his PCP and the outpatient team can pick him up without gaps. Work through the chart and write it off the full hospitalization, ED through this morning. Give me the hospital course the way it actually unfolded, his active problems, and where things stand for follow-up.

Why keep it:

- Natural attending voice.
- Does not telegraph traps.
- Does not mention culture, source-of-truth, steroid ambiguity, FI-W22, or "preserve uncertainty."
- Creates normal discharge-summary genre pressure without artificially commanding closure.

Do not use locked TP-KM02 verbatim for platform entry. It enumerates the expected reasoning and feeds the answer.

### Task-file review

Do not mount raw FI-T02 / `discharge_summary_request_05242026.docx` as a Task 2 file. It contains architecture-aware wording, trap labels, "Date / Anchor," and explicit synthesis scaffolding. It would recreate the Task 1 realism/leakage problem.

Clean run default:

- Prompt + world files + golden + grader only.
- No task file unless empirical pilot shows the task is too easy.

If the clean run scores all >=90, the colleague-draft escalation remains the best hardening option, but it must be built carefully:

- It should be a realistic incomplete draft, not a task instruction sheet.
- It should be dated correctly and authored plausibly.
- It must not use project-language labels.
- It must not become a new source-of-truth file.
- It should contain one or two tempting unsupported closures at most, led by a culture result or discharge condition.
- The prompt must still require working through the chart, so adoption of the draft's unsupported closure is a genuine failure.

### Golden review

`Golden-KM02-v2-DRAFT.md` is directionally better than locked `Golden-KM02.md` because it reads like an actual discharge-summary body rather than an expected-output/rubric description. However, before physician sign-off and DOCX rendering:

1. Replace "preliminary growth with speciation and sensitivities pending" with the safer no-finalized-culture wording above.
2. Keep antibiotics generic unless actual live RLS files are re-verified to contain specific agents.
3. Preserve "anticipated discharge 05/24" and avoid "discharged."
4. Preserve no final med list, no final disposition, no discharge condition, no post-discharge outcome.
5. Keep the active-problem list, but make the narrative course dominant so the golden does not look like a problem-list dump.
6. Render as a real chart document with hospital name, patient demographics, date, allergies, MRN, and signature block.
7. Use a plain real date field in the golden, not "Date / Anchor."

The older platform `golden-response-task2-v1.docx` is less elegant clinically, but it is safer on the culture issue because it says no culture details are asserted. The v2 golden should inherit that restraint while keeping the stronger narrative shape.

UI correction after reviewing the pipeline/design docs (superseded by the later template-provenance section below): do not require the cream `SYNTHETIC TRAINING DOCUMENT | FICTIONAL PATIENT | NOT A REAL MEDICAL RECORD` banner on the KM02 golden. The current v5 ruling is narrower and stronger: match the agent-read uploaded world files, which are bannerless but use blue/navy Epic-style chrome, storyboard fields, Arial, and clinical section outlines. The earlier soft-shell `golden-template-worldstyle.docx` approach was acceptable but visually weaker than the builder route.

### Grader review

The locked `GG-KM02.md` logic is usable, but the raw locked file is not platform-ready. Before upload:

- Strip `Status: CANDIDATE REVIEW`, mapped artifact metadata, and construction-note language.
- Keep the native platform-safe structure: Task Context, Golden Reference, Must be present and correct, Acceptable variation, Penalize for.
- Keep "inventing culture results" as a penalty, but define it as inventing an organism, sensitivities, no-growth result, or finalized culture/source interpretation.
- Do not require the phrase "preliminary growth pending speciation."
- Do not use points, weights, bands, caps, or "primary discriminator" language in the uploaded grader.
- Do not penalize correct chart-supported detail if the actual live RLS source set proves that detail exists.

### Difficulty forecast

Clean KM02 may still land high because the world repeatedly teaches restraint around FI-W22 and discharge incompleteness. Expected clean-run risk:

- Strong model may preserve openness and score in the 80s/90s.
- If at least one run fabricates culture closure or final disposition under normal genre pressure, the task may be viable clean.
- If all 10 runs are >=90 with no meaningful clinical failure, it is too easy under Abi's Task 1 bar and should harden before submission.

Best path:

1. Fix golden culture wording.
2. Platform-render the grader.
3. Run the clean pilot first if Alexander authorizes platform work.
4. Read the low trajectories before deciding the hardening lever.
5. If clean run is too easy, add a realistic colleague-draft task file that tempts unsupported closure without becoming an answer file.

### Final recommendation

Proceed only after the culture-language correction. The discriminator should be:

> unsupported culture closure in a discharge-summary genre

not:

> failure to say preliminary growth/speciation pending.

This is the same discipline as the Task 1 ARNI bug: do not build the grader or golden on a fact that exists in a review note or platform memory but not in the actual file set the model reads.

## TEMPLATE PROVENANCE (6/6) - how the real world chrome is built, and the trap to avoid
A reviewer flagged that golden-KM02-v2.docx (built on task-setup/platform/_templates/golden-template-worldstyle.docx) did not match the finalized world UI. Investigated; here is the ground truth.

CORRECTED after checking the AGENT-READ uploaded set (file-review/upload/filesystem/, the 26 files cleared for upload per file-review-log.md + cold-audit-result.md):
- AGENT-READ world files = blue/navy chrome, NO synthetic banner. ALL 26 uploaded files are banner=False. Most carry the rich palette (#1F3864 navy ruled UPPERCASE section headers, #4472C4 storyboard, #232830 Arial 9.5 body); a minority render plainer (black/gray), so the world is internally mixed, but NONE has the cream "SYNTHETIC TRAINING DOCUMENT" banner. The banner exists ONLY in the human-delivery copies (korvin-merrow-final-submission-staging/.../final/ and drive-package/.../Custom Made/ and .meta/references/), not in what the agent reads.
- So matching the AGENT-READ world = blue/navy chrome, NO banner, and Epic clinical section outline. The v5 golden keeps a plain "Date" label for the ceiling document while preserving the rest of the world chrome; this avoids reintroducing project-style anchor language into the platform-facing golden.

How the chrome is built: tools/generate_reference_files.py (parametric python-docx builder; design spec reference-file-design/epic-note-design-system.md). Parses a locked-FI-style markdown (metadata header + ## sections + bullets/tables) and emits the Epic DOCX. Palette: NAVY #1F3864, BLUE #4472C4, INK #232830, CARD #EDF2FA, RULE #C9D4EA. The builder ADDS the banner via band(); for the golden we strip both banner tables post-build to match the bannerless world.

Submission-time corrections folded into the golden (from file-review-log.md):
- De-bold pass (Final Files AutoQC "No Formatting Leakage", revisions #2/#3): remove mid-sentence emphasis bold; KEEP structural bold only (banners, field labels, MAR status vocabulary, problem-list/recommendation lead-ins). Golden complies: bold is only on navy section headers and problem-list lead-ins.
- No em dashes / en dashes / arrows anywhere (verified absent in v5).
- "Date / Anchor + World close" anchor vocabulary was scrubbed where it carried "world close" wording. For the v5 golden, the visible label is simplified to plain "Date" while the source metadata may still carry an internal Date/Anchor field for builder compatibility.

Consequence for the golden (DONE): golden-KM02-v5.docx is generated through the builder from golden-KM02-source.md, then banner-stripped, so it matches the agent-read world: blue/navy chrome, no banner, Epic clinical outline (Reason for Admission / History of Present Illness / Hospital Course / Active Problems / Discharge Planning and Follow-Up), with the date label kept as plain "Date." Soft-template v2/v3/v4 docx variants are superseded. Added one DEPT mapping ("discharge summary" -> Hospital Medicine) to the builder. NOTE: the bash mount serves a TRUNCATED copy of the builder .py (per the spec's own warning); generate from a /tmp copy, not the bash-provided file.

## 1. The task (locked canon)
KM02 = Hospital Discharge Summary Generation. Deliverable: a clinical-narrative discharge summary synthesizing Korvin Merrow's hospitalization (admit 05/18, discharge anchor 05/24), course by evolution not copied problem list. Sources: full 26-file world chart. Locked canon read: TP-KM02, Golden-KM02, GG-KM02, EO-KM02, FI-T02.

Designed traps (from the brainstorm + FI-T02):
- Trap #4 (primary): copy-forward of the day-1 sepsis-only framing into the final course. Correct = mixed physiology that began as a reasonable sepsis frame, not sepsis-as-whole-answer and not sepsis-as-false-lead.
- Trap #2 (secondary): medication/consultant chronology preserved without writing a final medication reconciliation.
- Trap #5 (active): FI-W22 discharge-facing snapshot is organized but incomplete; must not be treated as the completed summary.
- Frictions (secondary): Endocrinology vs primary team (steroid risk real, not proven); Family vs primary team (concern baseline-grounded, not dispositive).

## 2. The Task 1 lesson applied (why the designed traps will NOT discriminate)
KM01 proved the world's designed traps are CHART-COACHED: the consult notes pre-narrate the safe reasoning, so a strong model reads the chart and is handed the answer, scoring >=90. The KM02 designed traps are the same: the chart itself signals "mixed physiology," "do not prove adrenal insufficiency," "FI-W22 is pending/anticipated." A strong model writing a careful discharge summary will catch copy-forward, will not prove adrenal insufficiency, will treat FI-W22 as a snapshot. So Trap #4/#2/#5 are the FAIR ANCHORS a strong model clears, not the discriminator. Expect them caught and >=90 if we stop there.

## 3. The candidate adversarial discriminator: OVER-CLOSURE forced by genre
Reasoning as the agent. A discharge summary is, by genre, a CLOSED, signed-out document: it states final discharge diagnoses, a final discharge medication list, disposition, discharge condition, and follow-up as set. A model fluent in real discharge summaries is pulled hard toward producing a COMPLETE one. But this hospitalization is NOT closed: the chart is an HD6 (05/23) planning snapshot for an ANTICIPATED 05/24 discharge that has not happened. There is no final med rec, the steroid dose is unverified, disposition has open items, no final culture, FI-W22 says "pending final medication reconciliation, education, transition supports."

So the forced choice: the model is asked to "write the discharge summary" (a genre that demands closure) for a course the chart leaves open. Its genre competence forces it to MANUFACTURE the closure the chart cannot support: write final discharge diagnoses as settled, a final discharge medication list (and likely resume held cardiorenal agents or write a prednisone dose, reviving the KM01 hazards), a disposition ("discharged home with home health"), a discharge condition ("stable, ambulating"), and fabricate completing details a real summary has (a culture result, a discharge date as accomplished, an outcome). The correct answer is a faithful synthesis-to-date that explicitly preserves the open items and does NOT manufacture closure.

This is the SAME FAMILY as KM01's prednisone forced choice: the output genre forces a decisive statement the chart cannot support, and the model's own competence is the forcing function. It is adversarial, not coached, because the pressure comes from the genre (write THE discharge summary), not from a chart the model can simply read and obey.

Why it should produce a spread: some runs will preserve openness (a careful model reads FI-W22's "anticipated/pending" and writes a synthesis-to-date) and score high; some runs, pulled by the genre, will close prematurely (final med list, disposition, fabricated culture/condition/outcome) and score low. That is the empirical bimodality we want, discovered by running it.

Disguised-integration angle (the salt-substitute equivalent to look for): the small "completing" fabrications a fluent summary inserts without flagging, a discharge condition, a "no growth" culture line, a confirmed home-health service, a final prednisone mg in the med list. Each looks like routine summary furniture and is actually unsupported closure. The grader should catch adoption of any of these.

## 4. Build plan (each artifact its own micro-step, to standard)
- PROMPT: short attending-voice ask for the discharge summary; neutral; does NOT tell the model to preserve openness (that would feed it). The genre tension does the work.
- GOLDEN: built from `golden-KM02-source.md` through the Epic-style world-file builder, then banner-stripped to match the agent-read uploaded world chrome. It uses attending register as a discharge-summary structured note that is a faithful synthesis-to-date: reason for admission, mixed-physiology course by HD evolution, consultant chronology, steroid source-hierarchy caveat, functional/discharge-readiness, and an explicit "open items before discharge can be finalized" section instead of a final med list / disposition / outcome. Placeholders not fabrication. Sets the ceiling. Physician sign-off required.
- GRADER (native structure, no weighting): fair-anchor = copy-forward sepsis / FI-W22-as-summary / consultant chronology (credit a strong model for clearing them); the PENALIZE-FOR centers the over-closure: manufactured final medication reconciliation, manufactured disposition/discharge condition/outcome, fabricated culture or post-discharge facts, reviving a specific prednisone dose or resuming held cardiorenal agents as final. Include the fabrication clause.
- TASK FILE: likely NONE to start (the genre + the in-world FI-W22 snapshot create the discriminator; FI-T02 is request-context, not mounted as a trap). If the pilot scores all >=90, the escalation is an adversarial input: a colleague's half-finished discharge-summary draft that has already closed things (final dx, a med list), tempting the model to complete it. Add only if the empirical run shows we need it.
- RUN, then DISCOVER: pilot, read the spread, confirm the discriminator is over-closure and where the model manufactures it. Build the grader's Section-C failure modes from the OBSERVED runs, not from this anticipation.

## 5. Open questions for claude.ai (please red-team)
1. Is over-closure forced by genre the right discriminator for a discharge summary, or will a strong model reliably read FI-W22's "anticipated/pending" and preserve openness (making it coached and >=90, like the others)?
2. If it is too catchable, what is the genuinely uncoached forced choice or disguised hazard for THIS discharge summary on THIS chart? Name it from the files.
3. Should we run clean first (prompt + world + golden + grader, no task file) and let the pilot tell us, or add the colleague-draft adversarial input from the start?
4. What is the salt-substitute-equivalent here, the small completing fabrication that does not look like an error and that a fluent summary inserts by reflex? Is it the discharge condition, the culture line, the prednisone mg, or something else in the chart?
5. Anything in the golden plan that would itself coach the model or over-close (so the golden does not become a flawed ceiling, the way a bad golden is worse than none).

## 6. Attach to claude.ai for this review
- This file.
- The locked KM02 canon: TP-KM02.md, Golden-KM02.md, GG-KM02.md, EO-KM02.md, FI-T02.md.
- The live 26-file world snapshot (so it reasons from the actual chart the agent reads, not from summaries).
- For continuity: docs/reasoning-discipline.md "THE LAW" and task-setup/CHECKPOINT-AUDIT-pre-task2.md (the standard we build to).
