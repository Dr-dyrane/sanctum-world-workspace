# FA/GA CANONICAL (LOCKED) - the single standard for Failure and Grader Analysis

This is the locked standard. Read it before writing or revising any FA/GA. It supersedes any divergent wording in the failure-grader-analysis skill cache. If the skill and this doc disagree, this doc wins. Prompt, golden, and grader are already locked; this locks the FA/GA so we stop re-deriving it.

## Provenance (the authoritative chain)
- `reference/source/instruction-doc/[EXP] Project Sanctum Instruction Document (06_09).md`, Step 14: "Failure Analysis (FA) - what the agent got wrong + why" and "Grader Analysis (GA) - how well the grader scored the agent's work." FA = half a page, 3 paragraphs, 10-12 sentences, covering four components. GA = 4-6 sentences.
- `reference/source/worked-examples/FA_GA.md` and `reference/source/worked-examples/FA_GA-2.md`: the two official worked examples. Both GAs end with constructive feedback to the grader.
- `worlds/korvin-merrow/task-setup/task1/fa-ga/FA-GA-final.md`: the DELIVERED, Abi-approved FA/GA, GA rated Great. Uses "what the model did well / what it failed" and "what the grader got right / what the grader got wrong or could improve."
- `worlds/korvin-merrow/task-setup/task9/fa-ga/FA-GA-current.md`: prose-paragraph form, grader audit + one weakness + calibration close.
- King P, 2026-06-14 (DO-NOT-REPEAT #20): bind to the SECOND-lowest distinct run, not the strict lowest. This supersedes the EXP doc's "lowest-scoring run."
- Abi O and Larry E, 2026-06-18 Vagus pins: writer submits an own score with FA; FA/GA uses the 2nd-lowest score; if Taiga trajectories and QA are rerun, redo FA/GA from the latest run set; GA distinguishes grader misses from mis-scores; PL uses A1-B3. Larry also restated that platform-facing FA/GA cannot be AI-authored. Codex may organize evidence or draft a scratch aid only when Alexander asks. Alexander must read, own, and rewrite or explicitly approve the final text before paste.

## Run binding
Bind the FA to ONE run: the second-lowest distinct score in the current valid run set. Pull that run's full output AND its grading transcript before writing. If Taiga trajectories and QA are rerun, the prior FA/GA is stale. Redo FA/GA from the latest run set. Do not infer the failure from the output alone (KM task1 guessed four wrong failure modes; the transcript showed the real miss). The Status line is internal and is NOT pasted into Studio, so the submitted FA field must itself name the run: open the FA's first paragraph with "On trajectory N" (the 1-10 count, the same number as the attempt). Use that one identifier, not both attempt and trajectory, and not the run or trajectory hash; the hashes and the distribution stay in the Status line. The GA names the same run the same way ("The grader scored trajectory N at X").

SAVE the run verbatim FIRST, before drafting. When a pilot returns, copy the selected run exactly (the trajectory output and its grading transcript, as pasted from Studio) into `tasks/taskN/pilot/runs/` named by job and attempt, and cite that file in the Status line. The FA/GA is then provably derived from a saved primary source, not from chat memory. This is the only way the never-from-memory rule is enforceable: it makes the write-up auditable and revisable after the chat ends, and it satisfies the verify-the-primary-artifact guardrail. A run that lives only in the chat is gone at compaction, and the next pass would be from memory, which is where invented detail creeps in.

## Failure Analysis - the four components (EXP Step 14)
Cover all four, in prose, organized by severity (clinical first, then administrative, then style):
1. What the agent got RIGHT - a brief competent baseline, one or two sentences, named specifically, as the setup for the turn. Lead with it but keep it short. Ahmad (Trigeminus, more recent than 06_09) cut the standalone "what the agent got right" paragraph: the FA stays failure-only, no praise paragraph.
2. What the agent got WRONG - the central failure as a turn (it had the contradicting evidence and failed anyway), tied to the golden.
3. Why the failure MATTERS - clinical mechanism and consequence. Quantify when possible. State the severity tier. State plainly that the output would not be deliverable by any competent practicing clinician; if you cannot say that, the failure is insufficient (Phase 3).
4. The SCORE - state the analyzed run's score and the writer's own score, and tie the failure to them. Reference ONLY this run; the full distribution stays in the Status line, never the body (Abi single-run rule). Conclude the FA with the exact required line: `Overall Failure Score: X.XX / 1.0`. This is Alexander's own score, not the trajectory score.

Writing standards (EXP), all required:
- Be specific, not generic. Not "got the med list wrong" but "listed metformin as active despite Endocrinology holding it until creatinine returns to baseline, risking lactic acidosis."
- Name the SPECIFIC source documents a reviewer opens to verify, by author or date (e.g. "the wound-care consult (Olwyn, CWOCN, 05/20)"), not a generic reference. The QA rubric requires specific documents and sections, not generic references, and lint_fa_ga.py FAILS an FA that carries no dated citation.
- Separate clinical error from formatting preference. Do not conflate.
- Quantify the consequence when possible.
- Write for a non-specialist. Explain any jargon.
- Distinguish severity tiers (a patient-safety failure is not a documentation preference).

## Grader Analysis - the grader audit (THE part we keep missing)
The GA assesses HOW WELL THE GRADER SCORED THE WORK. It is not a second justification of the score. It has three moves, and the FIRST TWO ARE BOTH MANDATORY:
1. What the grader got RIGHT. Name what it credited correctly and the central defect plus any secondary miss it caught. Map to the grader's own categories (non-negotiables, the acceptable-variation boundary, the common failure modes) where natural. Affirming a sound grader IS analysis, not a filler.
2. What the grader got WRONG or COULD IMPROVE. This is REQUIRED and is the move the calibration-close form drops. Give at least one constructive point: a miscalibration, a phrasing overstatement, a distinct failure mode it should have named explicitly so it did not have to infer partial credit, or a place it was lenient or harsh. If the grader was genuinely sound, say so plainly and still add the stricter-or-looser-reading caveat (KM task1: "I would dock a full omission of a held medication harder, but the score is defensible"). When the gap is a real grader MISS (it never saw the failure), recommend a concrete rubric or failure-mode addition in Larry 3:10 form: name the missed issue, say why it matters, then "Recommend adding: ..." (his example: the grader did not flag the missing medication reconciliation plan; Recommend adding: "Identifies stale medication lists without documenting a correction plan"). For a MIS-SCORE (it saw the issue but scored it wrong), recommend how the scoring guidance should be clarified instead.
3. Calibration judgment. The score is well placed or defensible. The closer "a deep floor would overstate X, and a high score would ignore Y, so the band is well placed" is acceptable, but it does NOT replace move 2.

The grader RATING (Poor / Fair / Good / Great) is entered directly in the Studio field, never written anywhere in the FA/GA file. The gate rejects a rating line even in the Status line, so carry the rating to the writer separately, not in the paste.

## Writer's score (project guidance, 2026-06-18)
Verbatim project guidance: "New Failure Analysis guidance. Please submit a score with your failure analysis about how you think the model did in your task. This score should be your own score, not the trajectory score, and will be compared against the agentic grader."

Submit your OWN score of how the model did, alongside the FA. It is the writer's independent assessment of the model's task performance on the 0.0 to 1.0 scale, NOT the trajectory score (the agentic grader's number), and it is compared against the agentic grader to calibrate human-versus-grader agreement. Score the run on the task's own logic: the central failure caps it low, give partial credit for the accurate items, no credit for refusing to finish. Judge it independently; do not copy the trajectory number. It usually lands near the grader when the grader is calibrated; when it diverges, the GA's calibration move should explain why. Placement: the writer's score goes in the Studio score field AND inside the submitted FA field, because the Status line is internal and is not pasted into Studio. The FA must end with the exact required line: `Overall Failure Score: X.XX / 1.0`. Record it in the Status line too. This is the writer's own number; it is distinct from the banned grader-rating line (Poor / Fair / Good / Great), which never appears in the file, not even the Status line. Bind it to the same run the FA analyzes.

## Phase 3 alignment: scoring bands, grader rating, headings-as-prose (official, captured 2026-06-19)
Source of truth: reference/source/phase-3-evaluating/. Folded in 2026-06-19 (Stage 2). Structure decision B (Dyrane): keep the compressed two-paragraph prose form, which is clearing AutoQC and human review. Cover the official Phase 3 headings as prose beats, not literal headings.

Self-score bands (the writer's Overall Failure Score; score independently, ignore the grader's number):
- 91-100 perfect, deliverable as is.
- 71-90 good enough to send. A self-score in this band means the task is TOO EASY and cannot be submitted.
- 51-70 at least one significant error on a core question; needs real rework.
- 31-50 noticeable core errors (several, or one that flips the conclusion).
- 21-40 fundamentally defective; pervasive errors, not trustworthy.
- below 20 unusable; misunderstands the assignment or hallucinates authority.

Hard gate: any self-score above 70 means too easy, do not proceed. (The source 31-50 and 21-40 bands overlap; captured as written, flagged for clarification, does not change the above-70 gate.)

Grader rating (Studio field only, never in the file; scale Poor / Fair / Good / Great), set by the gap between the writer's score and the grader's score:
- Great within 5 points, Good within 10, Fair within 15, Poor more than 15 off.
- If the grader's score is above 70, the rating cannot be Great.
- The gap sets the CEILING. Downgrade for weak reasoning, never upgrade.

The three GA rules (Phase 3):
1. The GA must agree with the FA. The FA already scored the run at or below 70. Refute any grader claim that the output is "overwhelmingly correct" or otherwise flawless. A critical failure and near-perfection cannot coexist.
2. If the grader scored above 70, the rating cannot be Great.
3. Reasoning outweighs the gap. Start at the gap-implied ceiling, downgrade for weak reasoning, never upgrade.

Headings as prose beats (decision B). The FA covers What the Agent Got Wrong (central failure anchored to the golden), Why the Failure Matters (would not be deliverable by a competent clinician), and the Output Score line. The GA covers Suggested Score (restate the writer's score in one line and name the gap to the grader's score) and Score Comparison (the grader audit, what it got right and wrong, citing the grading summary directly). Do not reference the self-score bands in the prose.

## Guardrails (gate-enforced; presubmit_task_gate.py + verify_voice.py)
- Failure-only prose. Do not write "the grader credited"; write "it gave appropriate credit for" or "it credited correctly." The both-sides gate also bans the literal phrases "what the grader got right" and "what the model did well" anywhere in the file, including the Status line; phrase it "the grader correctly identified" or "it caught."
- No grader-section names (do not write Section A/B/C; state the content).
- No grader-rating line anywhere in the file, including the Status line. The rating lives only in the Studio field.
- Single-run rule (Abi 6/05). The FA and GA analyze ONE run, named by its trajectory number, and cite only that run's score and the writer's own score. Do not mention other runs' scores or the distribution in either field; the distribution lives in the Status line. If trajectories and QA are rerun, throw out the old FA/GA and rebind to the latest valid run set.
- No em dashes or en dashes anywhere. Plain hyphens and commas.
- Plain clinical language, not compressed nomenclature. Write the way an attending speaks, not in stacked hyphenated tokens that read like a variable name or a rubric label (see docs/alexander-voice-dna.md). Also avoid essayistic framing ("the sharper point is", "the real issue is") and narrated grader effort ("labored over", "deliberated over"); state the point directly with "but the note still..." and say "the grader was unsure whether X counted."
- No evaluation scaffolding (OCR, directory listings, "the transcript shows," tool calls). Name the clinical mechanism.
- Alexander voice: varied, declarative sentences, no AI transitions (Furthermore, Moreover, Consequently, Notably, In addition).
- Vary the rhythm so it reads like a clinician reading the chart, not a machine ticking boxes. Mix a short line for emphasis with a longer one that carries two or three joined ideas, and let commas do the breathing. Do not open sentence after sentence with the same subject (the "It... It... It..." beat is the tell). Join related clauses with a comma or a conjunction where it flows, and keep the full stop for emphasis. Keep most sentences in the teens to mid-twenties, break one that genuinely runs past about thirty, but never chop the prose into uniform short beats. Still no semicolons, use a comma or a full stop, and still no dashes. Not the staccato "It saw the note. It declined. It left the block blank." but "It even surfaced the attending's note, yet having seen that, it declined to enter the determination, leaving the block blank."

## Length
The platform allows up to half a page / 10-12 sentences for the FA and 4-6 sentences for the GA. The local gate caps each field at about 1000 characters and two paragraphs. Treat the local cap as the working bound: a compressed but complete version that still carries all four FA components and both mandatory GA moves. Completeness of components beats hitting a character count.

## The locked checklist (run before handing back)
FA: opens with "On trajectory N" (the 1-10 count); leads with what the model did right; names the central failure as a turn; states the clinical mechanism and consequence with a severity tier; states plainly it would not be deliverable by a competent clinician; names the specific source documents by author or date (not a generic reference); ends with `Overall Failure Score: X.XX / 1.0`; references only this run, never other runs' scores.
GA: restates the writer's suggested score and the gap to the grader's score; names what the grader identified correctly; names what the grader missed or mis-scored (NOT optional); cites the grading summary; recommends the relevant rubric or scoring clarification when needed; judges calibration; does not reference the self-score bands; rating only in Studio, never in the file.
Rating (Studio only): set by the score gap (Great within 5, Good within 10, Fair within 15, Poor over 15); never Great if the grader scored above 70; downgrade only for weak reasoning, never upgrade.
Both: failure-only, no section names, no rating line in prose, no dashes, plain clinical speech, second-lowest distinct run from the latest valid run set, gates clean.
Self-check: run `python3 tools/verify/lint_fa_ga.py <file>` and clear every FAIL (it enforces the "On trajectory N" opener, single-run-only, the score-line, a dated source-document citation, and the structure rules; it warns on semicolons and long sentences).
