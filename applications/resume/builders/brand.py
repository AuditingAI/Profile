"""The letterhead, in one place.

Every branded builder draws its header through brand_header(). Two modes:

  wordmark  - "Audit the Algorithm" as real text in the brand gold. This is
              what assets/images/logo.svg itself is - a text wordmark - so it
              is the logo, not a stand-in for it. An ATS reads it; the PDF
              stays ~7 KB.
  mark      - a raster mark centred above the wordmark, used automatically
              when assets/images/logo-mark.png exists. Drop the file in and
              every builder picks it up on the next run. Keep it under
              ~600 px wide; it is drawn 0.55 in high.

Colours match logo.svg: gold #B8860B (gradient end #DAA520), muted #6F6754.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph

ROOT = Path(__file__).resolve().parents[3]
MARK = ROOT / "assets" / "images" / "logo-mark.png"

GOLD = HexColor("#B8860B")
GOLD2 = HexColor("#DAA520")
MUTED = HexColor("#6F6754")

WORDMARK = ('<font color="#B8860B"><b>Audit</b></font> '
            '<font color="#6F6754"><i>the</i></font> '
            '<font color="#B8860B"><b>Algorithm</b></font>')


def brand_header(body_style, scale=1.0, mark_height=0.55 * inch):
    """Return the flowables for the letterhead. `body_style` sets the font family."""
    mark_style = ParagraphStyle("mark", parent=body_style, alignment=TA_CENTER,
                                fontSize=15 * scale, leading=17 * scale, spaceAfter=1)
    out = []
    if MARK.exists():
        img = Image(str(MARK))
        ratio = img.imageWidth / float(img.imageHeight)
        img.drawHeight = mark_height
        img.drawWidth = mark_height * ratio
        img.hAlign = "CENTER"
        out.append(img)
        mark_style.fontSize = 10 * scale
        mark_style.leading = 12 * scale
    out.append(Paragraph(WORDMARK, mark_style))
    return out


def header_mode():
    return "mark" if MARK.exists() else "wordmark"
