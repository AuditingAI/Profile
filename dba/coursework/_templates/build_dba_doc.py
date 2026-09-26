#!/usr/bin/env python3
"""
DBA coursework document builder — Yasir A. Malik.

House format taken from his own submitted work, not invented here:
  dba/Research_Paper_YMalik_SUBMISSION.docx
  dba/Data_Collection_Readiness.docx
  dba/2026-06-14_Catchup_Status_to_Rey.docx

  - Times New Roman 11pt, 1.15 line spacing
  - Native Word Heading 1 / Heading 2 / List Bullet styles, so the document
    opens with a working navigation pane and the professor's own styling
  - An identification block under the title: project, author, programme,
    course, instructor, date
  - NO wordmark, NO repository URL, NO "Audit the Algorithm"

That last line is the point of this file existing separately from
build_submission.py. The consulting brand belongs on portfolio and public
documents. A class submission carries the university's identity, not a
practice's — a professor reading a consulting letterhead on coursework sees a
vendor, not a doctoral student.

Usage:  python3 build_dba_doc.py <spec.json> <out.docx>
"""
import re
import json, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = 'Times New Roman'
INK  = RGBColor(0x00, 0x00, 0x00)

def _font(obj, name=FONT, size=11, bold=None, italic=None, color=INK,
          highlight=False):
    obj.font.name = name
    obj.font.size = Pt(size)
    if color is not None: obj.font.color.rgb = color
    if bold is not None: obj.bold = bold
    if italic is not None: obj.italic = italic
    if highlight: obj.font.highlight_color = WD_COLOR_INDEX.YELLOW
    rpr = obj._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), name)
    return obj

_BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
_ITAL_RE = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
_BI_RE = re.compile(r"\*\*\*(.+?)\*\*\*", re.S)

def _md(text):
    """Split a string on **bold** and *italic* into runs.

    Bold is matched first so a double asterisk is never read as two italic
    markers. Unmatched asterisks stay literal.

    The specs are written as readable prose, so emphasis is marked the way it
    would be in a markdown note. Without this the asterisks printed verbatim
    into the Word file, which is what they were doing.
    """
    def _ital(chunk):
        out, i = [], 0
        for m in _ITAL_RE.finditer(chunk):
            if m.start() > i:
                out.append(chunk[i:m.start()])
            out.append({"t": m.group(1), "i": True})
            i = m.end()
        if i < len(chunk):
            out.append(chunk[i:])
        return out

    def _bold(chunk):
        out, i = [], 0
        for m in _BOLD_RE.finditer(chunk):
            if m.start() > i:
                out.extend(_ital(chunk[i:m.start()]))
            out.append({"t": m.group(1), "b": True})
            i = m.end()
        if i < len(chunk):
            out.extend(_ital(chunk[i:]))
        return out

    # triple asterisks first, or the bold pass leaves a stray marker behind
    out, i = [], 0
    for m in _BI_RE.finditer(text):
        if m.start() > i:
            out.extend(_bold(text[i:m.start()]))
        out.append({"t": m.group(1), "b": True, "i": True})
        i = m.end()
    if i < len(text):
        out.extend(_bold(text[i:]))
    return out or [text]


_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s)<>\]]+)|(?<![\w/])((?:www\.)?linkedin\.com/in/[\w-]+)")

def _add_hyperlink(par, text, url, size=11):
    """A clickable link, as Word's own w:hyperlink, not underlined text.

    A URL printed as plain text is not a link. Every PDF this repository had
    produced so far carried its addresses that way, which is why "the links
    don't work": there were none to work.
    """
    part = par.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r"); rPr = OxmlElement("w:rPr")
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0B3D91"); rPr.append(c)
    new_run.append(rPr)
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); new_run.append(t)
    h.append(new_run); par._p.append(h)
    # size and face are applied through the run object so they match the body
    from docx.text.run import Run
    _font(Run(new_run, par), size=size)

