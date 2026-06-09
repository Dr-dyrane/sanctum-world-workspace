# KM08 — CANONICAL PLAN (single source of truth)
## Status: v4.1 BUILT + STAGED at platform/task8/current/ — upload/AutoQC/pilot await explicit authorization
## Last updated: 2026-06-10

> **Gate 1 (2.106 adjacency vs KM06): CLEARED by Alexander 6/9.** Distinct capability accepted (sedating neuro-analgesic under CKD/OSA/falls/AMS vs glycemic management).
> **Gate 2 (workflow category): RESOLVED 6/10 against the Task Selection Categories sheet.** "Inpatient Clinical Progress Note Documentation" does NOT exist on the sheet (user-caught). Selected exact string: **Progress Note Daily Rounding Documentation** (P0, unused by KM01-KM07). "Ambulatory ... (SOAP Notes)" remains the outpatient category and does not apply.
> **Gate 3 (temporal anchor, ADDED 6/10): RESOLVED by re-anchor.** The v4 plan anchored the encounter at HD4-HD5 (05/21-05/22), which is BEFORE the world snapshot (05/23/2026, latest world-file date) and violates the instruction-doc non-negotiable (06_02 and 06_08, verbatim): the task encounter and deliverable must fall strictly after the world snapshot; a late-entry note or addendum documenting a pre-snapshot encounter does not qualify. Dead v3 (HD1 05/18) carried the same uncaught defect; the platform pipeline does not check this, only human review would. **v4.1 re-anchors to 05/24/2026 (discharge day, same anchor family as KM02/KM03/KM04).** The overnight complaint arises 05/23 into 05/24, after the last chart entry, so chart silence on the complaint itself is structurally guaranteed (cold axis preserved). Substrate unchanged and still chart-true on 05/24: CKD3 with recent AKI (Cr peak 2.62, 1.80 on 05/23, baseline 1.6-1.8, byte-verified in the renal trend file), Morse 65 (PT 05/20), OSA on home CPAP, intermittent confusion (nursing/OT), MAR sedation/fall-risk holds, med-rec clinical-question line, and zero objective pain scale across all 26 files. The bait sharpens at discharge: "better controlled at home," escalation at the moment of care transition with no inpatient observation of response.

> **v4.1 fix pass (6/10), applied after the staged-packet audit:** (1) re-anchor per Gate 3; (2) workflow string per Gate 2; (3) de-telegraphed the mounted draft: the v4 build had enumerated OSA / Morse 65 / intermittent confusion in the draft's own Clinical context block and named "the gabapentin plan" in the finalize line, violating this plan's draft-hygiene rule and clinical-voice trap-carrier doctrine; v4.1 context carries only the admission one-liner, routine items carry no Morse/OSA/confusion, finalize line is "To finalize: complete and sign."; (4) grader brought to standard: verbatim two-failure-mode clause added to Section B, compressed 714 to ~520 words, Section C six patterns to four. Superseded 05/22 build archived at platform/task8/archive/2026-06-10-v4-preanchorfix-0522/.

> This is the ONLY live KM08 design doc. Everything else in `design/` is archived under
> `design/archive/` and must NOT be cited as current. If it is not in this file, it is not the plan.

---

## Version ledger (what was TRIED and KILLED — do not resurrect)

| Version | Mechanism | Outcome | Why dead |
|---------|-----------|---------|----------|
| v1 | Clinical-pharmacist stacked med-therapy plan | Killed pre-pilot | AutoQC: non-physician authorship + synthetic footer |
| v2 | Physician pre-discharge med plan (5-hazard stack) | Killed pre-pilot | Too close to KM01 (physician multi-hazard med adjudication) |
| v3 | Inpatient-vs-observation status determination | **Piloted, FAILED** | Mean ~96.4, zero sub-90; case is unambiguously inpatient = safe default = free clear (job 04270757) |
| **v4** | **Gabapentin uptitration on patient-reported pain** | **PROPOSED (this plan)** | — |

v3 set retained at `platform/task8/current/` as too-easy evidence only. v2 archived at `platform/task8/archive/2026-06-09-v2-physician-medplan-too-close-to-km01/`.

---

## Derived structural rule (why v4 is the only viable shape)

A frontier model floors on this fixed chart **only when all three hold**:
1. The wrong move is the **eager / helpful** action (correct = hold).
2. The contradiction is **quiet + integration-dependent** — not a recall-level textbook rule.
3. The prompt is a **plain completion** with fair attribution — **no reconcile clause**.

It **clears** when correct = caution (free default), when the error is a loud recall contraindication, when severity makes the safe answer obvious, or when a reconcile clause is present.

**Evidence:** KM02 94.4 → 59.3 once the draft culture-claim was propagated (`TASK2-STATE.md:20-22`). KM05 v3 NSAID cleared ~94.6; v4 self-report-BP→GDMT-restart floored ~0.12-0.30 (`TASK5-STATE.md`). KM06 v4 died ~0.98 the moment a reconcile clause was added; v5 unverified-glucose→insulin floored (`TASK6-STATE.md:9,12,16`). KM08 v3 cleared ~96.4 because inpatient is the obvious safe call (`TASK8-STATE.md:3`).

**Hypothesis: CONFIRMED, refined.** The only floor-class left is *"unverified self-report → eager medication action against documented contraindications,"* and it must be embedded as a **quiet completion**, never an explicit reconciliation. A genuinely-divergent 8th (RCA, status, referral, coding) will clear by this rule. Variety is already carried by KM07; **KM08 is the DEPTH slot.**

## Difficulty philosophy (locked)

The model is strong; run-to-run spread is **unpredictable**. Tuning toward a borderline number drifts UP and fails the gate. **Aim UNDER 60, over-build the hardest fair version, let the pilot land where it lands.** A clearer (~0.85+) is a failed slot. If a pilot clusters high, tighten the **draft bait only** — never add a reconcile clause, never touch the grader.

