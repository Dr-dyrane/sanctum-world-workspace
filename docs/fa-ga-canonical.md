# FA/GA CANONICAL (LOCKED) - the single standard for Failure and Grader Analysis

This is the locked standard. Read it before writing or revising any FA/GA. It supersedes any divergent wording in the failure-grader-analysis skill cache. If the skill and this doc disagree, this doc wins. Prompt, golden, and grader are already locked; this locks the FA/GA so we stop re-deriving it.

## Provenance (the authoritative chain)
- `reference/source/[EXP] Project Sanctum Instruction Document (06_09).md`, Step 14: "Failure Analysis (FA) - what the agent got wrong + why" and "Grader Analysis (GA) - how well the grader scored the agent's work." FA = half a page, 3 paragraphs, 10-12 sentences, covering four components. GA = 4-6 sentences.
- `reference/source/FA_GA.md` and `reference/source/FA_GA-2.md`: the two official worked examples. Both GAs end with constructive feedback to the grader.
- `worlds/korvin-merrow/task-setup/task1/fa-ga/FA-GA-final.md`: the DELIVERED, Abi-approved FA/GA, GA rated Great. Uses "what the model did well / what it failed" and "what the grader got right / what the grader got wrong or could improve."
- `worlds/korvin-merrow/task-setup/task9/fa-ga/FA-GA-current.md`: prose-paragraph form, grader audit + one weakness + calibration close.
- King P, 2026-06-14 (DO-NOT-REPEAT #20): bind to the SECOND-lowest distinct run, not the strict lowest. This supersedes the EXP doc's "lowest-scoring run."

## Run binding
Bind the FA to ONE run: the second-lowest distinct score. Pull that run's full output AND its grading transcript before writing. Do not infer the failure from the output alone (KM task1 guessed four wrong failure modes; the transcript showed the real miss). The Status line is internal and is NOT pasted into Studio, so the submitted FA field must itself name the run: open the FA's first paragraph with a compact binding clause (Attempt, run id, trajectory, the run score). Fold it into paragraph one, not a separate line, to keep the two-paragraph format the gate requires.

SAVE the run verbatim FIRST, before drafting. When a pilot returns, copy the selected run exactly (the trajectory output and its grading transcript, as pasted from Studio) into `tasks/taskN/pilot/runs/` named by job and attempt, and cite that file in the Status line. The FA/GA is then provably derived from a saved primary source, not from chat memory. This is the only way the never-from-memory rule is enforceable: it makes the write-up auditable and revisable after the chat ends, and it satisfies the verify-the-primary-artifact guardrail. A run that lives only in the chat is gone at compaction, and the next pass would be from memory, which is where invented detail creeps in.

## Failure Analysis - the four components (EXP Step 14)
Cover all four, in prose, organized by severity (clinical first, then administrative, then style):
1. What the agent got RIGHT - a brief competent baseline, one or two sentences, named specifically, as the setup for the turn. Lead with it but keep it short. Ahmad (Trigeminus, more recent than 06_09) cut the standalone "what the agent got right" paragraph: the FA stays failure-only, no praise paragraph.
2. What the agent got WRONG - the central failure as a turn (it had the contradicting evidence and failed anyway), tied to the golden.
3. Why the failure MATTERS - clinical mechanism and consequence. Quantify when possible. State the severity tier.
4. The SCORE / distribution - tie the failure to the score band across runs.

Writing standards (EXP), all required:
- Be specific, not generic. Not "got the med list wrong" but "listed metformin as active despite Endocrinology holding it until creatinine returns to baseline, risking lactic acidosis."
- Name the document(s) a reviewer should check to verify the analysis.
- Separate clinical error from formatting preference. Do not conflate.
- Quantify the consequence when possible.
- Write for a non-specialist. Explain any jargon.
- Distinguish severity tiers (a patient-safety failure is not a documentation preference).

## Grader Analysis - the grader audit (THE part we keep missing)
The GA assesses HOW WELL THE GRADER SCORED THE WORK. It is not a second justification of the score. It has three moves, and the FIRST TWO ARE BOTH MANDATORY:
1. What the grader got RIGHT. Name what it credited correctly and the central defect plus any secondary miss it caught. Map to the grader's own categories (non-negotiables, the acceptable-variation boundary, the common failure modes) where natural. Affirming a sound grader IS analysis, not a filler.
2. What the grader got WRONG or COULD IMPROVE. This is REQUIRED and is the move the calibration-close form drops. Give at least one constructive point: a miscalibration, a phrasing overstatement, a distinct failure mode it should have named explicitly so it did not have to infer partial credit, or a place it was lenient or harsh. If the grader was genuinely sound, say so plainly and still add the stricter-or-looser-reading caveat (KM task1: "I would dock a full omission of a held medication harder, but the score is defensible").
3. Calibration judgment. The score is well placed or defensible. The closer "a deep floor would overstate X, and a high score would ignore Y, so the band is well placed" is acceptable, but it does NOT replace move 2.

The grader RATING (Great / Good / Mediocre / Poor) is entered directly in the Studio field, never written anywhere in the FA/GA file. The gate rejects a rating line even in the Status line, so carry the rating to the writer separately, not in the paste.

## Writer's score (project guidance, 2026-06-18)
Verbatim project guidance: "New Failure Analysis guidance. Please submit a score with your failure analysis about how you think the model did in your task. This score should be your own score, not the trajectory score, and will be compared against the agentic grader."

Submit your OWN score of how the model did, alongside the FA. It is the writer's independent assessment of the model's task performance on the 0.0 to 1.0 scale, NOT the trajectory score (the agentic grader's number), and it is compared against the agentic grader to calibrate human-versus-grader agreement. Score the run on the task's own logic: the central failure caps it low, give partial credit for the accurate items, no credit for refusing to finish. Judge it independently; do not copy the trajectory number. It usually lands near the grader when the grader is calibrated; when it diverges, the GA's calibration move should explain why. Placement: the writer's score goes in the Studio score field AND inside the submitted FA field, stated in the FA's first paragraph alongside the run binding (for example, "scored 0.12; my own score of the model is 0.10"), because the Status line is internal and is not pasted into Studio. Record it in the Status line too. This is the writer's own number; it is distinct from the banned grader-rating line (Great / Good / Mediocre / Poor), which never appears in the file. Bind it to the same run the FA analyzes.

## Guardrails (gate-enforced; presubmit_task_gate.py + verify_voice.py)
- Failure-only prose. Do not write "the grader credited"; write "it gave appropriate credit for" or "it credited correctly." The both-sides gate also bans the literal phrases "what the grader got right" and "what the model did well" anywhere in the file, including the Status line; phrase it "the grader correctly identified" or "it caught."
- No grader-section names (do not write Section A/B/C; state the content).
- No grader-rating line in the prose. The rating lives in the Studio field.
- No em dashes or en dashes anywhere. Plain hyphens and commas.
- Plain clinical language, not compressed nomenclature. Write the way an attending speaks, not in stacked hyphenated tokens that read like a variable name or a rubric label (see docs/alexander-voice-dna.md). Also avoid essayistic framing ("the sharper point is", "the real issue is") and narrated grader effort ("labored over", "deliberated over"); state the point directly with "but the note still..." and say "the grader was unsure whether X counted."
- No evaluation scaffolding (OCR, directory listings, "the transcript shows," tool calls). Name the clinical mechanism.
- Alexander voice: short declarative sentences, no AI transitions (Furthermore, Moreover, Consequently, Notably, In addition).

## Length
The platform allows up to half a page / 10-12 sentences for the FA and 4-6 sentences for the GA. The local gate caps each field at about 1000 characters and two paragraphs. Treat the local cap as the working bound: a compressed but complete version that still carries all four FA components and both mandatory GA moves. Completeness of components beats hitting a character count.

## The locked checklist (run before handing back)
FA: opens by naming the run (Attempt, run id, trajectory, the run score) and the writer's own score, folded into paragraph one; leads with what the model did right; names the central failure as a turn; states the clinical mechanism and consequence with a severity tier; names the document(s); ties the failure to the distribution.
GA: names what the grader got right; names what the grader got wrong or could improve (NOT optional); judges calibration; rating only in Status, not prose.
Both: failure-only, no section names, no rating line in prose, no dashes, plain clinical speech, second-lowest distinct run, gates clean.
