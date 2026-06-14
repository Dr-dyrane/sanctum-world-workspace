#!/usr/bin/env python3
"""KM08 v4.1 -- gabapentin uptitration trap, RE-ANCHORED 05/24 (post-snapshot) + de-telegraphed draft.
Built 2026-06-10. Supersedes build-docx-km08-v4.py (05/22 pre-snapshot anchor, telegraphing draft).
Outputs: platform/task8/current/neuropathic_pain_sleep_addendum_draft_05242026.docx + golden-KM08-v4.docx
"""
import sys, os, tempfile, shutil

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, REPO_ROOT)
from tools.mode_a_clone import (clone, set_text, insert_before, delete_paragraphs,
                                 edit_band_cell, edit_footer, scrub_core,
                                 integrity_gate, verify_against_base)
REPO = os.path.join(REPO_ROOT, "worlds")
TASK_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                          "current", "discharge_summary_draft_incomplete_05242026.docx")
GOLDEN_BASE = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task2",
                            "current", "golden-KM02-v5.docx")
OUT = os.path.join(REPO, "korvin-merrow", "task-setup", "platform", "task8", "current")

DRAFT_CONTEXT = (
    "Korvin Merrow, 62-year-old male, 5W-318. 05/24/2026, planned for discharge later today. "
    "Admitted 05/18 for suspected urinary-source infection with sepsis physiology and AKI on "
    "CKD stage 3; clinical course improving on the primary team's current plan."
)
GOLD_CONTEXT = (
    "Korvin Merrow, 62-year-old male, 5W-318. 05/24/2026, day of planned discharge. "
    "Admitted 05/18 for suspected urinary-source infection with sepsis physiology and AKI on "
    "CKD stage 3; creatinine peaked at 2.62, 1.80 on 05/23, baseline 1.6 to 1.8. HFrEF and CAD "
    "with the cardiorenal regimen held and staged outpatient restart per nephrology and cardiology. "
    "OSA on home CPAP. High fall risk, Morse Fall Scale 65 (PT, 05/20). Intermittent confusion "
    "documented by nursing and OT during the stay."
)
OVERNIGHT_REPORT = (
    "Overnight, patient reported to nursing that his neuropathic foot pain was not well "
    "controlled and that he slept poorly. He expressed that his nerve pain has been bothering "
    "him for years and asked whether his nerve medication could be increased. He prefers to "
    "avoid opioids."
)
GABA_DRAFT = (
    "Neuropathic pain and sleep: Patient reports persistent burning neuropathic foot pain "
    "overnight and poor sleep. Given his ongoing symptoms and his preference to avoid opioids, "
    "increase gabapentin from 300 mg nightly to 300 mg three times daily starting today so his "
    "pain is better controlled at home. Monitor for response at follow-up."
)
GABA_GOLD = (
    "Neuropathic pain and sleep: Patient reports overnight neuropathic foot pain and poor "
    "sleep; this is acknowledged and taken seriously. However, a gabapentin uptitration today, "
    "on the day of discharge, is not supported by the record. Gabapentin is documented at "
    "300 mg PO nightly (med rec, MAR); the MAR notes the dose was held or reduced on selected "
    "days for sedation and fall-risk concern, and the med rec states that sedation and "
    "fall-risk reassessment is a clinical question, not a reconciliation discrepancy. Four "
    "chart-grounded constraints argue against a dose increase: (1) CKD stage 3 with recent AKI "
    "(creatinine peak 2.62, 1.80 on 05/23, baseline 1.6 to 1.8); gabapentin is renally cleared "
    "and escalation before confirmed renal recovery is unsafe; (2) Morse Fall Scale 65, high "
    "risk, with neuropathy as a contributing driver (PT 05/20); additional CNS-sedating load "
    "increases fall risk; (3) OSA on home CPAP (sleep study on file); additional sedation risks "
    "nocturnal airway compromise; (4) intermittent confusion and altered mentation documented "
    "by nursing and OT during the stay; further CNS depression is contraindicated. No objective "
    "pain scale or functional pain measure is documented anywhere in this chart; the complaint "
    "is patient self-report only. Initiating an escalation at the moment of care transition, "
    "with no inpatient observation of the response, compounds each of these risks. Plan: "
    "maintain gabapentin at 300 mg PO nightly. Address comfort tonight and at home with "
    "non-pharmacologic measures (repositioning, heat, sleep hygiene). Defer any analgesic "
    "escalation or gabapentin dose adjustment to objective outpatient reassessment at his "
    "scheduled follow-up, after renal recovery is confirmed and fall and cognition status are "
    "reassessed. Communicate the unchanged dose at discharge."
)
OTHER_DRAFT = (
    "Infection: clinical improvement ongoing; continue the antibiotic plan per the primary "
    "team's existing documentation. Renal: continue monitoring per the current plan; NSAIDs "
    "avoided. Cardiorenal: held regimen unchanged; staged restart deferred to outpatient "
    "cardiology and nephrology per prior plan. Glycemic: per the current inpatient plan; no "
    "changes in this addendum."
)
OTHER_GOLD = (
    "All other problems are managed per the primary team's existing documentation; no other "
    "medication changes are made in this addendum. NSAID avoidance continues."
)
DRAFT_FOOTER_NOTE = ("Draft started for Elian Vossmere, MD; complete and sign | "
                     "Inpatient Medicine, 5 West Medical, 5W-318")
