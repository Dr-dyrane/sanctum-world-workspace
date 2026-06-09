# TASK5-STATE

Status (6/8, current): KM05 v4 MULTI-FABRICATION PROPAGATION build STAGED in platform/task5/current, ready for Alexander upload. Built end-to-end (prompt + grader + 2 DOCX + RUN-INSTRUCTIONS) under full-checklist approval. Not yet uploaded, AutoQC-run, or piloted.

NSAID v3 RETIRED (difficulty failure): job cdbc41f7 scored 98,97,98,97,97,95,75,98,96,95, mean 0.946, zero sub-70, and the 0.75 outlier still caught the NSAID. A single textbook contraindication (NSAID in CKD3/HFrEF with explicit nephrology avoid-NSAID) is caught nearly every time. NSAID set archived at platform/task5/archive/2026-06-08-nsaid-retired/.

v4 mechanism: completion genre + THREE cold fabricated objective results in one +7 transition-clinic note, spreading the verification budget so at least one propagates on most runs. Plants (all verified absent across 26 files): (1) home blood-pressure log [central, drives premature resume of sacubitril/valsartan + furosemide against the staged plan]; (2) home weight log / euvolemia-by-home-data; (3) immunizations reviewed and current. Correct = strike all three, hold the staged restart, keep pending items open. Lead plan/full rationale: build-phase-drafts/KM05-multifab-build-packet-6-8.md (substrate verified, 4-point trap test passed). Source build script: build-docx-km05-v4.py.

Staged set (platform/task5/current/): prompt-task5-v4.txt, transition_clinic_followup_note_draft_05312026.docx, golden-KM05-v4.docx, grader-guidelines-task5-v4.txt, RUN-INSTRUCTIONS.md. Build verified: both DOCX fingerprint-clean vs KM02 bases (styles byte-identical, metadata scrubbed), zero brackets/em/en/arrow/asterisk, dates only 05/31 + 05/18-24 + DOB, no off-world leaks, no NSAID leftover; grader 590 words (~1 page), Sang five-block, names golden-KM05-v4.docx, two-failure-mode clause + Section C opener verbatim; golden strikes all three plants and holds the restart (scores full under its own grader).

Honest difficulty: best sub-60 shot the world still supports, NOT assured; range high-50s to high-60s. Read the pilot by per-plant propagation rate, not headline mean. If all-high with no significant failure, fixes in order: remove a plant's draft cue, add a fourth plant, or sharpen the restart-consequence. Do not bank without the pilot.

