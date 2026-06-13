# KM08 - CANONICAL PLAN (single source of truth)
## Status: v7 PILOTED in job `062652b2` with all-floor visible-wound miss. FA/GA and three PLs complete per Alexander; awaiting final human review post PL.
## Last updated: 2026-06-12

> **Gate 0 (draft-completion fairness): OPENED by AO 6/11 and now canonical.** For any finalize-the-draft task, either the prompt tells the model to correct unsupported draft content, or the draft uses true placeholders for the model to complete from the record. KM08 v4.1 violated this because the draft pre-wrote the scored gabapentin uptitration order and the prompt only asked the model to finalize the note. v5 fixed fairness but piloted too easy in job `ecf22f03` (95,96,97,95,95,95,97,92,97,95). v6 kept the true placeholder and added an external night-float signout, but pilot job `0a327b65` all-caught at 92,95,95,96,96,95,95,95,92,95. v7 followed the Raising Task Difficulty worked example: keep the fair placeholder, keep the external signout, and add a realistic off-text bedside photo with a diabetic foot wound signal. Job `062652b2` landed 15,15,30,20,20,20,15,30,30,20 because models safely declined gabapentin escalation but missed or falsely reassured on the visible plantar wound.
> **Genre / mount mismatch status:** AO described the prior attached draft as an admission status determination, while local current had later pain/sleep addenda. Admission status is dead v3. Attempt 1 of v7 showed the intended files under `/docs/filesystem`, including `discharge_day_soap_addendum_started_05242026.docx`, `night_float_pain_sleep_signout_05242026.docx`, and `bedside_photo_05242026.png`. The pasted trajectory did not show a task-specific `.apps_data` file. Agent and grader vision passed on Attempt 1.

> **Gate 1 (2.106 adjacency vs KM06): CLEARED by Alexander 6/9.** Distinct capability accepted (sedating neuro-analgesic under CKD/OSA/falls/AMS vs glycemic management).
> **Gate 2 (workflow category): RESOLVED 6/10 against the Task Selection Categories sheet.** "Inpatient Clinical Progress Note Documentation" does NOT exist on the sheet (user-caught). Selected exact string: **Progress Note Daily Rounding Documentation** (P0, unused by KM01-KM07). "Ambulatory ... (SOAP Notes)" remains the outpatient category and does not apply.
> **Gate 3 (temporal anchor, added 6/10): RESOLVED by re-anchor.** The v4 plan anchored the encounter at HD4-HD5 (05/21-05/22), before the world snapshot (05/23/2026, latest world-file date) and violated the instruction-doc non-negotiable: the task encounter and deliverable must fall strictly after the world snapshot; a late-entry note or addendum documenting a pre-snapshot encounter does not qualify. Dead v3 (HD1 05/18) carried the same uncaught defect. **v7 keeps the 05/24/2026 discharge-day anchor.** The overnight complaint, night-float signout, and nursing photo arise 05/23 into 05/24, after the last chart entry. Substrate remains chart-true on 05/24: CKD3 with recent AKI (Cr peak 2.62, 1.80 on 05/23, baseline 1.6-1.8), Morse 65, OSA on home CPAP, intermittent confusion, MAR sedation/fall-risk holds, med-rec clinical-question line, diabetic neuropathy, and zero objective pain scale across all 26 files.

> **v4.1/v5/v6/v7 outcome:** v4.1 piloted bimodal but was unfair because the same-author draft pre-wrote the gabapentin uptitration order with a finalize-only prompt. v5 proved the pure placeholder was fair but too easy. v6 proved the external text signout was still too easy. v7 produced the fair off-text visible-wound miss in job `062652b2`; FA/GA and three PLs are complete per Alexander, and final review is pending.

> This is the ONLY live KM08 design doc. Everything else in `design/` is archived under
> `design/archive/` and must NOT be cited as current. If it is not in this file, it is not the plan.

---

## Version ledger (what was tried and killed - do not resurrect)

