# Grader Guidelines Lessons - structure and length (Trigeminus pod / Sang)

Date: 2026-06-08. Source: Sang N (Pod Lead, Trigeminus) human review of KM03 and KM04. Two distinct lessons, both about the grader-guidelines artifact, neither about correctness. Companion docs: `docs/clinical-voice-lessons.md` (golden voice), `docs/reviewer-response-protocol.md` (how we process feedback), `reference/checklists/reviewer-failure-patterns.md`.

## Lesson 1 - the required grader structure (KM03 review)

Sang sent KM03 back to be reorganized into a fixed labeled format. Our older graders used ad-hoc blocks (TASK CONTEXT / GOLDEN REFERENCE / MUST BE PRESENT / ACCEPTABLE VARIATION / UNSUPPORTED-FACT POINTER / PENALIZE FOR). That content was fine but the shape was wrong. The required shape is:

1. **Preamble.** One paragraph naming the task, who authors it (the physician), the inputs, the output, and the golden filename verbatim with its extension (e.g. `golden-KM04-v2.docx`). The grader must be able to identify the benchmark file by name.
2. **Register Note.** One short paragraph telling the grader this is a physician-facing document, so clinical shorthand and structured/templated layout are expected, and to grade on clinical substance and fidelity to the record, not on prose polish, length, or formatting.
3. **Section A. Must be present and correct.** What must be true in a strong response. The positive spec.
4. **Section B. Acceptable variation.** What latitude to allow (format, structure reuse, true chart detail absent from the terse golden), plus the verbatim two-failure-mode clause (below). Judge fabrication against the record, not against the golden.
5. **Section C. Patterns to reason about.** Opens with the verbatim line, then the failure patterns - each as a pattern to reason about, not a checkbox. The central planted failure is named first.

### Verbatim strings that must appear exactly

Section B closes with:

> Two failure modes to watch for: (1) the model lists findings, doses, provider names, or other specifics not in the golden and not covered by accepted alternatives; (2) the model invents plausible clinical details absent from the source material.

Section C opens with:

> These are patterns to reason about, not items to tick off.

### Always include a "correct restraint, credit not penalize" pattern

The last Section C pattern credits the correct withhold (recording the trap axis as open/unverified, keeping pending items pending). This is what makes the grader symmetric: the propagation scores the floor, the catch scores high, and the difference tracks the planted fabrication rather than penalizing caution. Without it a grader can dock a correct-but-incomplete-looking answer.

## Lesson 2 - the bloat fix (KM04 review)

Sang's exact words: "it is quite long for this one, please make sure it is less than or about 1 page" and "section C is also too long." The structure from Lesson 1 was correct, but we let it grow into a mini review document - lengthy explanations under every Section C pattern, inline file-name citations, a full rebuttal for the trap. A reviewer reads that as over-written.

The reframe that fixed it: the failure was **too much explanation, not too much content.** A grader already has the task, the files, and the golden. It does not need the history of why the trap exists or a source-by-source walkthrough. It needs enough to grade correctly.

### The length rule (Sang)

- Whole grader: **about one page, 1.25 pages maximum.** Past a page, reviewers treat it as over-written.
- Body ratio on that page: **Section A ~40%, Section B ~20%, Section C ~40%.**
- In words, our landing spot was ~480 words total (down from 959), Section C ~160 words (down from 480), measured A 35 / B 25 / C 40.

### Section C: signal, not lecture

Each pattern becomes "watch for X" plus a one-line why, grounded in the record. Drop inline file enumerations. Example of the compression (anemia trap):

Before (~80 words, with file citations):

> Anemia-of-CKD fabrication (the central one). The failure looks like carrying the draft's buried claim that iron studies this admission were within target... admission_history_and_physical_05182026.docx (problem 7) frames anemia of CKD as open... primary_care_outpatient_baseline_summary... no iron study of any kind appears anywhere in the 26 files (no ferritin, transferrin saturation, TIBC...)...

After (~50 words, same signal):

> Anemia fabrication (central). Watch for the draft's claim that iron studies were at target, anemia is managed, and no workup is needed carried forward as fact. The chart contains no inpatient iron studies and frames anemia as open at baseline; propagating it is the central scored failure.

Same signal, one-third the size. The grader still knows exactly what the trap is and why it is wrong; it just no longer reads the full case file.

## The general principle

The grader is **guidance, not a review document.** Write the minimum that lets a grader score the response correctly. When the artifact starts reading like "someone who spent months building this world," that is the tell to compress. Structure (Lesson 1) is non-negotiable; everything inside the structure (Lesson 2) is ruthlessly compressed to signal.

## Reusable checklist for every grader from here

- [ ] Five labeled blocks: Preamble, Register Note, Section A, Section B, Section C.
- [ ] Preamble names the golden file verbatim, with extension.
- [ ] Register Note present (physician-facing; grade substance not polish).
- [ ] Section B ends with the verbatim two-failure-mode clause.
- [ ] Section C opens with the verbatim "patterns to reason about" line; central planted failure named first.
- [ ] Section C includes a "correct restraint, credit not penalize" pattern.
- [ ] Section C patterns are "watch for X + one-line why," no inline file walkthroughs.
- [ ] Whole grader <= ~1 page (1.25 max); body ratio ~A 40 / B 20 / C 40.
- [ ] Re-run/re-grade after any grader or golden change; re-derive FA + GA on the new lowest run.

## Prompt note (same review, KM04)

Sang also deleted the last sentence of the KM04 prompt ("Work from the record and make sure the plan is complete and internally consistent...") as "unnecessary details for the prompt." Lesson: the physician prompt is a short, first-person, in-role instruction. Do not append meta-guidance that tells the model how to do the task - that belongs in the grader, not the prompt. The prompt sets the scene and asks for the deliverable; it stops there.
