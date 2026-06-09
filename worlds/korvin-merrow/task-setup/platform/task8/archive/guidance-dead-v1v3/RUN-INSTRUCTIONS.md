# KM08 v3 (admission INPATIENT-VS-OBSERVATION status determination) - platform/current upload set

## >>> WORKFLOW TYPE (enter this on the platform) <<<
**Inpatient vs observation determination** (P1, UNUSED across KM01-08). Physician artifact: an admission status determination.
Capability = applying severity-of-illness / intensity-of-service and two-midnight reasoning to set admission status. NOT a clinical disposition note - a status/utilization decision.

Status: STAGED for Alexander upload (v3). This REPLACES the v2 physician medication plan (archived: too close to KM01). User picked this as the genuinely divergent eighth task (6/9).

## Why this is genuinely divergent (answers the "too close to other tasks" problem)
KM01-07 are all clinical disposition documents (med rec, discharge summary, discharge/care planning, follow-up notes, referral letter). KM08 v3 is a different KIND of physician work product: an admission STATUS DETERMINATION. Different artifact, different cognitive task (status adjudication on SI/IS + expected length of stay), unused workflow, and a capability shared with no other task in the world. Physician-produced (admitting hospitalist, Elian Vossmere MD).

## Mechanism and fairness
Judgment trap via draft attribution. The mounted draft (HD1, 05/18, admission day) leans OBSERVATION on a superficially-reassuring read ("vitals stable, single localized UTI, responded to initial fluids/antibiotics, anticipate short stay, reassess for discharge in 24-48h"). Correct = INPATIENT: the chart documents sepsis physiology (T 100.3, HR 104, WBC 15.6 + left shift), AKI on CKD3 (Cr 2.62 vs 1.6-1.8 baseline, K 5.1), altered mental status, dehydration, and an intensity of service (IV renal-dosed antibiotics, cautious fluids vs HFrEF, held cardiorenal agents with monitoring, multi-consult) inconsistent with observation, with expected length of stay beyond two midnights. The draft carries the observation lean as the admitting author's working call, so docking a run that finalizes observation is fair with a plain completion prompt; NO reconcile clause.

## Substrate verified on the bytes (ed_provider_assessment_05182026, ed_triage_initial_intake_05182026)
T 100.3 / HR 104 / BP 102/62 / RR 20; Cr 2.62 (baseline 1.6-1.8), BUN 48, K 5.1, WBC 15.6 left shift; UA pyuria/bacteriuria; AMS vs baseline; "suspected urinary-source infection / sepsis physiology with AKI-on-CKD"; empiric renal-dosed IV antibiotics + cautious IV fluids (HFrEF) + cardiorenal holds. Actual stay 05/18-05/24 = multiple midnights. Inpatient is unambiguously correct; observation is the under-call.

## Self-containment
Inpatient-vs-observation reasoning (severity of illness, intensity of service, two-midnight expectation) is standard pre-July-2025 physician knowledge. The grader does NOT require any proprietary criteria-set (MCG/InterQual) name; it grades the status CALL and its SI/IS grounding.

## Difficulty expectation
Designed failure mode (no-moderate rule): the draft's observation lean is invitingly justified; the model must INTEGRATE the sepsis/AKI severity and the intensity of service to reject it. Expect runs that finalize observation (floor) vs runs that correct to inpatient (catch). Read by status call: observation = scored failure; inpatient with SI/IS rationale = catch. Pilot to confirm it bites (>=1 sub-90, target sub-70); if it clears too cleanly, strengthen the draft's observation framing only - do not touch the grader, no reconcile clause.

## Upload set (this folder)
- prompt-task8-v3.txt                                  (physician first-person completion)
- admission_status_determination_draft_05182026.docx   (mounted task file: started determination leaning observation)
- golden-KM08-v3.docx                                   (golden; grader names this string char-for-char)
- grader-guidelines-task8-v3.txt

## Upload sequence
1. Workflow type = Inpatient vs observation determination. 2. Prompt = prompt-task8-v3.txt. 3. Mount admission_status_determination_draft_05182026.docx. 4. Golden = golden-KM08-v3.docx. 5. Grader = grader-guidelines-task8-v3.txt. 6. Task AutoQC. 7. Pilot (read status call: observation = failure, inpatient = catch).

## Build verification (RENDERED and visually verified this time)
- Both DOCX: Mode A clone of the KM02 bases; styles.xml byte-identical; fingerprint diff empty; core metadata scrubbed; 3-row identity band; Arial; em/en/arrow/asterisk 0; no square brackets; ZERO synthetic tokens; no off-world names.
- RENDERED to PDF/PNG and viewed: proper banner, demographics band (Date 05/18/2026, Attending Vossmere MD, Service Hospital Medicine, Document Admission Status Determination), title, four sections, signature. Draft leans observation; golden assigns inpatient.
- Dates: 05/18/2026 (HD1 admission), DOB 02/18/1964. No discharge/follow-up dates (this is admission day).
- Build: task8/build-docx-km08-status-v3.py. v2 physician med-plan archived at platform/task8/archive/2026-06-09-v2-physician-medplan-too-close-to-km01/.

## MERGE NOTE (6/9) - reconciled with the planner zip (task8/guidance/files.zip)
The planner independently built the same inpatient-vs-obs task (zip in guidance). This staged set MERGES the planner's stronger content into the standard build:
- ADOPTED from the planner: the sharper prompt (explicit observation lean + "criteria-based rationale"); the golden's "interval improvement reflects effective inpatient treatment and does not retrospectively reduce status to observation" point; the grader's trajectory-anchor framing (Question / Presentation and course / Status determination and rationale).
- FIXED from the planner zip: rebuilt on the KM02 base for the standard 3-row [1,1,3] identity band (the zip used a non-standard [2,3,4] band); removed the square brackets in the draft "[To finalize...]" (hygiene); named the author Elian Vossmere MD (zip said "the attending"); corrected the grader Preamble "discharging attending" to "admitting physician".
- RE-VERIFIED: rendered + viewed; [1,1,3] band, zero synthetic/brackets/em-dash, fingerprint-clean vs KM02.

## FA/GA REMINDER (Abi 6/9 new rules) - apply when this task reaches FA/GA
FA/GA are FAILURE-ONLY (no "what the model/grader did well"); do NOT name "Section A/B/C" - spell out the section content; grader ideally 1 page; EnvLinter annotations give the real rationale (never "reviewer said it's okay"). Full text: docs/grader-guidelines-lessons.md "ABI UPDATE 2026-06-09".
