#!/usr/bin/env python3
"""AIB-LAC 2027 paper, revision 2: Newburry's 28 September comments applied.

Input: aiblac_paper.json (blinded v1, from build_aiblac_submission.py).
Output: aiblac_paper_v2.json, aiblac_extended_abstract_v2.json, and the two blinded .docx files.

Newburry's tracked changes are accepted as he wrote them (title, abstract, Latin America opening,
"often", ecological fallacy, his three references). His ten comments are answered as follows:
C19 limitation clause softened · C20 power-analysis analogy (Cohen) · C22/C30 page numbers from the
PDFs (Lopez p. 1236, Zeng p. 1599) · C31 Geleilate et al. (2016) · C32 citations in every hypothesis
· C33 formal statement at the end of each hypothesis · C40 method citations · C41 discussion
citations · C42 a Latin America section. Every added citation was checked against a publisher or
index record on 28 Sep 2026. Also: Harzing et al. is 2013, 7(1): 112-134, and "weakly" is gone.
"""
import json, copy, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
src = json.load(open(os.path.join(HERE, "aiblac_paper.json")))
p = copy.deepcopy(src); b = p["body"]

def find(sub):
    hits = [i for i, it in enumerate(b) if isinstance(it, list) and any(isinstance(s, str) and sub in s for s in it)]
    assert len(hits) == 1, (sub[:60], hits); return hits[0]
def head(title):
    return next(i for i, it in enumerate(b) if isinstance(it, dict) and list(it.values())[0] == title)
def rep(old, new):
    i = find(old); b[i] = [s.replace(old, new) if isinstance(s, str) else s for s in b[i]]
def append_to(sub, extra):
    i = find(sub); b[i] = [s + extra if isinstance(s, str) and sub in s else s for s in b[i]]

# ---- Newburry's tracked changes ---------------------------------------------------------------
p["title"] = p["title"].replace("When Comparative Research", "When Comparative International Research")
rep("Reachable usable sample is modelled", "A reachable usable sample is modelled")
rep("why standardization costs response most", "why standardization costs most")
rep("with an instrument that means the same thing in each place.",
    "with an instrument that means the same thing in each place. Even in a region such as Latin America, "
    "which is more homogeneous than most, researchers must take efforts to adapt their research instruments to "
    "differences in language, culture and other variables. For example, Hermans et al. (2017) needed to adapt "
    "their survey instrument to variations in Spanish across the region.")
rep("this requirement is demanding but routine.", "this requirement is demanding but routine, as in the Latin America example above.")
rep("a limitation is confessed after the study has failed", "a limitation is often confessed after the study has failed")
append_to("The Korean telephone datum is precisely such a case.",
    " In a sense, this is parallel to the ecological fallacy, which is a significant issue in cultural and other "
    "research, and refers to 'applying aggregate-level reasoning at the individual level' (Hofstede, 2001: 16; "
    "Robinson, 1950).")

# ---- C19, C20 ------------------------------------------------------------------------------------
rep("That distinction is invisible to a literature that reports sampling as a limitation, because a limitation is by definition something discovered afterward.",
    "That distinction is easy to miss in a literature that reports sampling as a limitation rather than modelling it as a constraint on the design.")
rep("A parameter is estimated before a study is designed and it constrains the design;",
    "A parameter is estimated before a study is designed and it constrains the design, in the way an a priori power analysis fixes the sample a design needs before any data are collected (Cohen, 1988);")

# ---- C22, C30: page numbers (checked in the PDFs) -------------------------------------------------
t = json.dumps(b)
t = t.replace('can hide an important difference among firms,\\u201d', 'can hide an important difference among firms\\u201d (p. 1236),')
t = t.replace('can hide an important difference among firms,\\"', 'can hide an important difference among firms\\" (p. 1236),')
t = re.sub(r'(affect intended outcomes,?)(\\u201d|\\")', lambda m: m.group(1).rstrip(",") + m.group(2) + " (p. 1599),", t)
# ---- Harzing is 2013 --------------------------------------------------------------------------------
t = t.replace("Harzing, Reiche and Pudelko (2012)", "Harzing, Reiche and Pudelko (2013)").replace("Harzing et al. (2012)", "Harzing et al. (2013)")
b = json.loads(t); p["body"] = b
assert "(p. 1236)" in json.dumps(b) and "(p. 1599)" in json.dumps(b), "page numbers not placed"

# ---- C31 -----------------------------------------------------------------------------------------
append_to("Contractor, Kundu and Hsu (2003) resolved three decades",
    "")  # locate only
