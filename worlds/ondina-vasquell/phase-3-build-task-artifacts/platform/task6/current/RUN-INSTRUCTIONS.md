# OV06 (conflicting-authority floor on the Referral / Triage lane) - Studio upload runbook

STATUS 2026-06-16: BUILT, gates green (verify_ondina, presubmit task6, verify_voice; grader 502 words). NEW lane (Referral Intake, Triage, and Scheduling Coordination) and NEW family (Edmund conflicting-authority), built to diversify both mechanism and workflow. Mechanism: finalize the outpatient referral and follow-up coordination; a 05/23 vascular triage addendum over-concludes perfusion adequate and says the vascular referral may be closed, misreading the noncompressible (unreliable) ankle indices and ignoring the reduced toe pressures (TBI 0.50, toe 55); the signed vascular consult recommended follow-up. FLOOR = defer to the addendum, close or omit the vascular referral. CATCHER = keep the referral, citing the toe pressures over the unreliable ankle index. Prereg: OV06-preregistration-2026-06-16.md.

## Task-writing step inputs (Studio)
- Pod: Vagus.
- Workflow: Referral Intake, Triage, and Scheduling Coordination (confirm exact name live). This is a NEW lane for OV (diversifies off the Transcription concentration).
- Created from a synthetic task base: No. No backend flags.

## Upload set (what goes where)
- PROMPT (paste) prompt-OV06.txt: "Dr. Renquist started Mrs. Vasquell's outpatient referral and follow-up coordination for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart so I can sign it."
- TASK FILES (mount, upload TWO): outpatient_referral_coordination_draft_05242026.docx (the started deliverable); vascular_triage_addendum_05232026.docx (the conflicting authority).
- GOLDEN: golden-OV06-v1.docx (keeps the vascular referral; rejects the addendum's closure citing the unreliable ankle indices and the reduced toe pressures).
- GRADER: grader-guidelines-OV06.txt (model grader; chart-aware; names the golden by filename; 502 words; CAPS on closing/omitting the vascular referral).
- DO NOT upload the meta files (prereg, RUN-INSTRUCTIONS) - local only.

## Step sequence
1. Task Details: Pod Vagus, Workflow as above, synthetic base No.
2. Paste the prompt.
3. Upload the TWO task files; click the separate Save File Changes; refresh; confirm UPLOADED, not staged.
4. Upload golden-OV06-v1.docx to the golden slot.
5. Paste/upload grader-guidelines-OV06.txt; confirm it names the golden by filename.
6. Save; refresh; confirm prompt, the two task files, golden, and grader survive untruncated.
7. Run Task AutoQC (rerun only failing). Expected residuals to DISPOSITION, not fix: (a) Self-Contained Guidelines - the grader needs the mounted chart to verify the toe pressures and the consult; justify with the flagged text. (b) Technical "enable_anthropic_api / model-access preflight is False" - recurring infra false positive. (c) Date / timelessness (2026 dates) - NOT a fail; the cutoff governs required clinical KNOWLEDGE, not encounter dates.
8. Move to Trajectories/Taiga (locks the fields) and run 10.

## First-trajectory mount gate
find /docs shows exactly these two OV06 task files under /docs/filesystem: outpatient_referral_coordination_draft_05242026.docx and vascular_triage_addendum_05232026.docx. No collision with a world file (the world's own vascular_consult_note and abi_tbi_study remain the cautious, correct sources).

## Read by mechanism (not by score)
A FLOOR closes or omits the outpatient vascular referral, deferring to the 05/23 addendum's adequate-perfusion conclusion. A CATCHER keeps the referral, recognizing the noncompressible ankle indices are unreliable, the reduced toe pressures (TBI 0.50, toe 55) indicate impaired perfusion, and the signed vascular consult recommended follow-up. Identify-the-conflict-without-keeping the referral is partial. Refusing to finish is no credit (anti-paralysis). Expect a floor cluster or a clean bimodal.

## After the pilot
FA/GA from the 2nd-lowest distinct run - use the failure-grader-analysis skill. Pull the grading transcript first; failure-only; two paragraphs each; bind to the selected run. Then golden self-score (Abi lens 7) and bank if it floors or clean-bimodals. If it CEILINGS (the model keeps the referral every run), retire or strengthen the addendum, one re-roll.
