"""
Generates the research-model path diagram for Chapter 3:
8 intervention IVs -> 2 mediators (AJQ, APR) -> DV (RAB),
with 8 direct paths (dashed) and 8 mediated paths (solid).
Outputs: Anchoring_Bias_Research_Model.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(13.5, 9.0), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 10.4)
ax.axis("off")

# ---- colors ----
IV_FACE   = "#E8F0FE"; IV_EDGE   = "#1A4E8A"
MED_FACE  = "#FFF4E5"; MED_EDGE  = "#B8650A"
DV_FACE   = "#E9F7EF"; DV_EDGE   = "#1E7A46"
DIRECT_C  = "#8A8F98"   # dashed direct paths
MED_C     = "#1A4E8A"   # solid IV->mediator
PATH_C    = "#B8650A"   # mediator->DV

def box(x, y, w, h, text, fc, ec, fs=10.5, bold=True):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.12",
                       linewidth=1.6, facecolor=fc, edgecolor=ec, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", color="#1a1a1a", zorder=4)

# ---- node coordinates ----
# 8 IVs, top-to-bottom; first 6 feed AJQ, last 2 feed APR
ivs = [
    ("Training &\nAwareness (TA)",            9.55, "AJQ", "H1", "H2"),
    ("Rotation of\nAuditors (RA)",            8.40, "AJQ", "H3", "H4"),
    ("Use of Analytical\nTools (AT)",         7.25, "AJQ", "H5", "H6"),
    ("Feedback &\nReflection (FR)",           6.10, "AJQ", "H9", "H10"),
    ("Regulatory & Prof.\nGuidance (RPG)",    4.95, "AJQ", "H13", "H14"),
    ("Performance Metrics\n& Incentives (PMI)",3.80,"AJQ", "H15", "H16"),
    ("Structured Auditing\nProcesses (SAP)",  2.55, "APR", "H7", "H8"),
    ("Independent\nReviews (IR)",             1.30, "APR", "H11", "H12"),
]
IV_X, IV_W, IV_H = 2.05, 2.7, 0.92
MED_X = 6.85
AJQ_Y, APR_Y = 6.85, 1.95
DV_X, DV_Y = 11.1, 4.6

# ---- draw IV boxes ----
for label, y, med, hd, hm in ivs:
    box(IV_X, y, IV_W, IV_H, label, IV_FACE, IV_EDGE, fs=9.6)

# ---- mediator + DV boxes ----
box(MED_X, AJQ_Y, 2.9, 1.05, "Auditor Judgment\nQuality (AJQ)", MED_FACE, MED_EDGE, fs=10.5)
box(MED_X, APR_Y, 2.9, 1.05, "Audit Process\nRigor (APR)",     MED_FACE, MED_EDGE, fs=10.5)
box(DV_X, DV_Y, 2.7, 1.45, "Reduction in\nAnchoring Bias\n(RAB)", DV_FACE, DV_EDGE, fs=11.5)

def arrow(p0, p1, color, ls="-", lw=1.6, rad=0.0, z=2):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=15,
                        connectionstyle=f"arc3,rad={rad}", linewidth=lw,
                        linestyle=ls, color=color, zorder=z,
                        shrinkA=2, shrinkB=3)
    ax.add_patch(a)

def lbl(x, y, t, color):
    ax.text(x, y, t, fontsize=8.2, color=color, fontweight="bold",
            ha="center", va="center", zorder=5,
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85))

# ---- mediated paths: IV -> mediator (solid blue) ----
for label, y, med, hd, hm in ivs:
    my = AJQ_Y if med == "AJQ" else APR_Y
    start = (IV_X + IV_W/2, y)
    end   = (MED_X - 2.9/2, my)
    rad = 0.06 if y > my else -0.06
    arrow(start, end, MED_C, ls="-", lw=1.5, rad=rad)
    # label near the IV end
    lbl(start[0] + 0.85, (y*0.7 + my*0.3) + (0.12 if y > my else -0.12), hm, MED_C)

# ---- mediator -> DV (solid orange, heavier) ----
arrow((MED_X + 2.9/2, AJQ_Y), (DV_X - 2.7/2, DV_Y + 0.35), PATH_C, lw=2.4, rad=-0.08)
arrow((MED_X + 2.9/2, APR_Y), (DV_X - 2.7/2, DV_Y - 0.35), PATH_C, lw=2.4, rad=0.08)
lbl(9.05, 6.0, "a-paths", PATH_C)
lbl(9.05, 3.2, "b-paths", PATH_C)

# ---- direct paths: IV -> DV (dashed grey, bowed outward) ----
for label, y, med, hd, hm in ivs:
    start = (IV_X + IV_W/2, y - 0.18)
    end   = (DV_X - 2.7/2, DV_Y + (y - DV_Y) * 0.16)
    rad = 0.30 if y > DV_Y else -0.30
    arrow(start, end, DIRECT_C, ls=(0, (5, 3)), lw=1.1, rad=rad, z=1)
    lbl(IV_X + IV_W/2 + 0.55, y - 0.55, hd, DIRECT_C)

# ---- title + legend ----
ax.text(6.5, 10.15, "Figure 1.  Research Model: Audit-Process Interventions, Judgment Mediators,",
        ha="center", va="center", fontsize=13, fontweight="bold", color="#1a1a1a")
ax.text(6.5, 9.78, "and the Reduction of Anchoring Bias in Long-Term Auditor Engagements",
        ha="center", va="center", fontsize=13, fontweight="bold", color="#1a1a1a")

leg_y = 0.45
ax.plot([0.4, 1.3], [leg_y, leg_y], color=MED_C, lw=1.6)
ax.text(1.45, leg_y, "Mediated path (IV → mediator)", fontsize=9, va="center")
ax.plot([5.0, 5.9], [leg_y, leg_y], color=PATH_C, lw=2.4)
ax.text(6.05, leg_y, "Mediator → DV path", fontsize=9, va="center")
ax.plot([8.2, 9.1], [leg_y, leg_y], color=DIRECT_C, lw=1.1, linestyle=(0, (5, 3)))
ax.text(9.25, leg_y, "Direct path (IV → DV)", fontsize=9, va="center")

plt.tight_layout()
out = "Anchoring_Bias_Research_Model.png"
plt.savefig(out, bbox_inches="tight", facecolor="white")
print("wrote", out)