i = find("Contractor, Kundu and Hsu (2003) resolved three decades")
b[i] = [s.replace("reporting each segment as a finding about the whole.",
    "reporting each segment as a finding about the whole. Geleilate, Magnusson, Parente and Alvarado-Vargas (2016) "
    "carried the question into emerging markets with a meta-analysis of 170 studies and found that home-country "
    "institutions shape the relationship in contrasting ways for emerging- and developed-market multinationals: "
    "the curve is not the same curve everywhere, and a result estimated on one population of firms does not "
    "transfer to another by default.") if isinstance(s, str) else s for s in b[i]]

# ---- the stray "weakly" -------------------------------------------------------------------------------
rep("every additional country weakly worsens the design and no additional country can improve it",
    "every additional country leaves the design where it was or makes it worse, and no additional country can improve it")

# ---- C32 citations in each hypothesis ---------------------------------------------------------------
rep("The mean is nearly uninformative about the design's viability, and reporting it is reporting the wrong statistic.",
    "The mean is nearly uninformative about the design's viability, and reporting it is reporting the wrong statistic. "
    "Response-rate research in organizational studies has documented how low and how variable achieved response is, "
    "for individuals and organizations alike (Baruch & Holtom, 2008) and for senior managers in particular, whose "
    "response has declined over time (Cycyota & Harrison, 2006). Harzing, Reiche and Pudelko (2013) show that the "
    "same variation is large across national frames within a single project. What that literature reports as an "
    "average, the conjunction structure of a comparative design converts into a minimum.")
append_to("and they do not transfer without being rebuilt.",
    " Ghemawat (2001) makes the general point that cultural, administrative, geographic and economic distance each "
    "raise the cost of operating away from home, and recruitment channels are exposed to all four.")
rep("The logic is the one Lopez, Kundu and Ciravegna used on born globals, transposed.",
    "The logic is the one Lopez, Kundu and Ciravegna (2009) used on born globals, transposed. The born-global "
    "category was defined by early and wide international activity (Knight & Cavusgil, 2004); Lopez and colleagues "
    "showed that when activity was measured by where sales actually land, most such firms were regional.")
rep("The logic comes from Meyer, Li and Schotter's insistence",
    "Survey methodology has long treated data-collection mode as a determinant of both who responds and how they "
    "answer (de Leeuw, 2005), but comparative business research rarely models mode as a level in its own right. "
    "The logic here comes from Meyer, Li and Schotter's (2020) insistence")
append_to("so every element held constant for the sake of equivalence is an element that cannot be adapted for the sake of response.",
    " There is direct evidence that tolerance for standardization is itself cultural. Newburry and Yakova (2006) "
    "found that employees from cultures high in power distance and uncertainty avoidance prefer more "
    "standardization, while those from more individualist cultures prefer less. If respondents differ in the same "
    "way, a standardized instrument will be tolerated unevenly across frames, which is the mechanism this "
    "hypothesis proposes.")

# ---- C33 formal statements at the end of each hypothesis section ------------------------------------
H = [("H1. The binding-frame hypothesis", "In a comparative design that requires a minimum usable sample in every national frame, joint feasibility",
      "Hypothesis 1: In a comparative design that requires a minimum usable sample in every national frame, joint feasibility is determined by the least feasible frame rather than by the mean across frames, and adding a national frame leaves joint feasibility unchanged or lowers it."),
     ("H2. The regional bounding hypothesis", "The observable prevalence of a narrow specialist professional population",
      "Hypothesis 2: The observable prevalence of a narrow specialist professional population on a commercial research panel is higher within the panel provider's home region than outside it, controlling for the size of the national frame."),
     ("H3. The born-regional design hypothesis", "Published studies that describe themselves as cross-national achieve",
      "Hypothesis 3: Published studies that describe themselves as cross-national achieve national coverage that is more regionally concentrated than their stated design implies, and the discrepancy increases with the narrowness of the target population."),
     ("H4. The mode dominance hypothesis", "Variance in achieved response attributable to data-collection mode exceeds",
      "Hypothesis 4: Variance in achieved response attributable to data-collection mode exceeds variance attributable to country."),
     ("H5. The standardization tension hypothesis", "The degree of instrument standardization across national frames is negatively",
      "Hypothesis 5: The degree of instrument standardization across national frames is negatively associated with achieved response rate, and the association is stronger in frames with lower baseline response.")]
