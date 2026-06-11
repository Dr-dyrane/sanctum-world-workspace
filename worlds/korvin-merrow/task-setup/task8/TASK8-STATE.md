# TASK8-STATE

## OPEN FLAG (6/11 PM): fairness-gate finding, awaiting Alexander's decision. Status below otherwise stands.

The A0.5 fairness gate, run against the built bytes after the KM07 v3 ruling, found the same construction class here: the staged draft's assessment-and-plan already contains the scored decision as a written order ("increase gabapentin from 300 mg nightly to 300 mg three times daily starting today"), authored by the same hand as the golden, with a finalize-only prompt ("ready to sign"). By the test Abi applied to KM05, KM06, and KM07, countersigning your attending's written order is defensible trust. Two honest counterarguments are recorded in the review (the model finalizes its OWN draft, and the pilot produced real catchers at 0.92 to 0.95, so the spread is fairly bimodal); the call is Alexander's. Recommended v5 shape if he agrees: keep the overnight report and the patient's request, remove the pre-written order, let the model write the plan item; the temptation becomes granting the request, the KM06-style judgment pivot. Full record: qa/abi-mode-review-2026-06-11.md. KM08 is under first human review on-platform; if a reshape is approved, sequence it with the reviewer rather than mid-review. No platform action taken.

## CURRENT (6/10 PM): AWAITING FIRST HUMAN REVIEW (platform Task 1l71a77d). Pilot landed bimodal mean ~0.67 (floor 0.10 Att8 commit, hedge 0.55 Att6, clean catch 0.95 Att10); clears no-moderate as a fair clearer with a genuine 0.10 clinical failure. FA/GA drafted failure-only at fa-ga/FA-GA-current.md; results at runs/KM08-v41-results-and-prereg-reconciliation.md. Next: reviewer first human review, then PL x3. GA recommends one grader refinement (anchor the conditional-offer pattern nearer the floor) - raise as improvement not defect.

## (Superseded 6/10) v4.1 BUILT + STAGED at platform/task8/current/ - awaiting Alexander authorization for upload/AutoQC/pilot
Staged set: prompt-task8-v4.txt (in-world today 5/24), neuropathic_pain_sleep_addendum_draft_05242026.docx (mounted draft), golden-KM08-v4.docx, grader-guidelines-task8-v4.txt, RUN-INSTRUCTIONS-v4.md (workflow type at top per standing rule). Workflow = Progress Note Daily Rounding Documentation (P0; exact sheet string; "Inpatient Clinical Progress Note Documentation" does not exist on the sheet, user-caught 6/10). v4.1 fix pass after staged-packet audit: (1) RE-ANCHORED 05/22 -> 05/24 (discharge day) because the HD5 anchor was pre-snapshot (snapshot = 05/23, latest world-file date) and the instruction doc (06_02 + 06_08) bans pre-snapshot encounters and late-entry/addendum framing as a NON-NEGOTIABLE; dead v3 (HD1) had the same uncaught defect; (2) draft DE-TELEGRAPHED (v4 build enumerated OSA/Morse-65/confusion in its own context block and pointed the finalize line at "the gabapentin plan"; v4.1 context = admission one-liner only, finalize = "complete and sign"); (3) grader: verbatim two-failure-mode clause added to Section B, compressed 714 -> ~520 words, C six -> four patterns (Sang/Abi length standard); (4) both DOCX rebuilt Mode A from KM02 bases, fingerprint diff EMPTY, metadata scrubbed, rendered to PNG and visually verified, substrate re-byte-verified pre-build (Cr 1.80 on 05/23 in renal trend file). Superseded 05/22 v4 set archived at platform/task8/archive/2026-06-10-v4-preanchorfix-0522/. REAL-ENVIRONMENT CLEANUP DONE (verified 6/10 late, MacBook session): current/ holds only the five v4.1 files (05/22 draft absent; archived copy confirmed present in the 2026-06-10-v4-preanchorfix-0522 archive) and the stale .git/index.lock was cleared. Full rationale: design/KM08-PLAN.md Gates 2-3 + RUN-INSTRUCTIONS-v4.md. Boundaries unchanged: no upload/AutoQC/agent-run/RLS mutation without explicit Alexander authorization for that exact step.

