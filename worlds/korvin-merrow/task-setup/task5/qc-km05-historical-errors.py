#!/usr/bin/env python3
"""KM05 audit against every known error class from KM01-KM04 logs + AutoQC preflight."""
import zipfile, re, os
from docx import Document

BASE = r"c:\Users\Dyrane\Documents\sanctum-world-workspace\worlds\korvin-merrow\task-setup\platform\task5\current"

fails = []
warns = []
def check(label, result, critical=True):
    status = "OK" if result else ("FAIL" if critical else "WARN")
    print(f"  [{status:4s}] {label}")
    if not result:
        (fails if critical else warns).append(label)

# Load all files
prompt = open(f"{BASE}\\prompt-task5-v2.txt", encoding="utf-8").read()
grader = open(f"{BASE}\\grader-guidelines-task5-v2.txt", encoding="utf-8").read()

draft_path = f"{BASE}\\transition_clinic_followup_note_draft_05312026.docx"
golden_path = f"{BASE}\\golden-KM05-v2.docx"
d = Document(draft_path)
g = Document(golden_path)

def all_text(doc, path):
    t = ""
    for p in doc.paragraphs: t += p.text + "\n"
    for tb in doc.tables:
        for r in tb.rows:
            for c in r.cells: t += c.text + "\n"
    for s in doc.sections:
        for fp in s.footer.paragraphs: t += fp.text + "\n"
        for hp in s.header.paragraphs: t += hp.text + "\n"
    return t

def xml_text(path):
    return zipfile.ZipFile(path).read("word/document.xml").decode()

def core_xml(path):
    return zipfile.ZipFile(path).read("docProps/core.xml").decode()

draft_text = all_text(d, draft_path)
golden_text = all_text(g, golden_path)
draft_xml = xml_text(draft_path)
golden_xml = xml_text(golden_path)
draft_core = core_xml(draft_path)
golden_core = core_xml(golden_path)