for title, stmt_start, formal in H:
    h = head(title)
    # section runs to the next heading
    end = next(j for j in range(h + 1, len(b)) if isinstance(b[j], dict))
    s_idx = next(j for j in range(h + 1, end) if isinstance(b[j], list) and b[j][0].startswith(stmt_start))
    b.pop(s_idx); end -= 1
    # place before any "Insert ... About Here" lines at the end of the section
    k = end
    while isinstance(b[k - 1], list) and b[k - 1][0].startswith("Insert "): k -= 1
    b[k:k] = [["Based on the above logic, we hypothesize:"], [formal]]
p["body"] = b

# ---- C40 method citations -------------------------------------------------------------------------
append_to("For H5 the standardization-by-baseline interaction is the term of interest",
    " Multilevel models are the approach recommended for international business hypotheses that span levels of "
    "analysis (Peterson, Arregle & Martin, 2012), and cross-classified random effects accommodate providers that "
    "operate in several frames at once (Raudenbush & Bryk, 2002).")

# ---- C41 discussion citations ----------------------------------------------------------------------
rep("Under H1 that number is the wrong summary statistic and a per-frame minimum should be reported alongside it.",
    "Under H1 that number is the wrong summary statistic and a per-frame minimum should be reported alongside it. "
    "Response-rate benchmarks in organizational research are averages across studies (Baruch & Holtom, 2008); for "
    "comparative designs the benchmark that matters is the weakest frame.")
rep("which is one of the routes to contribution the seminar identifies.",
    "and it applies to research practice the same measurement correction Lopez, Kundu and Ciravegna (2009) applied to the born-global category (Knight & Cavusgil, 2004).")
rep("commits the error Meyer and colleagues warn against and does so systematically.",
    "commits the error Meyer and colleagues warn against and does so systematically; it is the research-design "
    "counterpart of the ecological fallacy (Robinson, 1950), and it is the reason multilevel designs are "
    "recommended for such questions (Peterson, Arregle & Martin, 2012).")
append_to("If mode does dominate country,", "")
rep("If mode does dominate country, then a portion of the cross-national variation",
    "If mode does dominate country, consistent with what survey methodology would predict (de Leeuw, 2005), then a portion of the cross-national variation")
rep("which is a specific and testable recommendation rather than general advice to balance the two.",
    "which is a specific and testable recommendation rather than general advice to balance the two. Because tolerance for standardization varies with national culture (Newburry & Yakova, 2006), the binding frames may also be the ones least tolerant of it.")

# ---- C42 Latin America section --------------------------------------------------------------------
LA = [{"h2": "Why this matters for Latin America and the Caribbean"},
 ["Latin American and Caribbean research is where these constraints bite first. Comparative work on the region "
  "is usually multi-country by necessity, because single national samples of managers or professionals are small, "
  "and the region's economies differ widely in size. A design that pairs Brazil or Mexico with smaller economies in "
  "Central America or the Caribbean will be bound, under H1, by the smallest frame, and for a narrow specialist "
  "population that frame may hold only a handful of reachable people. The region's pooled designs are therefore "
  "more exposed to the binding-frame effect than their overall sample sizes suggest."],
 ["Language compounds the problem rather than removing it. Even in a region more homogeneous than most, instruments "
  "have to be adapted to national variations in Spanish, and to Portuguese in Brazil (Hermans et al., 2017). That is "
  "the standardization tension of H5 in its most familiar form: every adaptation made for response is a departure "
  "from equivalence, and the frames that most need adaptation are often the smallest ones."],
 ["The regional bounding argument of H2 has a specific implication here. If panel coverage is strongest in a "
  "provider's home region, Latin American frames served by providers based elsewhere will be systematically thinner "
  "for specialists, and studies of the region's firms will under-represent exactly the professionals, in finance, "
  "audit, risk and compliance, whose judgment the research is about. Research on emerging-market multinationals from "
  "the region (Cuervo-Cazurra, Newburry & Park, 2016) and on the institutional conditions that shape their "
  "performance (Geleilate et al., 2016) depends on reaching those people in more than one country at once."],
 ["The practical benefit is proportionate. Research budgets in the region are tight, and a pre-commitment test that "
  "identifies an infeasible frame before fieldwork, or that points a project toward an interview-based design when "
  "a comparative survey cannot be sustained, protects scarce funding and the goodwill of small professional "
  "communities that are surveyed often."]]
m = head("Managerial and practical contributions"); b[m:m] = LA

