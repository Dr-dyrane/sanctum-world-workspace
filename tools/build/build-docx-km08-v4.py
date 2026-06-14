#!/usr/bin/env python3
"""KM08 v4 -- gabapentin uptitration judgment trap DOCX via Mode A clone.
HD5 inpatient pain-and-sleep addendum (05/22/2026). Completion genre.
Draft escalates gabapentin 300 mg nightly -> 300 mg TID on patient self-report of
neuropathic pain/poor sleep. Golden holds at 300 mg nightly, citing CKD3/AKI, Morse 65,
OSA, and AMS. No objective pain scale anywhere in the 26-file record (verified 6/9).
Distinct from KM06 (glycemic axis) and KM05 (HF-restart axis). Adjacency cleared 6/9.
"""
import sys, os, tempfile, shutil

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import (clone, set_text, insert_before, delete_paragraphs,
                                 edit_band_cell, edit_footer, scrub_core,
                                 integrity_gate, verify_against_base)

REPO = os.path.join(REPO_ROOT, "worlds")
# Mode A bases (KM02 set -- proven clean, styles byte-identical, no synthetic tokens)
TASK_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                          "current", "discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                            "current", "golden-KM02-v5.docx")
OUT = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task8", "current")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------
# Shared header / context paragraphs
# ---------------------------------------------------------------------------
HEADER_CONTEXT = (
    "Korvin Merrow, 62-year-old male, 5W-318. Hospital day 5, 05/22/2026. "
    "Admitted 05/18 for suspected urinary-source infection with sepsis physiology "
    "and AKI on CKD stage 3. Renal function improving; CKD stage 3 baseline "
    "creatinine 1.6-1.8, peaked at 2.62, trending toward baseline. "
    "HFrEF and CAD on hold regimen. Type 2 diabetes, polymyalgia rheumatica "
    "on prednisone taper. Obstructive sleep apnea on home CPAP. High fall risk "
    "(Morse Fall Scale 65 per PT, 05/20). Intermittent confusion noted on nursing "
    "and OT assessments."
)

OVERNIGHT_REPORT = (
    "Overnight, patient reported to nursing that his neuropathic foot pain was "
    "not well controlled and that he slept poorly. He expressed that his nerve pain "
    "has been bothering him for years and asked whether his nerve medication could be "
    "increased. He prefers to avoid opioids."
)

# THE GABAPENTIN ITEM: draft escalates (trap) vs golden holds (catch)
GABA_DRAFT = (
    "Neuropathic pain and sleep: Patient reports persistent burning neuropathic "
    "foot pain overnight and poor sleep. Given his ongoing symptoms and preference "
    "to avoid opioids, increase gabapentin from 300 mg nightly to 300 mg three "
    "times daily. Monitor for response and reassess tomorrow."
)

GABA_GOLD = (
    "Neuropathic pain and sleep: Patient reports overnight neuropathic foot pain "
    "and poor sleep; this is acknowledged and taken seriously. However, an inpatient "
    "gabapentin uptitration is not supported by the record at this time. "
    "Gabapentin is documented at 300 mg PO nightly (med rec, MAR); the MAR notes "
    "the dose was held or reduced on selected days for sedation and fall-risk concern, "
    "and the med-rec states that sedation and fall-risk reassessment is a clinical "
    "question, not a reconciliation issue. Four chart-grounded constraints argue "
    "against an inpatient dose increase: (1) CKD stage 3 with AKI history (Cr peak "
    "2.62, baseline 1.6-1.8) -- gabapentin is renally cleared and dose-escalation "
    "without confirmed renal recovery is unsafe; (2) Morse Fall Scale 65, high risk, "
    "with neuropathy as a contributor (PT 05/20) -- any additional CNS-sedating load "
    "increases fall risk; (3) OSA on home CPAP (sleep study on file) -- additional "
    "sedation risks airway compromise overnight; (4) intermittent confusion and altered "
    "mentation documented by nursing and OT across multiple hospital days -- further "
    "CNS depression is contraindicated. No objective pain scale or functional pain "
    "measure is documented in this chart; the complaint is patient self-report only "
    "and is insufficient grounds for empiric uptitration in this clinical context. "
    "Plan: maintain gabapentin at 300 mg PO nightly. Address overnight comfort with "
    "non-pharmacologic measures (repositioning, heat, sleep hygiene). Defer any "
    "analgesic escalation or gabapentin dose adjustment to objective outpatient "
    "pain reassessment after renal recovery is confirmed and fall/cognition status "
    "is reassessed. Notify pharmacy and nursing of unchanged dose."
)

