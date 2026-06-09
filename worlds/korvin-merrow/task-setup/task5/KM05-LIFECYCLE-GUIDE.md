# KM05 Lifecycle Guide: How to Bring Task 5 to Life

Prepared 2026-06-08. Derived from auditing the full lifecycle of KM01 (306-line log, 4 batches, 3 human reviews), KM03 (v2.1 difficulty fail, v2.2 clear, Sang review, rerun, FA/GA, PL), and KM04 (v1 difficulty fail, v2 clear, Sang review, rerun, FA/GA, PL in progress). This maps the exact steps, in order, to bring KM05 from its current staged state to final delivery.

---

## The Full Task Lifecycle (distilled from KM01-KM04)

### Phase 1: Design and Build (COMPLETE for KM05)

| Step | What | KM05 Status |
|------|------|-------------|
| 1.1 | Select mechanism, verify on agent-read bytes | DONE. NSAID ibuprofen 600 mg TID, nephrology rebuttal verified |
| 1.2 | Write prompt (txt) | DONE. prompt-task5-v2.txt staged |
| 1.3 | Write grader (txt, Sang structure) | DONE. grader-guidelines-task5-v2.txt staged |
| 1.4 | Write mounted draft source (md) | DONE. mounted-draft-source-task5-v2.md staged |
| 1.5 | Write golden source (md) | DONE. golden-source-task5-v2.md staged |
| 1.6 | Write RUN-INSTRUCTIONS | DONE. RUN-INSTRUCTIONS.md staged |

### Phase 2: DOCX Build (NEXT for KM05)

| Step | What | KM05 Status |
|------|------|-------------|
| 2.1 | Mode A clone the mounted draft DOCX from the mount base | PENDING. Alexander builds transition_clinic_followup_note_draft_05312026.docx |
| 2.2 | Mode A clone the golden DOCX from the golden base | PENDING. Alexander builds golden-KM05-v2.docx |
| 2.3 | Alexander reviews golden in physician voice, signs off | PENDING |
| 2.4 | Fingerprint verify: styles.xml byte-identical, fills/borders identical, palette subset | PENDING |
| 2.5 | Metadata scrub: core metadata clean after python-docx save | PENDING |
| 2.6 | Character audit: em dashes 0, en dashes 0, arrows 0 | PENDING |
| 2.7 | Date audit: 05/31/2026 visit date allowed; no fabricated result dated 05/25-05/31 | PENDING |
| 2.8 | Golden filename matches grader's named string exactly | PENDING (golden-KM05-v2.docx) |
| 2.9 | Clinical-register and leakage scan on all platform files | PENDING (G7) |

### Phase 3: Platform Upload

| Step | What | Notes |
|------|------|-------|
| 3.1 | Upload prompt to 1.2 | Paste prompt-task5-v2.txt |
| 3.2 | Upload task file to 1.3 | Upload transition_clinic_followup_note_draft_05312026.docx. Click "Save File Changes" (the separate button, NOT top Save). Confirm no collision with the 26 world files |
| 3.3 | Upload golden to 1.4 | Upload golden-KM05-v2.docx. Confirm filename matches grader reference |
| 3.4 | Paste grader to 1.4 | Paste grader-guidelines-task5-v2.txt. If platform sanitizes the golden filename (dots to underscores), edit the grader reference to match |

### Phase 4: Task AutoQC

| Step | What | Notes |
|------|------|-------|
| 4.1 | Run Task AutoQC | Target: PASS or justified-only warnings |
| 4.2 | Expected warnings: Self-Contained Guidelines (the grader cross-references the chart for the NSAID check). Justify with include_input_files evidence, do NOT fix to golden-only |
| 4.3 | If No Weight Distribution or No Scoring Framework fires: the grader uses clinical-severity language only (no numeric weights, no "cap the score", no "primary discriminator"). Justify if false positive; fix if the language actually contains ranking |
| 4.4 | Record AutoQC ID in TASK5-STATE.md |
| 4.5 | If fails fire that are NOT justifiable: fix and rerun. Do not proceed to Taiga with real AutoQC failures |

### Phase 5: Taiga Trajectories (Pilot Run)

| Step | What | Notes |
|------|------|-------|
| 5.1 | Run Taiga trajectories (10 runs) | Alexander operates |
| 5.2 | Read by NSAID ADOPTION RATE, not headline mean | Count how many of 10 keep ibuprofen (or any NSAID) in the finalized note |
| 5.3 | Expected: sub-90 tail on NSAID-adopting runs, mean low-to-mid 80s | This is KM01 family, a gate-clearer |
| 5.4 | If all 10 catch the NSAID (clusters >=90): HOLD. Do not accept an all-high no-failure result. Add a second plant only with Alexander authorization |
| 5.5 | Record job ID, scores, and spread in TASK5-STATE.md |

### Phase 6: Taiga QA (Env Linter + Data Quality)

| Step | What | Notes |
|------|------|-------|
| 6.1 | Respond to EVERY Env Linter + Data Quality flag | tech issue = thumbs down + exactly "tech issue" in annotation + full sentence in dismissal field. Substantive = thumbs down + thorough professional rebuttal. NEVER thumbs up |
| 6.2 | enable_anthropic_api = recurring false positive, respond "tech issue" |
| 6.3 | Run Taiga QA Feedback AutoQC (5.1) | Target: PASS |
| 6.4 | Address any 5.2 notes |

### Phase 7: Failure Analysis and Grader Analysis