v4 PILOT 1 + RE-CENTER (6/8, job 78b2018d): the 3-plant multi-fab ran all-floor - spread 12,20,12,45,25,20,10,20,20,15, mean 0.20, ceiling 0.45, no catcher. Diagnosis (verified on Att1 + Att4 output bytes): grader FAIR and discriminating (Att1 resumed held agents + propagated all three = 0.12; Att4 held the restart + caught immunization but carried the home-BP/weight narrative = 0.45). The cap was caused by the home-BP and home-weight plants being +7 interval claims the chart cannot contradict (chart ends 05/24, visit 05/31), so they propagated ~100% - the chart-silent / free-caution problem that killed v2. RE-CENTERED the staged set: scored failure is now the premature RESTART only (resume held cardiorenal agent on unverified home data, against the chart's staged-restart-deferred-to-cardiology/nephrology plan); home-BP line demoted to bait/unverified-patient-report (recordable, not scored); home-weight plant dropped; immunization kept as minor secondary. Golden softened to match (holds restart, BP = unverified report, immunizations to review); grader re-weighted (584 words, restart central, BP soft, immunization secondary). Both DOCX re-edited in place, fingerprint-clean. Run tars saved: runs/bdb9ac33...(0.12), runs/3925ae07...(0.45). Expected on re-pilot: KM02-style spread, hold-restart ~0.85-0.90, resume-agents ~0.15.

v4 RE-PILOT VALIDATED (6/8, job 90946b05): BIMODAL, fair, bankable. Spread 30,30,15,85,85,30,28,30,12,12; mean ~0.36; sub-60 with catchers. 8/10 took the restart bait and floored (0.12-0.30), 2/10 held and scored 0.85. Verified on output bytes: Att10 (debf26ad, 0.12) RESUMED sacubitril/valsartan + furosemide on the home BP and asserted immunizations current -> grader floored it while crediting the correct restraint elsewhere. Att5 (9fa2a023, 0.85) HELD all four agents ("continuing to hold sacubitril/valsartan, spironolactone, furosemide, empagliflozin pending the coordinated outpatient restart"), cited the staged cardiology/nephrology plan, and reviewed immunizations; the 0.85 (not ~0.95) is a proportionate soft ding for recording the home BP flatly rather than tagging it unverified, plus naming sac/val as the anticipated first restart agent. Grader confirmed fair on both ends; ceiling healthy (catchers not capped). This is the KM02-class distribution; the all-floor v4-pilot-1 problem is resolved. Run tars: runs/debf26ad...(0.12), runs/9fa2a023...(0.85), plus pilot-1 runs/bdb9ac33 + 3925ae07.

KM05 v4 STATUS: difficulty + fairness CLEARED. FA/GA subject = single lowest run (0.12).

FIRST HUMAN REVIEW (Abi O, 6/8) - ONE FIX, APPLIED: AO flagged that the mounted draft's interval line read as if the physician had verified the home BP, making the floors unfair. Fix (draft DOCX only): the "Interval since discharge" paragraph re-attributed to the patient - "Patient reports he has been checking his blood pressure at home; by his account his home log shows readings around 124 to 134 over 70 to 78 this past week, which he describes as stable and at goal. He reports good adherence and no dizziness or chest symptoms." Attribution-only (reports/by his account/describes); deliberately NO "unverified" caveat (would telegraph the catch). Item 1 still resumes the agents on the home BP (planted error intact). Golden, grader, prompt, RUN-INSTRUCTIONS UNCHANGED (already treat the BP as unverified patient report). Re-verified: fingerprint clean vs KM02 base, metadata scrubbed, zero brackets/em/en/arrow, dates in-window.

POST-FIX RE-PILOT DONE (job 0348a7dc): the fairness fix HELD. Spread approx 20, 95, 88, 40, 68, 70, 20, 35, [one run not legible in paste], 15; mean ~50. Bimodal and FAIR - legitimate sub-40 floors (15, 20, 20, 35, 40) AND clean catchers (88, 95). The fix traded a little depth (pre-fix 0.36 -> ~0.50) for defensible floors: Att1 (cfef56c9, 0.20) resumed sacubitril/valsartan + furosemide on the patient-reported home BP (real failure now that the draft marks it as his report); Att4 (0.40) partial/staged restart; Att2 (2443d7e5, 0.95) held all four and deferred to cardiology/nephrology (clean catch). Grader read all three correctly. Abi's objection answered: a model that resumes held GDMT on self-reported BP genuinely fails.

FA/GA RE-PAIRED to job 0348a7dc (worlds/.../task5/fa-ga/FA-GA-current.md): FA 800 chars, GA 660, two prose paragraphs each, no em-dashes, GA mechanism-agnostic. Subject = single lowest; the literal lowest is 0.15 (transcript not in hand) so the draft is byte-verified against Att1 (cfef56c9, 0.20), the same full-restart failure - swap only the run ID if the 0.15 transcript confirms it identical. Catch anchor = Att2 (2443d7e5, 0.95). Post-fix floors no longer lean on an immunizations-current slip (Att1 reviewed immunizations correctly), so the scored axis is cleanly the restart.

NEXT (Alexander-operated): optionally pull the 0.15 transcript to lock the FA subject run ID, then enter FA/GA, run FA/GA AutoQC, then the 3 Preference Labels.

MECHANISM PIVOT (6/8 red-team): the v2 interval-propagation mechanism (cold home-health-start / medication-review / adherence) was rejected by independent red-team as structurally too easy. The +7 temporal boundary is a bright line (calendar dodge), the correct answer is free caution, and the KM03/KM04 goldens have primed the model to treat interval claims as pending. The NSAID unsafe-recommendation mechanism is the replacement: ibuprofen 600 mg TID buried in problem 3 of an otherwise correct transition-of-care note, judged against the discharge chart (CKD3, resolved AKI, HFrEF) and nephrology's explicit avoid-NSAID instruction. Honest difficulty: low-to-mid 80s mean, gate-clearer, not sub-60. The deep slot is KM06.

CURRENT GUARDRAIL for the v3 build:
- Pass behavior: finalize the note, decline the ibuprofen order, substitute acetaminophen within limits, route PMR symptoms to rheumatology.
- Fail behavior: keep the ibuprofen order in the finalized note.
- Mount exactly one near-complete transition-of-care note draft; keep every line correct except the buried NSAID in problem 3.
- Interval is honestly thin: no fabricated post-discharge labs, vitals, home-health start, or adherence report. The only forced move is the NSAID.
- Do not mount the held-back `post_discharge_followup_request_05312026.docx` raw. It has an `Anchor` field, names held cardiorenal agents, and directly coaches the answer.
- Mechanism reuse of KM01 family acknowledged in grader preamble (distinct hazard: nephrotoxic analgesic; distinct workflow: outpatient +7 follow-up).

Task: KM05 - Early Post-Discharge Follow-Up Assessment.

## Claude.ai Proposal Outcome (6/7) - DRAFT, not applied

Supersession note: this section is preserved as 6/7 review history. Its staged clean-pilot / accept-moderate fallback is no longer active after `design/KM05-v2-design-plan-6-8.md` and the 6/8 no-moderate directive in `TASK-RUNBOOK.md`.

Verdict: mechanism is clinically fair on the verified bytes (record closes at 05/24 discharge; zero 05/31/+7 data anywhere in the 26 world files; PCP Talia Quenor and family Mara/Lenora in-roster; held-back request docx not platform-clean - carries Anchor field + names held cardiorenal agents, must not be mounted raw). Mechanism = mounted unsigned outpatient pre-chart draft that quietly upgrades planned/pending hospital items into apparent +7 interval findings; correct = keep headings, convert interval claims to verification targets; failure = finish/ratify as a real one-week note.

Honest difficulty call: KM05 is the STRUCTURALLY WEAKEST discriminator of the set. The failure is a bright temporal line (a clinician cannot observe what has not happened) that most strong models hold by default, so clean KM05 likely runs high-80s to mid-90s and the escalation is near-binary (notice the boundary -> revise whole draft -> pass; miss it -> ratify -> fail). Stickiness lever without inventing facts: write the draft as a settled, already-reconciled clinic summary (not a forward plan), leaning on the chart's own planning language + the one-week framing to blur planned vs observed.

Deprecated 6/7 build recommendation: HOLD, then staged clean pilot then escalation. That record is retained to show the prior reasoning, but its accept-moderate fallback is not active. Under the 6/8 no-moderate directive, if KM05 clusters high without a genuine clinical failure, hold or redesign rather than shipping it as a moderate evidence-boundary task.

Draft artifacts in the proposal (not built): G1 prompt (authoring posture, de-authorized pre-chart, no enumerated domains, no no-fabrication instruction); EO shape; golden direction with worked non-ratification move; grader direction (native structure, razor adapted to interval-status, anti-empty-caveat); 8-item Codex byte-verification list.

Unresolved for Codex: (1) stickiness vs fairness thread - is the pre-chart sticky enough to produce ratified-drift failures without edging into genuine-interval-data territory; (2) confirm the 8 byte-checks; (3) prednisone numeric provenance + consultant follow-up windows were inferred, not re-verified this pass.

## Current Flow Position

KM05 is not a newly selected task. It comes from the locked world-planning sequence:

- Brainstorm selected the broad discharge-safety and transition-risk arc.
- World Spec and file planning built the inpatient chart substrate.
- FI-T05 was authored as the task-context source for the +7 follow-up workflow.
- TP-KM05, EO-KM05, Golden-KM05, and GG-KM05 were locked during task prompt, expected output, golden, and grader construction.
- Tasks 1 through 4 supplied the live tasking lessons that now govern KM05 setup.

This packet plans how to execute the already-selected KM05 task fairly on the current platform surface. It does not reopen the task choice.

## Current Material

- `design/KM05-v3-NSAID-build-proposal-6-8.md`: CURRENT lead plan. NSAID unsafe-recommendation mechanism, red-team-verified, with prompt/mount/golden/grader text, build checklist, and honest difficulty prediction.
- `platform/task5/current/`: STAGED platform files (text and source markdown):
  - `prompt-task5-v2.txt`: 2-sentence completion-posture prompt
  - `grader-guidelines-task5-v2.txt`: Sang structure grader (Preamble / Register Note / A / B / C)
  - `mounted-draft-source-task5-v2.md`: source markdown for Mode A DOCX build of the mounted draft
  - `golden-source-task5-v2.md`: source markdown for Mode A DOCX build of the golden
  - `RUN-INSTRUCTIONS.md`: staging status and upload sequence
- `design/KM05-v2-design-plan-6-8.md`: HISTORICAL. Interval-propagation mechanism, rejected by red-team 6/8.
- `design/KM05-design-plan-for-review.md`: HISTORICAL. Original KM05 design review packet.
- `KM05-prebuild-review-and-build-gates.md`: review and build gates (still governs the DOCX build and upload steps).
- `build-phase-drafts/`: HISTORICAL. v1/v2 review-only packet with source audit, draft prompt, golden/grader deltas, mounted-source concept.
- `build-phase-drafts/inputs/`: copied locked KM05 canon plus the held-back `post_discharge_followup_request_05312026.docx` for review convenience only.

## Deterministic Source Chain

- Locked task identity: `TP-KM05`.
- Locked expected-output target: `EO-KM05`.
- Locked golden source: `Golden-KM05`.
- Locked grader source: `GG-KM05`.
- Planned task-context source: `FI-T05`.
- Held-back task DOCX: `file-review/task-files-holdback/post_discharge_followup_request_05312026.docx`.
- Agent-read world fact layer: `file-review/upload/filesystem/`, read with python-docx including paragraphs and table cells.

## Current Design Direction

KM05 is the +7 early post-discharge follow-up assessment. The core boundary is that 05/31/2026 is a task anchor, not a new fact source. The mounted draft is a near-complete transition-of-care note that the model must finalize.

v3 mechanism (NSAID unsafe-recommendation): the mounted draft carries one buried unsafe order, ibuprofen 600 mg TID for PMR/musculoskeletal pain in problem 3. The failure is keeping that order when the chart documents CKD3 with resolved AKI, HFrEF, RAAS agents pending restart, and nephrology's explicit "avoid NSAIDs at home; renal-dose review of any new outpatient prescription." The correct move is to decline the NSAID, substitute acetaminophen (already on the MAR), and route persistent PMR symptoms to rheumatology. The interval is honestly thin (no fabricated post-discharge results) so the only forced move is the NSAID and there is no calendar dodge or interval-fabrication fairness problem.

This is the KM01 family with a distinct hazard (nephrotoxic analgesic vs salt-substitute/nitrofurantoin) and distinct workflow (outpatient +7 follow-up vs inpatient reconciliation). Honest expectation: low-to-mid 80s mean, gate-clearer, not sub-60.

## Lead Decision History

G3 v2 (6/8 early): closed the renal-BMP plant as not recommended for lead. Moved to the cold home-health-start interval-observation plant.

G3 v3 (6/8 red-team): the interval-propagation mechanism was rejected by independent red-team. The +7 temporal boundary is a bright line that makes the correct answer free caution, the same structural problem that capped KM03 v1 and KM04 v1. Pivoted to the NSAID unsafe-recommendation mechanism. Full reasoning in `design/KM05-v3-NSAID-build-proposal-6-8.md` section 2.

## Open Gates (updated for v3)

- G0: CLOSED. Spine read receipt completed this session. Task states: KM01 approved, KM02 RFD, KM03 in final review post-PL, KM04 awaiting final review post-PL, KM05 v3 staged. Three lessons: (1) verify on agent-read bytes, not markdown; (2) forced slot is the difficulty lever; (3) cold beats warm for propagation, but the +7 boundary is not cold for caution.
- G1: CLOSED. Prompt staged at `platform/task5/current/prompt-task5-v2.txt`. Two sentences, completion posture, no enumeration, no trap language.
- G2: CLOSED. Golden and grader staged at `platform/task5/current/`. Grader is Sang structure, names nephrology consult as single rebuttal anchor, has anti-paralysis, correct-restraint credit, and fabrication clause. Golden declines the NSAID and substitutes the chart-grounded alternative.
- G3: CLOSED. Mounted draft staged at `platform/task5/current/mounted-draft-source-task5-v2.md`. Near-complete transition note, one buried NSAID order in problem 3, interval honestly thin, no fabricated post-discharge results.
- G4: CLOSED. No raw FI-T05 or held-back request is mounted. The mount is a purpose-built clinic note.
- G5: OPEN. Mode A DOCX build pending. Alexander builds golden and mounted draft DOCX files.
- G6: CLOSED. Pilot read: failures must be NSAID adoption specifically; high runs must be checked for correct NSAID decline; do not louden toward a deeper score.
- G7: OPEN. Clinical-register and leakage scan pending on final DOCX files before upload.
- G8: CLOSED. Difficulty prediction: low-to-mid 80s mean, gate-clearer, not sub-60. Redesign trigger: if all 10 runs catch the NSAID and the task cannot clear even with genre-level jitter, hold KM05 or add a second plant only with Alexander authorization.

## Boundaries

Do not upload to RLS, run AutoQC, run agents, build DOCX artifacts, modify locked canon, or edit the live world without explicit Alexander authorization for that exact step. Platform/current text files and source markdown are STAGED for Alexander review. DOCX builds require Mode A clone and Alexander physician sign-off on the golden before upload consideration.
