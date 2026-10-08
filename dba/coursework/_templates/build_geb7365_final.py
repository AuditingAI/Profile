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
p["ident"] = p["ident"][:4] + ["9 October 2026"]
D = os.path.join(HERE, "..", "GEB7365_International_Business")
out = os.path.join(D, "Malik_GEB7365_ProjectReport_FINAL.docx")
build(p, out)
d = Document(out); single = False
for para in d.paragraphs:
    if para.style.name == "Heading 1":
        single = para.text.strip() in ("References", "Tables and Figures")
    elif single:
        para.paragraph_format.line_spacing = 1.0
        para.paragraph_format.space_after = Pt(6)
d.save(out)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", D, out], check=True, capture_output=True)