| Step | What | Notes |
|------|------|-------|
| 7.1 | Click "Start Failure Analysis & Grader Analysis" on the platform | Do NOT write FA/GA before clicking this button |
| 7.2 | Select the SINGLE LOWEST run as FA/GA subject | Read the grading transcript to confirm the failure is NSAID adoption specifically |
| 7.3 | Write FA: two paragraphs, natural prose, no bullets, no headers | Para 1: what the model failed (kept the ibuprofen order despite CKD3/AKI/HFrEF and nephrology's instruction). Para 2: what the model did well in that same run |
| 7.4 | Write GA: two paragraphs, natural prose, Section A/B/C mapped | Para 1: what the grader got right (scored the NSAID adoption correctly, caught it against the golden and nephrology evidence). Para 2: what the grader got wrong or could improve |
| 7.5 | Character limits: FA under 1000 chars, GA under 1000 chars |
| 7.6 | No em dashes, no bullets, no headers, no "what I missed" |
| 7.7 | Run FA/GA AutoQC (7.1) | Target: PASS or justified. The "Human-Written (Grader Analysis)" check may fire on the agentic grader's machine-generated transcript, not on Alexander's GA. If so, justify as false positive |
| 7.8 | Address 7.2 notes |

### Phase 8: Preference Labeling (THREE PLs)

| Step | What | Notes |
|------|------|-------|
| 8.1 | Select three distinct trajectory pairs, each on a different trajectory | Per Abi 6/7 rule: three PLs, three separate A/B comparisons |
| 8.2 | Read BOTH transcripts in full against the golden | Do not infer from scores alone |
| 8.3 | Write justification: natural clinical prose, no stacked hedges, no templated section structure | The rubric fails 3+ AI prose patterns. Vary sentence structure across all three PLs |
| 8.4 | Required headers: Prompt adherence, Correctness, Completeness, Methodology, Quality and clarity | These are required; the prose within them is not templated |
| 8.5 | PL tier must match the gap | If both runs handle the NSAID correctly, the tier is B1/A1 (slightly). Reserve B2+/A2+ for a real caught-finding difference |
| 8.6 | Submit each PL on the platform | Run PL AutoQC after each submission |

### Phase 9: Final Human Review

| Step | What | Notes |
|------|------|-------|
| 9.1 | Submit for final review (likely Sang N if he reviews KM05, or Abi O) | |
| 9.2 | Reviewer checks: prompt natural, task files realistic, grader appropriate, golden realistic, AutoQC reviewed, at least one trajectory below 90, Env Linter/DQ/responses reviewed, FA/GA passed, PLs submitted |
| 9.3 | If sent back: fix and resubmit. Common fixes from KM01-KM04: grader structure (Sang wants Preamble/Register Note/A/B/C), golden rewrite in physician words, FA/GA prose formatting, PL tier mismatch |
| 9.4 | If reviewer requires grader restructure or golden rewrite: make the change, rerun Taiga, re-derive FA/GA from the NEW lowest run, re-do PLs if the spread changed materially |

### Phase 10: Task Approved / Delivered

Task is complete when the final reviewer approves.

---

## Where KM05 Is Right Now

```
Phase 1 (Design/Build)    : COMPLETE
Phase 2 (DOCX Build)      : PENDING - Alexander's next step
Phase 3 (Platform Upload)  : BLOCKED on Phase 2
Phase 4 (Task AutoQC)      : BLOCKED on Phase 3
Phase 5 (Taiga Pilot)      : BLOCKED on Phase 4
Phase 6 (Taiga QA)         : BLOCKED on Phase 5
Phase 7 (FA/GA)            : BLOCKED on Phase 6
Phase 8 (Preference Label) : BLOCKED on Phase 7
Phase 9 (Final Review)     : BLOCKED on Phase 8
Phase 10 (Delivered)       : BLOCKED on Phase 9
```

## The Immediate Next Action

Alexander builds the two DOCX files (Phase 2):

1. Mode A clone `transition_clinic_followup_note_draft_05312026.docx` from the mount base, using `mounted-draft-source-task5-v2.md` as the content source.
2. Mode A clone `golden-KM05-v2.docx` from the golden base, using `golden-source-task5-v2.md` as the content source. Review and sign off in physician voice.
3. Run the Phase 2 verification checklist (fingerprint, metadata, character audit, date audit, leakage scan).
4. Place both DOCX files in `platform/task5/current/`.
5. Proceed to Phase 3 (platform upload).

## Key Lessons Baked In From KM01-KM04

- **Click "Save File Changes"** for task files (1.3), not just top "Save Changes" (KM01 gotcha).
- **Justify Self-Contained, do not fix it** to golden-only (KM01 v2 lesson; the grader has the chart via include_input_files).
- **Read the pilot by propagation rate**, not headline mean (KM02/KM03/KM04 lesson).
- **FA/GA: one run, prose, no headers, under 1000 chars** (Abi format, KM01 round-2 lesson).
- **PL: three PLs, three different trajectories, natural prose, tier matches gap** (Abi 6/7 + KM04 PL rewrite lesson).
- **Grader: Sang structure** (Preamble / Register Note / A / B / C), no scoring bands, under a page (KM03 Sang fix).
- **Golden: physician-authored, chart-format, signable** (KM01 Abi realism, KM03 Sang requirement).
- **If reviewer sends back**: fix, rerun Taiga, re-derive FA/GA from the new lowest. Do not port old FA/GA forward (KM01 lesson).