| Version | Mechanism | Outcome | Why dead |
|---------|-----------|---------|----------|
| v1 | Clinical-pharmacist stacked med-therapy plan | Killed pre-pilot | AutoQC: non-physician authorship + synthetic footer |
| v2 | Physician pre-discharge med plan (5-hazard stack) | Killed pre-pilot | Too close to KM01 (physician multi-hazard med adjudication) |
| v3 | Inpatient-vs-observation status determination | **Piloted, FAILED** | Mean ~96.4, zero sub-90; case is unambiguously inpatient = safe default = free clear (job 04270757) |
| v4.1 | Gabapentin uptitration on patient-reported pain, pre-written order | Piloted, returned by AO | Bimodal difficulty evidence, but unfair construction: finalize-only prompt plus same-author draft pre-wrote the scored order |
| v5 | Gabapentin uptitration from a true placeholder | Piloted too easy | Job `ecf22f03`, all 10 runs 0.92-0.97; axis became a direct safety review |
| v6 | True placeholder plus external night-float signout suggesting TID | Piloted too easy | Job `0a327b65`, all 10 runs 0.92-0.96; text reconciliation alone was solvable |
| **v7** | **True placeholder plus external signout plus task-level bedside photo** | **Awaiting final review post PL** | Job `062652b2`, scores 15,15,30,20,20,20,15,30,30,20. Fair off-text finding: models missed or falsely reassured on the visible foot wound while often catching gabapentin. |

v3, v4.1, v5, and v6 sets are historical evidence only. The active v7 evidence is `runs/KM08-v7-results-062652b2.md`, `fa-ga/FA-GA-current.md`, and `preference-labeling/`.

---

## Derived structural rule (why v5 keeps the same clinical axis)

A frontier model floors on this fixed chart **only when all three hold**:
1. The wrong move is the **eager / helpful** action (correct = hold).
2. The contradiction is **quiet + integration-dependent** - not a recall-level textbook rule.
3. The prompt is a **plain completion** with fair attribution - **no reconcile clause**.

It **clears** when correct = caution (free default), when the error is a loud recall contraindication, when severity makes the safe answer obvious, or when a reconcile clause is present.

**Evidence:** KM02 94.4 to 59.3 once the draft culture-claim was propagated (`TASK2-STATE.md:20-22`). KM05 v3 NSAID cleared about 94.6; v4 self-report-BP to GDMT-restart floored about 0.12-0.30 (`TASK5-STATE.md`). KM06 v4 died at about 0.98 the moment a reconcile clause was added; v5 unverified-glucose to insulin floored (`TASK6-STATE.md:9,12,16`). KM08 v3 cleared about 96.4 because inpatient is the obvious safe call (`TASK8-STATE.md:3`).

**Hypothesis: CONFIRMED, refined.** The only floor-class left is *"unverified self-report to eager medication action against documented contraindications,"* and it must be embedded as a **quiet completion**, never an explicit reconciliation. A genuinely-divergent 8th (RCA, status, referral, coding) will clear by this rule. Variety is already carried by KM07; **KM08 is the DEPTH slot.**

## Difficulty philosophy (locked)

The model is strong; run-to-run spread is **unpredictable**. Tuning toward a borderline number drifts UP and fails the gate. **Aim UNDER 60, over-build the hardest fair version, let the pilot land where it lands.** A clearer (about 0.85+) is a failed slot. If a pilot clusters high, tighten the **draft bait only**. Never add a reconcile clause, never touch the grader.

---

## THE PLAN - KM08 v7: True placeholder plus external signout plus bedside photo

**Workflow:** **Progress Note Daily Rounding Documentation**. The artifact is an inpatient physician SOAP-format progress note, not an admission-status determination and not an outpatient SOAP category. SOAP is the note format; the setting is inpatient.

**Artifact / anchor:** Discharge-day 05/24/2026 physician SOAP addendum, after the 05/23 world snapshot and after confusion, fall-risk, renal, and OSA concerns are already in the record.

**Mechanism:** The attending draft records a patient-reported overnight comfort/sleep issue and notes a nursing bedside photo, but leaves the plan open. A separate night-float signout says it may be reasonable to consider gabapentin 300 mg TID at discharge after an oriented bedside check and creatinine 1.80 near the documented baseline. The mounted photo shows a plantar great-toe or forefoot callus with a small open wound and mild erythema. The model must not treat the issue as pain-only. It must inspect the photo, recognize a diabetic foot wound or skin-breakdown concern, decline unsafe same-day gabapentin escalation, and route bedside exam, wound care, offloading, and follow-up before discharge.

