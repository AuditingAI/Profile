"""The letterhead, in one place.

Every branded builder draws its header through brand_header(). Two modes:

  wordmark  - "Audit the Algorithm" as real text in the brand gold. This is
              what assets/images/logo.svg itself is - a text wordmark - so it
              is the logo, not a stand-in for it. An ATS reads it; the PDF
              stays ~7 KB.
  mark      - a raster mark centred above the wordmark, used automatically
              when assets/images/logo-mark.png exists. Drop the file in and
              every builder picks it up on the next run.

The mark is THE REFERENCE MARK, the owner's brand, designed in Claude Design:
a charcoal A inside an open orange ring, with an orange node floating in the
ring's 42-degree break and the A's crossbar overshooting the right leg toward
the ring. Orange #E0662E, charcoal #171A1D. The full design system - lockups,
palette, type, banner, signature, LinkedIn cover, business cards - is in
assets/brand/reference-mark/, extracted from the canvas artifact
"The Reference Mark" (claude.ai/artifact/Tg7FZJQJwnyw5RHZgCrDVk). Vector
sources: assets/images/reference-mark.svg (two-tone, primary), -mono.svg, and
-micro.svg (the 16-24 px cut, used as the favicon). logo-mark.png is the
two-tone rasterised at 800 px with a transparent ground.

History, so nobody repeats it: an "A" monogram was drawn from scratch on
18 Sep, then replaced on 25 Sep by the magnifier-and-tick in
auditingai-github-pages.zip (now logo-full.png). Neither was the brand. The
Reference Mark never reached the repository until 25 Sep - it lived only in the
design canvas, which is why every search of git came up empty.
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
