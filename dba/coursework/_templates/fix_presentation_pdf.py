import pymupdf

SRC = '/root/.claude/uploads/7e1785ef-22ca-5560-965d-d01b23a570da/e9fe0724-Internationalization_and_Performance_PRESENTATION.pdf'
OUT = '/home/user/Profile/dba/coursework/GEB7365_International_Business/Internationalization_and_Performance_PRESENTATION_FINAL.pdf'
FD  = '/mnt/skills/examples/canvas-design/canvas-fonts/'

NAVY  = (7/255, 30/255, 61/255)
CARD  = (13/255, 40/255, 74/255)
GOLD  = (193/255, 136/255, 30/255)
WHITE = (1, 1, 1)
MUTED = (0.66, 0.72, 0.81)
DIM   = (0.42, 0.50, 0.62)
RULE  = (0.16, 0.24, 0.38)
TITLE_NAVY = (11/255, 32/255, 75/255)
CREAM = (246/255, 244/255, 235/255)

# Full-coverage faces for the pages I add. The deck's own fonts are embedded
# SUBSETS — they carry only the glyphs Daniela's slides happened to use, so
# reusing them dropped ampersands, parentheses, quotes and half the digits
# into empty boxes. Matching the look is not worth losing characters.
FONTS = {"ser": FD+"IBMPlexSerif-Regular.ttf", "serb": FD+"IBMPlexSerif-Bold.ttf",
         "seri": FD+"IBMPlexSerif-Italic.ttf", "mono": FD+"IBMPlexMono-Regular.ttf",
         "monob": FD+"IBMPlexMono-Bold.ttf"}
FF = {k: pymupdf.Font(fontfile=v) for k, v in FONTS.items()}

doc = pymupdf.open(SRC)

# ------------------------------------------------------------- text repairs
# 1 · the title slide misspells his name: "Yasi A. Malik"
p = doc[0]
p.add_redact_annot(pymupdf.Rect(246, 336, 480, 354), fill=TITLE_NAVY)
p.apply_redactions()
p.insert_font(fontname="F2", fontfile="F2.ttf")
p.insert_text((248.28, 349.44), "Daniela Garcia Aguirre / Yasir A. Malik",
              fontname="F2", fontsize=11.52, color=WHITE)

# 2 · slide 6 heading: misspelled, and white-on-cream, i.e. invisible
p = doc[5]
p.add_redact_annot(pymupdf.Rect(412, 314, 660, 335), fill=CREAM)
p.apply_redactions()
p.insert_font(fontname="F2", fontfile="F2.ttf")
p.insert_text((414.72, 329.52), "Seven themes organize the literature",
              fontname="F2", fontsize=13.2, color=TITLE_NAVY)

# 3 · an empty cream box sits over the footer rule, bottom-left of slide 6
p.draw_rect(pymupdf.Rect(3.0, 500.2, 335.0, 523.3), color=None, fill=CREAM, overlay=True)
p.draw_line(pymupdf.Point(32.76, 503.88), pymupdf.Point(334.2, 503.88),
            color=(215/255, 209/255, 197/255), width=0.6)

# --------------------------------------------- crop the letterbox off
# Every page is 16:9 artwork centred on US Letter, leaving white bands top and
# bottom. Cropping to the artwork makes it a real 16:9 deck.
for pg in doc:
    pg.set_cropbox(pymupdf.Rect(0, 83.28, 792, 528.84))

W, H = 792.0, 445.56
M = 48.0

def newpage():
    pg = doc.new_page(width=W, height=H)
    pg.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=NAVY)
    for k, v in FONTS.items():
        pg.insert_font(fontname=k, fontfile=v)
    return pg

def text(pg, x, y, s, font="ser", size=9, color=WHITE):
    pg.insert_text((x, y), s, fontname=font, fontsize=size, color=color)

