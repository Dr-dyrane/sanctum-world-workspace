#!/usr/bin/env python3
"""Epic-style note renderer - matches the KM design system EXACTLY.

Constants and helpers reproduced from tools/generate_reference_files.py (the generator
that produced the 33 approved KM reference files), so fingerprints match the KM target:
  body        Arial 9.5pt, color INK 232830, space-after 4pt, line 1.08
  section     BLUE 4472C4 bold 10pt, bottom rule C9D4EA
  note title  NAVY 1F3864 bold 14pt
  masthead    facility NAVY 11pt bold + dept GRAY 8pt; Confidential BLUE 8.5pt
  blue bar    1x1 B_HEX 4472C4 accent
  storyboard  name row B_HEX + white; 4 card cells CARD EDF2FA
  table       header B_HEX + white; alternate rows CARD; borders C9D4EA
  signature   top rule C9D4EA + GRAY italic
Header/footer are CLEARED (KM clone leaves KM identifiers there) and rewritten clean:
  header  "<name>  |  MRN <mrn>"   footer  "<facility>  |  <doctype>  |  Confidential"
GUARD rejects banned characters before they can reach a file. No synthetic banner.
"""
from __future__ import annotations
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK = RGBColor(0x23, 0x28, 0x30)
BLUE = RGBColor(0x44, 0x72, 0xC4)
NAVY = RGBColor(0x1F, 0x38, 0x64)
GRAY = RGBColor(0x5E, 0x66, 0x70)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
B_HEX = "4472C4"
CARD = "EDF2FA"
RULE = "C9D4EA"

BANNED = "—–→•°×⁹¹⁰*[]"


def GUARD(text: str) -> str:
    bad = [c for c in str(text) if c in BANNED]
    if bad:
        raise ValueError(f"banned character {bad!r} in: {str(text)[:60]!r}")
    return str(text)


def _run(p, t, sz=9.5, c=INK, b=False, i=False):
    GUARD(t)
    r = p.add_run(t)
    r.font.name = "Arial"; r.font.size = Pt(sz); r.font.color.rgb = c
    r.font.bold = b; r.font.italic = i
    return r


def _shade(cell, fill):
    pr = cell._tc.get_or_add_tcPr()
    s = OxmlElement("w:shd"); s.set(qn("w:val"), "clear"); s.set(qn("w:fill"), fill)
    pr.append(s)


def _borders(t, none=False):
    pr = t._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + e)
        if none:
            el.set(qn("w:val"), "none")
        else:
            el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:color"), RULE)
        b.append(el)
    pr.append(b)


def clear_body(doc):
    body = doc.element.body
    for child in list(body):
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)


def _clear_part(hf):
    """Empty a header/footer part of all inherited content (KM identifiers live here)."""
    el = hf._element
    for child in list(el):
        el.remove(child)


def clear_and_set_hf(doc, name, mrn, facility, doctype):
    """Wipe every header/footer part (KM clone leaves KM name/MRN/facility there)
    and write a clean running header and footer. name=None -> blank header and a
    plain Confidential footer (external task files)."""
    from docx.text.paragraph import Paragraph
    header_txt = f"{name}  |  MRN {mrn}" if name else ""
    footer_txt = f"{facility}  |  {doctype}  |  Confidential" if facility else "Confidential"
    GUARD(header_txt); GUARD(footer_txt)
    for s in doc.sections:
        s.different_first_page_header_footer = False
        for hf in (s.header, s.first_page_header, s.even_page_header):
            hf.is_linked_to_previous = False
            _clear_part(hf)
            p = hf._element.makeelement(qn("w:p"), {})
            hf._element.append(p)
            if header_txt:
                _run(Paragraph(p, hf), header_txt, 7.5, GRAY)
        for hf in (s.footer, s.first_page_footer, s.even_page_footer):
            hf.is_linked_to_previous = False
            _clear_part(hf)
            p = hf._element.makeelement(qn("w:p"), {})
            hf._element.append(p)
            par = Paragraph(p, hf)
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _run(par, footer_txt, 7.5, GRAY)


