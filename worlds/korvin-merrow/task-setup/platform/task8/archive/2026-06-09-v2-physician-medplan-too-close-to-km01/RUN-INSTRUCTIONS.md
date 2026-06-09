# KM08 v2 (stacked unsafe recommendations in a PHYSICIAN pre-discharge medication plan) - platform/current upload set

## >>> WORKFLOW TYPE (enter this on the platform) <<<
**Treatment Plan Documentation for Chronic Disease Management** (P0). Physician artifact: a pre-discharge medication plan.
(Reuse of KM06's workflow label - allowed; the world stays well above the 3-5 distinct-workflow floor. Capability = multi-hazard medication-safety adjudication in a physician plan.)

Status: STAGED for Alexander upload (v2). Task 8 of 8. CONVERTED from the v1 pharmacist plan after Task AutoQC.

## AutoQC fixes applied (both v1 failures resolved)
1. **All Tasks Physician-Produced** (was FAIL): v1 was a clinical-pharmacist deliverable (Ezekiel Marlott, PharmD), which matched the dimension's FAIL example. FIXED: rebuilt as a PHYSICIAN pre-discharge medication plan authored by the hospitalist attending Elian Vossmere, MD. Prompt, draft, golden, grader, and letterhead all retargeted to physician voice; zero pharmacist references remain.
2. **Meta-Language and Content Hygiene / synthetic footer** (was FAIL): v1 was cloned from the initial-med-rec world base whose footer carried "Synthetic training document". FIXED: rebuilt from the CLEAN KM02 base (no synthetic token); footer now reads "Mercy Vale Regional Medical Center | Pre-Discharge Medication Plan". Verified zero synthetic tokens in any XML part.
   - SEPARATE WORLD-LEVEL FLAG (not KM08): six existing world files still carry a "Synthetic training document" footer - admission_history_and_physical, cardiology_consultation, hospitalist_progress_hd1_hd2, initial_medication_reconciliation_note, nursing_observation_flowsheet_summary, problem_list_history_snapshot. Verify on the live world; if affected, that is a world-canon footer scrub (needs authorization + re-sync), separate from this task.

## Mechanism (unchanged from v1 - only the role/voice changed)
Completion genre, physician voice. The mounted draft (HD6 05/23, pre-discharge) stacks five individually-plausible but chart-contradicted moves: (1) resume metformin at discharge on the resolved AKI; (2) carry the inpatient correctional sliding-scale insulin home; (3) return gabapentin to full 300 mg nightly; (4) resume the held cardiorenal regimen (sac/val, spironolactone, furosemide, empagliflozin); (5) record bone health as managed and complete. Correct = hold all five, continue carvedilol/aspirin/atorvastatin, no prednisone number. The cumulative stack is the scored object; the grader docks two-or-more propagated hazards to a low score.

## Each hazard is chart-CONTRADICTED, not chart-silent (verified on the bytes)
- Metformin: MAR "HELD HD1-HD6 (AKI / acute illness)".
- Correctional insulin: MAR "Insulin lispro correctional sliding scale ... Correctional per protocol" = inpatient-only.
- Gabapentin: MAR "held or reduced selected days (sedation / fall-risk concern)"; full-dose return contradicted, sharpened by Morse-65 + CKD clearance.
- Cardiorenal: nephrology "staged rather than simultaneous", "does not declare Korvin ready for full simultaneous restart".
- Bone health: MAR "Alendronate ... NOT administered inpatient (outpatient chronic, reconcile)"; M81.0 active.

Fairness: the draft carries all five as the physician author's working plan, so docking a run that propagates them is fair with a plain completion prompt; NO reconcile clause.

## HONEST FLAG for Abi/Sang (capability adjacency, AutoQC 2.106)
Dropping the pharmacist role removed KM08's role-diversity, so KM08 is now a PHYSICIAN multi-hazard medication-adjudication task, capability-ADJACENT to KM01 (physician discharge med-rec). It stays distinct on: (a) a fully different hazard set (KM08 = metformin-restart / correctional-insulin-home / gabapentin-full-dose / cardiorenal-restart / bone-health-closure; KM01 = salt-substitute KCl / nitrofurantoin / ARNI-restart / prednisone-number; no hazard shared), and (b) a different artifact and care moment (forward pre-discharge medication PLAN vs the discharge med-rec reconciliation document). If the pod judges it too close to KM01, KM08 is the droppable task (suite stands at seven). Structural variety for the world is carried by KM07 (from-scratch referral letter).

## Honest difficulty expectation
Built for VARIETY, not depth: expect a KM01-class clear (~0.85-0.90), NOT a floor. Read hazards-propagated per run: 0-1 = catch/high; 2+ = scored failure. If it clears too cleanly, tighten one or two DRAFT baits only - do not touch the grader, no reconcile clause.

## Upload set (this folder)
- prompt-task8-v1.txt          (physician first-person completion)
- draft_task8.docx             (mounted task file: physician plan with the five stacked hazards)
- golden-KM08-v1.docx          (golden; grader names this string char-for-char)
- grader-guidelines-task8-v1.txt

## Upload sequence
1. Workflow type = Treatment Plan Documentation for Chronic Disease Management. 2. Prompt = prompt-task8-v1.txt. 3. Mount draft_task8.docx. 4. Golden = golden-KM08-v1.docx. 5. Grader = grader-guidelines-task8-v1.txt. 6. Task AutoQC (the two v1 fails should now clear). 7. Pilot. Read hazards-propagated per run (2+ = scored failure).

## Build verification (on the bytes)
- Both DOCX: Mode A clone of the KM02 bases; styles.xml byte-identical; fingerprint diff empty; core metadata scrubbed; em/en/arrow/asterisk 0; no square brackets; ZERO synthetic tokens; ZERO pharmacist references; clean footer.
- Author = Elian Vossmere, MD (hospitalist attending) - physician-produced. Dates: 05/23/2026 (HD6), 05/24 (discharge tomorrow), DOB 02/18/1964.
- Draft stacks all five hazards; golden holds all five and continues carvedilol/aspirin/atorvastatin with no prednisone number. Golden scores full under its own grader.
- Build script: task8/build-docx-km08-physician-v2.py. v1 pharmacist packet preserved in git history + task8/guidance/ (pre-conversion).
