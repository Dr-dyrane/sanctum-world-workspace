#!/usr/bin/env python3
"""Build the Marva Lydell World Spec DOCX via Mode A clone of the approved KM spec.

Clones the KM spec base (styles.xml, theme, numbering byte-identical), clears the
body, and rebuilds it from the audited submission markdown applying KM's exact
per-element design recipe, verified from the KM spec bytes:

  font            Arial throughout (inherited from docDefaults)
  body / tables   8pt (sz 16); cover banner 16pt (sz 32)
  cover box       D6E4F0 fill, 4472C4 bold text
  metadata table  label column D6E4F0 + bold; both columns 262B33 text
  data tables     header row 4472C4 fill + white bold; body cells 262B33
  draft prompt    its own 1x1 D6E4F0 box
  note callouts   e8f5e9 fill, 43a047 text (terminology, self-containment)

Fills stay in {4472C4, D6E4F0, e8f5e9}, borders in {000000, 43a047, 4472C4,
CCCCCC}, run colors in the base palette, so the Mode A fingerprint stays empty.
"""

from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.shared import Inches

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.mode_a_clone import integrity_gate, scrub_core, verify_against_base, make_deterministic  # noqa: E402

BASE = REPO / "worlds/korvin-merrow/file-review/pipeline-output/.meta/references/Alexander_World_Merrow_latest_6_4.docx"
SRC = REPO / "worlds/marva-lydell/submission/Marva_Lydell_World_Spec.md"
OUT = REPO / "worlds/marva-lydell/submission/Alexander_World_Marva_latest_6_20.docx"

LIGHTBLUE = "D6E4F0"
DARKBLUE = "4472C4"
GREENFILL = "e8f5e9"
BLUE = "4472C4"
WHITE = "FFFFFF"
BODY = "262B33"
GREEN = "43a047"
MUTED = "666666"   # cover subtitle gray
GRAY = "808080"    # callout body gray
SZ = "16"          # 8pt, KM table/body size
SUB_SZ = "20"      # 10pt, KM cover subtitle
SMALL_SZ = "13"    # 6.5pt, KM file-plan filenames
COVER_SZ = "32"    # 16pt, KM cover banner


def clear_body(doc) -> None:
    body = doc.element.body
    for child in list(body):
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)


def shade(cell, fill: str) -> None:
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)


def fmt_runs(cell, *, color: str, size: str, bold: bool) -> None:
    for p in cell.paragraphs:
        if not p.runs:
            continue
        for run in p.runs:
            rpr = run._r.get_or_add_rPr()
            if bold:
                rpr.append(OxmlElement("w:b"))
            c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
            s = OxmlElement("w:sz"); s.set(qn("w:val"), size); rpr.append(s)


def fmt_para(p, *, color: str, size: str, bold: bool, italic: bool = False, center: bool = False) -> None:
    if center:
        ppr = p._p.get_or_add_pPr()
        jc = OxmlElement("w:jc"); jc.set(qn("w:val"), "center"); ppr.append(jc)
    for run in p.runs:
        rpr = run._r.get_or_add_rPr()
        if bold:
            rpr.append(OxmlElement("w:b"))
        if italic:
            rpr.append(OxmlElement("w:i"))
        c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
        s = OxmlElement("w:sz"); s.set(qn("w:val"), size); rpr.append(s)


def set_borders(table, outer: str, inner: str) -> None:
    borders = OxmlElement("w:tblBorders")
    for edge, color in (("top", outer), ("left", outer), ("bottom", outer),
                        ("right", outer), ("insideH", inner), ("insideV", inner)):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0"); el.set(qn("w:color"), color)
        borders.append(el)
    table._tbl.tblPr.append(borders)


# File-plan 7-col widths (inches), sized for the landscape text area (~9.8in):
# # | ID | Filename.type | Date | Reference File Origin | Description | Pearls
FILEPLAN_W = [0.25, 0.48, 1.7, 1.0, 2.15, 2.42, 1.8]


def set_section(section, *, landscape: bool, margin: float) -> None:
    if landscape:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width, section.page_height = Inches(11), Inches(8.5)
    else:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width, section.page_height = Inches(8.5), Inches(11)
    section.left_margin = section.right_margin = Inches(margin)
    section.top_margin = section.bottom_margin = Inches(margin)


def set_fixed_widths(table, widths) -> None:
    """Fixed table layout with per-column widths so no column clips in Word."""
    table.autofit = False
    table.allow_autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for r in range(len(table.rows)):
        for c, w in enumerate(widths):
            table.cell(r, c).width = Inches(w)


