"""
Dissertation-extension model figure (v2): the validated human-side core
(interventions -> AJQ/APR -> RAB) plus the AI layer — algorithmic anchor,
LLM sycophancy reinforcement, and epistemic risk — with the broadened
risk & assurance population frame. Outputs: Anchoring_Bias_Model_v2_Dissertation.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(13.5, 8.2), dpi=200)
ax.set_xlim(0, 13.5)
ax.set_ylim(0, 9.2)
ax.axis("off")

IV_FACE, IV_EDGE = "#E8F0FE", "#1A4E8A"
MED_FACE, MED_EDGE = "#FFF4E5", "#B8650A"
DV_FACE, DV_EDGE = "#E9F7EF", "#1E7A46"
AI_FACE, AI_EDGE = "#FDECEC", "#B00020"

def box(x, y, w, h, text, fc, ec, fs=10.5):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        linewidth=1.7, facecolor=fc, edgecolor=ec, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, fontweight="bold",
            color="#1c2733", zorder=4)

def arrow(x1, y1, x2, y2, color, style="-", lw=1.8):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
        mutation_scale=16, linewidth=lw, linestyle=style, color=color, zorder=2))

# Population frame
ax.add_patch(FancyBboxPatch((0.2, 0.25), 13.1, 8.6, boxstyle="round,pad=0.02,rounding_size=0.18",
    linewidth=1.2, facecolor="none", edgecolor="#8A8F98", linestyle=(0,(4,3)), zorder=1))
ax.text(6.75, 8.62, "BROADENED POPULATION — RISK & ASSURANCE PROFESSIONALS "
        "(external/internal audit · ERM · compliance · credit review · QA · SOX)",
        ha="center", fontsize=9.5, color="#5A6068", fontweight="bold")

# Human-side core (validated, this study)
box(2.1, 6.6, 3.4, 1.5, "8 MITIGATION\nINTERVENTIONS\n(TA·RA·AT·SAP·FR·IR·RPG·PMI)", IV_FACE, IV_EDGE, 10)
box(6.15, 7.3, 2.9, 1.0, "Auditor Judgment\nQuality (AJQ)", MED_FACE, MED_EDGE)
box(6.15, 5.85, 2.9, 1.0, "Audit Process\nRigor (APR)", MED_FACE, MED_EDGE)
box(10.7, 6.6, 3.2, 1.3, "REDUCTION IN\nANCHORING BIAS (RAB)", DV_FACE, DV_EDGE)
arrow(3.8, 6.95, 4.7, 7.3, "#1A4E8A"); arrow(3.8, 6.25, 4.7, 5.9, "#1A4E8A")
arrow(7.6, 7.3, 9.2, 6.85, "#B8650A"); arrow(7.6, 5.85, 9.2, 6.35, "#B8650A")
arrow(3.8, 6.6, 9.1, 6.6, "#8A8F98", style=(0,(4,3)), lw=1.4)
ax.text(3.05, 8.05, "VALIDATED HUMAN-SIDE CORE (this study)", fontsize=9.5,
        color="#1A4E8A", fontweight="bold")

# AI extension layer (dissertation) — refined 4-node chain
box(1.85, 2.9, 2.9, 1.5, "LLM / AI\nAUDIT TOOL", AI_FACE, AI_EDGE, 10)
box(4.95, 2.9, 2.9, 1.5, "AUTOMATED\nANCHORING\n(system-generated anchors\npumped at scale)", AI_FACE, AI_EDGE, 8.6)
box(8.05, 2.9, 2.9, 1.5, "SYCOPHANTIC\nCONFIRMATION\n(model affirms the\nstated position)", AI_FACE, AI_EDGE, 8.6)
box(11.35, 2.9, 3.0, 1.5, "RECURSIVE\nEPISTEMIC DRIFT\n(models redoing the same\nwork converge on error)", AI_FACE, AI_EDGE, 8.6)
arrow(3.3, 2.9, 3.5, 2.9, "#B00020")
arrow(6.4, 2.9, 6.6, 2.9, "#B00020")
arrow(9.5, 2.9, 9.85, 2.9, "#B00020")

# Cross-layer links
arrow(11.35, 3.68, 10.7, 5.9, "#B00020", style=(0,(4,3)))
ax.text(11.5, 4.75, "erodes RAB", fontsize=9, color="#B00020", rotation=75, va="center")
arrow(2.1, 5.8, 2.1, 3.62, "#1A4E8A", style=(0,(4,3)))
ax.text(1.75, 4.7, "govern the tool", fontsize=9, color="#1A4E8A", rotation=90, va="center")
arrow(6.15, 5.3, 8.0, 3.68, "#B00020", style=(0,(4,3)))
ax.text(7.15, 4.65, "prior anchor enters the prompt", fontsize=8.5, color="#B00020", rotation=-35, va="center")

ax.text(3.05, 1.85, "AI EXTENSION LAYER (dissertation)", fontsize=9.5, color="#B00020", fontweight="bold")
ax.text(6.75, 0.62, "Refined chain: LLM output becomes the anchor itself — automated, continuous, at scale (automation bias: Parasuraman & Manzey, 2010) → sycophancy confirms it (Sharma et al., 2024; Fanous et al., 2025)\n→ feedback loops amplify (Glickman & Sharot, 2025) → recursive reprocessing converges and drifts (Shumailov et al., 2024, Nature; Messeri & Crockett, 2024) — the LLM layer itself produces the risk (NIST AI 600-1)",
        ha="center", fontsize=8.0, color="#5A6068")

plt.tight_layout()
plt.savefig("Anchoring_Bias_Model_v2_Dissertation.png", bbox_inches="tight", facecolor="white")
print("wrote Anchoring_Bias_Model_v2_Dissertation.png")
