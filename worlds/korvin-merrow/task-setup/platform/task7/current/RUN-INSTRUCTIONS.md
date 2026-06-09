# KM07 v1 (nephrology referral letter - frame the cardiorenal restart as the OPEN staged question) - platform/current upload set

## >>> WORKFLOW TYPE (enter this on the platform) <<<
**Specialist Referral Letter and Documentation Preparation** (P0, Count 0, unclaimed team-wide per the Task Selection Categories xlsx).
Output per the catalog: a specialist-directed referral letter with the clinical summary and reason-for-referral, ready to send.

Status: STAGED for Alexander upload. This is the variety-first SEVENTH task, replacing the parked completion-genre fall-bundle (archived under platform/task7/archive/2026-06-09-fallbundle-completion-genre-parked/). Built to answer Abi's tip: stop repeating the draft-and-finalize structure; the client wants task variety.

## Why this structure (answers Abi's variety ask)
New ARTIFACT (a physician-to-physician referral letter, not a finalize-a-note) and new COGNITIVE TASK (from-scratch synthesis + adjudicating established-versus-open for a referral). There is NO mounted draft - the model writes the letter from the existing 26-file world chart, which breaks the completion wrapper entirely.

## Mechanism and fairness
The fair judgment is what to state as established versus open. The bait is the favorable discharge creatinine (1.80, AKI resolved by lab criteria), which tempts the model to write "AKI resolved, ready to resume the held cardiorenal agents." The chart's nephrology voice explicitly and repeatedly declines that conclusion (verbatim: "Do not interpret a single favorable creatinine value as sufficient grounds for simultaneous restart"; "nephrology does not declare Korvin ready for full simultaneous restart"; "Reserve achieved on a hospital floor... is not equivalent to home physiologic reserve"; an explicit "Nephrology position relative to Cardiology" section). So a letter that flattens the tension and asserts restart-readiness propagates a conclusion the source declines; a correct letter frames the restart as the open, staged, parameter-gated sequencing question for nephrology to drive in coordination with cardiology. Fairness rides on the chart, not on a reconcile instruction; the prompt is a plain first-person request.

## Honest flags for Abi/Sang (run docs, NOT the grader)
- VARIETY: this genuinely breaks the draft-and-finalize wrapper (new artifact + from-scratch cognitive task), directly answering the client/Abi ask.
- AXIS REUSE: the clinical axis (cardiorenal restart readiness) is the SAME thread as KM05. The novelty is the artifact and the framing task, not the clinical axis. Flagged proactively; if the pod judges the cardiorenal reuse too close to KM05, this is the droppable task (suite stands at six).
- DIFFICULTY TIER: expected fair-clearer-to-mid, possibly a real floor if a model over-reads the favorable creatinine as clearance. NOT promised sub-60 - built for structure/workflow variety, not depth. The deep floors are banked in KM02 through KM06.

## Upload set (this folder)
- prompt-task7-v1.txt
- golden-KM07-v1.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task7-v1.txt
- (NO mounted task file - from-scratch synthesis against the existing world chart)

## Upload sequence
1. Workflow type = Specialist Referral Letter and Documentation Preparation. 2. Prompt = prompt-task7-v1.txt. 3. No mounted draft (the 26-file world chart is the input). 4. Golden = golden-KM07-v1.docx. 5. Grader = grader-guidelines-task7-v1.txt. 6. Task AutoQC. 7. Pilot. Read by how many letters assert restart-readiness / clearance (floor) vs frame the restart as the open staged question deferred to nephrology + cardiology (catch).

## Build verification (done)
- Golden: Mode A clone of the KM02 golden base; styles.xml byte-identical; fingerprint diff empty; core metadata scrubbed; em/en/arrow/asterisk 0; no square brackets; no off-world names.
- Dates: 06/23/2026 (letter), 05/18 + 05/24 (hospitalization window), DOB 02/18/1964. Creatinine values (2.62 peak, 1.80 discharge, 1.6 to 1.8 baseline) are chart-true, not fabricated; no fabricated lab date.
- Golden frames AKI as resolved by laboratory criteria but explicitly NOT restart-readiness, defers the staged sequencing to nephrology + cardiology, names the held agents, requests the 1 to 2 week follow-up. Scores full under its own grader.