# =====================================================================
print("=" * 70)
print("ERROR CLASS 1: PYTHON-DOCX METADATA LEAK (KM02 footer lesson)")
print("  Source: KM02-learnings #7, guardrails-lessons #4")
print("=" * 70)
check("Draft core: no 'python-docx' string", "python-docx" not in draft_core)
check("Golden core: no 'python-docx' string", "python-docx" not in golden_core)
check("Draft core: dc:creator empty", "<dc:creator></dc:creator>" in draft_core or "<dc:creator/>" in draft_core)
check("Draft core: dc:description empty", "<dc:description></dc:description>" in draft_core or "<dc:description/>" in draft_core)
check("Draft core: cp:lastModifiedBy empty", "<cp:lastModifiedBy></cp:lastModifiedBy>" in draft_core or "<cp:lastModifiedBy/>" in draft_core)
check("Golden core: dc:creator empty", "<dc:creator></dc:creator>" in golden_core or "<dc:creator/>" in golden_core)
check("Golden core: dc:description empty", "<dc:description></dc:description>" in golden_core or "<dc:description/>" in golden_core)
check("Golden core: cp:lastModifiedBy empty", "<cp:lastModifiedBy></cp:lastModifiedBy>" in golden_core or "<cp:lastModifiedBy/>" in golden_core)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 2: SYNTHETIC FOOTER / BANNER (KM02 lesson #7)")
print("  Source: KM02-learnings #7, task1-lifecycle-log BANNER lines")
print("=" * 70)
check("Draft XML: no 'Synthetic' token", "Synthetic" not in draft_xml)
check("Golden XML: no 'Synthetic' token", "Synthetic" not in golden_xml)
check("Draft XML: no 'SYNTHETIC TRAINING' banner", "SYNTHETIC TRAINING" not in draft_xml)
check("Golden XML: no 'SYNTHETIC TRAINING' banner", "SYNTHETIC TRAINING" not in golden_xml)
check("Draft footer: no 'Synthetic'", "synthetic" not in draft_text.lower().split("FOOTER")[-1] if "FOOTER" in draft_text else True)
check("Golden footer: no 'Synthetic'", "synthetic" not in golden_text.lower())

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 3: EM DASH / EN DASH / ARROW (guardrails #12, KM01 lifecycle)")
print("=" * 70)
check("Draft XML: em dash count = 0", draft_xml.count("\u2014") == 0)
check("Draft XML: en dash count = 0", draft_xml.count("\u2013") == 0)
check("Draft XML: arrow count = 0", draft_xml.count("\u2192") == 0)
check("Golden XML: em dash count = 0", golden_xml.count("\u2014") == 0)
check("Golden XML: en dash count = 0", golden_xml.count("\u2013") == 0)
check("Golden XML: arrow count = 0", golden_xml.count("\u2192") == 0)
check("Grader: em dash count = 0", grader.count("\u2014") == 0)
check("Grader: en dash count = 0", grader.count("\u2013") == 0)
check("Prompt: em dash count = 0", prompt.count("\u2014") == 0)
check("Prompt: en dash count = 0", prompt.count("\u2013") == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 4: SCORING / WEIGHT LANGUAGE (KM01 lifecycle v8->v9 lesson)")
print("  Source: task1-lifecycle-log GRADER v8->v9, KM02-learnings")
print("=" * 70)
banned = ["weight", "cap the score", "primary discriminator", "lower-weight",
          "most discriminating", "passing band", "score below", "score well below",
          "scoring framework", "numeric weight", "percentage", "out of 100",
          "fails the task", "failing answer"]
hits = [w for w in banned if w in grader.lower()]
check(f"Grader: no scoring/weight language (found: {hits})", len(hits) == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 5: REGISTER / META-LANGUAGE LEAK (guardrails #10)")
print("=" * 70)
meta_words = ["the world tests", "locked workflow", "this artifact", "submission candidate",
              "benchmark", "architecture", "friction", "trap", "plant", "fabricat",
              "golden response", "grader guid", "expected output", "rubric"]
for label, text in [("Draft", draft_text), ("Golden", golden_text), ("Prompt", prompt)]:
    hits = [w for w in meta_words if w in text.lower()]
    check(f"{label}: no meta-language leak (found: {hits})", len(hits) == 0)
# Grader is allowed to reference golden and grading terms
grader_meta = [w for w in ["trap", "plant", "friction", "benchmark", "architecture",
                            "the world tests", "submission candidate"] if w in grader.lower()]
check(f"Grader: no internal architecture language (found: {grader_meta})", len(grader_meta) == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 6: DATE CONSISTENCY (KM02 golden-date miss, guardrails #13)")
print("=" * 70)
check("Prompt has visit date 5/31", "5/31" in prompt)
check("Draft band has 05/31/2026", "05/31/2026" in draft_text)
check("Golden band has 05/31/2026", "05/31/2026" in golden_text)
# No fabricated interval dates
date_pat = re.compile(r"05/(2[5-9]|30)/2026")
check("Draft: no fabricated dates 05/25-05/30", len(date_pat.findall(draft_text)) == 0)
check("Golden: no fabricated dates 05/25-05/30", len(date_pat.findall(golden_text)) == 0)
# Hospitalization dates correct
check("Draft: hospitalization 05/18 to 05/24", "05/18" in draft_text and "05/24" in draft_text)
check("Golden: hospitalization 05/18 to 05/24", "05/18" in golden_text and "05/24" in golden_text)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 7: FONT / CHROME MISMATCH (KM01 lifecycle CHROME VERIFIED)")
print("=" * 70)
from docx.shared import RGBColor
draft_colors = set()
golden_colors = set()
for p in d.paragraphs:
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            draft_colors.add(str(r.font.color.rgb))
for p in g.paragraphs:
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            golden_colors.add(str(r.font.color.rgb))
expected_colors = {"1F3864", "5E6670", "4472C4", "232830"}
check(f"Draft body colors subset of expected {expected_colors}: {draft_colors}", draft_colors <= expected_colors)
check(f"Golden body colors subset of expected {expected_colors}: {golden_colors}", golden_colors <= expected_colors)

# Check for Calibri (world is Arial 24/26)
check("Draft XML: no Calibri font", "Calibri" not in draft_xml)
check("Golden XML: no Calibri font", "Calibri" not in golden_xml)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 8: STYLES.XML IDENTITY (Mode A requirement)")
print("=" * 70)
import hashlib
task_base = r"c:\Users\Dyrane\Documents\sanctum-world-workspace\worlds\korvin-merrow\task-setup\platform\task2\current\discharge_summary_draft_incomplete_05242026.docx"
golden_base = r"c:\Users\Dyrane\Documents\sanctum-world-workspace\worlds\korvin-merrow\task-setup\platform\task2\current\golden-KM02-v5.docx"

draft_styles_md5 = hashlib.md5(zipfile.ZipFile(draft_path).read("word/styles.xml")).hexdigest()
golden_styles_md5 = hashlib.md5(zipfile.ZipFile(golden_path).read("word/styles.xml")).hexdigest()
base_task_styles = hashlib.md5(zipfile.ZipFile(task_base).read("word/styles.xml")).hexdigest()
base_golden_styles = hashlib.md5(zipfile.ZipFile(golden_base).read("word/styles.xml")).hexdigest()

check(f"Draft styles.xml == task base styles.xml ({draft_styles_md5[:8]} == {base_task_styles[:8]})", draft_styles_md5 == base_task_styles)
check(f"Golden styles.xml == golden base styles.xml ({golden_styles_md5[:8]} == {base_golden_styles[:8]})", golden_styles_md5 == base_golden_styles)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 9: LETTER-O 'PO' ROUTE TOKEN (KM01 lifecycle)")
print("=" * 70)
po_pattern = re.compile(r"\bPO\b")
check("Draft: no 'PO' route token (use 'Oral')", len(po_pattern.findall(draft_text)) == 0)
check("Golden: no 'PO' route token (use 'Oral')", len(po_pattern.findall(golden_text)) == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 10: INVENTED CLINICAL SPECIFICITY (guardrails #5)")
print("=" * 70)
check("Draft: no fabricated post-discharge labs/vitals", "resulted" not in draft_text.lower() or "pending" in draft_text.lower())
check("Golden: no fabricated post-discharge labs/vitals", "resulted" not in golden_text.lower() or "pending" in golden_text.lower())
check("Draft: interval honestly thin", "available yet" in draft_text.lower())
check("Golden: interval honestly thin", "available yet" in golden_text.lower())
# No invented encounter/FIN numbers
check("Draft: FIN is 'Outpatient Visit' not invented number", "Outpatient Visit" in draft_text)
check("Golden: FIN is 'Outpatient Visit' not invented number", "Outpatient Visit" in golden_text)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 11: GRADER STRUCTURE - SANG REQUIREMENTS (KM03 Sang fix)")
print("=" * 70)
check("Preamble section present", grader.startswith("Preamble"))
check("Register Note section present", "\nRegister Note\n" in grader)
check("Section A present", "\nSection A." in grader)
check("Section B present with variation clause", "\nSection B." in grader)
check("Section C present", "\nSection C." in grader)
check("Section C verbatim opener", "These are patterns to reason about, not items to tick off." in grader)
check("Correct-restraint credit pattern in Section C", "Correct restraint" in grader)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 12: AUTOQC PREFLIGHT")
print("=" * 70)
# Self-Contained Guidelines warning expected
check("Grader references chart file (expect Self-Contained warning)", "nephrology_consultation_05212026.docx" in grader, critical=False)
# Golden filename match
check("Grader names golden-KM05-v2.docx (must match upload)", "golden-KM05-v2.docx" in grader)
# Reuse acknowledgment for AutoQC 2.91 duplicate trap check
check("Grader acknowledges Task 1 reuse (for AutoQC 2.91)", "Task 1" in grader or "reuses" in grader.lower())
# No Weight Distribution / No Scoring Framework
check("No weight/rank/scale language that trips AutoQC", len(hits) == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 13: MOJIBAKE / ENCODING (guardrails #12)")
print("=" * 70)
mojibake_chars = ["\u00c2", "\ufffd"]  # A-circumflex, replacement char
for label, text in [("Draft", draft_text), ("Golden", golden_text), ("Grader", grader), ("Prompt", prompt)]:
    has_mojibake = any(c in text for c in mojibake_chars)
    check(f"{label}: no mojibake markers (A-circumflex, U+FFFD)", not has_mojibake)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 14: KEYWORD-TELL / TRAP CUE IN PROMPT (KM01 lifecycle)")
print("=" * 70)
tell_words = ["nsaid", "ibuprofen", "nephrotox", "unsafe", "contraindic", "kidney",
              "renal", "ckd", "aki", "safety", "error", "wrong", "trap"]
prompt_hits = [w for w in tell_words if w in prompt.lower()]
check(f"Prompt: no trap keyword tells (found: {prompt_hits})", len(prompt_hits) == 0)

# =====================================================================
print("\n" + "=" * 70)
print("ERROR CLASS 15: INTEGRITY GATE (guardrails #4, KM01 lifecycle)")
print("=" * 70)
for label, path in [("Draft", draft_path), ("Golden", golden_path)]:
    raw = open(path, "rb").read()
    check(f"{label}: EOCD present (not truncated)", raw.find(b"PK\x05\x06") >= 0)
    names = zipfile.ZipFile(path).namelist()
    check(f"{label}: word/styles.xml present", "word/styles.xml" in names)
    check(f"{label}: word/document.xml present", "word/document.xml" in names)
    try:
        Document(path)
        check(f"{label}: python-docx opens successfully", True)
    except:
        check(f"{label}: python-docx opens successfully", False)

# =====================================================================
print("\n" + "=" * 70)
if fails:
    print(f"RESULT: {len(fails)} FAILURES, {len(warns)} WARNINGS")
    for f in fails:
        print(f"  FAIL: {f}")
    for w in warns:
        print(f"  WARN: {w}")
else:
    print(f"RESULT: ALL CHECKS PASSED ({len(warns)} warnings)")
    for w in warns:
        print(f"  WARN: {w}")
print("=" * 70)