def _links(text):
    """Split a plain string into text and {t,url} link segments."""
    out, i = [], 0
    for m in _LINK_RE.finditer(text):
        if m.start() > i:
            out.append(text[i:m.start()])
        if m.group(1):
            out.append({"t": m.group(1), "url": m.group(2)})
        elif m.group(3):
            # a sentence-ending period or comma is not part of the address
            u = m.group(3).rstrip(".,;:)")
            tail = m.group(3)[len(u):]
            out.append({"t": u, "url": u})
            if tail:
                out.append(tail)
        else:
            out.append({"t": m.group(4), "url": "https://" + m.group(4).removeprefix("www.")})
        i = m.end()
    if i < len(text):
        out.append(text[i:])
    return out or [text]

def _segs(par, segs, size=11):
    """A paragraph body: a string, or a list of strings and {t,b,i,hl} dicts."""
    if isinstance(segs, str): segs = [segs]
    flat = []
    for s in segs:
        flat.extend(_md(s) if isinstance(s, str) else [s])
    # links are found after emphasis, on the plain pieces only
    linked = []
    for s in flat:
        linked.extend(_links(s) if isinstance(s, str) else [s])
    for s in linked:
        if isinstance(s, str):
            _font(par.add_run(s), size=size)
        elif "url" in s:
            _add_hyperlink(par, s["t"], s["url"], size=size)
        else:
            _font(par.add_run(s["t"]), size=size,
                  bold=s.get("b", False), italic=s.get("i", False),
                  highlight=s.get("hl", False))

def _set_lang(doc, lang):
    """Declare the document language on the Normal style so it inherits."""
    rpr = doc.styles['Normal'].element.get_or_add_rPr()
    el = rpr.find(qn('w:lang'))
    if el is None:
        el = OxmlElement('w:lang')
        rpr.append(el)
    el.set(qn('w:val'), lang)


def _alt(shape, text):
    """Write the alt text Word and the accessibility checkers actually read.

    python-docx leaves <wp:docPr> with only a name, which every checker reports
    as a missing text alternative. Both attributes are set: descr is what
    screen readers announce, title is what older Word versions show.
    """
    if not text:
        return
    dp = shape._inline.docPr
    dp.set('descr', text)
    dp.set('title', text[:255])