# Other plan items (shared, correct in both versions)
OTHER_ITEMS = (
    "Infection/sepsis: IV antibiotics continued; clinical improvement ongoing. "
    "Renal: AKI improving toward baseline; continue renal monitoring, hold NSAIDs. "
    "Cardiorenal: held regimen unchanged; staged restart deferred to outpatient "
    "cardiology and nephrology per prior plan. "
    "Glycemic: continue current inpatient insulin protocol; no changes today. "
    "Fall/mobility: Morse 65 fall precautions maintained; PT/OT engaged."
)

DRAFT_FOOTER_NOTE = (
    "Draft started for Elian Vossmere, MD; review, complete, and sign | "
    "Inpatient Medicine, 5 West Medical, 5W-318"
)
GOLD_FOOTER_NOTE = (
    "Electronically signed by Elian Vossmere, MD | "
    "Inpatient Medicine, 5 West Medical, 5W-318"
)


def build(which: str):
    base = TASK_BASE if which == "draft" else GOLDEN_BASE
    tmp = os.path.join(tempfile.gettempdir(), f"km08v4_{which}.docx")
    d = clone(base, tmp)
    paras = d.paragraphs

    # Band / header cells
    doc_label = "Inpatient Pain and Sleep Addendum" + (" - Draft" if which == "draft" else "")
    set_text(paras[1], "INPATIENT PAIN AND SLEEP ADDENDUM" + (" - DRAFT" if which == "draft" else ""))
    set_text(paras[2], (
        "Author: Elian Vossmere, MD  |  Department: Inpatient Medicine  |  "
        "05/22/2026  |  Status: " + ("Draft for finalization" if which == "draft" else "Signed")
    ))

    heading_like = paras[3]
    body_like = paras[4]
    start = 3 if which == "golden" else 4
    if which == "draft":
        set_text(paras[3], "DRAFT for finalization -- Korvin Merrow pain and sleep addendum, HD5, 05/22/2026.")
    sig = paras[len(paras) - 1]
    delete_paragraphs(list(paras[start:len(paras) - 1]))

    gaba = GABA_DRAFT if which == "draft" else GABA_GOLD
    closing = (
        "To finalize: review chart context, complete the gabapentin plan, and sign."
        if which == "draft" else
        "Finalized: gabapentin held at current dose; outpatient analgesic reassessment deferred."
    )

    body = [
        (True,  "Clinical context"),
        (False, HEADER_CONTEXT),
        (True,  "Overnight report"),
        (False, OVERNIGHT_REPORT),
        (True,  "Assessment and plan"),
        (False, "1. " + gaba),
        (False, "2. " + OTHER_ITEMS),
        (False, closing),
    ]
    for is_h, t in body:
        insert_before(sig, heading_like if is_h else body_like, t)

    set_text(sig, DRAFT_FOOTER_NOTE if which == "draft" else GOLD_FOOTER_NOTE)

    # Band cells
    edit_band_cell(d, "Document", doc_label,
                   "Discharge Summary - Working Draft" if which == "draft" else "Hospital Discharge Summary")
    edit_band_cell(d, "Date", "05/22/2026", "05/24/2026")
    edit_band_cell(d, "Attending",
                   "E. Vossmere, MD",
                   "E. Vossmere, MD" if which == "draft" else "Elian Vossmere, MD")
    edit_band_cell(d, "Unit", "5 West Medical, Room 5W-318",
                   "5 West Medical, Room 5W-318")

    # Footer
    edit_footer(d,
                "Discharge Summary - Working Draft" if which == "draft" else "Hospital Discharge Summary",
                doc_label)

    d.save(tmp)
    scrub_core(tmp)
    integrity_gate(tmp)

    fname = ("neuropathic_pain_sleep_addendum_draft_05222026.docx"
             if which == "draft" else "golden-KM08-v4.docx")
    out = os.path.join(OUT, fname)
    shutil.copy(tmp, out)
    print(f"=== {which.upper()} ===")
    verify_against_base(out, base)
    print("Saved:", out)


if __name__ == "__main__":
    print("Building KM08 v4 gabapentin-uptitration DOCX...")
    build("draft")
    build("golden")
    print("Done. Render both to PDF/PNG and visually confirm before staging.")
