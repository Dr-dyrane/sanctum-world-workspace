# TASK5-STATE

Status: KM05 v3 NSAID build, platform/current STAGED (text files and source markdown). DOCX files not yet built (Mode A clone pending). Not uploaded, not AutoQC-run, not agent-run. Current lead plan: `design/KM05-v3-NSAID-build-proposal-6-8.md`. Next: Alexander reviews staged files, authors physician-voice golden, builds DOCX via Mode A, then upload only on explicit authorization.

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
