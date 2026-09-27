#!/usr/bin/env python3
"""GEB 7365 final paper, Draft 2: the course copy revised against the residency minutes.

Source: geb7365_report.json (Draft 1, 11 Sep). Edits carry the 19 September residency
feedback and Newburry's final-paper guidance into the Canvas copy, without blinding:

  1. H1 in words: "unchanged or lower", not "weakly decreases" (text and Table 3)
  2. Level of analysis stated first in the method, with the nesting and the sample size
  3. Region is a variable, not a setting (the question put to Group C)
  4. Which hypothesis carries the contribution (the note to Group A)
  5. Controls: why firm size and profitability have no analogue, and what stands in for them
  6. Preliminary evidence gets its own section between method and discussion
  7. Gap framed as what the literature has focused on, not what nobody has done
"""
import json, copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
src = json.load(open(os.path.join(HERE, "geb7365_report.json")))
spec = copy.deepcopy(src)

REPL = [
 ("The gap is that nobody has asked what happens to this picture when the target population is rare.",
  "The gap is that the literature has focused on the extent of response variation in general populations and has not asked what happens to this picture when the target population is rare."),
 ("Adding a national frame to such a design weakly decreases joint feasibility and can never increase it.",
  "Adding a national frame to such a design leaves joint feasibility unchanged or lowers it, and can never raise it."),
 ("every additional country weakly worsens the design and no additional country can improve it",
  "every additional country leaves the design where it was or makes it worse, and no additional country can improve it"),
 ("adding a frame weakly decreases it", "adding a frame leaves it unchanged or lowers it"),
 ("Five hypotheses follow. The first is analytic and states the structure of the problem. The remaining four are empirical and each draws its theoretical logic from one of the streams above.",
  "Five hypotheses follow. The first is analytic and states the structure of the problem. The remaining four are empirical and each draws its theoretical logic from one of the streams above. They do not carry equal weight. H1 is the structural result on which the others rest, and it is not itself the contribution to international business. H2 is: it is where regionalization theory makes a prediction about the infrastructure through which the field reaches its respondents, and it is the hypothesis the design is built to identify."),
 ("The unit of analysis is the country-panel-occupation cell: one specialist occupation, on one panel provider, in one national frame.",
  "The study has three levels of analysis, and stating them matters because the model attributes each term to a different one. The unit is the country-panel-occupation cell: one specialist occupation, on one panel provider, in one national frame. Cells are nested within national frames, frames are nested within regions, and providers are cross-classified with frames because one provider operates in several."),
 ("Panel providers are selected to vary on home region deliberately, because H2 is unidentifiable if every provider originates in the same place.",
  "Panel providers are selected to vary on home region deliberately, because H2 is unidentifiable if every provider originates in the same place. Region is therefore a variable in this design, not a setting. A study confined to one country or one region could not test H2, because region concordance would not vary; the matrix is chosen so that every frame is observed both inside and outside a provider's home region."),
 ("and any finding that does not separate it from the terms that are not under control would be uninterpretable.",
  "and any finding that does not separate it from the terms that are not under control would be uninterpretable. Firm size and profitability, the controls a firm-level study in international business would almost always carry, have no direct analogue here because the unit is a cell rather than a firm. Their nearest counterpart is the provider's total panel size, which is entered at the provider level so that a large provider's reach is not mistaken for a regional effect."),
 ("and the preliminary evidence reported in the discussion comes from the author's prior study",
  "and the preliminary evidence reported in the next section comes from the author's prior study"),
]
def edit(x):
    if isinstance(x, str):
        for a, b in REPL: x = x.replace(a, b)
        return x
    if isinstance(x, list): return [edit(v) for v in x]
    if isinstance(x, dict): return {k: edit(v) for k, v in x.items()}
    return x
spec["body"] = edit(spec["body"]); spec["tables"] = edit(spec["tables"])
flat = json.dumps(spec)
missing = [a[:60] for a, n in REPL if n not in flat]
assert not missing, missing
assert "weakly" not in flat, "a 'weakly' survived"

# 6. Move the validating case into its own Preliminary Evidence section before the discussion
b = spec["body"]
def idx(head):
    return next(i for i, it in enumerate(b) if isinstance(it, dict) and list(it.values())[0] == head)
vc = next(i for i, it in enumerate(b) if isinstance(it, list) and any(isinstance(s, str) and s.startswith("The author's own study supplies one fully documented validating case") for s in it))
case = b.pop(vc)
case = [s.replace("The author's own study supplies one fully documented validating case.",
                  "The author's own study supplies one fully documented validating case, and it is the only evidence this paper offers in advance of fieldwork.") if isinstance(s, str) else s for s in case]
d = idx("Discussion and Conclusions")
b[d:d] = [{"h1": "Preliminary Evidence"}, case,
          ["Carried through Tables 1 and 2, those inputs illustrate H1 in magnitude. To yield 30 usable responses, a "
           "design confined to Spain needs a frame of about 18.8 million panel members; adding Germany, Japan, the United "
           "Kingdom and China raises the requirement in every country to about 72.2 million, roughly four times as large, "
           "while the mean response rate falls by only about a third. The panel that produced the validating case had "
           "334,976 members. This is a validation of the model's inputs and an illustration of the binding-frame effect, "
           "not a test of any hypothesis, and it says nothing yet about H2 to H5, which need the matrix described above."]]

spec["subtitle"] = "Formal Project Report · Draft 2"
spec["ident"] = [s if not s.startswith("Draft 1") else
                 "Draft 2 · 27 September 2026 · revised after the 19 September residency · Report due 9 October 2026"
                 for s in spec["ident"]]
json.dump(spec, open(os.path.join(HERE, "geb7365_report_draft2.json"), "w"))

from build_dba_doc import build
out = os.path.join(HERE, "..", "GEB7365_International_Business", "Malik_GEB7365_ProjectReport_DRAFT2.docx")
build(spec, out)
words = len(" ".join(s for it in spec["body"] if isinstance(it, list) for s in it if isinstance(s, str)).split())
print("built", os.path.abspath(out), "body words", words)
