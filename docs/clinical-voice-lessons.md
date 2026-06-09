# Clinical Voice Lessons - what the pipeline's rewrite taught us

Date: 2026-06-04. Source: paired corpus from Korvin Merrow run #1 - writer templates (`.meta/references/`) vs pipeline-generated clinical files (`filesystem/`), same facts, different register. Mined so World #2 templates sound clinical at authoring time. Companion: `worlds/korvin-merrow/reference-file-design/epic-note-design-system.md` (visuals), `reference/checklists/spec-autoqc-preflight.md` (compliance).

## The ten patterns (template habit -> clinical habit)

1. **Open in the patient's voice.** Template: jumps to "REASON FOR ADMISSION" abstraction. Generated: `CHIEF COMPLAINT: "I just feel worn out and a little wobbly." Family adds: ...` A quoted chief complaint instantly humanizes the chart and is standard H&P furniture.

2. **The one-sentence identity stack.** Generated HPI opens with the classic attending construction: "Korvin Merrow is a 62-year-old man with HFrEF, CAD s/p remote PCI, CKD stage 3, T2DM, PMR on chronic prednisone of unclear current dose, OSA... admitted from the Emergency Department after his wife brought him in for...". One sentence carries demographics + problem burden + arrival story. Templates listed these in separate labeled fields.

3. **Micro-narrative beats abstract description.** Template: "Today he nearly fell at home while standing/walking." Generated: "Yesterday, 05/17/2026, while standing from a kitchen chair he became lightheaded and nearly fell; his wife was at his side and prevented impact." Concrete object (kitchen chair), named person, inline date, mechanism. Specific scenes read human; category summaries read synthetic.

4. **Inventory the negatives.** Generated adds full pertinent-negative strings: "He denies chest pain, dyspnea at rest, orthopnea worse than baseline, productive cough, fevers that he himself noticed... no head strike, no loss of consciousness, no witnessed seizure activity, no post-event focal complaint." Templates carried almost no negatives. Real clinicians document what is absent; their absence is an AI tell.

5. **Grade your sources.** Generated weaves epistemics into prose: "Per the patient and corroborated more reliably by his wife," "he is conversational but slow, defers details to his wife, and is not a fully reliable historian on medication timing." Reliability judgments about informants are physician instinct and free trap-substrate (they justify ambiguity without meta-language).

6. **Quote the family verbatim, sparingly.** "mild evening confusion that the wife describes as 'not his normal'"; Mara's "Better than Monday is not the same as ready to manage the next steps without support." One or two short quotes per file - anchors, not transcripts.

7. **Staff the chart realistically.** Generated: "Elian Vossmere, MD - Hospitalist Attending | Co-author: Ines Travyn, MD (PGY-2)", NPIs, FIN + MRN, room 5W-318, named day/night RNs on the flowsheet, signed time-stamped consultant ADDENDA (HD5, HD6) rather than edited base notes. Teaching-service co-authorship, addendum culture, and identifier plumbing are cheap realism multipliers.

8. **Time-anchor everything, approximately.** "began roughly three weeks ago in late April," "gradual rather than abrupt," "over the past one to two weeks the trajectory has been more concerning." Real history-taking produces fuzzy-but-bounded time, not clean ranges; precision lives in labs/vitals, approximation lives in story.

9. **Don't repeat the header in the body.** Templates re-listed Date/Service/Attending/Patient/MRN as body fields after the masthead already carried them. Generated keeps metadata in chrome once and spends body space on clinical content.

10. **Enumerate errors concretely.** Template: "medication-management mistakes." Generated: "(a missed evening dose on one day, an apparent double-up on another, and inconsistency around when prednisone had last been taken)." When the spec needs an ambiguity, generate the *specific instances* that produce it - the instances are facts, the conclusion stays open.

11. **Each document type keeps its native grammar.** Progress notes are true SOAP (SUBJECTIVE -> objective data block -> assessment -> numbered problem-oriented plan); the H&P runs the full admission arc (chief complaint -> HPI -> baseline functional/cognitive status -> PMH -> medications -> exam -> admission data -> assessment -> plan by problem); consults run the consult skeleton (reason for consultation -> history/source review -> exam -> interpretation -> recommendations -> friction with primary team -> dated addenda). The numbered problem list in the plan ("5. Polymyalgia rheumatica with prednisone provenance pending.") is the signature of physician authorship - prose plans without problem numbering read like summaries, not notes. World #2 templates should declare the document grammar per file type in the file inventory so generation locks onto it.

## Caution - where clinical polish hurts

The same rewrite engine that produced the above also (a) let nephrology enumerate its restart-gating parameters and name the first restart agent with dose strategy, and (b) made HD3 declare PT/OT findings "central rather than supplementary." Polished clinical voice loves synthesis and explicit weighting - which is exactly what kills consultant-friction and buried-evidence traps. Rule: adopt the voice patterns above for TEXTURE (history, exams, negatives, attribution); never let a physician summary perform the TASK'S synthesis (weighting sources, sequencing restarts, declaring readiness). Trap carriers get the plainest prose in the world.

## Application for World #2

- Bake patterns 1-10 into the reference-file templates at authoring time (file-inventory drafting stage), so generation has less to "fix" and less occasion to over-help.
- Add to template self-review: chief-complaint quote present; identity-stack sentence present; >= 3 pertinent-negative strings per H&P/consult; informant reliability graded; metadata not duplicated; trap-carrier sections checked for accidental synthesis.
- Keep the paired corpus (references/ vs filesystem/) archived as the style reference - it is the best clinical-voice training material we own.