def add_data_table(doc, rows, *, meta=False) -> None:
    if not rows:
        return
    ncol = len(rows[0])
    t = doc.add_table(rows=len(rows), cols=ncol)
    t.style = "TableNormal"
    if meta:
        set_borders(t, outer="000000", inner="CCCCCC")
        for r in range(len(rows)):
            for c in range(ncol):
                cell = t.cell(r, c)
                cell.text = rows[r][c] if c < len(rows[r]) else ""
                if c == 0:
                    shade(cell, LIGHTBLUE)
                    fmt_runs(cell, color=BODY, size=SZ, bold=True)
                else:
                    fmt_runs(cell, color=BODY, size=SZ, bold=False)
    else:
        set_borders(t, outer=DARKBLUE, inner="CCCCCC")
        is_fileplan = rows[0][:3] == ["#", "ID", "Filename.type"]
        for r, row in enumerate(rows):
            for c in range(ncol):
                cell = t.cell(r, c)
                cell.text = row[c] if c < len(row) else ""
                if r == 0:
                    shade(cell, DARKBLUE)
                    fmt_runs(cell, color=WHITE, size=SZ, bold=True)
                elif is_fileplan and c == 2:
                    fmt_runs(cell, color=BODY, size=SMALL_SZ, bold=False)  # 6.5pt filenames
                else:
                    fmt_runs(cell, color=BODY, size=SZ, bold=False)
        if is_fileplan and ncol == len(FILEPLAN_W):
            set_fixed_widths(t, FILEPLAN_W)


def add_box(doc, text: str, *, fill: str, color: str, bold: bool, size: str, border: str) -> None:
    t = doc.add_table(rows=1, cols=1)
    t.style = "TableNormal"
    set_borders(t, outer=border, inner=border)
    cell = t.cell(0, 0)
    cell.text = text
    shade(cell, fill)
    fmt_runs(cell, color=color, size=size, bold=bold)


def add_cover_box(doc, title: str, subtitles: list) -> None:
    """Cover banner (KM pattern): centered blue bold title (16pt) over centered
    muted-gray subtitle lines (10pt)."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "TableNormal"
    set_borders(t, outer="000000", inner="000000")
    cell = t.cell(0, 0)
    shade(cell, LIGHTBLUE)
    cell.paragraphs[0].text = title
    fmt_para(cell.paragraphs[0], color=BLUE, size=COVER_SZ, bold=True, center=True)
    for sub in subtitles:
        if sub.strip():
            psub = cell.add_paragraph(sub.strip())
            fmt_para(psub, color=MUTED, size=SUB_SZ, bold=False, center=True)


def add_header_block(doc, fields) -> None:
    """Soya-style header block: one 5-col table. Row 1 codename banner (blue fill, white
    bold), row 2 descriptive title (bold), then Patient / World Type / Setting / Workflows
    as full-width merged rows, then a 5-col footer (Specialty | Tasks | Project | Version |
    Date). Fills stay in {4472C4, D6E4F0} so the Mode A fingerprint stays empty."""
    info = [("Patient", fields.get("Patient", "")),
            ("World Type", fields.get("World Type", "")),
            ("Setting", fields.get("Setting", "")),
            ("Workflows", fields.get("Workflows", ""))]
    tasks = fields.get("Total Tasks", "").strip()
    ver = fields.get("Version", "").strip()
    footer = [fields.get("Specialty", ""),
              (tasks + " Tasks") if tasks else "",
              fields.get("Project", "Project Sanctum"),
              ("Version " + ver) if ver else "",
              fields.get("Document date", "")]
    nrows = 2 + len(info) + 1
    t = doc.add_table(rows=nrows, cols=5)
    t.style = "TableNormal"
    set_borders(t, outer="000000", inner="000000")

    def merged(r):
        cells = t.rows[r].cells
        m = cells[0]
        for cc in cells[1:]:
            m = m.merge(cc)
        return m

    b = merged(0); shade(b, DARKBLUE); b.text = fields.get("Codename", "")
    fmt_para(b.paragraphs[0], color=WHITE, size=COVER_SZ, bold=True, center=True)
    ti = merged(1); shade(ti, LIGHTBLUE); ti.text = fields.get("Title", "")
    fmt_para(ti.paragraphs[0], color=BODY, size=SUB_SZ, bold=True, center=True)
    for k, (label, val) in enumerate(info):
        cc = merged(2 + k); shade(cc, LIGHTBLUE); cc.text = f"{label}: {val}"
        fmt_para(cc.paragraphs[0], color=BODY, size=SZ, bold=False, center=True)
    fr = nrows - 1
    for c in range(5):
        cell = t.cell(fr, c); shade(cell, LIGHTBLUE); cell.text = footer[c]
        cell.width = Inches(1.3)
        fmt_para(cell.paragraphs[0], color=BODY, size=SZ, bold=False, center=True)


def add_note_box(doc, text: str) -> None:
    """Green note callout: green bold label before the first colon, italic gray body."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "TableNormal"
    set_borders(t, outer=GREEN, inner=GREEN)
    cell = t.cell(0, 0)
    shade(cell, GREENFILL)
    p = cell.paragraphs[0]
    if ": " in text:
        label, body = text.split(": ", 1)
        r1 = p.add_run(label + ": ")
        rpr = r1._r.get_or_add_rPr()
        rpr.append(OxmlElement("w:b"))
        c = OxmlElement("w:color"); c.set(qn("w:val"), GREEN); rpr.append(c)
        s = OxmlElement("w:sz"); s.set(qn("w:val"), SZ); rpr.append(s)
        r2 = p.add_run(body)
        rpr2 = r2._r.get_or_add_rPr()
        rpr2.append(OxmlElement("w:i"))  # italic body, KM terminology-box style
        c2 = OxmlElement("w:color"); c2.set(qn("w:val"), GRAY); rpr2.append(c2)
        s2 = OxmlElement("w:sz"); s2.set(qn("w:val"), SZ); rpr2.append(s2)
    else:
        p.text = text
        fmt_para(p, color=GRAY, size=SZ, bold=False, italic=True)


