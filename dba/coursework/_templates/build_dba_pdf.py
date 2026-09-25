#!/usr/bin/env python3
"""FIU DBA coursework PDF, from the same spec JSON that build_dba_doc.py consumes.

LibreOffice cannot convert in this container, and Word is not available here, so
the PDF is composed directly rather than derived from the .docx. Both read one
spec, so the two outputs cannot drift apart in content.

The .docx remains the editable master. This exists to be attached to an email.

  python3 build_dba_pdf.py spec.json out.pdf

Note on accessibility: reportlab does not emit a tagged PDF, so this file does
NOT meet WCAG 2.1 AA and must not be used for a FIU Scholarship Commons deposit.
For that route the .docx goes through Word's own PDF export with document
structure tags enabled. See dba/OPPORTUNITIES/FIU_SCHOLARSHIP_COMMONS.md.
"""
import json, sys
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, PageBreak,
                                KeepTogether)
from reportlab.pdfbase.pdfmetrics import stringWidth
from PIL import Image as PILImage

INK   = colors.HexColor("#14171C")
RULEC = colors.HexColor("#B9BEC6")
SERIF, SERIFB, SERIFI = "Times-Roman", "Times-Bold", "Times-Italic"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def segs(item):
    """Spec body items are a string, or a list of strings / {t,b,i} runs."""
    if isinstance(item, str):
        return esc(item)
    out = []
    for s in item:
        if isinstance(s, str):
            out.append(esc(s))
        else:
            t = esc(s["t"])
            if s.get("b"): t = f"<b>{t}</b>"
            if s.get("i"): t = f"<i>{t}</i>"
            out.append(t)
    return "".join(out)


def build(spec, out):
    ds = spec.get("double_spaced", False)
    size, lead = (12, 24) if ds else (11, 14)

    body = ParagraphStyle("body", fontName=SERIF, fontSize=size, leading=lead,
                          alignment=TA_JUSTIFY, spaceAfter=6, textColor=INK)
    h1   = ParagraphStyle("h1", fontName=SERIFB, fontSize=size + 3, leading=(size + 3) * 1.2,
                          spaceBefore=16, spaceAfter=8, textColor=INK, keepWithNext=1)
    h2   = ParagraphStyle("h2", fontName=SERIFB, fontSize=size + 1, leading=(size + 1) * 1.2,
                          spaceBefore=12, spaceAfter=6, textColor=INK, keepWithNext=1)
    bullet = ParagraphStyle("bullet", parent=body, leftIndent=18, bulletIndent=6,
                            spaceAfter=4)
    ident = ParagraphStyle("ident", fontName=SERIF, fontSize=size - 0.5,
                           leading=(size - 0.5) * 1.25, spaceAfter=1, textColor=INK)
    cap   = ParagraphStyle("cap", fontName=SERIFI, fontSize=size - 1.5,
                           leading=(size - 1.5) * 1.3, alignment=TA_CENTER,
                           spaceBefore=6, spaceAfter=14, textColor=INK)
    ref   = ParagraphStyle("ref", parent=body, alignment=TA_JUSTIFY,
                           leftIndent=0.5 * inch, firstLineIndent=-0.5 * inch)
    cell  = ParagraphStyle("cell", fontName=SERIF, fontSize=size - 2.5,
                           leading=(size - 2.5) * 1.25, textColor=INK)
    cellb = ParagraphStyle("cellb", parent=cell, fontName=SERIFB)

    story = []
    title_style = ParagraphStyle("title", fontName=SERIFB, fontSize=size + 4,
                                 leading=(size + 4) * 1.22, spaceAfter=6, textColor=INK)
    story.append(Paragraph(esc(spec["title"]), title_style))
    if spec.get("subtitle"):
        story.append(Paragraph(f"<i>{esc(spec['subtitle'])}</i>",
                     ParagraphStyle("sub", fontName=SERIFI, fontSize=size + 1,
                                    leading=(size + 1) * 1.25, spaceAfter=10, textColor=INK)))
    for line in spec.get("ident", []):
        story.append(Paragraph(esc(line), ident))
    if spec.get("ident"):
        story.append(Spacer(1, 10))

    avail = LETTER[0] - 2 * inch

    in_refs = [False]

    def emit(items):
        for it in items:
            if isinstance(it, dict) and "h1" in it:
                # reference lists take a hanging indent, per APA and JIBS
                in_refs[0] = it["h1"].strip().lower().startswith("reference")
                story.append(Paragraph(esc(it["h1"]), h1))
            elif isinstance(it, dict) and "h2" in it:
                story.append(Paragraph(esc(it["h2"]), h2))
            elif isinstance(it, dict) and "bullet" in it:
                story.append(Paragraph(segs(it["bullet"]), bullet, bulletText="•"))
            elif isinstance(it, dict) and "pagebreak" in it:
                story.append(PageBreak())
            elif isinstance(it, dict) and "image" in it:
                w = it.get("width_in", 6.0) * inch
                w = min(w, avail)
                iw, ih = PILImage.open(it["image"]).size
                img = Image(it["image"], width=w, height=w * ih / iw)
                img.hAlign = "CENTER"
                block = [img]
                if it.get("caption"):
                    block.append(Paragraph(esc(it["caption"]), cap))
                story.append(KeepTogether(block))
            elif isinstance(it, dict) and "__table__" in it:
                rows = spec["tables"][it["__table__"]]
                ncol = len(rows[0])
                # width by longest cell, then normalised to the frame
                raw = [max(stringWidth(r[c], SERIF, size - 2.5) for r in rows) + 16
                       for c in range(ncol)]
                scale = avail / sum(raw)
                widths = [max(w * scale, 42) for w in raw]
                over = sum(widths) - avail
                if over > 0:
                    widest = widths.index(max(widths))
                    widths[widest] -= over
                data = [[Paragraph(esc(v), cellb if ri == 0 else cell) for v in row]
                        for ri, row in enumerate(rows)]
                t = Table(data, colWidths=widths, repeatRows=1)
                t.setStyle(TableStyle([
                    ("GRID", (0, 0), (-1, -1), 0.5, RULEC),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF2F6")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(t)
                story.append(Spacer(1, 10))
            else:
                story.append(Paragraph(segs(it), ref if in_refs[0] else body))

    emit(spec["body"])

    surname = spec.get("running_head", "Malik")

    def page_furniture(canv, doc):
        canv.saveState()
        canv.setFont(SERIF, 10)
        canv.setFillColor(colors.HexColor("#6E757F"))
        canv.drawRightString(LETTER[0] - inch, 0.62 * inch, str(canv.getPageNumber()))
        canv.drawString(inch, 0.62 * inch, surname)
        canv.restoreState()

    doc = BaseDocTemplate(out, pagesize=LETTER,
                          leftMargin=inch, rightMargin=inch,
                          topMargin=inch, bottomMargin=inch,
                          title=spec["title"], author=spec.get("author", "Yasir A. Malik"),
                          subject=spec.get("subtitle", ""))
    frame = Frame(inch, inch, avail, LETTER[1] - 2 * inch, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=page_furniture)])
    doc.build(story)
    print("wrote", out)


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    build(spec, sys.argv[2])
