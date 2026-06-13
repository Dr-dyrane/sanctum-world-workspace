#!/usr/bin/env python3
"""Build the Ondina Vasquell World Spec DOCX via Mode A clone of the approved KM spec.

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

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.mode_a_clone import integrity_gate, scrub_core, verify_against_base  # noqa: E402

BASE = REPO / "worlds/korvin-merrow/file-review/pipeline-output/.meta/references/Alexander_World_Merrow_latest_6_4.docx"
SRC = REPO / "worlds/ondina-vasquell/submission/Ondina_Vasquell_World_Spec.md"
OUT = REPO / "worlds/ondina-vasquell/submission/Alexander_World_Vasquell_latest_6_13.docx"

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


def fmt_para(p, *, color: str, size: str, bold: bool) -> None:
    for run in p.runs:
        rpr = run._r.get_or_add_rPr()
        if bold:
            rpr.append(OxmlElement("w:b"))
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


def add_box(doc, text: str, *, fill: str, color: str, bold: bool, size: str, border: str) -> None:
    t = doc.add_table(rows=1, cols=1)
    t.style = "TableNormal"
    set_borders(t, outer=border, inner=border)
    cell = t.cell(0, 0)
    cell.text = text
    shade(cell, fill)
    fmt_runs(cell, color=color, size=size, bold=bold)


def add_cover_box(doc, title: str, subtitle: str) -> None:
    """Cover banner: blue bold title (16pt) + muted-gray subtitle (10pt)."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "TableNormal"
    set_borders(t, outer="000000", inner="000000")
    cell = t.cell(0, 0)
    shade(cell, LIGHTBLUE)
    cell.paragraphs[0].text = title
    fmt_para(cell.paragraphs[0], color=BLUE, size=COVER_SZ, bold=True)
    psub = cell.add_paragraph(subtitle)
    fmt_para(psub, color=MUTED, size=SUB_SZ, bold=False)


def add_note_box(doc, text: str) -> None:
    """Green note callout: green bold label before the first colon, gray body."""
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
        c2 = OxmlElement("w:color"); c2.set(qn("w:val"), GRAY); rpr2.append(c2)
        s2 = OxmlElement("w:sz"); s2.set(qn("w:val"), SZ); rpr2.append(s2)
    else:
        p.text = text
        fmt_para(p, color=GRAY, size=SZ, bold=False)


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
            add_data_table(doc, parse_md_table(block), meta=not first_table_seen)
            first_table_seen = True
            continue
        if ln.startswith("# "):
            doc.add_paragraph(ln[2:].strip(), style="Heading 1")
        elif ln.startswith("## "):
            doc.add_paragraph(ln[3:].strip(), style="Heading 2")
        elif ln.startswith("### "):
            doc.add_paragraph(ln[4:].strip(), style="Heading 2")
        elif ln.startswith("Cover:"):
            payload = ln[len("Cover:"):].strip()
            title, sub = (payload.split("||", 1) + [""])[:2]
            add_cover_box(doc, title.strip(), sub.strip())
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
    print("integrity gate:", integrity_gate(str(OUT)))
    print("verify_against_base:", verify_against_base(str(OUT), str(BASE)))
    print("written:", OUT)


if __name__ == "__main__":
    build()