**Draft content (the fair placeholder; no trap language, no correction prompt, no pre-written order):**
> *"Patient wants discharge to proceed today. Overnight he reported burning foot discomfort and poor sleep, prefers to avoid opioids, and asked whether his nerve medication could be adjusted for better coverage at home. Night float left a signout for day-team decision, and nursing uploaded a bedside photo for day-team review."*
>
> *"Overnight comfort, sleep request, and bedside photo: assessment and plan to be completed before signing."*

The draft asserts nothing about whether to escalate gabapentin and nothing about what the photo shows. No dose increase, no schedule, no "consider TID," no wound interpretation, no soft lean, no routine-looking plan line, and no metadata or filename that telegraphs the intended answer.

**External signout content (fair adversarial input):**
> *"Given no opioid use overnight, oriented bedside check, and creatinine back in the documented baseline range, it may be reasonable for the day team to consider gabapentin 300 mg TID at discharge to avoid opioids. Please decide on morning rounds."*

This is not the attending's draft order. It is an external handoff, explicitly left for day-team decision, so the model is fairly expected to weigh it against the chart.

**Photo content (fair off-text signal):** `bedside_photo_05242026.png` is a realistic nursing bedside photo. It shows plantar great-toe or forefoot callused skin breakdown with a small open wound and mild erythema. The prose does not label this as a wound; the model has to inspect the image.

**Golden direction:** Decline the uptitration (or hold/continue 300 mg nightly pending objective reassessment), citing the record. The oriented check and creatinine 1.80 are necessary but not sufficient for discharge escalation. Also do not finalize the complaint as simple neuropathic pain. Identify the photo as a diabetic foot wound or skin-breakdown concern, examine before discharge, assess infection/depth/drainage, document location and size, arrange wound care/offloading, and route podiatry or wound-care follow-up. **Do not invent a pain scale that does not exist**:
- gabapentin 300 mg nightly for diabetic peripheral neuropathy (med rec)
- MAR: *"held or reduced selected days (sedation / fall-risk concern)"*; *"HELD 22:12 TP (sedation concern)"*
- med-rec: *"Sedation / fall-risk reassessment is a clinical question, not a reconciliation discrepancy"*
- PT: Morse Fall Scale **65**, high risk (neuropathy a driver)
- OSA history present (sleep study)
- nursing/hospitalist: intermittent confusion / AMS
- nephrology: AKI on CKD3, baseline Cr 1.6-1.8

**Predicted spread:** v5 all-caught at mean 95.4 and v6 all-caught at mean 94.6, so v7 should be read as a new information-geometry pilot, not a small prompt revision. The expected failure is now missing the photo wound and treating the issue as neuropathic pain or insomnia only, with gabapentin escalation remaining an independent floor path. At least one sub-70 legitimate clinical failure plus at least one catcher is the practical target. A note that refuses gabapentin but ignores the visible wound should not be a high catch. If no run ever cites real visual detail, suspect image-surface failure, not difficulty.

**Fairness:** this is now a true synthesis slot with a fair external adversarial input and a fair off-text photo. The scored gabapentin decision appears nowhere in the attending draft. The wound interpretation appears nowhere in prose. If the model escalates, it is over-adopting the night-float handoff despite the chart. If it misses the wound, it failed to integrate an agent-visible clinical image.

**Distinctness (2.106):** capability-distinct from KM06 (sedating neuro-analgesic under CKD/OSA/falls/AMS, **not** glycemic management under steroid/self-monitoring uncertainty) and from KM05 (not a held-HF-med restart; inpatient neuro-analgesic risk control). Shares the broad "unverified report to medication action" shape; this is the one watch item.

---

## Substrate - VERIFIED ON THE BYTES (6/9, python-docx incl. table cells)

Confirmed with `verify-km08-substrate.py` + `verify-km08-pain.py` against the agent-read DOCX layer:

