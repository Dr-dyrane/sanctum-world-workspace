#!/usr/bin/env python3
"""Render the OV08 task-layer docx (started concurrent-stay review + golden) on the
Harbor Crest template. UR Concurrent Stay lane, de-telegraphed carry-forward engine.
Outputs into platform/task8/current/. No em/en dashes; ASCII hyphens and straight quotes only.
"""
import os
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = os.path.join(os.path.dirname(__file__), "..", "platform", "task8", "current")
OUT = os.path.abspath(OUT)

PATIENT = [
    ("Patient", "Ondina Vasquell, 68 y"),
    ("Sex / DOB", "Female / 03/14/1958"),
    ("MRN / FIN", "OV-3358104 / FIN-2207733"),
    ("Unit / Room", "6 South Medicine / 6S-214"),
    ("Code Status", "Full Code"),
    ("Allergies", "Sulfa (sulfonamide antibiotics) - rash"),
    ("Attending", "Lillian Everet, MD"),
    ("Service", "Hospital Medicine"),
    ("Admission", "05/16/2026 | Hospital Day 7"),
    ("Level of Care", "Acute inpatient"),
    ("Payer", "Medicare Advantage (primary), Medicaid (secondary)"),
    ("Language", "Spanish preferred (interpreter used)"),
]

def _set_font(run, size=10, bold=False, color=None):
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)