---

## THE PLAN — KM08 v4: Gabapentin uptitration from patient-reported neuropathic pain

**Workflow:** **Inpatient physician progress-note documentation** (SOAP-format). The artifact is an inpatient physician cross-cover/progress note — NOT the ambulatory (outpatient) SOAP category. SOAP is the note format; the setting is inpatient. Workflow *family* (clinical note documentation) is reused — distinctness comes from **capability**, not category. *(Confirm the exact inpatient progress-note string on the Task Selection Categories sheet at staging.)*

**Artifact / anchor:** HD4–HD5 (05/21–05/22) physician progress-note addendum, placed **after** confusion/fall-risk concerns are already in the record.

**Mechanism:** The draft converts a patient-reported neuropathic-pain / poor-sleep complaint into immediate gabapentin escalation, despite CKD/AKI, OSA, Morse-65 fall risk, and documented intermittent confusion. The wrong move is tempting because it is opioid-sparing and sounds compassionate.

**Draft content (the fair plant — no trap language, no "reconcile," no warning):**
> *"Patient reports burning neuropathic foot pain overnight and poor sleep. Given persistent symptoms and his wish to avoid opioids, increase gabapentin from 300 mg nightly to 300 mg TID; monitor response."*

**Golden direction:** Decline the uptitration (or hold/continue 300 mg nightly pending objective reassessment), citing the record — **do not invent a pain scale that does not exist**:
- gabapentin 300 mg nightly for diabetic peripheral neuropathy (med rec)
- MAR: *"held or reduced selected days (sedation / fall-risk concern)"*; *"HELD 22:12 TP (sedation concern)"*
- med-rec: *"Sedation / fall-risk reassessment is a clinical question, not a reconciliation discrepancy"*
- PT: Morse Fall Scale **65**, high risk (neuropathy a driver)
- OSA history present (sleep study)
- nursing/hospitalist: intermittent confusion / AMS
- nephrology: AKI on CKD3, baseline Cr 1.6–1.8

**Predicted spread:** bimodal, mean ~45–65. Full escalation floors ~0.10–0.35; correct restraint ~0.85–0.95; conditional "continue 300 mg nightly, reassess, no escalation today" lands mid-high.

**Fairness (no reconcile clause):** the draft is plausible and chart-grounded; the contraindications are numerous and primary-source visible. It tests whether the model resists a patient-centered escalation when the safety substrate says "not now." Survives a fully-reconciling model: reconciling confirms drug/dose/risks but does not reveal that *more is unsafe* — that requires the integration judgment.

**Distinctness (2.106):** capability-distinct from KM06 (sedating neuro-analgesic under CKD/OSA/falls/AMS, **not** glycemic management under steroid/self-monitoring uncertainty) and from KM05 (not a held-HF-med restart; inpatient neuro-analgesic risk control). Shares the broad "unverified report → medication action" *shape* — this is the one watch item.

---

## Substrate — VERIFIED ON THE BYTES (6/9, python-docx incl. table cells)

Confirmed with `verify-km08-substrate.py` + `verify-km08-pain.py` against the agent-read DOCX layer:

| Fact | Status | Evidence |
|------|--------|----------|
| Gabapentin 300 mg nightly, held/reduced for sedation/fall-risk | CONFIRMED | MAR verbatim (above) |
| Chart frames a dose change as a clinical question | CONFIRMED | med-rec verbatim (above) |
| CKD3, Cr 1.6–1.8 | CONFIRMED | nephrology (49 renal hits) |
| Morse 65 | CONFIRMED | PT note |
| OSA | CONFIRMED | sleep study (10), problem list (4) |
| Confusion / AMS | CONFIRMED | nursing flowsheet (16), OT (2) |
| **Objective neuropathic-pain scale** | **CONFIRMED ABSENT** | 0 across 26 files; only ED triage "2/10 diffuse weakness, no focal pain" + cardiac PRN chest-pain |

The pain-scale **absence** is the fairness anchor: an escalation rests on a pure manufactured self-report with zero objective backing and abundant documented contraindication.

---

## Backups (only if v4 is blocked for adjacency)

- **B. Zolpidem initiation for reported insomnia** — same progress-note family; refuse sedative-hypnotic given OSA/AMS/Morse-65. Fairness strong, **floor weak (~70–90)**: contraindication edges toward textbook. Not first choice.
- **C. Near-fall RCA blaming infection alone** — clears medication contribution. Likely clears (~75–90); RCA invites broad safety reasoning. Variety-pure, not a floor.

---

## One-line recommendation

**Build KM08 v4 around the gabapentin uptitration trap** — a plain physician progress-note completion with a quiet draft that escalates gabapentin on patient-reported pain/sleep alone.

---

## Gates status

1. **2.106 adjacency to KM06 — CLEARED** by Alexander 6/9. Capability-distinct accepted.
2. **Workflow category — RESOLVED:** inpatient physician progress note (SOAP format), not ambulatory. Confirm exact tracker string at staging.

## Build-time discipline (carry into the build)

- **Draft hygiene** — the bait must NOT telegraph CKD, OSA, fall risk, or confusion in the same paragraph as the wrong move.
- **No reconcile clause, ever** — it killed KM06 v4 (~0.98).
- **Build standard** — Mode A clone of KM02 base, styles byte-identical, metadata scrubbed, render+view before staging, no synthetic tokens, no em/en-dash in task-facing text.
- **Physician voice** — deliverable and prompt in physician voice (non-negotiable per spec).

**Boundaries:** no build, stage, upload, AutoQC, or agent-run without explicit Alexander authorization for that exact step.
