# -*- coding: utf-8 -*-
"""Figure for GEB 7911 Learning Memo 6.

The argument of Gerlach and Cenfetelli (2020) runs in four moves, and each
move is carried by a different writing device from Creswell and Poth's
Chapter 9. Drawing the two rows together is the point: the rhetoric is not
decoration on the argument, it is how the argument advances.
"""
from PIL import Image, ImageDraw, ImageFont

W, H, S = 1560, 1394, 2          # S = supersample factor
F = "/usr/share/fonts/truetype/liberation/"
def f(n, sz): return ImageFont.truetype(F + n, sz * S)
SER, SERB, SERI = "LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf", "LiberationSerif-Italic.ttf"
MON, MONB = "LiberationMono-Regular.ttf", "LiberationMono-Bold.ttf"

INK = (20, 23, 28); MUTE = (118, 125, 134); PAPER = (252, 251, 248)
BLUE = (8, 30, 63); GOLD = (182, 134, 44); RUST = (140, 58, 27)
TEAL = (28, 107, 99); RULE = (216, 212, 203); SOFT = (232, 237, 244)
WARM = (250, 243, 228); WHITE = (255, 255, 255)

im = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(im)

def box(x, y, w, h, fill=None, outline=None, lw=1, r=8):
    d.rounded_rectangle([x*S, y*S, (x+w)*S, (y+h)*S], radius=r*S,
                        fill=fill, outline=outline, width=lw*S)
def txt(s, x, y, font, sz, col=INK, anchor="la"):
    d.text((x*S, y*S), s, font=f(font, sz), fill=col, anchor=anchor)
def wrap(s, x, y, w, font, sz, col=INK, lead=None):
    fo = f(font, sz); lead = lead or sz * 1.35
    words, line, yy = s.split(), "", y
    for wd in words:
        cand = (line + " " + wd).strip()
        if d.textlength(cand, font=fo) <= w * S:
            line = cand
        else:
            d.text((x*S, yy*S), line, font=fo, fill=col); yy += lead; line = wd
    if line: d.text((x*S, yy*S), line, font=fo, fill=col); yy += lead
    return yy

def arrow(x1, y1, x2, y2, col=MUTE, lw=3, head=14):
    d.line([x1*S, y1*S, x2*S, y2*S], fill=col, width=lw*S)
    d.polygon([(x2*S, y2*S), ((x2-head)*S, (y2-head*0.55)*S),
               ((x2-head)*S, (y2+head*0.55)*S)], fill=col)

# ---- title ----
txt("HOW THE WRITING DOES THE ARGUMENT", 60, 52, MONB, 19, GOLD)
txt("Gerlach & Cenfetelli (2020) unseat a label in four moves.", 60, 88, SERB, 34, BLUE)
txt("Each move is carried by a different device from Creswell & Poth, Chapter 9.",
    60, 132, SERI, 23, MUTE)
d.line([60*S, 182*S, (W-60)*S, 182*S], fill=RULE, width=2*S)

# ---- four panels ----
PANELS = [
 ("1", "THE LABEL", BLUE, SOFT,
  "Constant checking is named as addiction, in the press and in the literature.",
  ["Epigraph before the Introduction, from a news report (Shanker 2017)",
   "Scare quotes on every contested term: “technology addiction,” “behavioral addictions”",
   "Block quote of the opposing definition, six criteria, cited to the page (Turel et al. 2011, p. 1044)"]),
 ("2", "THE DOUBT", RUST, WARM,
  "The label is shown to be manufactured rather than found.",
  ["Block quotes from critics, used adversarially rather than supportively",
   "A ridiculing example left in quotation marks: addiction to “Argentine tango”",
   "Scare quotes on “discovery” to mark a claim the authors will not grant"]),
 ("3", "THE EVIDENCE", TEAL, WHITE,
  "Ninety participants speak, and the reader is told what to hear before they speak.",
  ["Long block quotes, indented, each closed with (#26, 31f): number, age, sex",
   "Lead-in, quote, interpretation. The analyst frames before and after, every time",
   "Data structure diagram: first-order codes, second-order categories, themes",
   "Appendix B: four further tables of quotes, with a caveat that they are out of context"]),
 ("4", "THE REPLACEMENT", GOLD, WARM,
  "A new construct is defined and the old one is retired.",
  ["A formal definition, set apart and repeated verbatim in the abstract",
   "Eight numbered propositions, indented like hypotheses but never called hypotheses",
   "Figure 1, an overview model, so the theory can be seen whole",
   "Practical implications addressed to designers, to businesses, and to users themselves"]),
]

PW, GAP, X0, Y0, PH, VGAP = 716, 24, 60, 208, 366, 22
for i, (num, head, col, fill, claim, devices) in enumerate(PANELS):
    cx, cy = i % 2, i // 2
    x = X0 + cx * (PW + GAP)
    y = Y0 + cy * (PH + VGAP)
    box(x, y, PW, PH, fill=fill, outline=col, lw=2, r=10)
    box(x, y, PW, 6, fill=col, r=3)
    box(x + 22, y + 26, 36, 36, fill=col, r=6)
    txt(num, x + 40, y + 33, MONB, 19, WHITE, anchor="ma")
    txt(head, x + 72, y + 35, MONB, 16, col)
    yy = wrap(claim, x + 22, y + 86, PW - 44, SERB, 21, INK, lead=29)
    d.line([(x+22)*S, (yy+12)*S, (x+PW-22)*S, (yy+12)*S], fill=col, width=1*S)
    yy += 32
    txt("THE DEVICE", x + 22, yy, MONB, 12, col)
    yy += 26
    for dev in devices:
        d.ellipse([(x+24)*S, (yy+8)*S, (x+31)*S, (yy+15)*S], fill=col)
        yy = wrap(dev, x + 42, yy, PW - 68, SER, 17, (58, 64, 72), lead=23) + 9

# ---- the band underneath ----
BY = Y0 + 2 * PH + VGAP + 34
box(60, BY, W - 120, 250, fill=BLUE, r=10)
txt("RUNNING THROUGH ALL FOUR", 88, BY + 22, MONB, 13, GOLD)
band = [
 ("First person plural", "“we chose,” “we coded,” “we felt.” The authors are present as actors, never as persons"),
 ("Metatext at every seam", "“In what follows, we first …”  “Up to this point, we have reported … We now move to”"),
 ("Procedural reflexivity", "Preconceptions are managed by design, not disclosed by biography. No positionality statement appears"),
]
by = BY + 52
for lab, ex in band:
    txt(lab, 88, by, SERB, 21, WHITE)
    by = wrap(ex, 88, by + 30, W - 200, SER, 17, (185, 199, 216), lead=23) + 10

# ---- footer ----
FY = BY + 272
d.line([60*S, FY*S, (W-60)*S, FY*S], fill=RULE, width=1*S)
yy = wrap("Read 1 to 4. The paper does not argue against the addiction label and then present its findings. "
          "The findings are staged so that the label has already been weakened before the first participant speaks.",
          60, FY + 18, W - 120, SERI, 20, INK, lead=27)
txt("Yasir A. Malik  ·  GEB 7911  ·  Learning Memo 6", 60, yy + 12, MONB, 13, MUTE)

im.resize((W, H), Image.LANCZOS).save(
    "/home/user/Profile/dba/coursework/GEB7911_Qualitative_Research_Methods/figures/memo6_rhetoric.png")
print("figure written")
