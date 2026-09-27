#!/usr/bin/env python3
"""AIB-LAC 2027 submission, Interactive track, built from the GEB 7365 report spec.

Takes geb7365_report.json (the course paper) and produces two blinded specs:
the conference paper and a sub-1,500-word extended abstract. Blinding means
no author, institution, cohort, instructor or course line anywhere, and the
course's AI-use disclosure removed, since it names the university and is a
requirement of the course, not of the conference.

Four content edits carry the 19 September feedback into the paper: the gap is
what the literature has not asked rather than what nobody has done; H1 says
unchanged-or-lower rather than "weakly decreases"; the level of analysis is
stated in words; and the abstract and keywords the call for papers requires
are added. The course copy is untouched.
"""
import json, copy, re, sys, subprocess, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "geb7365_report.json")))

ABSTRACT = (
 "Comparative international business research assumes it can reach the same population in every "
 "country in a design. For narrow specialist professional populations that assumption fails in a "
 "way the literature reports as a limitation after the fact. This paper argues it is a parameter "
 "that can be estimated before a study is fielded. Reachable usable sample is modelled as the "
 "product of frame size, specialist prevalence, response rate and screen survival, each decided at "
 "a different level of analysis. Because a comparative claim is a conjunction, joint feasibility is "
 "set by the least feasible national frame, not the average, and adding a frame can only leave it "
 "unchanged or lower it. Four further hypotheses draw on regionalization theory, born-regional "
 "internationalization, levels-of-analysis research and control-versus-coordination work to predict "
 "where specialist prevalence concentrates and why standardization costs response most in the frames "
 "that already bind. The design reads reachable counts from panel providers' own audience-configuration "
 "interfaces, before any commitment, across a matrix of occupations, national frames and providers. "
 "A documented case in which a panel of 334,976 yielded roughly twenty eligible participants validates "
 "the model. No data have yet been collected for the study proposed.")
KEYWORDS = ("Keywords: comparative research design; specialist populations; sampling feasibility; "
            "regionalization; levels of analysis; survey methodology; response rates")

def edit_text(s):
    s = s.replace("The gap is that nobody has asked what happens to this picture when the target population is rare.",
                  "The gap is that the literature has focused on the extent of response variation in general populations and has not asked what happens to this picture when the target population is rare.")
    s = s.replace("Adding a national frame to such a design weakly decreases joint feasibility and can never increase it.",
                  "Adding a national frame to such a design leaves joint feasibility unchanged or lowers it, and can never raise it.")
    s = s.replace("The unit of analysis is the country-panel-occupation cell: one specialist occupation, on one panel provider, in one national frame.",
                  "The study has three levels of analysis, and stating them matters because the model attributes each term to a different one. The unit is the country-panel-occupation cell: one specialist occupation, on one panel provider, in one national frame. Cells are nested within national frames, frames are nested within regions, and providers are cross-classified with frames because one provider operates in several.")
    s = s.replace("The author's own study", "A prior study by the author")
    s = s.replace("the author's own study", "a prior study by the author")
    return s

def walk(x):
    if isinstance(x, str): return edit_text(x)
    if isinstance(x, list): return [walk(v) for v in x]
    if isinstance(x, dict): return {k: walk(v) for k, v in x.items()}
    return x

def blinded(spec, subtitle):
    out = copy.deepcopy(spec)
    out["title"] = spec["title"]
    out["subtitle"] = subtitle
    out["ident"] = []                       # no author, no institution, no course
    body = walk(out["body"])
    # drop the course AI-use disclosure (names the university; a course rule, not the conference's)
    cut = next((i for i, it in enumerate(body) if isinstance(it, dict) and "Disclosure" in str(list(it.values())[0])), None)
    if cut is not None: body = body[:cut]
    body = [{"h2": "Abstract"}, [ABSTRACT], [KEYWORDS]] + body
    out["body"] = body
    out["tables"] = walk(out.get("tables", {}))
    return out

paper = blinded(src, "Submission to the AIB Latin America and the Caribbean Chapter Conference 2027, San Juan · Interactive session · Blinded for review")
json.dump(paper, open(os.path.join(HERE, "aiblac_paper.json"), "w"))

# ---- extended abstract: introduction, the five hypotheses in one paragraph each, method, one table ----
def para(after, n=1, body=paper["body"]):
    for i, it in enumerate(body):
        if isinstance(it, dict) and list(it.values())[0] == after:
            return [b for b in body[i+1:i+1+n] if isinstance(b, list)]
    return []
ea_body = [{"h2": "Abstract"}, [ABSTRACT], [KEYWORDS], {"h2": "The problem"}] + para("Introduction", 2) + \
          [{"h2": "The model and the hypotheses"}] + para("H1. The binding-frame hypothesis", 1) + \
          para("H2. The regional bounding hypothesis", 1) + para("H3. The born-regional design hypothesis", 1) + \
          para("H4. The mode dominance hypothesis", 1) + para("H5. The standardization tension hypothesis", 1) + \
          [{"h2": "Method"}] + para("Study context", 3) + [{"h2": "Contribution"}] + para("Theoretical contributions", 1) + \
          [{"__table__": "t3"}]
ea = copy.deepcopy(paper); ea["subtitle"] = "Extended abstract · AIB-LAC 2027, San Juan · Interactive session · Blinded for review"
ea["body"] = ea_body
json.dump(ea, open(os.path.join(HERE, "aiblac_extended_abstract.json"), "w"))

def words(spec):
    t=[]
    def w(x):
        if isinstance(x,str): t.append(x)
        elif isinstance(x,list): [w(v) for v in x]
        elif isinstance(x,dict): [w(v) for v in x.values()]
    w(spec["body"]); w(spec.get("tables",{})); return len(" ".join(t).split())
print("paper words (all inclusive):", words(paper)); print("extended abstract words (all inclusive):", words(ea))
full=json.dumps(paper)+json.dumps(ea)
for bad in ("Malik","Yasir","Florida International","FIU","Cohort","Newburry","GEB 7365","IRB-25"):
    if bad in full: print("  BLINDING FAILURE:", bad)
print("blinding check done")