def box(pg, x, y, w, s, font="ser", size=9, color=WHITE, lead=1.36, align=0):
    """Wrap with the metrics of the font actually used, and fail loudly."""
    h = 400
    r = pymupdf.Rect(x, y - size, x + w, y - size + h)
    left = pg.insert_textbox(r, s, fontname=font, fontsize=size, color=color,
                             lineheight=lead, align=align)
    if left < 0:
        raise SystemExit(f"OVERFLOW: {s[:50]!r} needs {-left:.0f}pt more")
    used = h - left
    return y - size + used

def chrome(pg, eyebrow, title, num):
    pg.draw_rect(pymupdf.Rect(M, 30, M + 3, 52), color=None, fill=GOLD)
    text(pg, M + 12, 41, "FLORIDA INTERNATIONAL UNIVERSITY", "monob", 7.0, WHITE)
    text(pg, M + 12, 52, "Chapman Graduate School of Business  ·  Doctor of Business Administration",
         "ser", 6.8, MUTED)
    text(pg, M, 104, eyebrow, "monob", 7.0, GOLD)
    text(pg, M, 134, title, "serb", 21, WHITE)
    pg.draw_line(pymupdf.Point(M, H - 40), pymupdf.Point(W - M, H - 40), color=RULE, width=0.6)
    text(pg, M, H - 26, "Yasir A. Malik  ·  Cohort 8.14", "mono", 6.6, MUTED)
    text(pg, 318, H - 26, "GEB 7365  ·  Module 2  ·  27 August 2026", "mono", 6.6, DIM)
    text(pg, W - M - FF["mono"].text_length(num, 6.6), H - 26, num, "mono", 6.6, MUTED)

# ------------------------------------------------------------- Appendix A
pg = newpage()
chrome(pg, "APPENDIX A  ·  BACKUP — ONLY IF ASKED", "The same error, in my own study.", "A1")
pg.draw_rect(pymupdf.Rect(M, 152, W - M, 196), color=RULE, fill=CARD, width=0.6)
box(pg, M + 14, 172, W - 2*M - 28,
    "Tversky & Kahneman (1974) — a wheel of fortune gave subjects 10 or 65 before they estimated "
    "the share of African countries in the UN. Median answers: 25 and 45.", "ser", 9.0, WHITE)

for i, (h, b) in enumerate([
    ("WHAT MY MODEL MEASURES",
     "Eight organisational interventions — training, rotation, analytical tools, structured "
     "processes, feedback, independent review, regulatory guidance, incentives — against anchoring "
     "bias, with expertise and confidence as moderators."),
    ("WHAT IT ACTUALLY MEASURES",
     "Anchoring bias is captured by self-report, reverse-coded. It asks auditors to report how far "
     "their judgment was driven by a reference point — the one thing the bias reliably prevents "
     "them from noticing. Perceived judgment discipline, described as anchoring reduction."),
]):
    x = M + i * 356
    text(pg, x, 226, h, "monob", 6.6, GOLD)
    box(pg, x, 244, 330, b, "ser", 8.4, MUTED)

pg.draw_rect(pymupdf.Rect(M, 318, W - M, 372), color=GOLD, fill=CARD, width=0.9)
box(pg, M + 14, 338, W - 2*M - 28,
    "Contractor measured segments of a curve. Mezias's field measured aggregate performance. "
    "I measured self-reported bias resistance. Three instances of the same error, and one of them "
    "is mine.", "serb", 9.6, WHITE)
box(pg, M, 392, W - 2*M,
    "→  TVERSKY & KAHNEMAN ALREADY WARNED ME: “PAYOFFS FOR ACCURACY DID NOT REDUCE THE "
    "ANCHORING EFFECT.”", "monob", 6.6, GOLD)

