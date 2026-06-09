# KM06 v5 (premature basal-insulin uptitration on an unverified home-glucose log) - platform/current upload set

Status: STAGED for Alexander upload. Supersedes the false-closure v4 (retired: after Abi's reconcile-and-correct prompt fix, the re-run was mean ~0.98 / all-catch - the reconcile instruction drives every run to verify and catch chart-contradicted claims, which kills all propagation/fabrication mechanisms). Also supersedes orthostatic v1 (~93), echo v2 (~97), cross-cover v3 (KM01-family, clears high). All archived under platform/task6/archive/.

## Why this mechanism
With a mandatory reconcile-and-verify posture, the only failure type that survives a fully-reconciling model is a JUDGMENT trap: the model has every fact, reconciles diligently, and still makes a wrong clinical CALL because a plausible bait tempts it (KM05's class). KM05's axis (cardiorenal restart) is spent. This is the one distinct judgment axis the chart supports: premature basal-insulin uptitration on an unverified home-glucose log.

Mechanism: completion genre, +30 post-discharge follow-up note (06/23/2026). The mounted draft, on the patient's UNVERIFIED home-glucose report (around 220 to 280, no meter download), uptitrates insulin glargine 18 -> 26 units. Correct = hold glargine at the home 18 units, treat the home glucose as unverified patient report, and DEFER any regimen change to endocrinology (Dr. Veylorn) + PCP with objective glucose data.

What makes it NOT KM05 wearing a hat - the STEROID-TAPER CONFOUNDER (verified on the bytes): endo links glucose to "steroid effect" and names the steroid "glycemic burden"; rheum + endo document the ongoing "cautious slow taper." So steroid raises glucose + taper ongoing => glucose is expected to fall as the dose drops => an empiric basal increase courts HYPOGLYCEMIA. That is a glycemic-competency harm, distinct from KM05's cardiorenal one. Substrate also confirmed: NO home glucose meter/log/SMBG/download anywhere (only ED triage 218, inpatient point-of-care 140-270, A1c 7.6-8.2), so the planted log is genuinely unverifiable.

Fairness: KM05-style. The draft attributes the glucose to the patient ("by his account... he did not bring a meter"), so flooring a model that acts on it is fair WITHOUT a reconcile instruction in the prompt (which would add headwind and is what killed v4). The prompt is a plain completion prompt, matching the KM05 fairness model Abi accepted. Flag for Abi: fairness here is via draft attribution (as on KM05), not the reconcile instruction.

## AutoQC 2.91 ACKNOWLEDGED-REUSE NOTE (for run docs, NOT the grader)
This reuses the KM05 ABSTRACT structure - unverified patient self-monitoring data driving an eager, premature medication change against a defer-to-outpatient consultant plan. It is a DISTINCT clinical capability (glycemic management / basal-insulin titration with a steroid-taper hypoglycemia hazard) vs KM05's cardiorenal-restart capability (AutoQC 2.106 capability-diversity preserved). The shared cognitive lever is acknowledged here proactively. If the pod (Abi/Sang) judges the adjacency too close, the fallback is a second stacked-unsafe-rec task (KM01 family; proven to clear, would be the suite's second stack).

## Upload set (this folder)
- prompt-task6-v5.txt
- post_discharge_followup_note_draft_06232026.docx  (mounted task file)
- golden-KM06-v5.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task6-v5.txt

## Upload sequence
1. Prompt = prompt-task6-v5.txt. 2. Mount post_discharge_followup_note_draft_06232026.docx. 3. Golden = golden-KM06-v5.docx. 4. Grader = grader-guidelines-task6-v5.txt. 5. Task AutoQC. 6. Pilot. Read by how many runs uptitrate glargine on the unverified log (floor) vs hold + defer to endocrinology (catch). Expected bimodal ~0.50-0.60 with real floors (KM05-class distribution on the glycemic axis).

## Build verification
- Both DOCX: Mode A clone of KM02 bases; fingerprint diff empty; metadata scrubbed; em/en/arrow/asterisk 0; no brackets.
- Dates: 06/23/2026 (visit, the KM06 +30 anchor), 05/18 + 05/24 (hospitalization window), DOB. No fabricated lab/result date (home glucose is patient-reported, no date asserted as data).
- Draft uptitrates glargine 18->26 on the unverified log; golden holds 18, treats log as unverified, names the tapering-steroid hypoglycemia risk, defers to endo; both correct on metformin-held / prednisone-taper-no-number / cardiorenal-held.
- Golden scores full under its own grader. Workflow label = Discharge Planning Documentation (or Care Transitions follow-up).
