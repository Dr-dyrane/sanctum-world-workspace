#!/usr/bin/env python3
"""Epic-style note renderer for the Ondina Vasquell world files.

Recipe extracted from the shipped-clean KM base bytes (ed_provider_assessment):
  font            Arial throughout (Normal style = Arial 9.5pt)
  body            sz 19 (9.5pt), black
  section header  sz 20 (10pt) BOLD black, plain (no navy) - matches KM bytes
  note title      sz 24 (12pt) BOLD black
  masthead table  1x2, no fill, sz 22 bold
  patient banner  fill EAEAEA, sz 18 grid
  margins         top 0.5in, bottom 0.55in, left/right 0.65in (inherited from clone)

Hard rule: GUARD() rejects any banned character (em/en dash, arrow, asterisk,
square bracket, degree, multiply, superscripts) before it can reach a file.
All chrome is rebuilt after clear_body so NO base (KM) content can survive.
"""
from __future__ import annotations
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLACK = "000000"
GRAYLABEL = "595959"
BANNERFILL = "EAEAEA"
RULE = "BFBFBF"
BODY_SZ = "19"      # 9.5pt
SEC_SZ = "20"       # 10pt
TITLE_SZ = "24"     # 12pt
MAST_SZ = "22"      # 11pt
BANNER_SZ = "18"    # 9pt
SMALL_SZ = "17"     # 8.5pt filing/signature

BANNED = {"—": "-", "–": "-", "→": " to ", "•": "-",
          "*": "", "[": "(", "]": ")", "°": " ", "×": "x",
          "⁹": "9", "¹": "1", "⁰": "0"}


def GUARD(text: str) -> str:
    """Reject banned characters outright; callers must pre-clean. Returns text
    unchanged if clean, else raises so a bad char can never be written silently."""
    bad = [c for c in text if c in BANNED]
    if bad:
        raise ValueError(f"banned character {bad!r} in: {text[:60]!r}")
    return text


def clear_body(doc) -> None:
    body = doc.element.body
    for child in list(body):
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)


def _runfmt(run, *, size, bold, color=BLACK, italic=False):
    rpr = run._r.get_or_add_rPr()
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "Arial"); fonts.set(qn("w:hAnsi"), "Arial")
    rpr.append(fonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
    s = OxmlElement("w:sz"); s.set(qn("w:val"), size); rpr.append(s)


def _shade(cell, fill):
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)


def _borders(table, color=RULE):
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        b.append(e)
    table._tbl.tblPr.append(b)


def facility_band(doc, facility, filed):
    GUARD(facility); GUARD(filed)
    t = doc.add_table(rows=1, cols=2); t.style = "TableNormal"
    t.cell(0, 0).text = facility
    _runfmt(t.cell(0, 0).paragraphs[0].runs[0], size=MAST_SZ, bold=True)
    t.cell(0, 1).text = filed
    p = t.cell(0, 1).paragraphs[0]
    p.alignment = 2  # right
    _runfmt(p.runs[0], size="15", bold=False, color=GRAYLABEL)
    doc.add_paragraph()


def patient_banner(doc, name, mrn, grid):
    """grid: list of (label, value) pairs rendered 4-up under a name row."""
    GUARD(name); GUARD(mrn)
    rows = 1 + (len(grid) + 1) // 2
    t = doc.add_table(rows=rows, cols=4); t.style = "TableNormal"
    _borders(t)
    # name row spans
    top = t.cell(0, 0).merge(t.cell(0, 3))
    _shade(top, BANNERFILL)
    p = top.paragraphs[0]
    r1 = p.add_run(name); _runfmt(r1, size="22", bold=True)
    r2 = p.add_run("      MRN " + mrn); _runfmt(r2, size=BANNER_SZ, bold=True)
    r = 1; c = 0
    for label, value in grid:
        GUARD(label); GUARD(str(value))
        lc = t.cell(r, c); _shade(lc, BANNERFILL)
        rl = lc.paragraphs[0].add_run(label); _runfmt(rl, size="16", bold=True, color=GRAYLABEL)
        vc = t.cell(r, c + 1); _shade(vc, BANNERFILL)
        rv = vc.paragraphs[0].add_run(str(value)); _runfmt(rv, size=BANNER_SZ, bold=False)
        c += 2
        if c > 3:
            c = 0; r += 1
    doc.add_paragraph()


def note_title(doc, title):
    GUARD(title)
    p = doc.add_paragraph(); r = p.add_run(title)
    _runfmt(r, size=TITLE_SZ, bold=True)


def filing_line(doc, text):
    GUARD(text)
    p = doc.add_paragraph(); r = p.add_run(text)
    _runfmt(r, size=SMALL_SZ, bold=False, color=GRAYLABEL)
    doc.add_paragraph()


def section(doc, name):
    GUARD(name)
    p = doc.add_paragraph(); r = p.add_run(name)
    _runfmt(r, size=SEC_SZ, bold=True)
    # thin bottom rule
    ppr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), RULE)
    pbdr.append(bottom); ppr.append(pbdr)


def body(doc, text, *, bold=False):
    GUARD(text)
    p = doc.add_paragraph(); r = p.add_run(text)
    _runfmt(r, size=BODY_SZ, bold=bold)


def bullets(doc, items):
    for it in items:
        GUARD(it)
        p = doc.add_paragraph(style="List Bullet"); r = p.add_run(it)
        _runfmt(r, size=BODY_SZ, bold=False)


def data_table(doc, rows, *, header=True):
    if not rows:
        return
    ncol = len(rows[0])
    t = doc.add_table(rows=len(rows), cols=ncol); t.style = "TableNormal"
    _borders(t)
    for ri, row in enumerate(rows):
        for ci in range(ncol):
            val = row[ci] if ci < len(row) else ""
            GUARD(str(val))
            cell = t.cell(ri, ci); cell.text = str(val)
            if ri == 0 and header:
                _shade(cell, BANNERFILL)
                _runfmt(cell.paragraphs[0].runs[0], size="17", bold=True)
            else:
                if cell.paragraphs[0].runs:
                    _runfmt(cell.paragraphs[0].runs[0], size="17", bold=False)
    doc.add_paragraph()


def signature(doc, text):
    GUARD(text)
    doc.add_paragraph()
    p = doc.add_paragraph(); r = p.add_run(text)
    _runfmt(r, size=BODY_SZ, bold=False, italic=True)
