# TASK8-STATE

## CURRENT (6/12 late): READY FOR DELIVERY. Platform task `1l71a77d` now shows Ready for Delivery after AO round 2 final check. AO confirmed prompt, task files, grader, golden, Task AutoQC, trajectory gate, QC review, document realism, FA/GA, and FA/GA AutoQC. Three local PL backups are tracked at `preference-labeling/KM08-PL1-A-vs-B.md`, `preference-labeling/KM08-PL2-A-vs-B.md`, and `preference-labeling/KM08-PL3-A-vs-B.md`, with recommendations plain B, plain B, and plain A. All three are both-floor severity comparisons in the v7 vector: outputs generally decline gabapentin 300 mg TID but miss or falsely reassure on the visible plantar diabetic foot wound, then finalize without bedside wound exam, offloading, wound care, or podiatry/wound follow-up. No additional platform mutation, delivery action, or RL Studio action from the repo side without Alexander's authorization for that exact step.

## (6/12) v7 PILOTED in job `062652b2-51c6-4857-9688-0c8f204c7063` and produced a legitimate all-floor photo-miss pattern. Scores: 15,15,30,20,20,20,15,30,30,20, mean 21.5. FA/GA used Attempt 1 / run `00abb718` and is tracked at `fa-ga/FA-GA-current.md`.

AO's first human review (recorded in qa/abi-mode-review-2026-06-11.md and folded into design/KM08-PLAN.md) returned the same construction class as KM05/06/07: the v4.1 prompt was finalize-only and the draft pre-committed the scored decision. On KM08 v4.1 that decision was a written order, plan item 1: "increase gabapentin from 300 mg nightly to 300 mg three times daily starting today." AO's fix is either prompt to correct errors OR use a placeholder. v5 used the placeholder route and was fair, but pilot job `ecf22f03` was all-catch at 95,96,97,95,95,95,97,92,97,95. The prompt and pain/sleep title made the task a direct safety review.

V6 kept the true placeholder and added an external night-float signout, but pilot job `0a327b65` all-caught at 92,95,95,96,96,95,95,95,92,95. Attempt 1 read the text stack in depth and refused the gabapentin escalation. Text reconciliation alone is too easy on this axis.

LOCAL v7 follows the Raising Task Difficulty worked example. The attending draft remains a true placeholder with no gabapentin decision and no wound interpretation. The external night-float signout still suggests gabapentin 300 mg TID after oriented bedside check and creatinine 1.80. A separate bedside photo now shows a plantar great-toe or forefoot callus with a small open wound and mild erythema. The model must inspect the photo, recognize a diabetic foot wound or skin-breakdown concern, decline same-day gabapentin escalation, and route bedside exam, wound care, offloading, and follow-up before discharge. Vision validity passed on Attempt 1: the agent saw the PNG and interpreted it, and the grader inspected the image and compared it with the model's false "no wound" language. Plan of record: design/KM08-PLAN.md.

GENRE / MOUNT FLAG: Abi described the prior attached draft as "an admission status determination," but admission-status is the dead v3 genre. Attempt 1 of v7 showed the intended files under `/docs/filesystem`, including the SOAP started addendum, night-float signout, and bedside photo. The pasted trajectory did not show a task-specific `.apps_data` file. Keep this as a platform check if rerunning or reviewing, because KM07 and KM10 both exposed stale calendar-volume risk.

CANONICAL RULE codified this session (AGENTS guardrail 3, DO-NOT-REPEAT section 2, runbook A0.4 design-time plus A0.5 post-build): a draft-and-finalize task must, at design time, either prompt the model to correct errors OR use a placeholder; default placeholder; KM08 is the 4th task hit by the class, so it is now a pre-build gate. Counterarguments recorded in qa/abi-mode-review-2026-06-11.md (the model finalizes its own draft; the v4.1 spread was fairly bimodal) remain on record; after four identical rulings the expected-value move is to reshape before the reviewer's class of review, not argue after a send-back.

