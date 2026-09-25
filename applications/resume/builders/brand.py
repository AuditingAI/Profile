"""The letterhead, in one place.

Every branded builder draws its header through brand_header(). Two modes:

  wordmark  - "Audit the Algorithm" as real text in the brand gold. This is
              what assets/images/logo.svg itself is - a text wordmark - so it
              is the logo, not a stand-in for it. An ATS reads it; the PDF
              stays ~7 KB.
  mark      - a raster mark centred above the wordmark, used automatically
              when assets/images/logo-mark.png exists. Drop the file in and
              every builder picks it up on the next run.

The mark is THE AUDIT LENS, the owner's choice on 25 Sep 2026: the navy
magnifying glass from the original Audit the Algorithm logo, with its gold tick
replaced by the orange A from The Reference Mark. The lens stands in for the
Reference Mark's open ring, and the A's crossbar still reaches toward the rim
without closing on it. Navy #1B365D, orange #E0662E.

Vectors in assets/images/:
  audit-lens-mark.svg             primary, clean - used here and as favicon
  audit-lens-mark-detailed.svg    with the original's text lines behind the A;
                                  large sizes only, it smudges below ~60 px
  audit-lens-lockup(-detailed).svg  with AUDIT THE ALGORITHM beneath
logo-mark.png is the primary rasterised at 800 px, transparent.

Kept as brand history, not in use on documents: reference-mark*.svg and the
full Reference Mark design system in assets/brand/reference-mark/, and
logo-full.png, the original magnifier-and-tick.
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


def brand_header(body_style, scale=1.0, mark_height=0.38 * inch):
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
        # The Reference Mark stands alone. The owner asked for the wordmark
        # text to go, and the old gold "Audit the Algorithm" clashes with the
        # mark's orange and charcoal.
        return out
    out.append(Paragraph(WORDMARK, mark_style))
    return out


def brand_block(mark_style, mark_height=0.38 * inch):
    """Letterhead for a builder that already owns a tuned wordmark style.

    Same two modes as brand_header(), but it draws into the caller's existing
    style instead of deriving one. That keeps every branded builder on one
    letterhead without re-tuning type that is already sized for its page.
    """
    out = []
    if MARK.exists():
        img = Image(str(MARK))
        ratio = img.imageWidth / float(img.imageHeight)
        img.drawHeight = mark_height
        img.drawWidth = mark_height * ratio
        img.hAlign = "CENTER"
        out.append(img)
        return out  # the mark stands alone - see brand_header()
    out.append(Paragraph(WORDMARK, mark_style))
    return out


def header_mode():
    return "mark" if MARK.exists() else "wordmark"