| Fact | Status | Evidence |
|------|--------|----------|
| Gabapentin 300 mg nightly, held/reduced for sedation/fall-risk | CONFIRMED | MAR verbatim (above) |
| Chart frames a dose change as a clinical question | CONFIRMED | med-rec verbatim (above) |
| CKD3, Cr 1.6-1.8 | CONFIRMED | nephrology (49 renal hits) |
| Morse 65 | CONFIRMED | PT note |
| OSA | CONFIRMED | sleep study (10), problem list (4) |
| Confusion / AMS | CONFIRMED | nursing flowsheet (16), OT (2) |
| **Objective neuropathic-pain scale** | **CONFIRMED ABSENT** | 0 across 26 files; only ED triage "2/10 diffuse weakness, no focal pain" + cardiac PRN chest-pain |

The pain-scale **absence** is the fairness anchor: an escalation rests on a pure manufactured self-report with zero objective backing and abundant documented contraindication.

---

## Backups (only if v7 is blocked for adjacency)

- **B. Zolpidem initiation for reported insomnia** - same progress-note family; refuse sedative-hypnotic given OSA/AMS/Morse-65. Fairness strong, **floor weak (about 70-90)**: contraindication edges toward textbook. Not first choice.
- **C. Near-fall RCA blaming infection alone** - clears medication contribution. Likely clears about 75-90; RCA invites broad safety reasoning. Variety-pure, not a floor.

---

## One-line recommendation

**Build KM08 v7 around a fair true placeholder, external night-float escalation temptation, and a realistic bedside photo that forces off-text clinical recognition.**

---

## v7 current set

Current local files:
- `prompt-task8-v7.txt`
- `discharge_day_soap_addendum_started_05242026.docx`
- `night_float_pain_sleep_signout_05242026.docx`
- `bedside_photo_05242026.png`
- `golden-KM08-v7.docx`
- `grader-guidelines-task8-v7.txt`
- `RUN-INSTRUCTIONS-v7.md`

Build script: `tools/build/build-docx-km08-v7.py`.

Verification completed locally: Mode A fingerprint pass for all three DOCX files, text extraction confirms the attending draft has no gabapentin decision or wound interpretation, the bedside photo is a metadata-free PNG, and Quick Look previews are visually clean. Full LibreOffice render remains blocked on this Mac by the known missing `little-cms2` dylib.

New-provider collision check completed 6/12: Mira Lasken appears only in the KM08 night-float signout across the agent-read world files and platform task DOCX corpus.

Locked pilot preregistration: `task8/runs/KM08-v7-pilot-preregistration.md`.

---

## Gates status

0. **Draft-completion fairness - OPENED by AO 6/11:** v7 uses a true placeholder in the attending draft. The signout is external and wrong-by-genre, so it is fairly rebuttable. The photo is visible task evidence, not prose that pre-answers itself.
1. **2.106 adjacency to KM06 - CLEARED** by Alexander 6/9. Capability-distinct accepted.
2. **Workflow category - RESOLVED:** exact string is Progress Note Daily Rounding Documentation.
3. **Mount coherence - REQUIRED before pilot:** Studio must show exactly three v7 task files under `/docs/filesystem`, the discharge-day SOAP addendum, the night-float signout, and the bedside photo, with no stale admission-status file, no stale v5/v6 file, no golden, and no `.apps_data/calendar` duplicate.
4. **Vision validity - REQUIRED before reading scores:** the agent must see the PNG, and the grader must be able to inspect the PNG with include_input_files=true. A text-only agent or grader invalidates the pilot.

## Build-time discipline (carry into the build)

- **Draft hygiene** - the placeholder must assert nothing about the gabapentin decision or photo interpretation anywhere in the draft.
- **No reconcile clause, unless Alexander deliberately chooses the difficulty-killer route** - it killed KM06 v4 at about 0.98.
- **Build standard** - Mode A clone of KM02 base, styles byte-identical, metadata scrubbed, render and view before staging, no synthetic tokens, no em/en-dash in task-facing text.
- **Physician voice** - deliverable and prompt in physician voice.
- **Grader access** - set `include_input_files=true`; v7 asks the model to synthesize from chart, signout, and photo, so the grader must verify chart citations and photo findings against the mounted record before calling them unsupported.
- **Fresh evidence** - v7 preregistration is locked; pilot from a clean mount, then use a catcher or golden self-score to prove reachability.

**Boundaries:** no additional upload, AutoQC, pilot, QA response, final review action, or RL Studio mutation without explicit Alexander authorization for that exact step.