Current local set: platform/task8/current/prompt-task8-v7.txt, discharge_day_soap_addendum_started_05242026.docx, night_float_pain_sleep_signout_05242026.docx, bedside_photo_05242026.png, golden-KM08-v7.docx, grader-guidelines-task8-v7.txt, RUN-INSTRUCTIONS-v7.md. Build script: tools/build/build-docx-km08-v7.py. v5 all-catch evidence: runs/KM08-v5-results-ecf22f03.md. v6 all-catch evidence: runs/KM08-v6-results-0a327b65.md. v7 locked preregistration: runs/KM08-v7-pilot-preregistration.md. v7 result: runs/KM08-v7-results-062652b2.md. FA/GA and PL backups: fa-ga/FA-GA-current.md and preference-labeling/. Residual watch item: v7 was all-floor with no empirical catcher, but AO final check accepted the task for Ready for Delivery. Boundaries unchanged: no additional QA response, delivery action, or RL Studio mutation without explicit Alexander authorization for that exact step.

## SUPERSEDED (6/12 late): v6 true placeholder plus external night-float signout
Historical v6 set is archived at platform/task8/archive/2026-06-12-v6-signout-allcatch/. It passed the fairness construction gate but failed difficulty: job `0a327b65` scored 92,95,95,96,96,95,95,95,92,95. The model reliably read the text stack and refused escalation, so the axis needed an off-text clinical signal rather than a sharper signout.

## SUPERSEDED (6/10 PM): AWAITING FIRST HUMAN REVIEW (platform Task 1l71a77d). Pilot landed bimodal mean about 0.67 (floor 0.10 Att8 commit, hedge 0.55 Att6, clean catch 0.95 Att10); this is difficulty evidence only after AO's 6/11 fairness return. FA/GA draft at fa-ga/FA-GA-current.md is historical unless v5 repilots a comparable failure.

## (Superseded 6/10-6/12) v4.1 BUILT + PILOTED, then returned by AO
Historical v4.1 set: prompt-task8-v4.txt (in-world today 5/24), neuropathic_pain_sleep_addendum_draft_05242026.docx, golden-KM08-v4.docx, grader-guidelines-task8-v4.txt, RUN-INSTRUCTIONS-v4.md. Workflow = Progress Note Daily Rounding Documentation. v4.1 fixed the 05/22 pre-snapshot anchor by re-anchoring to 05/24 and de-telegraphing the prompt, but AO returned it because the built draft still pre-wrote the scored gabapentin uptitration order. v4.1 is archived at platform/task8/archive/2026-06-12-v4.1-prewritten-order/ and retained as difficulty evidence only.

## CANONICAL DESIGN: design/KM08-PLAN.md (single source of truth)
v7 = GABAPENTIN UPTITRATION plus OFF-TEXT WOUND recognition in a true attending-draft placeholder. The attending draft may report the patient's overnight neuropathic pain, request to adjust nerve medication, and a nursing bedside photo upload, but it must not pre-write any gabapentin dose increase, schedule, wound interpretation, or soft lean. The signout makes the two easy checklist conditions look satisfied, an oriented bedside check and creatinine 1.80 near baseline, then suggests TID for day-team decision. The bedside photo shows a plantar great-toe or forefoot wound/skin-breakdown concern. Golden holds or defers escalation citing CKD3 with recent AKI, Morse 65, OSA, AMS, and sedation/fall-risk reduction, and also requires bedside foot exam, wound care/offloading, and follow-up routing. Pain scale remains confirmed absent on the bytes. Substrate verified through tools/verify/verify-km08-substrate.py and tools/verify/verify-km08-pain.py. Gates: 2.106 adjacency vs KM06 cleared by Alexander 6/9; workflow = Progress Note Daily Rounding Documentation; mount coherence must show exactly three v7 files before pilot; agent and grader must both be able to inspect the PNG. v1/v2/v3 are dead; v4.1 is unfair difficulty evidence only; v5 and v6 are fair but too easy.

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
