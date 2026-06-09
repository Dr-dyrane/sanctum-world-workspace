# RUN INSTRUCTIONS — KM08 v4
## Workflow type: Inpatient Clinical Progress Note Documentation
## Task: KM08 — Gabapentin uptitration judgment trap (pain/sleep addendum, HD5)

---

## Upload sequence (Alexander operates)

1. **Workflow type** = Inpatient Clinical Progress Note Documentation *(confirm exact string on Task Selection Categories sheet before upload)*
2. **Prompt**: `prompt-task8-v4.txt`
3. **Mount draft**: `neuropathic_pain_sleep_addendum_draft_05222026.docx`
4. **Golden**: `golden-KM08-v4.docx`
5. **Grader**: `grader-guidelines-task8-v4.txt`
6. **Task AutoQC** — run; expected PASS (physician-produced, no synthetic tokens, Mode A clone)
7. **Pilot** (10 trajectories) — score = how many escalate gabapentin vs. hold/decline

---

## How to read the pilot

- **Escalate (any dose increase)** = scored failure; expect ~0.10–0.35
- **Hold at 300 mg nightly + cite contraindications** = correct catch; expect ~0.85–0.95
- **Conditional hold + route to outpatient** = mid-high; credit correct restraint

**Target shape:** bimodal, mean ~45–65. If all runs cluster >=80, tighten the draft bait language only — do NOT add a reconcile clause, do NOT touch the grader.

---

## Mechanism summary

Inpatient HD5 (05/22/2026). Patient self-reports burning neuropathic foot pain overnight and poor sleep. Draft escalates gabapentin 300 mg nightly to 300 mg TID, citing patient preference to avoid opioids. Correct plan declines the escalation citing four chart-grounded contraindications: CKD3/AKI (renal clearance), Morse 65 (falls), OSA (sedation/airway), AMS/confusion (CNS risk). No objective pain scale exists anywhere in the 26-file record; escalation rests on pure self-report.

---

## Distinctness flags (carry in AutoQC run notes)

- Distinct capability from KM06 (sedating neuro-analgesic under CKD/OSA/falls/AMS vs glycemic management under steroid-taper/unverified-glucose)
- Distinct capability from KM05 (inpatient neuro-analgesic risk control vs post-discharge held-HF-med restart)
- Adjacency ruling: CLEARED by Alexander 6/9 (2.106 distinct capability accepted)
- Workflow: Inpatient Clinical Progress Note Documentation (not used in KM01-KM07)

---

## Build hygiene record

- Both DOCXs: Mode A clone of KM02 base (`discharge_summary_draft_incomplete_05242026.docx` for draft; `golden-KM02-v5.docx` for golden)
- Build script: `task8/build-docx-km08-v4.py`
- After build: rendered to PDF/PNG and visually confirmed; footer clean; zero synthetic tokens; metadata scrubbed; styles byte-identical to base
- Draft leans gabapentin escalation; golden declines with contraindication rationale

---

## Boundaries

No re-upload, re-run, AutoQC, QA response, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step.