def parse_md_table(block):
    rows = []
    for ln in block:
        if ln.replace("|", "").replace("-", "").replace(":", "").strip() == "":
            continue
        rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
    return rows


def build() -> None:
    md = SRC.read_text(encoding="utf-8")
    doc = Document(str(BASE))
    clear_body(doc)

    lines = md.split("\n")
    i, n = 0, len(lines)
    first_table_seen = False
    while i < n:
        ln = lines[i]
        if ln.startswith("|"):
            block = []
            while i < n and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            rows = parse_md_table(block)
            if not first_table_seen:
                add_header_block(doc, {r[0]: r[1] for r in rows[1:] if len(r) >= 2})
            else:
                add_data_table(doc, rows, meta=False)
            first_table_seen = True
            continue
        if ln.startswith("# "):
            title = ln[2:].strip()
            # KM pattern: wide file-plan tables go in a landscape section so no column clips.
            if title.startswith("3. World File Plan"):
                set_section(doc.add_section(WD_SECTION.NEW_PAGE), landscape=True, margin=0.6)
            elif title.startswith("4. World Summary"):
                set_section(doc.add_section(WD_SECTION.NEW_PAGE), landscape=False, margin=1.0)
            doc.add_paragraph(title, style="Heading 1")
        elif ln.startswith("## "):
            doc.add_paragraph(ln[3:].strip(), style="Heading 2")
        elif ln.startswith("### "):
            doc.add_paragraph(ln[4:].strip(), style="Heading 2")
        elif ln.startswith("Cover:"):
            parts = [s.strip() for s in ln[len("Cover:"):].split("||")]
            add_cover_box(doc, parts[0], parts[1:])
        elif ln.startswith("Draft Prompt:"):
            add_box(doc, ln.strip(), fill=LIGHTBLUE, color=BODY,
                    bold=False, size=SZ, border=DARKBLUE)
        elif ln.startswith("Terminology note:") or ln.startswith("Self-Containment Principle:"):
            add_note_box(doc, ln.strip())
        elif ln.startswith("Anchor:"):
            p = doc.add_paragraph(ln.strip(), style="normal")
            fmt_para(p, color=BODY, size="19", bold=False)  # 9.5pt task meta line
        elif ln.strip() == "":
            pass
        else:
            p = doc.add_paragraph(ln.strip(), style="normal")
            fmt_para(p, color=BODY, size=SZ, bold=False)
        i += 1

    doc.save(str(OUT))
    scrub_core(str(OUT))
    make_deterministic(str(OUT))
    print("integrity gate:", integrity_gate(str(OUT)))
    print("verify_against_base:", verify_against_base(str(OUT), str(BASE)))
    print("written:", OUT)


if __name__ == "__main__":
    build()