# ------------------------------------------------------------- Appendix B
pg = newpage()
chrome(pg, "APPENDIX B  ·  EVERY QUOTE AND FIGURE, WITH ITS PAGE", "Verification record.", "A2")
rows = [
 ("8", "Sigmoid, three stages; four findings are segments of one curve", "Contractor p.7, Fig. 1"),
 ("8", "“Depending on which part of Figure 1 we examined…”", "Contractor p.7"),
 ("9", "Knowledge-based vs capital-intensive; lower fixed capital burden", "Contractor p.9"),
 ("9", "“Few companies possess the managerial tools…”", "Contractor p.11"),
 ("10", "486 foreign subsidiaries vs 486 US, same industries and cities", "Mezias p.229–231"),
 ("10", "“labor lawsuits only measure labor-related disadvantage”", "Mezias p.231"),
 ("10", "78.9% / 70.0% / 58.4%; award > $600,000; fees ~$100,000", "Mezias p.232"),
 ("11", "“varied and at times incompatible findings”", "Arregle, abstract"),
 ("12", "Performance is 12% of the 220 studies", "Arregle p.6"),
 ("12", "Kundu authored both the 2003 and 2021 papers", "Both title pages"),
 ("A1", "Wheel of fortune: 10 → 25, 65 → 45; payoffs did not reduce it", "Tversky & Kahneman p.1128"),
]
y = 168
for lab, hx in (("PAGE", M), ("CLAIM", M + 46), ("SOURCE", 500), ("CHECKED", 690)):
    text(pg, hx, y, lab, "monob", 6.2, GOLD)
y += 7
pg.draw_line(pymupdf.Point(M, y), pymupdf.Point(W - M, y), color=RULE, width=0.5)
y += 14
for slide, claim, src in rows:
    text(pg, M, y, slide, "mono", 6.8, MUTED)
    text(pg, M + 46, y, claim, "ser", 7.6, WHITE)
    text(pg, 500, y, src, "ser", 7.2, MUTED)
    text(pg, 690, y, "EXACT", "monob", 6.2, GOLD)
    y += 16.6
text(pg, M, y + 8, "All verified against the source PDFs, 26 August 2026. Nothing is paraphrased "
                   "and presented as a quote.", "seri", 7.4, MUTED)

# ------------------------------------------------------------- Appendix C
pg = newpage()
chrome(pg, "APPENDIX C", "References.", "A3")
refs = [
 ("DANIELA", "Ghemawat, P. (2001). Distance still matters: The hard reality of global expansion. "
             "Harvard Business Review, 79(8), 137–147."),
 ("DANIELA", "Arregle, J.-L., Chirico, F., Kano, L., Kundu, S. K., Majocchi, A., & Schulze, W. S. "
             "(2021). Family firm internationalization: Past research and an agenda for the future. "
             "Journal of International Business Studies, 52, 1159–1198."),
 ("YASIR",   "Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of "
             "international expansion: The link between multinationality and performance in the "
             "service sector. Journal of International Business Studies, 34(1), 5–18."),
 ("YASIR",   "Mezias, J. M. (2002). Identifying liabilities of foreignness and strategies to "
             "minimize their effects: The case of labor lawsuit judgments in the United States. "
             "Strategic Management Journal, 23(3), 229–244."),
 ("APPENDIX A", "Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and "
             "biases. Science, 185(4157), 1124–1131."),
]
y = 168
for who, ref in refs:
    pg.draw_rect(pymupdf.Rect(M, y - 8, M + 2.5, y + 4), color=None, fill=GOLD)
    text(pg, M + 12, y, who, "monob", 6.2, GOLD)
    y = box(pg, M + 12, y + 14, W - 2*M - 24, ref, "ser", 8.6, WHITE) + 14
text(pg, M, H - 54, "Presented by Daniela Garcia Aguirre and Yasir A. Malik  ·  GEB 7365 "
                    "International Business Theory and Practice  ·  Prof. William Newburry",
     "ser", 6.8, DIM)

doc.save(OUT, garbage=3, deflate=True)
print("wrote", OUT, "| pages", doc.page_count)