def build(spec, out):
    doc = Document()

    # ---- document properties -------------------------------------------
    # Required by WCAG 2.1 AA and checked by the FIU repository: a document
    # title distinct from the filename, and a declared language.
    cp = doc.core_properties
    cp.title = spec["title"]
    cp.author = spec.get("author", "Yasir A. Malik")
    if spec.get("subtitle"):
        cp.subject = spec["subtitle"]
    _set_lang(doc, spec.get("lang", "en-US"))

    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = Inches(1.0)
    sec.left_margin = sec.right_margin = Inches(1.0)

    ds = spec.get("double_spaced", False)
    size, ls = (12, 2.0) if ds else (11, 1.15)

    n = doc.styles['Normal']
    _font(n, size=size)
    n.paragraph_format.line_spacing = ls
    n.paragraph_format.space_after = Pt(8)

    for sname, ssize in (('Heading 1', size + 3), ('Heading 2', size + 1)):
        st = doc.styles[sname]
        _font(st, size=ssize, bold=True, color=INK)
        st.paragraph_format.space_before = Pt(14)
        st.paragraph_format.space_after = Pt(6)
    _font(doc.styles['List Bullet'], size=size)
    _font(doc.styles['Heading 3'], size=size, bold=True)

    # ---- masthead with a personal mark, when the spec carries one --------
    # A two-cell table with no borders: the mark on the left, the name and
    # byline on the right. Used for the academic set, never for coursework,
    # which carries the university's identity instead.
    if spec.get("logo") and spec.get("masthead") == "centered":
        # The executive-résumé layout Yasir chose: mark centred above the
        # name, name in spaced capitals, a one-line title strip, a one-line
        # contact strip, and section heads in spaced capitals over a rule.
        lp = doc.add_paragraph(); lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        lp.paragraph_format.space_after = Pt(2)
        pic = lp.add_run().add_picture(spec["logo"], width=Inches(spec.get("logo_in", 0.42)))
        _alt(pic, spec.get("logo_alt", "Personal mark"))
        np_ = doc.add_paragraph(); np_.alignment = WD_ALIGN_PARAGRAPH.CENTER
        np_.paragraph_format.space_after = Pt(2)
        r = np_.add_run(spec["title"].upper()); _font(r, size=size + 9, bold=False)
        r.font.all_caps = True
        r._element.get_or_add_rPr().append(OxmlElement('w:spacing'))
        r._element.rPr.find(qn('w:spacing')).set(qn('w:val'), '60')
        if spec.get("subtitle"):
            sp = doc.add_paragraph(); sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            sp.paragraph_format.space_after = Pt(2)
            _font(sp.add_run(spec["subtitle"]), size=size - 0.5)
        for line in spec.get("ident", []):
            ip = doc.add_paragraph(); ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
            ip.paragraph_format.space_after = Pt(1); ip.paragraph_format.line_spacing = 1.0
            _segs(ip, line.replace(" · ", "  \u2022  "), size=size - 1)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        # section heads: spaced capitals over a hairline
        h2 = doc.styles['Heading 2']
        h2.font.all_caps = True
        pPr = h2.element.get_or_add_pPr()
        bdr = OxmlElement('w:pBdr'); bot = OxmlElement('w:bottom')
        for k, v in (('w:val', 'single'), ('w:sz', '6'), ('w:space', '2'), ('w:color', '1A1A1A')):
            bot.set(qn(k), v)
        bdr.append(bot); pPr.append(bdr)
        rPr = h2.element.get_or_add_rPr()
        spc = OxmlElement('w:spacing'); spc.set(qn('w:val'), '40'); rPr.append(spc)
        spec = dict(spec, title=None, subtitle=None, ident=[])
    elif spec.get("logo"):
        mt = doc.add_table(rows=1, cols=2)
        mt.autofit = False
        lc, rc = mt.rows[0].cells
        # Word honours cell widths; LibreOffice honours column widths and the
        # table grid. Set all three, or one of the two renderers ignores it.
        for col, w in zip(mt.columns, (0.95, 5.55)):
            col.width = Inches(w)
        lc.width = Inches(0.95); rc.width = Inches(5.55)
        tblPr = mt._tbl.tblPr
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
        tblW = tblPr.find(qn('w:tblW'))
        if tblW is None:
            tblW = OxmlElement('w:tblW'); tblPr.append(tblW)
        tblW.set(qn('w:type'), 'dxa'); tblW.set(qn('w:w'), str(int(6.5 * 1440)))
        grid = mt._tbl.tblGrid
        for gc, w in zip(grid.findall(qn('w:gridCol')), (0.95, 5.55)):
            gc.set(qn('w:w'), str(int(w * 1440)))
        for cell in (lc, rc):
            tcPr = cell._tc.get_or_add_tcPr()
            borders = OxmlElement('w:tcBorders')
            for side in ('top', 'left', 'bottom', 'right'):
                b = OxmlElement('w:' + side); b.set(qn('w:val'), 'nil'); borders.append(b)
            tcPr.append(borders)
        lp = lc.paragraphs[0]
        pic = lp.add_run().add_picture(spec["logo"], width=Inches(spec.get("logo_in", 0.72)))
        _alt(pic, spec.get("logo_alt", "Personal mark"))
        rp = rc.paragraphs[0]
        rp.style = doc.styles['Heading 1']
        _font(rp.add_run(spec["title"]), size=size + 9, bold=True)
        if spec.get("subtitle"):
            sp = rc.add_paragraph()
            sp.paragraph_format.space_after = Pt(4)
            _font(sp.add_run(spec["subtitle"]), size=size + 1, italic=True)
        for line in spec.get("ident", []):
            ip = rc.add_paragraph()
            ip.paragraph_format.space_after = Pt(1)
            ip.paragraph_format.line_spacing = 1.0
            _segs(ip, line, size=size - 0.5)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        spec = dict(spec, title=None, subtitle=None, ident=[])

    # ---- title ---------------------------------------------------------
    h = doc.add_paragraph(spec["title"], style='Heading 1') if spec.get("title") else None
    if h is not None:
        for r in h.runs: _font(r, size=size + 4, bold=True)
    if spec.get("subtitle"):
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(10)
        _font(p.add_run(spec["subtitle"]), size=size + 1, italic=True)

    # ---- identification block ------------------------------------------
    for line in spec.get("ident", []):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.0
        # through _segs, so an address in the byline becomes a real link
        _segs(p, line, size=size - 0.5)
    if spec.get("ident"):
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ---- body ------------------------------------------------------------
    in_refs = [False]

    def emit(items):
        for it in items:
            if isinstance(it, dict) and "h1" in it:
                # reference lists take a hanging indent, per APA and JIBS
                in_refs[0] = it["h1"].strip().lower().startswith("reference")
                p = doc.add_paragraph(it["h1"], style='Heading 1')
                for r in p.runs: _font(r, size=size + 3, bold=True)
            elif isinstance(it, dict) and "h2" in it:
                p = doc.add_paragraph(it["h2"], style='Heading 2')
                for r in p.runs: _font(r, size=size + 1, bold=True)
            elif isinstance(it, dict) and "h3" in it:
                p = doc.add_paragraph(style='Heading 3')
                p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
                _font(p.add_run(it["h3"]), size=size, bold=True)
            elif isinstance(it, dict) and "bullet" in it:
                p = doc.add_paragraph(style='List Bullet')
                p.paragraph_format.line_spacing = ls
                _segs(p, it["bullet"], size=size)
            elif isinstance(it, dict) and "pagebreak" in it:
                doc.add_page_break()
            elif isinstance(it, dict) and "image" in it:
                doc.add_picture(it["image"], width=Inches(it.get("width_in", 6.0)))
                doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
                # WCAG 2.1 AA: every meaningful image needs a text alternative.
                # FIU Scholarship Commons returns untagged / un-alt-texted files.
                _alt(doc.inline_shapes[-1],
                     it.get("alt") or it.get("caption") or "")
                if it.get("caption"):
                    cp = doc.add_paragraph()
                    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    cp.paragraph_format.space_after = Pt(12)
                    cp.paragraph_format.line_spacing = 1.0
                    _font(cp.add_run(it["caption"]), size=size - 1.5, italic=True)
            elif isinstance(it, dict) and "__table__" in it:
                rows = spec["tables"][it["__table__"]]
                t = doc.add_table(rows=0, cols=len(rows[0]))
                t.style = 'Table Grid'
                for ri, row in enumerate(rows):
                    cells = t.add_row().cells
                    for ci, val in enumerate(row):
                        cp = cells[ci].paragraphs[0]
                        cp.paragraph_format.space_after = Pt(2)
                        cp.paragraph_format.line_spacing = 1.0
                        _font(cp.add_run(val), size=size - 1.5,
                              bold=(ri == 0), color=INK)
                doc.add_paragraph().paragraph_format.space_after = Pt(6)
            else:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.line_spacing = ls
                p.paragraph_format.space_after = Pt(8)
                if in_refs[0]:
                    p.paragraph_format.left_indent = Inches(0.5)
                    p.paragraph_format.first_line_indent = Inches(-0.5)
                _segs(p, it, size=size)

    emit(spec["body"])

    for tb in (spec.get("table"), spec.get("table2")):
        if not tb: continue
        if tb.get("caption"):
            p = doc.add_paragraph(tb["caption"], style='Heading 2')
            for r in p.runs: _font(r, size=size + 1, bold=True)
        t = doc.add_table(rows=0, cols=len(tb["rows"][0]))
        t.style = 'Table Grid'
        for ri, row in enumerate(tb["rows"]):
            cells = t.add_row().cells
            for ci, val in enumerate(row):
                cp = cells[ci].paragraphs[0]
                cp.paragraph_format.space_after = Pt(2)
                cp.paragraph_format.line_spacing = 1.0
                _font(cp.add_run(val), size=size - 1.5,
                      bold=(ri == 0), color=INK)

    if spec.get("appendix"):
        doc.add_page_break()
        emit(spec["appendix"])

    doc.save(out)
    print("wrote", out)

if __name__ == "__main__":
    build(json.load(open(sys.argv[1])), sys.argv[2])
