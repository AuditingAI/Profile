#!/usr/bin/env python3
"""GEB 7365 final paper for Canvas, 9 Oct 2026: Draft 3 content, final labels, fitted to the
30-page limit (inclusive) by single-spacing the references and the tables-and-figures section.
Body text stays double-spaced. Content edits remain Yasir's voice pass."""
import json, os, subprocess, sys
from docx import Document
from docx.shared import Pt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from build_dba_doc import build
p = json.load(open(os.path.join(HERE, "geb7365_report_draft3.json")))
p["subtitle"] = "Formal Project Report"
p = json.loads(json.dumps(p).replace("was used to organise this draft", "was used to organise this paper"))
p["ident"] = p["ident"][:4] + ["9 October 2026"]

FIG2 = os.path.join(HERE, "..", "GEB7365_International_Business", "figures", "fig2_study_model.png")
b = p["body"]
i_pe = next(i for i, x in enumerate(b) if isinstance(x, dict) and x.get("h1") == "Preliminary Evidence")
b[i_pe:i_pe] = [
    {"h2": "Data sources, analysis software and timeframe"},
    ["Figure 2 brings the five hypotheses together in one model. The data come from two sources. The first is the audience-configuration estimates that commercial panel providers return for each occupation, country and provider cell, which supply the dependent variable for H1, H2 and H4 before any fieldwork is commissioned. The second is a coded sample of published cross-national survey studies in international business journals, which supplies achieved coverage and response for H3, H4 and H5, alongside the response-rate evidence reported by Harzing, Reiche and Pudelko (2013). The sensitivity analysis for H1 is run in Python, and the multilevel and cross-classified models for H2, H4 and H5 in R using the lme4 package. The study is planned over about twelve months: quotes collected across the cell matrix in months one to three, the published studies coded in months two to six, models estimated in months seven to nine, and the paper written in months ten to twelve."],
]
i_d = next(i for i, x in enumerate(b) if isinstance(x, dict) and x.get("h1") == "Disclosure of Artificial Intelligence Use")
for x in b:
    if isinstance(x, dict) and "image" in x and "fig1" in x["image"]: x["width_in"] = 5.6
b[i_d:i_d] = [
    {"h2": "Figure 2. The study model: five hypotheses"},
    {"image": FIG2, "width_in": 5.6, "alt": "Model diagram. Three inputs on the left, region concordance (H2, positive), data-collection mode (H4) and instrument standardization (H5, negative, moderated by baseline response), point to the dependent variable in the centre, reachable usable sample per cell and achieved response. Two outcomes on the right follow from it: joint feasibility, set by the least feasible frame (H1, analytic), and the regionally concentrated coverage of studies described as cross-national (H3). A top band gives the levels of analysis and a bottom band lists the controls.", "caption": "Figure 2. The five hypotheses in one model. Prepared with AI assistance for layout from the author's hypotheses."},
]
p = json.loads(json.dumps(p).replace("to produce Figure 1 from the author's own model code,", "to produce Figure 1 from the author's own model code and lay out Figure 2 from the author's hypotheses, to draft the paragraph on data sources, software and timeframe from the author's design,"))
D = os.path.join(HERE, "..", "GEB7365_International_Business")
out = os.path.join(D, "Malik_GEB7365_ProjectReport_FINAL.docx")
build(p, out)
d = Document(out); single = False
for para in d.paragraphs:
    if para.style.name == "Heading 1":
        single = para.text.strip() in ("References", "Tables and Figures", "Disclosure of Artificial Intelligence Use")
    elif single:
        para.paragraph_format.line_spacing = 1.0
        para.paragraph_format.space_after = Pt(6)
d.save(out)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", D, out], check=True, capture_output=True)
