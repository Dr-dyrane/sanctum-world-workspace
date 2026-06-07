# KM02 (Hospital Discharge Summary) - design plan for 3rd-party review

Status: PRE-BUILD design. No prompt, golden, or grader written yet. This is the discriminator design, sent to claude.ai to red-team BEFORE we build, so we build slowly and right. Governed by docs/reasoning-discipline.md "THE LAW" (build real; build the task with the world's rigor; reason from the full context to outsmart the model, not feed it; difficulty is empirical and adversarial, not architectural).

Note: old drafts in platform/task2/ predate the law and are SUPERSEDED. We build from this read, not from them.

## VERIFIED AGAINST FILES (6/6, after claude.ai red-team)
claude.ai red-teamed v1 of this plan and flagged two factual claims as load-bearing. Both checked against the live world; the reviewer is right on both, and the discriminator is revised accordingly. claude.ai should still verify independently from the attached files.

1. FI-W22 self-flags as incomplete (CONFIRMED, stronger than v1 said). FI-W22 contains a literal "## Items To Complete Before Final Discharge Order" section, the line "No final discharge order has been entered in this snapshot," an "Anticipated Disposition Frame," and a Guardrails block stating it "is not a completed discharge summary, final disposition decision, final medication reconciliation, final prednisone taper plan." So OVER-CLOSURE BROADLY IS CHART-COACHED: a careful model reads "anticipated / items to complete" and writes an open synthesis, the same way KM01's coached traps cleared >=90. Over-closure is therefore DEMOTED from the discriminator to a fair anchor. The reviewer's core objection stands: the FI-W22 language I leaned on to justify the trap is the same language that defuses it.

2. The chart never finalizes a culture (CONFIRMED). grep across all 22 world files: no organism, no speciation, no "no growth," no sensitivities anywhere. Infection is "suspected urinary-source" from ED through HD6. FI-W12 only quietly notes culture "is not summarized here as a definitive single-cause answer," buried in a trend-source file, and nothing anywhere says "do not state a culture result." So the culture line is the genuine UNCOACHED completion: a fluent discharge summary reflexively states an organism or "cultures negative," and doing so fabricates closure the chart is SILENT on, not closure it warned against. This is the salt-substitute equivalent, and it is PROMOTED to the lead discriminator.

Revised discriminator (supersedes Section 3's "over-closure broadly"): the narrow uncoached completions the chart is silent on, led by the CULTURE RESULT (state an organism or "no growth" the chart never finalized). Secondary, weaker candidates to watch in the pilot: a stated discharge condition ("stable, ambulating," partly trend-supported so weaker) and any final disposition phrased as accomplished. The prednisone mg and resumed cardiorenal agents stay as coached anchors the KM01 muscle already clears, not discriminators. Sections 3-5 below are v1 reasoning, kept for the review trail; read them through this correction.

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
- GOLDEN: built in the world-template (golden-template-worldstyle.docx) + attending register, as a discharge-summary structured note that is a faithful synthesis-to-date: reason for admission, mixed-physiology course by HD evolution, consultant chronology, steroid source-hierarchy caveat, functional/discharge-readiness, and an explicit "open items before discharge can be finalized" section instead of a final med list / disposition / outcome. Placeholders not fabrication. Sets the ceiling. Physician sign-off required.
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