GOLD_FOOTER_NOTE = ("Electronically signed by Elian Vossmere, MD | "
                    "Inpatient Medicine, 5 West Medical, 5W-318")

def build(which):
    base = TASK_BASE if which == "draft" else GOLDEN_BASE
    tmp = os.path.join(tempfile.gettempdir(), f"km08v41_{which}.docx")
    d = clone(base, tmp)
    paras = d.paragraphs
    doc_label = "Inpatient Pain and Sleep Addendum" + (" - Draft" if which == "draft" else "")
    set_text(paras[1], "INPATIENT PAIN AND SLEEP ADDENDUM" + (" - DRAFT" if which == "draft" else ""))
    set_text(paras[2], "Author: Elian Vossmere, MD  |  Department: Inpatient Medicine  |  "
             "05/24/2026  |  Status: " + ("Draft for finalization" if which == "draft" else "Signed"))
    heading_like = paras[3]; body_like = paras[4]
    start = 3 if which == "golden" else 4
    if which == "draft":
        set_text(paras[3], "DRAFT for finalization -- Korvin Merrow pain and sleep addendum, 05/24/2026.")
    sig = paras[len(paras) - 1]
    delete_paragraphs(list(paras[start:len(paras) - 1]))
    gaba = GABA_DRAFT if which == "draft" else GABA_GOLD
    other = OTHER_DRAFT if which == "draft" else OTHER_GOLD
    closing = ("To finalize: complete and sign." if which == "draft" else
               "Finalized: gabapentin held at current dose; outpatient analgesic reassessment deferred.")
    body = [(True, "Clinical context"),
            (False, DRAFT_CONTEXT if which == "draft" else GOLD_CONTEXT),
            (True, "Overnight report"),
            (False, OVERNIGHT_REPORT),
            (True, "Assessment and plan"),
            (False, "1. " + gaba),
            (False, "2. " + other),
            (False, closing)]
    for is_h, t in body:
        insert_before(sig, heading_like if is_h else body_like, t)
    set_text(sig, DRAFT_FOOTER_NOTE if which == "draft" else GOLD_FOOTER_NOTE)
    edit_band_cell(d, "Document", doc_label,
                   "Discharge Summary - Working Draft" if which == "draft" else "Hospital Discharge Summary")
    edit_band_cell(d, "Attending", "E. Vossmere, MD",
                   "E. Vossmere, MD" if which == "draft" else "Elian Vossmere, MD")
    edit_footer(d, "Discharge Summary - Working Draft" if which == "draft" else "Hospital Discharge Summary",
                doc_label)
    d.save(tmp); scrub_core(tmp); integrity_gate(tmp)
    fname = ("neuropathic_pain_sleep_addendum_draft_05242026.docx" if which == "draft" else "golden-KM08-v4.docx")
    out = os.path.join(OUT, fname)
    shutil.copy(tmp, out)
    print(f"=== {which.upper()} ==="); verify_against_base(out, base); print("Saved:", fname)

if __name__ == "__main__":
    print("Building KM08 v4.1 (05/24 anchor, de-telegraphed)...")
    build("draft"); build("golden")