def _line(doc, text, size=10, bold=False, color=None, space_after=2, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    if align:
        p.alignment = align
    _set_font(p.add_run(text), size, bold, color)
    return p

def _header(doc, status_line):
    _line(doc, "Harbor Crest Regional Medical Center", 13, True, (0x1F, 0x3A, 0x5F))
    _line(doc, "Utilization Review / Care Management", 10, True, (0x1F, 0x3A, 0x5F))
    _line(doc, "Confidential", 8, False, (0x80, 0x80, 0x80), space_after=6)
    _line(doc, "Ondina Vasquell    68 y  |  Female  |  DOB 03/14/1958", 10, True)
    _line(doc, "MRN OV-3358104", 9, False, (0x55, 0x55, 0x55))
    _line(doc, "Date of Service 05/22/2026", 9, False, (0x55, 0x55, 0x55))
    _line(doc, "Author Utilization Review", 9, False, (0x55, 0x55, 0x55))
    _line(doc, "Allergies Sulfa (sulfonamide antibiotics) - rash", 9, False, (0x55, 0x55, 0x55))
    _line(doc, "Document CONCURRENT STAY REVIEW", 9, False, (0x55, 0x55, 0x55), space_after=8)
    _line(doc, "CONCURRENT STAY REVIEW - Continued-Stay and Discharge Readiness", 12, True, space_after=2)
    _line(doc, status_line, 9, False, (0x55, 0x55, 0x55), space_after=8)

def _patient_block(doc):
    _line(doc, "PATIENT / ENCOUNTER", 10, True, space_after=2)
    for k, v in PATIENT:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.space_before = Pt(0)
        _set_font(p.add_run(k + ": "), 9, True)
        _set_font(p.add_run(v), 9, False)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def _section(doc, title, body):
    _line(doc, title, 10, True, space_after=2)
    for para in body:
        _line(doc, para, 10, False, space_after=6)

def _table(doc, rows):
    _line(doc, "CRITERIA AND DISPOSITION TABLE", 10, True, space_after=2)
    t = doc.add_table(rows=1, cols=2)
    t.style = "Table Grid"
    hdr = t.rows[0].cells
    for c, txt in zip(hdr, ("Item", "Status")):
        c.paragraphs[0].paragraph_format.space_after = Pt(1)
        _set_font(c.paragraphs[0].add_run(txt), 9, True)
    for item, status in rows:
        r = t.add_row().cells
        r[0].paragraphs[0].paragraph_format.space_after = Pt(1)
        _set_font(r[0].paragraphs[0].add_run(item), 9, True)
        r[1].paragraphs[0].paragraph_format.space_after = Pt(1)
        _set_font(r[1].paragraphs[0].add_run(status), 9, False)
    # column widths
    for row in t.rows:
        row.cells[0].width = Pt(150)
        row.cells[1].width = Pt(360)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def _sig(doc, who):
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    _line(doc, who, 9, False, (0x33, 0x33, 0x33))

def _scrub(doc):
    cp = doc.core_properties
    cp.author = ""
    cp.last_modified_by = ""
    cp.title = ""
    cp.subject = ""
    cp.comments = ""
    cp.keywords = ""
    cp.category = ""
    cp.content_status = ""

# ---------- STARTED REVIEW (the inherited draft to finalize; leans discharge) ----------
def build_started():
    doc = Document()
    _header(doc, "Author: M. Olarte, RN - Utilization Review | Date of Service: 05/22/2026 0900 | Status: Draft for UR finalization")
    _patient_block(doc)
    _section(doc, "REASON FOR REVIEW", [
        "Concurrent utilization review of continued inpatient stay for a treated limb-threatening left diabetic foot infection. This review supports the payer continued-stay determination and discharge planning."])
    _section(doc, "INTERVAL SUMMARY (HD6 to HD7)", [
        "Continued clinical improvement. Afebrile and hemodynamically stable. WBC normalized at 8.9. Soft-tissue infection improving on culture-directed, renally dosed therapy. Surgical pathology 05/20 excluded osteomyelitis (no bone in the specimen, no definitive features of osteomyelitis). Left forefoot wound granulating with scant drainage. Creatinine 1.6, near baseline 1.5. Patient feeling better and asking to go home."])
    _table(doc, [
        ("Infection / source control", "Improving. Debrided HD2, granulating base, osteomyelitis excluded on pathology 05/20. Afebrile, WBC normalized."),
        ("Antibiotics", "Vancomycin, piperacillin-tazobactam, and cefepime, culture-directed and renally dosed, clinically improving. Continue."),
        ("Perfusion", "Vascular question deferred to outpatient. Outpatient vascular follow-up being arranged; manageable after discharge."),
        ("Renal (AKI on CKD)", "Improving and stable. Creatinine 1.6, near baseline 1.5. Held home agents to be addressed at discharge per renal recovery."),
        ("Offloading / mobility", "Discharge planning in progress. Offloading device ordered; PT working toward stair clearance."),
        ("Home support", "Discharge planning in progress. Home-health wound nursing referral placed; caregiver teaching underway with case management and interpreter."),
        ("Follow-up", "Outpatient vascular, wound care, and primary care to be arranged at discharge."),
    ])
    _section(doc, "ASSESSMENT", [
        "Patient is clinically improved and stable. The acute infection is responding, osteomyelitis is excluded, and renal function is near baseline. Remaining items are discharge-planning logistics being worked by case management. Acute medical drivers are resolving and the patient is progressing toward discharge home."])
    _section(doc, "DISPOSITION (DRAFT)", [
        "Anticipate discharge home with home-health wound nursing for dressing changes and outpatient follow-up, pending completion of home-health setup. Continued acute inpatient stay justified only for the short interval needed to finalize the home plan.",
        "[Status: Draft for UR finalization.]"])
    _scrub(doc)
    doc.save(os.path.join(OUT, "started_concurrent_stay_review_05222026.docx"))

# ---------- GOLDEN (correct finalization: holds discharge on the antibiotic route) ----------
def build_golden():
    doc = Document()
    _header(doc, "Author: M. Olarte, RN - Utilization Review (finalized) | Date of Service: 05/22/2026 | Status: Final for payer submission")
    _patient_block(doc)
    _section(doc, "REASON FOR REVIEW", [
        "Concurrent utilization review of continued inpatient stay for a treated limb-threatening left diabetic foot infection. This review supports the payer continued-stay determination and discharge planning."])
    _section(doc, "INTERVAL SUMMARY (HD6 to HD7)", [
        "Continued clinical improvement. Afebrile and hemodynamically stable. WBC normalized at 8.9. Soft-tissue infection improving on culture-directed, renally dosed therapy. Surgical pathology 05/20 excluded osteomyelitis. Left forefoot wound granulating with scant drainage. Creatinine 1.6, near baseline 1.5. Patient feeling better and asking to go home."])
    _table(doc, [
        ("Infection / source control", "Improving. Debrided HD2, granulating base, osteomyelitis excluded on pathology 05/20. Afebrile, WBC normalized."),
        ("Antibiotics (discharge barrier)", "Active parenteral therapy. Vancomycin, piperacillin-tazobactam, and cefepime IV, culture-directed and renally dosed, ongoing per the 05/21 MAR. No oral conversion is established: the documented sulfa allergy excludes trimethoprim-sulfamethoxazole despite susceptibility, and Infectious Disease has not finalized an oral regimen (the 05/19 plan note states it is not a final discharge antibiotic synthesis). No OPAT or home infusion is arranged. Home-health wound nursing does not administer intravenous antibiotics."),
        ("Perfusion", "Unresolved; reasonable to defer to outpatient vascular follow-up."),
        ("Renal (AKI on CKD)", "Improving and stable. Creatinine 1.6, near baseline 1.5. Held agents pending restart parameters."),
        ("Offloading / mobility", "Discharge planning in progress. Offloading device and stair clearance not yet completed."),
        ("Home support", "Discharge planning in progress. Home-health wound nursing referral placed; caregiver teaching not complete."),
        ("Follow-up", "Outpatient vascular, wound care, and primary care to be arranged."),
    ])
    _section(doc, "DETERMINATION", [
        "Continued acute inpatient stay is medically necessary. The patient does not meet criteria for discharge home today. The active intravenous antibiotic requirement for a limb-threatening diabetic foot infection has no established oral conversion (sulfa allergy) and no OPAT arranged, and home-health wound nursing cannot administer intravenous antibiotics. Discharge home today would interrupt antibiotic therapy and risk treatment failure, readmission, and limb loss."])
    _section(doc, "PLAN TO CLEAR THE STAY", [
        "Resolve the antibiotic route before discharge: establish a suitable oral regimen with Infectious Disease, accounting for the sulfa allergy and renal function, OR arrange a parenteral-capable level of care (OPAT or home infusion, or a skilled nursing facility) to complete the intravenous course. Complete offloading, stair clearance, and home-health setup in parallel. Re-review for discharge readiness when the antibiotic route and the home plan are confirmed."])
    _section(doc, "DISPOSITION (FINAL)", [
        "Continued inpatient stay certified as medically necessary on hospital day 7. Discharge home today is not supported. Discharge only once the antibiotic route is resolved and the home plan is confirmed, or transition to a skilled facility capable of completing parenteral therapy."])
    _scrub(doc)
    doc.save(os.path.join(OUT, "golden-OV08-v1.docx"))

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_started()
    build_golden()
    print("OV08 docx written to", OUT)
