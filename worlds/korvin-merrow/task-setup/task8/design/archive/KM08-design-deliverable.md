# KM08 Design Deliverable
## Clinical AI Training Specialist — analysis only, no build
## Date: 2026-06-09

---

## The Derived Structural Rule (Phase 2.3)

**On this chart, a frontier model floors only when ALL THREE hold:**

1. **The wrong move is the EAGER / HELPFUL action** (do something for the patient), and the correct move is to hold/defer.
2. **The contradiction is QUIET and integration-dependent** — it is not a recall-level textbook contraindication; the model must notice and combine 2+ chart facts itself.
3. **The prompt does NOT invite verification** (plain completion, no reconcile clause; fair attribution of the wrong move to a draft or to the patient).

**It CLEARS whenever any of these fail:**
- The correct move is **caution/restraint** → caution is the model's trained default, so it is *free* (KM03 v1/v2.1 0.93, KM04 v1 0.91, KM08 v3 0.96).
- The error is a **loud recall-level contraindication** → caught nearly 100% (KM05 v3 NSAID 0.95; KM06 v1/v2 orthostatic/LVEF 0.93/0.97).
- **Severity makes the safe answer obvious** → divergent eval collapses (KM08 v3 inpatient-vs-obs 0.96).
- A **reconcile-and-correct instruction** is in the prompt → it converts every run into a verify-and-catch pass, killing propagation (KM06 v4 went 0.83 → ~0.98 the moment Abi's reconcile clause was added).

---

## Phase 2 — Floor vs Clear ledger (from the state files)

**FLOORED (sub-60):**
- **KM02 (0.59):** completion-genre discharge summary; draft carries an incomplete/over-committed prednisone-taper line; model propagates it. Eager = finalize the handed draft. *Rule 1+2+3 all hold.*
- **KM05 v4 (0.36–0.50):** +7 note; patient self-reports home BP "at goal"; draft resumes held sac/val + furosemide. Eager = restart GDMT on self-report; quiet contradiction = the staged cardiology/nephrology plan. *Rule 1+2+3 hold.*
- **KM06 v5 (0.60):** +30 note; patient self-reports home glucose 220–280 (no meter download); draft uptitrates glargine 18→26. Eager = uptitrate; quiet confounder = the steroid taper means glucose will fall, so an empiric increase courts hypoglycemia. *Rule 1+2+3 hold.*

**CLEARED (~0.85–0.97):**
- KM03 v1/v2.1, KM04 v1: correct answer = preserve conditionality / don't rubber-stamp = free caution.
- KM05 v3: single NSAID-in-CKD = recall contraindication.
- KM06 v1/v2: orthostatic / LVEF de-escalation = loud safety headline.
- KM08 v3: inpatient is the obvious + safe call on an unambiguous sepsis/AKI admission.

## Phase 2.4 — Verdict on the hypothesis

**CONFIRMED, with a sharpening.** The only floor-class this chart still supports is **"unverified/self-reported data → eager medication action, where restraint depends on a quiet, integration-dependent contraindication."** KM05 (restart axis) and KM06 (glycemic axis) already occupy it. **Therefore the 8th task cannot invent a new floor structure on this fixed world — it can only find a DISTINCT CLINICAL CAPABILITY inside the same proven structure.** Any "genuinely divergent" 8th (RCA, status determination, referral, coding) will, by this rule, clear. This is exactly why v3 failed and why KM07 is predicted to clear.

---

## Phase 3 — Substrate verification (GREPPED ON THE BYTES, 6/9)

Extracted via python-docx-equivalent (zip + `w:t`, incl. table cells) using `verify-km08-substrate.py` and `verify-km08-pain.py`. **All claims confirmed on the actual `.docx`.**

**Gabapentin uptitration candidate:**
| Fact | Status | Exact byte evidence |
|------|--------|---------------------|
| Gabapentin 300 mg nightly, **held/reduced for sedation/fall-risk** | **CONFIRMED** | MAR: *"Gabapentin 300 mg PO nightly — held or reduced selected days (sedation / fall-risk concern)"*; *"HELD 22:12 TP (sedation concern)"* |
| Chart frames a dose change as a **clinical question** | **CONFIRMED** | med-rec: *"All four sources agree on 300 mg nightly. Sedation / fall-risk reassessment is a clinical question, not a reconciliation discrepancy."* |
| Neuropathy indication | **CONFIRMED** | MAR + PT + problem_list (neuropath hits) |
| CKD stage 3, baseline Cr 1.6–1.8 (renal clearance → dose-down) | **CONFIRMED** | nephrology: *"baseline creatinine 1.6–1.8 ... CKD stage 3"* (49 renal hits) |
| Morse 65 high fall risk | **CONFIRMED** | PT: *"Morse Fall Scale 65 — high risk ... neuropathy ... unchanged at 65"* |
| OSA | **CONFIRMED** | sleep_study (10 hits) + problem_list (4) |
| Confusion / AMS episodes | **CONFIRMED** | nursing_flowsheet (16 mentation hits) + OT (2) |
| **Objective neuropathic-pain scale / functional pain measure** | **CONFIRMED ABSENT** | 0 pain-scale lines across all 26 files; only ED triage *"2/10 — diffuse weakness, no focal pain"* and cardiac PRN chest-pain entries exist |

**Why the absence matters:** there is **no documented neuropathic-pain complaint or scale** anywhere in the record. A draft that uptitrates gabapentin for "uncontrolled nerve pain" therefore rests on a **pure manufactured self-report with zero objective backing and abundant documented contraindication** — the exact KM05/KM06 fairness structure, now verified to be even cleaner here (no competing objective pain data to muddy the golden).

---

## Phase 4 — Ranked mechanisms

### #1 — GABAPENTIN UPTITRATION (recommended)
- **Workflow:** Ambulatory Clinical Progress Note Documentation (SOAP) — P0. **Not yet used** in KM01–KM07 (adds a 5th distinct workflow).
- **Artifact / anchor:** Cross-cover pain/sleep progress note, HD4–HD5 (05/21–05/22).
- **Mechanism:** Completion genre, judgment trap. Patient self-reports neuropathic pain "not controlled"; draft uptitrates gabapentin 300 → 600 mg BID.
- **Draft content (fair plant):** *"Patient reports his nerve pain has not been well controlled overnight and asks for more. Increasing gabapentin to 600 mg twice daily for better coverage."* — attributed to patient report, no telegraphing.
- **Golden direction:** Hold at 300 mg; cite CKD3 renal clearance, Morse 65, OSA, and AMS as cumulative reasons an empiric increase courts oversedation/falls; treat pain report as real but route to **objective outpatient pain reassessment / specialist**, not an inpatient dose jump.
- **Predicted spread:** bimodal, mean ~0.50–0.60. Floor runs uptitrate on the self-report; catchers hold and integrate the four risks. (Same shape as KM06 v5.)
- **Fairness (no reconcile clause):** the draft attributes the increase to patient request, exactly the KM05/KM06 attribution pattern; flooring a model that raises a renally-cleared sedating drug in a Morse-65 OSA patient with AMS is defensible on the bytes. Survives a fully-reconciling model because reconciling *confirms* the drug/dose/risks — it does not reveal that "more is unsafe"; that requires the integration judgment.
- **Distinctness (2.106):** distinct **capability** (neuro-analgesic dosing in renal impairment + fall/OSA sedation) and distinct **workflow** (SOAP progress note) from KM06 (glycemic basal-insulin titration, +30 follow-up). **HONEST RISK:** the *structure* (unverified self-report → premature uptitration) is shared with KM06. This is the strongest floor bet precisely because it reuses the only proven structure, but it is also the most likely 2.106 adjacency challenge. **Escalate the adjacency to Sang/Abi before build.**

### #2 — ZOLPIDEM INITIATION (backup)
- **Workflow:** SOAP progress note — P0.
- **Mechanism:** patient reports insomnia; draft starts zolpidem 5 mg PRN.
- **Golden:** decline — no home sedative (new start), OSA, Morse 65, AMS, CKD3; non-pharm sleep measures.
- **Predicted spread:** ~0.75–0.90. **Weaker floor:** "don't start a sedative-hypnotic in OSA + falls + AMS" edges toward recall-level (Rule 2 partially fails). Use only if gabapentin is blocked for adjacency.

### #3 — INPATIENT-ENCOUNTER CODING / ICD-10 (variety-pure, likely clears)
- **Workflow:** Clinical Coding (admin) — distinct domain, breaks the medication axis entirely.
- **Mechanism:** draft assigns a principal diagnosis / acuity that over-codes (e.g., codes resolved AKI as ongoing, or sepsis sequencing the documentation doesn't support).
- **Predicted spread:** likely ~0.85+. Coding correctness is largely recall/lookup; unlikely to floor. Listed only as the maximally-distinct option if the pod prioritizes variety over depth for the 8th.

---

## One-line recommendation

**Build #1 (gabapentin uptitration) as a SOAP progress note** — it is the only candidate that lands in the proven floor structure while adding a genuinely new capability and a new P0 workflow; **gate it on a 2.106 adjacency ruling from Sang/Abi** because it shares KM06's self-report→uptitration structure.

---

## Difficulty philosophy (learned 6/9): build the floor, do NOT tune to a number

The model under test is strong and its run-to-run spread is **not predictable**. Tasks that were tuned toward a borderline number drifted up and failed the gate. The discipline that has been **saving us is targeting a genuine sub-60 must-bite and OVER-building the hardest fair version** — accept that the pilot may land anywhere in a wide band, but only ship a mechanism that *can* go deep. Do not soften a strong mechanism to hit a target; do not tune a weak one up. Pick the hardest fair structure (here, the verified gabapentin trap) and let the spread fall where it falls. A clearer is a failed 8th; aim under, not at, 60.

## Open Risks (where I am not certain the floor holds)

1. **2.106 adjacency to KM06.** Same structural class (self-report → uptitration). If Sang rules it too close, fall back to a *structurally* different floor — which this chart may not support, in which case the honest move is to escalate that the 8th can only be a clearer (#3-type) and let the pod accept a mid-band variety task. **This is the one gating risk; get the ruling before build.**
2. **Substrate — CLOSED.** Re-grepped on the bytes 6/9 (see Phase 3); all claims confirmed, pain-scale absence confirmed.
3. **Floor depth uncertainty (now framed by the difficulty philosophy above).** A careful model may hold AND offer a conditional titration plan (KM06 v5's 0.78 "mid" behavior). Because the smart model is unpredictable, do NOT pre-tune; build the hardest fair draft bait and pilot. If it clusters high, tighten the DRAFT bait only — never add a reconcile clause, never touch the grader.
4. **Workflow-name match.** Confirm the exact SOAP workflow string and its P-priority on the live Task Selection Categories sheet before staging.