def masthead(doc, facility, dept):
    m = doc.add_table(rows=1, cols=2); _borders(m, none=True)
    _run(m.rows[0].cells[0].paragraphs[0], facility, 11, NAVY, b=True)
    if dept:
        _run(m.rows[0].cells[0].add_paragraph(), dept, 8, GRAY)
    pr = m.rows[0].cells[1].paragraphs[0]; pr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _run(pr, "Confidential", 8.5, BLUE, b=True)


def blue_bar(doc):
    hr = doc.add_table(rows=1, cols=1); _borders(hr, none=True)
    _shade(hr.rows[0].cells[0], B_HEX)
    tr = hr.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement("w:trHeight"); h.set(qn("w:val"), "40"); tr.append(h)


def storyboard(doc, name, demo, mrn, fields):
    """fields: list of exactly 4 (label, value) shown as light-blue cards."""
    sb = doc.add_table(rows=2, cols=4); _borders(sb)
    top = sb.rows[0]
    mc = top.cells[0].merge(top.cells[2]); _shade(mc, B_HEX)
    p = mc.paragraphs[0]
    _run(p, "  " + name, 13, WHITE, b=True)
    if demo:
        _run(p, "    " + demo, 9, WHITE)
    c3 = top.cells[3]; _shade(c3, B_HEX)
    p = c3.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _run(p, "MRN " + mrn + "  ", 10, WHITE, b=True)
    for j, (k, v) in enumerate(fields[:4]):
        cell = sb.rows[1].cells[j]; _shade(cell, CARD)
        p = cell.paragraphs[0]
        _run(p, k + "\n", 7.4, GRAY, b=True); _run(p, str(v)[:90], 8.2)
    doc.add_paragraph()


def note_title(doc, title):
    p = doc.add_paragraph(); _run(p, title, 14, NAVY, b=True)


def filing_line(doc, text):
    p = doc.add_paragraph(); _run(p, text, 8, GRAY)


def section(doc, name):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9); p.paragraph_format.space_after = Pt(3)
    _run(p, name.upper(), 10, BLUE, b=True)
    pr = p._p.get_or_add_pPr(); pb = OxmlElement("w:pBdr"); bo = OxmlElement("w:bottom")
    bo.set(qn("w:val"), "single"); bo.set(qn("w:sz"), "6"); bo.set(qn("w:color"), RULE); bo.set(qn("w:space"), "2")
    pb.append(bo); pr.append(pb)


def body(doc, text, *, bold=False):
    p = doc.add_paragraph(); _run(p, text, 9.5, INK, b=bold)


def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(1.5)
        _run(p, it, 9.5, INK)


def data_table(doc, rows, *, header=True):
    if not rows:
        return
    cols = max(len(r) for r in rows)
    tb = doc.add_table(rows=len(rows), cols=cols); _borders(tb)
    for ri, row in enumerate(rows):
        for ci in range(cols):
            c = tb.rows[ri].cells[ci]; pp = c.paragraphs[0]
            v = row[ci] if ci < len(row) else ""
            if ri == 0 and header:
                _shade(c, B_HEX); _run(pp, str(v), 8, WHITE, b=True)
            else:
                if ri % 2 == 0:
                    _shade(c, CARD)
                _run(pp, str(v), 8, INK)
    doc.add_paragraph()


def signature(doc, text):
    sg = doc.add_paragraph(); sg.paragraph_format.space_before = Pt(10)
    pr = sg._p.get_or_add_pPr(); pb = OxmlElement("w:pBdr"); bo = OxmlElement("w:top")
    bo.set(qn("w:val"), "single"); bo.set(qn("w:sz"), "4"); bo.set(qn("w:color"), RULE); bo.set(qn("w:space"), "4")
    pb.append(bo); pr.append(pb)
    _run(sg, text, 9, GRAY, i=True)


def encounter_block(doc, pairs):
    """KM PATIENT / ENCOUNTER block: metadata as labeled body lines."""
    section(doc, "PATIENT / ENCOUNTER")
    for k, v in pairs:
        p = doc.add_paragraph()
        _run(p, k + ": ", 9, INK, b=True); _run(p, str(v), 9, INK)