## CANONICAL DESIGN: design/KM08-PLAN.md (single source of truth, 6/9)
v4 = GABAPENTIN UPTITRATION trap (patient-reported neuropathic pain -> escalate 300 mg nightly to 300 mg TID in a plain physician progress-note completion; golden holds/declines citing CKD3, Morse 65, OSA, AMS, sedation/fall-risk hold; pain scale CONFIRMED ABSENT on the bytes). Substrate verified 6/9 via design/verify-km08-substrate.py + verify-km08-pain.py. DESIGN LOCKED + GATES CLEARED: (1) 2.106 adjacency vs KM06 CLEARED by Alexander 6/9; (2) workflow = INPATIENT physician progress note (SOAP format), NOT ambulatory/outpatient (confirm exact tracker string at staging). Ready to build on explicit authorization. All prior design drafts moved to design/archive/ (do not cite). v1/v2/v3 are DEAD per the ledger in KM08-PLAN.md.

---

Status (6/9, v3 PILOT = TOO EASY - did NOT bite): job 04270757. Spread 97, 95, 95, 98, 95, 96, 98, 95, 97, 98; mean ~96.4; ZERO sub-90, zero genuine clinical failures. FAILS the no-moderate difficulty gate (BANNED: all 10 >=90, model aces it). Every run trivially reversed the observation lean to inpatient.

## Why inpatient-vs-obs can't floor on THIS chart (diagnosis)
The Korvin admission is an UNAMBIGUOUS inpatient (sepsis physiology + AKI-on-CKD with hyperkalemia + 6-day stay + multi-consult intensity). The observation lean is a trivially-rejected under-call: any competent model integrates the severity and picks inpatient, and inpatient is ALSO the "thorough/safe" default, so the trap aligns with the model's natural bias instead of fighting it. There is no genuine clinical ambiguity to exploit, and the world is fixed (cannot make the case borderline). This axis is unsalvageable as a floor here. Hardening the draft's observation framing will not change the fact that the right answer is obvious.

## The structural finding (consistent across KM07 + KM08)
Variety-first divergent tasks on this world CLEAR (KM07 referral, KM08 inpatient-vs-obs ~0.96), they do not floor. The deep floors are banked in KM02-KM06 + KM05/06 (the unverified-self-report -> premature-action judgment traps and the cold fabrication). Abi's variety ask and Alexander's no-moderate (must-bite) rule collide on the 8th task: a genuinely-divergent 8th tends to be too easy; a 8th that bites tends to reuse a spent mechanism / the draft-and-finalize wrapper.

## Next-decision options (pending user/pod)
- A. KM08 -> GABAPENTIN judgment trap (verified-strong, a REAL sub-60 floor; physician-produced; distinct neuro-analgesic capability). Draft-and-finalize wrapper, but variety is already carried by KM07. DEPTH-first 8th; satisfies no-moderate. RECOMMENDED if an 8th must bite.
- B. One more divergent swing: Patient Safety RCA (single-cause propagation might bite, but likely clears too).
- C. Ship the suite at 7 (KM01-07); drop the 8th; escalate to Abi that inpatient-vs-obs structurally can't floor on this chart.
- D. Escalate the variety-vs-depth conflict to Abi before building anything else.

v3 set retained at platform/task8/current/ (too-easy; not shippable as-is). Build: build-docx-km08-status-v3.py.

---

## (Superseded) v3 staged - too easy in pilot
Status (6/9, v3 INPATIENT-VS-OBSERVATION - staged, then piloted TOO EASY): KM08 was an admission INPATIENT-VS-OBSERVATION STATUS DETERMINATION. Genuinely divergent but the case is unambiguously inpatient, so it cleared at ~0.96. See diagnosis above.

## Why v3 (the divergence fix)
User feedback (6/9): v2 physician med-plan was still too close to KM01 (both physician multi-hazard medication adjudication). User chose, from unused world-supported physician workflows, INPATIENT VS OBSERVATION DETERMINATION (P1, unused). This is a different KIND of physician work product: a status/utilization determination, not a clinical disposition note. Distinct artifact + cognitive task + capability, shared with no other task.

