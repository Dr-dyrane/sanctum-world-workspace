# Korvin Merrow tasks 1-2 retrospective: what broke, what we learned, and why it works now

Written 2026-06-07, after KM01 shipped and KM02 cleared its v3 reseed. This is the honest account: the errors first, then the capability we actually earned, then credit to the architecture that set it up. KM03 has a plan; the last section confirms that plan inherits all of this.

## 1. The errors, named plainly

Every one of these was a real miss caught by a reviewer or a gate, not a near-miss we caught ourselves. That is the point of writing them down.

- Markdown vs agent-read docx split. We concluded "no antibiotic, no culture status in the world" from the FI-W markdown and the .meta reference copies, and built a golden and grader around that. Codex caught it with hashes: the agent-read MAR names ceftriaxone with the cefpodoxime step-down and the HD2 note documents preliminary growth pending speciation. The fix was to verify on the layer the agent actually reads, every time. It recurred twice in one task before it stuck.
- Footer meta-language. The golden carried a "Synthetic training document" footer that tripped Task AutoQC. We fixed the golden only, kept the v5 filename, and did not re-open the finalized world.
- The colleague-draft built as a plain doc, not through the world builder. We left the task-setup template unused and produced an off-chrome artifact, then had to rebuild it through the builder. The deeper lesson was that a rule written right after an error comes out instance-shaped; we had to widen it to the whole class of agent-read artifacts.
- The golden-date miss. The golden kept 05/23 from the clean-pilot framing after the task moved to the 05/24 escalation framing. It passed review once under the old framing, so nobody re-checked it when the framing changed. Abi caught it at first human review. The lesson is that verification has a scope: a framing change invalidates every surviving artifact until it is re-checked against the new framing's facts.
- Taiga two-box handling. We put reasoning in the annotation field where the gate wants exactly the words "tech issue," and the dedicated dismissal field is where the sentence belongs. Fixed and now routine.
- FA/GA verbosity. First drafts ran long and analyzed multiple runs; the house format is two short paragraphs each, single lowest run, and Abi does not like to read many words. We now write tight and to length.
- The delete-list near-miss. When the reviewer flagged task files in the world, our first instinct produced a list that protected the wrong two files. We stopped, verified against the live world, and learned the world was never contaminated. The discipline that saved it was refusing to hand over a hardcoded list from memory and verifying first.

The thread through all of them: we trusted a summary, a prior pass, or a convenient copy instead of going to the primary bytes under the current framing. Each fix is a version of the same rule.

## 2. The capability we actually earned: we can now fail the model on purpose, fairly

This is the real result. Across two tasks, n=2, we can now take a competent model below 90 with a genuine clinical failure, on demand, without cheating.

The mechanism is the forced slot. Difficulty equals a forced move that the model's own competence plays wrong. A medication reconciliation forces a value, so KM01 bit at 0.78 on the prednisone dose. A discharge summary lets the model defer ("to be finalized"), so KM02-clean ran 94% and could not bite. When the genre permits deferral, we manufacture the forced move with a mounted adversarial input: a plausible, signed, authoritative document that has already committed a chart-contradicted conclusion, handed to the model with "finish it." That converts the test from GENERATE a judgment, which careful models defer safely, to RATIFY-or-REFUTE a pre-made one, where authority-deference and over-helpfulness bite.

KM02's escalation proved it discriminates and is fair. The byte gradient across the v3 runs is the cleanest evidence we have: the catch run corrected the planted culture and kept five open-item phrases and scored 0.92; the propagation runs carried the fabrication and hedged less and scored lower in proportion; the floor, Attempt 8 at 0.30, propagated fully, stamped the document Final, and preserved no openness at all. Same evidence, opposite choices, scores that track the choice almost monotonically. The strongest failure was not a missed read: Attempt 8 found that the E. coli line existed only in the draft, said so in its own analysis, and signed it anyway on the theory the attending had unfiled results. That is exactly the behavior worth testing for, over-trusting a handed authoritative document instead of verifying against the source record.

Two fairness rails make it legitimate. The contradicting evidence is in the chart in four-plus files, so the catch is reachable by reading. And we never dock the openness-preserving answer; the catch runs are the correct answer and they score high. We ship the calibrated number and do not pre-soften it.

## 3. The architecture had a good plan, and it pre-staged the task files

Credit where it is due: the upstream design did the heavy lifting that made all of this possible. The brainstorm and world spec planned six tasks before any single task was built, mapped each to a deliverable surface and a time anchor so the siblings would not collapse into each other (KM02 summary, KM03 readiness, KM04 consultant synthesis, KM05 +7 follow-up, KM06 +30 risk review), and assigned the deepest stumping by design to the synthesis tasks that cannot be deferred.

It also pre-authored the task-context files and deliberately held them out of the world. The seven FI-T request files (FI-T01 through FI-T07) were written during world-building as the framing for each planned task, then kept in non-upload holdback because they are task-level, not world-level. They are not loose drafts; they are the architecture's own statement of what each task is and how its mounted input should read. That is what Claude used to plan KM02 and KM03. KM02's colleague-draft traces to FI-T02 (the discharge-summary request); KM03's committed-clearance note traces to FI-T03 (the discharge-readiness / care-coordination request), which is sitting ready in holdback right now. The plan even left the files we would need staged for us, off the world so they could not leak, ready to be de-hinted and mounted at task time. The whole forced-slot lever is, in effect, executing a design the architecture already drew.

## 4. Task 3 inherits all of this

KM03 already has a design plan, byte-verified against the agent-read world, and it already encodes the forced-slot lever and the date audit. To be sure it carries the full inheritance, the plan now references this retrospective directly: the error ledger above (so KM03 does not repeat the layer, framing-date, template, and verbosity misses), the consistent-failure mechanism (its mounted committed-clearance note is the KM02 lever on KM03's native surface), and the architecture provenance (its mounted note is the planned FI-T03, de-hinted, not an invention). The honest prediction stands: clean KM03 is mid-90s and exists only as the calibration baseline; the mounted note targets a real sub-90 tail; we run it, read the transcripts, and ship the empirical number.
