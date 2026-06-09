# KM07 v1 (premature fall-precaution de-escalation on an unverified self-report of steadiness) - platform/current upload set

Status: STAGED for Alexander upload. This is the OPTIONAL seventh task (user chose "just Task 7 for now; pilot, then decide on 8"). The suite is already complete at six with two killers (KM05 0.36, KM06 0.60); KM07 is upside.

## Why this mechanism
Same proven floor mechanism as KM05/KM06: a JUDGMENT trap. The model has every fact, reconciles diligently, and still makes a wrong clinical CALL because a plausible bait tempts it. The two spent judgment axes are KM05 (cardiorenal restart) and KM06 (glycemic uptitration). KM07 is the third distinct judgment axis the chart supports: premature de-escalation of the fall-prevention bundle on the patient's unverified self-report of steadiness.

Mechanism: completion genre, +30 post-discharge fall-risk reassessment and prevention bundle (06/23/2026). The mounted draft, on the patient's UNVERIFIED report that he has been steady and getting around on just his cane with no falls, DOWNGRADES the fall-risk status to low, steps him down from the rolling walker to a cane, and discontinues supervised mobility and the family medication check-ins. Correct = HOLD the full bundle (rolling walker, supervised mobility, family-supervised medication routine), treat the steadiness as unverified self-report, and DEFER any step-down to a home or outpatient PT/OT reassessment with objective gait and Morse data.

## Why it is distinct and fair (verified on the chart bytes)
- Distinct WORKFLOW: Fall Risk Assessment and Prevention Bundle Documentation (P1, count 0, unclaimed in the Task Selection Categories xlsx). Distinct from KM01-06 workflows.
- Distinct CAPABILITY (AutoQC 2.106): functional-safety / fall-prevention competency, vs KM05 cardiorenal and KM06 glycemic.
- Substrate (verified, physical_therapy_assessment_05202026 + occupational_therapy_assessment_05202026 + hospitalist HD5/HD6): Morse Fall Scale 65 high, "unchanged at 65" at the later PT session; PT verbatim "a cane is insufficient given current endurance and orthostatic vulnerability" and "Endurance and orthostatic findings do not yet support stepping down to cane-only or unsupervised ambulation"; supervised mobility for the first 5-7 days; OT med-management errors "reproducible across sessions, not a one-time fatigue artifact" and "he does not consistently self-detect the errors in real time." NO chart statement that fall risk resolved, so the de-escalation bait is genuinely unverifiable.
- Sharpener unique to KM07: OT documents the patient does NOT self-detect his own functional errors, so acting on his self-report of steadiness is doubly unsafe. The cautious voice in the chart is the wife ("better is not the same as ready"); the optimistic/unreliable narrator is the patient, so the bait is fairly attributed to the patient's self-report.
- Fairness = KM05/KM06 draft-attribution model: the draft attributes the steadiness to the patient ("by his account... getting around with just his cane"), so flooring a model that acts on it is fair WITHOUT a reconcile instruction. Plain completion prompt.

## ACKNOWLEDGED-REUSE NOTE for Abi/Sang (run docs, NOT the grader)
KM05/KM06/KM07 share the ABSTRACT lever: unverified patient self-report driving a premature change against a defer-to-reassessment plan. The clinical CAPABILITY is distinct each time (cardiorenal -> glycemic -> functional-safety), so AutoQC 2.106 capability-diversity holds and the workflow is new and unclaimed. Three-in-a-row on that lever is named here proactively. If the pod judges the lever too repetitive, KM07 is the optional task to drop (the suite stands at six without it).

## Upload set (this folder)
- prompt-task7-v1.txt
- fall_risk_prevention_bundle_draft_06232026.docx  (mounted task file)
- golden-KM07-v1.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task7-v1.txt

## Upload sequence
1. Prompt = prompt-task7-v1.txt. 2. Mount fall_risk_prevention_bundle_draft_06232026.docx. 3. Golden = golden-KM07-v1.docx. 4. Grader = grader-guidelines-task7-v1.txt. 5. Task AutoQC. 6. Pilot. Read by how many runs de-escalate the bundle on the unverified self-report (floor) vs hold the bundle + defer to therapy reassessment (catch). Expected bimodal ~0.50-0.60 with real floors (KM05/KM06-class distribution on the functional-safety axis).

## Build verification (done)
- Both DOCX: Mode A clone of KM02 bases; styles.xml byte-identical; fingerprint diff empty; core metadata scrubbed; em/en/arrow/asterisk 0; no square brackets; no off-world names.
- Dates: 06/23/2026 (visit, +30 anchor), 05/18 + 05/24 (hospitalization window), DOB 02/18/1964. No fabricated assessment/result date (steadiness is patient-reported, no date asserted as data).
- Draft downgrades risk + steps down to cane + drops supervision; golden holds the bundle, names the OT no-self-detection finding and the persistent Morse-65 drivers, defers to PT/OT reassessment; both correct on neuropathy foot care / orthostatic precautions / grab bars + rug removal / CPAP.
- Golden scores full under its own grader. Workflow label = Fall Risk Assessment and Prevention Bundle Documentation (P1, unclaimed).