## v3 mechanism (judgment trap, draft attribution)
Admission day HD1 05/18. Mounted draft leans OBSERVATION (superficially-reassuring read); correct = INPATIENT given sepsis physiology (T 100.3, HR 104, WBC 15.6 + left shift) + AKI on CKD3 (Cr 2.62 vs 1.6-1.8, K 5.1) + AMS + intensity of service (IV renal-dosed abx, cautious fluids vs HFrEF, cardiorenal holds + monitoring, multi-consult) + expected >2 midnights. Floor = finalize observation; catch = inpatient with SI/IS rationale. Fair via draft attribution, plain prompt, no reconcile clause. Substrate verified on ed_provider_assessment + ed_triage bytes. Self-contained (two-midnight / SI-IS reasoning is pre-cutoff; grader requires no proprietary criteria-set name). Build: build-docx-km08-status-v3.py.

## Staged set: platform/task8/current/
prompt-task8-v3.txt, admission_status_determination_draft_05182026.docx, golden-KM08-v3.docx, grader-guidelines-task8-v3.txt (Sang five-block, central = observation under-call, names golden-KM08-v3.docx), RUN-INSTRUCTIONS.md (workflow type at top = Inpatient vs observation determination). Author = Elian Vossmere MD (admitting hospitalist), physician-produced.

## Build hygiene (RENDERED + viewed this time - the lesson from the docx-standard episode)
Both DOCX: Mode A clone of KM02 bases; styles byte-identical; fingerprint clean; 3-row band; Arial; metadata scrubbed; ZERO synthetic tokens (checked ALL xml parts incl footers); zero em/en/arrow/asterisk/bracket; no off-world names; dates 05/18 + DOB only. RENDERED to PDF/PNG and visually confirmed proper banner/band/sections/signature; draft leans observation, golden assigns inpatient.

## DOCX-standard lessons logged (do not repeat)
1. RENDER and VIEW every task DOCX before staging - byte checks alone missed nothing here but the v1 synthetic footer and the KM07 Service field were caught only by reading the runbook + rendering.
2. Scan ALL xml parts (footers/headers), not just document.xml, for synthetic/meta tokens (v1 miss).
3. Clone the KM02 base, NOT a raw world file (initial-med-rec base carried the synthetic footer + risked a 2-row band per runbook item 12).
4. Sandbox/Windows sync race can TRUNCATE a file written via the Edit tool mid-line; for build scripts, write via bash heredoc and run in the same bash session.

## Archived
v2 physician med-plan (too close to KM01): platform/task8/archive/2026-06-09-v2-physician-medplan-too-close-to-km01/. v1 pharmacist packet: git history + earlier guidance snapshot.

## Upload sequence (Alexander operates)
1. Workflow type = Inpatient vs observation determination. 2. Prompt. 3. Mount the determination draft. 4. Golden. 5. Grader. 6. Task AutoQC. 7. Pilot (status call: observation = failure, inpatient = catch). Then FA/GA -> 3 PLs.
Boundaries: no upload/AutoQC/agent-run without explicit Alexander authorization for that exact step.

---

## (Superseded) v2 PHYSICIAN med-plan - too close to KM01, archived
Status (6/9, v2): KM08 converted from pharmacist plan to PHYSICIAN pre-discharge medication plan. Rejected by user as too close to KM01. Replaced by v3 above.

## Task AutoQC (v1) returned TWO fails; both fixed in v2
1. All Tasks Physician-Produced (FAIL): v1 pharmacist deliverable (Ezekiel Marlott PharmD) matched the dimension's FAIL example. FIX (user chose "convert to physician-authored"): rebuilt as a physician pre-discharge medication plan, author = hospitalist Elian Vossmere, MD; prompt/draft/golden/grader/letterhead all physician voice; zero pharmacist references.
2. Meta-Language / synthetic footer (FAIL): v1 cloned the initial-med-rec base whose footer carried "Synthetic training document". FIX: rebuilt from the CLEAN KM02 base; footer now "Pre-Discharge Medication Plan"; zero synthetic tokens. (My earlier hygiene check missed it because I only scanned document.xml, not footer1.xml - lesson: scan ALL xml parts incl footers/headers.)
   - WORLD-LEVEL FLAG (separate, needs user): six existing world files still carry the synthetic footer (admission_history_and_physical, cardiology_consultation, hospitalist_progress_hd1_hd2, initial_medication_reconciliation_note, nursing_observation_flowsheet_summary, problem_list_history_snapshot). Verify on the LIVE world; if affected it is a world-canon scrub (authorization + re-sync), separate from KM08. KM02-06 passed their AutoQC, so the live files may be clean and only the local upload/filesystem copies are stale - user to confirm on the platform.