# ---- references ------------------------------------------------------------------------------------
r0 = head("References"); r1 = next(j for j in range(r0 + 1, len(b)) if isinstance(b[j], dict))
refs = [x[0] for x in b[r0 + 1:r1]]
refs = [r for r in refs if not r.startswith("Harzing")]
refs += [
 "Baruch, Y., & Holtom, B. C. (2008). Survey response rate levels and trends in organizational research. Human Relations, 61(8), 1139-1160.",
 "Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). Lawrence Erlbaum.",
 "Cuervo-Cazurra, A., Newburry, W., & Park, S. H. (2016). Emerging market multinationals: Managing operational challenges for sustained international growth. Cambridge University Press.",
 "Cycyota, C. S., & Harrison, D. A. (2006). What (not) to expect when surveying executives: A meta-analysis of top manager response rates and techniques over time. Organizational Research Methods, 9(2), 133-160.",
 "de Leeuw, E. D. (2005). To mix or not to mix data collection modes in surveys. Journal of Official Statistics, 21(2), 233-255.",
 "Geleilate, J.-M. G., Magnusson, P., Parente, R. C., & Alvarado-Vargas, M. J. (2016). Home country institutional effects on the multinationality-performance relationship: A comparison between emerging and developed market multinationals. Journal of International Management, 22(4), 380-402.",
 "Harzing, A.-W., Reiche, B. S., & Pudelko, M. (2013). Challenges in international survey research: A review with illustrations and suggested solutions for best practice. European Journal of International Management, 7(1), 112-134.",
 "Hermans, M., Newburry, W., Alvarado-Vargas, M. J., Baldo, C. M., Borda, A., Durán-Zurita, E. G., Geleilate, J. M. G., Guerra, M., Lasio Morello, M. V., Madero-Gómez, S. M., Olivas-Luján, M., & Zwerg-Villegas, A. M. (2017). Attitudes towards women's career advancement in Latin America: The moderating impact of perceived company international proactiveness. Journal of International Business Studies, 48(1), 90-112.",
 "Hofstede, G. (2001). Culture's consequences: Comparing values, behaviors, institutions, and organizations across nations (2nd ed.). Sage.",
 "Knight, G. A., & Cavusgil, S. T. (2004). Innovation, organizational capabilities, and the born-global firm. Journal of International Business Studies, 35(2), 124-141.",
 "Newburry, W., & Yakova, N. (2006). Standardization preferences: A function of national culture, work interdependence and local embeddedness. Journal of International Business Studies, 37(1), 44-60.",
 "Peterson, M. F., Arregle, J.-L., & Martin, X. (2012). Multilevel models in international business research. Journal of International Business Studies, 43(5), 451-457.",
 "Raudenbush, S. W., & Bryk, A. S. (2002). Hierarchical linear models: Applications and data analysis methods (2nd ed.). Sage.",
 "Robinson, W. S. (1950). Ecological correlations and the behavior of individuals. American Sociological Review, 15(3), 351-357."]
key = lambda r: re.sub(r"[^a-z]", "", r.lower().replace("de leeuw", "leeuw"))
refs = sorted(set(refs), key=key)
b[r0 + 1:r1] = [[r] for r in refs]

# ---- Table 3, H1 (reconciles Newburry's "weak frame" edit with the text) -----------------------------
p["body"] = b
p["tables"] = json.loads(json.dumps(p["tables"]).replace(
    "adding a frame weakly decreases it", "adding a frame weaker than the current minimum lowers it; adding any other frame leaves it unchanged").replace(
    "adding a frame leaves it unchanged or lowers it", "adding a frame weaker than the current minimum lowers it; adding any other frame leaves it unchanged").replace(
    "Harzing, Reiche and Pudelko (2012)", "Harzing, Reiche and Pudelko (2013)"))

# ---- checks ----------------------------------------------------------------------------------------
flat = json.dumps(p, ensure_ascii=False)
for bad in ("weakly", "(2012), Illustration", "to be confirmed", "the seminar", "by definition something", "Malik", "Florida International", "FIU", "Newburry, W. (2"):
    assert bad not in flat, bad
body_text = " ".join(s for it in b if isinstance(it, list) for s in it if isinstance(s, str))
cited = {"Baruch":"Baruch", "Cohen":"Cohen, 1988", "Cuervo":"Cuervo-Cazurra", "Cycyota":"Cycyota", "Leeuw":"de Leeuw", "Geleilate":"Geleilate",
         "Hermans":"Hermans et al.", "Hofstede":"Hofstede, 2001", "Knight":"Knight & Cavusgil", "Yakova":"Newburry and Yakova", "Peterson":"Peterson, Arregle", "Raudenbush":"Raudenbush", "Robinson":"Robinson, 1950"}