## v2 build (current)
build-docx-km08-physician-v2.py -> Mode A clone of KM02 bases. Both DOCX fingerprint-clean, metadata scrubbed, zero synthetic/pharmacist/em/en/arrow/asterisk/bracket, clean footer, valid. Author Vossmere MD. Dates 05/23 (HD6), 05/24 (discharge), DOB. WORKFLOW TYPE = Treatment Plan Documentation for Chronic Disease Management (P0, reuse of KM06's - allowed). Mechanism UNCHANGED: same five-hazard stack (metformin restart / correctional-insulin-home / gabapentin-full-dose / cardiorenal-restart / bone-health-closure), all verified chart-contradicted; golden holds all five; grader Sang five-block cumulative (2+ propagated = low).

## CAPABILITY-ADJACENCY FLAG (2.106) - carried in RUN-INSTRUCTIONS for Abi/Sang
Losing the pharmacist role makes KM08 a physician multi-hazard medication-adjudication task, adjacent to KM01. Distinct on hazard set (no shared hazard) + artifact/care-moment (forward pre-discharge PLAN vs discharge med-rec reconciliation). Droppable if the pod judges it too close to KM01; structural variety carried by KM07. Difficulty: clearer ~0.85-0.90, not a floor.

## v1 history (pre-conversion)
Original pharmacist packet (Ezekiel Marlott PharmD, cloned from initial-med-rec base) is in git history + task8/guidance/ was overwritten with the v2 physician set. The footer-only-fixed v1 pharmacist DOCX existed transiently before the physician rebuild.

---

## (v1 review, superseded) Status (6/9, REVIEWED + STAGED): planner-built pharmacist packet reviewed/verified/staged. Superseded by v2 physician conversion above after Task AutoQC flagged pharmacist authorship + synthetic footer.

## Review verdict (6/9): SHIP. Packet is well-built and fair.
Mechanism = stacked-unsafe-rec (KM01 family) in a CLINICAL PHARMACIST voice (new role + artifact + mechanism). Completion genre, HD6 05/23 pre-discharge pharmacist medication-therapy plan. Draft stacks five chart-contradicted moves; golden holds all five.
- All five stack legs VERIFIED chart-contradicted on the bytes: metformin "HELD HD1-HD6 (AKI)"; correctional lispro "per protocol" inpatient-only; gabapentin "held or reduced (sedation/fall-risk)"; cardiorenal held + nephrology "does not declare ready for full simultaneous restart"; bone health "Alendronate NOT administered inpatient, reconcile" + M81.0 active.
- DOCX hygiene PASS: styles.xml + fontTable.xml byte-identical to the initial-med-rec world base; Arial only; both valid (45 paras / 3 tables, symmetric); core metadata scrubbed; app.xml Company/Manager empty; zero synthetic/off-world/em/en/arrow/asterisk/bracket; dates 05/23, 05/24, DOB only. Author Ezekiel Marlott PharmD = in-world.
- Grader = Sang five-block, central = cumulative stack (2+ propagated hazards -> low), names golden-KM08-v1.docx. Prompt = clinical-pharmacist completion (new role).

## Alignment fixes applied by Claude
1. WORKFLOW TYPE moved to the TOP of RUN-INSTRUCTIONS (standing user rule) = Inpatient Pharmacotherapy Management (P1, unclaimed).
2. Added an HONEST FLAG for Abi: KM08 still uses the draft-and-finalize wrapper (needed for stack-attribution fairness); variety = role + mechanism + artifact, while KM07 is the task that fully breaks the wrapper. From-scratch pharmacist-plan alternative noted but not recommended (weakens the stack). Kept the draft version.

## Difficulty expectation
Built for VARIETY, not depth: expect a KM01-class clear ~0.85-0.90, NOT a floor. Read hazards-propagated per run (2+ = scored failure). If it clears too cleanly, tighten one or two DRAFT baits only - do not touch the grader, no reconcile clause.

## Staged set: platform/task8/current/
prompt-task8-v1.txt, draft_task8.docx, golden-KM08-v1.docx, grader-guidelines-task8-v1.txt, RUN-INSTRUCTIONS.md (workflow type at top). Originals preserved in task8/guidance/.

## Upload sequence (Alexander operates)
1. Workflow type = Inpatient Pharmacotherapy Management. 2. Prompt. 3. Mount draft_task8.docx. 4. Golden. 5. Grader. 6. Task AutoQC. 7. Pilot (read hazards-propagated). Then FA/GA -> 3 PLs.
Boundaries: no upload/AutoQC/agent-run without explicit Alexander authorization for that exact step.

## Working spec (provisional, pending guidance + a build go-ahead)
Task 8 = INPATIENT PHARMACIST MEDICATION-THERAPY PLAN (variety-first, answers Abi's no-draft-and-finalize tip).
- New ROLE (clinical pharmacist), new ARTIFACT (medication-therapy plan), new MECHANISM in this world (stacked-unsafe-rec, KM01 family - returns but in a new role).
- Structure: a plan that makes several individually-tempting but unsafe moves at once; the correct plan holds each pending its documented condition. Candidate stack legs (verified substrate exists for each):
  - restart metformin on the single resolved creatinine (nephrology holds it),
  - return gabapentin to full nightly dose despite the inpatient sedation/falls reduction (Morse 65),
  - resume a held cardiorenal agent (sac/val, spironolactone, empagliflozin, furosemide - all held, staged restart),
  - treat bone health as closed (alendronate "NOT administered inpatient, reconcile"; M81.0 open).
- Fairness: chart-grounded (each leg contradicted by the record) + plain prompt; clears the gate fairly the way KM01 did (~0.87). EXPLICITLY a clearer that adds role + mechanism diversity, NOT a floor. Deep floors are banked in KM02-KM06.
- WORKFLOW TYPE (provisional): Inpatient Pharmacotherapy Management (P1, unclaimed, count 0). Goes at the top of RUN-INSTRUCTIONS per standing rule.
- Alternative (lighter wrapper-break, if preferred): SOAP note "write the note from the record" from scratch. The pharmacist plan is the stronger variety move (changes role, artifact, and mechanism at once).

## Substrate already verified on bytes (6/9)
gabapentin 300 nightly reduced inpatient for sedation/fall-risk (MAR + med-rec note "sedation/fall-risk reassessment is a clinical question"); metformin + empagliflozin held; cardiorenal agents held with staged restart (nephrology); bone health open (alendronate not administered inpatient, reconcile; M81.0 named repeatedly); all in CKD3. Will re-verify each chosen stack leg before building.

## Folder map
- task8/guidance/      <- USER drops guiding docs here; read before authoring.
- task8/design/        <- design notes / plan.
- task8/fa-ga/         <- FA/GA after pilot.
- task8/preference-labeling/  <- 3 PLs after FA/GA.
- task8/runs/          <- gitignored run exports.
- platform/task8/current/   <- upload set (prompt, golden, grader, RUN-INSTRUCTIONS).
- platform/task8/archive/   <- superseded versions.

## Next steps
1. User adds guidance docs under task8/guidance/.
2. Claude reads guidance + re-verifies the chosen stack legs on the bytes.
3. Build packet (prompt + golden + grader + RUN-INSTRUCTIONS with workflow type at top), Mode A clone, byte-verify.
4. Alexander uploads -> Task AutoQC -> pilot. Then FA/GA -> 3 PLs.

Boundaries: no authoring/build/upload/AutoQC/agent-run without explicit Alexander authorization for that exact step. Hold until guidance docs are in.