refs_start = body_text.find(refs[0][:20])
missing = [k for k, v in cited.items() if v not in body_text[:refs_start]]
assert not missing, ("reference not cited in text", missing)
json.dump(p, open(os.path.join(HERE, "aiblac_paper_v2.json"), "w"))
words = len(body_text.split()) + len(" ".join(str(x) for x in json.dumps(p["tables"]).split()).split())
print("v2 built. body words incl. references:", len(body_text.split()))

# ---- italics for the formal statements, then build the paper and the extended abstract ------------
b = p["body"]
for i, it in enumerate(b):
    if isinstance(it, list) and isinstance(it[0], str) and it[0].startswith("Hypothesis ") and it[0][11:12].isdigit():
        b[i] = ["*" + it[0] + "*"]
p["body"] = b
json.dump(p, open(os.path.join(HERE, "aiblac_paper_v2.json"), "w"))

def section(title, n=None):
    i = next(j for j, it in enumerate(b) if isinstance(it, dict) and list(it.values())[0] == title)
    end = next(j for j in range(i + 1, len(b)) if isinstance(b[j], dict))
    out = [x for x in b[i + 1:end] if isinstance(x, list) and not x[0].startswith("Insert ")]
    return out[:n] if n else out
formals = [x for x in b if isinstance(x, list) and x[0].startswith("*Hypothesis ")]
ea = copy.deepcopy(p)
ea["subtitle"] = "Extended abstract · AIB-LAC 2027, San Juan · Interactive session · Blinded for review"
ea["body"] = ([{"h2": "Abstract"}] + section("Abstract") +
    [{"h2": "The problem"}] + section("Introduction", 2) +
    [{"h2": "The model and the hypotheses"}] + section("H1. The binding-frame hypothesis", 1) + formals +
    [{"h2": "Method"}] + section("Study context", 2) +
    [{"h2": "Why this matters for Latin America and the Caribbean"}] + section("Why this matters for Latin America and the Caribbean", 1) +
    [{"h2": "Contribution"}] + section("Theoretical contributions", 1) + [{"__table__": "t3"}])
cited_in_ea = json.dumps(ea["body"])
r0 = next(j for j, it in enumerate(b) if isinstance(it, dict) and list(it.values())[0] == "References")
r1 = next(j for j in range(r0 + 1, len(b)) if isinstance(b[j], dict))
def surname(r): return r.split(",")[0].replace("de Leeuw", "de Leeuw")
ea_refs = [x for x in b[r0 + 1:r1] if surname(x[0]) in cited_in_ea or surname(x[0]) in json.dumps(ea["tables"]["t3"])]
ea["body"] += [{"h1": "References"}] + ea_refs
json.dump(ea, open(os.path.join(HERE, "aiblac_extended_abstract_v2.json"), "w"))

from build_dba_doc import build
OUT = os.environ.get("AIB_OUT", HERE)
build(p, os.path.join(OUT, "AIBLAC2027_Feasibility_as_a_Parameter_BLINDED_v2.docx"))
build(ea, os.path.join(OUT, "AIBLAC2027_Feasibility_ExtendedAbstract_BLINDED_v2.docx"))
def wc(spec):
    t = []
    def w(x):
        if isinstance(x, str): t.append(x)
        elif isinstance(x, list): [w(v) for v in x]
        elif isinstance(x, dict): [w(v) for k, v in x.items() if k not in ("image",)]
    w(spec["body"]); w(spec.get("tables", {}) if spec is p else {"t3": spec["tables"]["t3"]}); return len(" ".join(t).split())
print("paper words all-inclusive:", wc(p), "| extended abstract words all-inclusive:", wc(ea))

# ---- submission rules (lac.aib.world/submission-guidelines-2027, read 30 Sep): track at top right of
# page 1, and no author information in the file properties ------------------------------------------
from docx import Document as _D
from docx.shared import Pt as _Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH as _AL
TRACK = "Track 1: Internationalization Strategies and Process"
for name in ("AIBLAC2027_Feasibility_as_a_Parameter_BLINDED_v2.docx", "AIBLAC2027_Feasibility_ExtendedAbstract_BLINDED_v2.docx"):
    f = os.path.join(OUT, name); d = _D(f)
    par = d.paragraphs[0].insert_paragraph_before(""); r = par.add_run(TRACK); r.bold = True; r.font.size = _Pt(11); par.alignment = _AL.RIGHT
    c = d.core_properties
    for k in ("author", "last_modified_by", "comments", "keywords", "category", "subject", "identifier"): setattr(c, k, "")
    c.title = "Feasibility as a Parameter"
    d.save(f.replace("_v2.docx", "_v2_Track1.docx"))
print("track line added; author metadata cleared")
