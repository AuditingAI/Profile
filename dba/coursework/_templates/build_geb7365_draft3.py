#!/usr/bin/env python3
"""GEB 7365 final paper, Draft 3: Newburry's 28 September comments carried into the course copy.

Input: geb7365_report_draft2.json (from build_geb7365_draft2.py). Applies the same content edits as
build_aiblac_v2.py (his tracked changes, his ten comments, verified citations, the Latin America
section, Harzing 2013), but not blinded: author, course and the FIU AI-use disclosure stay, and the
Preliminary Evidence section from Draft 2 stays. Anchors that do not exist in the course copy are
reported rather than failing, so the log shows exactly what landed.
"""
import json, copy, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
p = json.load(open(os.path.join(HERE, "geb7365_report_draft2.json"))); b = p["body"]
log = []
def idx(sub):
    return [i for i, it in enumerate(b) if isinstance(it, list) and any(isinstance(s, str) and sub in s for s in it)]
def rep(old, new, tag):
    hits = idx(old)
    if len(hits) != 1: log.append(f"SKIP {tag} ({len(hits)} hits)"); return
    i = hits[0]; b[i] = [s.replace(old, new) if isinstance(s, str) else s for s in b[i]]; log.append(f"ok   {tag}")
def app(anchor, extra, tag): rep(anchor, anchor + extra, tag)
def head(title): return next(j for j, it in enumerate(b) if isinstance(it, dict) and list(it.values())[0] == title)

p["title"] = p["title"].replace("When Comparative Research", "When Comparative International Research")
rep("with an instrument that means the same thing in each place.",
    "with an instrument that means the same thing in each place. Even in a region such as Latin America, which is more homogeneous than most, researchers must take efforts to adapt their research instruments to differences in language, culture and other variables. For example, Hermans et al. (2017) needed to adapt their survey instrument to variations in Spanish across the region.", "WN intro Latin America")
rep("this requirement is demanding but routine.", "this requirement is demanding but routine, as in the Latin America example above.", "WN 'as in the example'")
rep("a limitation is confessed after the study has failed", "a limitation is often confessed after the study has failed", "WN 'often'")
app("The Korean telephone datum is precisely such a case.", " In a sense, this is parallel to the ecological fallacy, which is a significant issue in cultural and other research, and refers to 'applying aggregate-level reasoning at the individual level' (Hofstede, 2001: 16; Robinson, 1950).", "WN ecological fallacy")
rep("That distinction is invisible to a literature that reports sampling as a limitation, because a limitation is by definition something discovered afterward.",
    "That distinction is easy to miss in a literature that reports sampling as a limitation rather than modelling it as a constraint on the design.", "C19")
rep("A parameter is estimated before a study is designed and it constrains the design;",
    "A parameter is estimated before a study is designed and it constrains the design, in the way an a priori power analysis fixes the sample a design needs before any data are collected (Cohen, 1988);", "C20")
t = json.dumps(b)
n0 = t.count("(p. 1236)") + t.count("(p. 1599)")
t = t.replace('can hide an important difference among firms,\\u201d', 'can hide an important difference among firms\\u201d (p. 1236),').replace('can hide an important difference among firms,\\"', 'can hide an important difference among firms\\" (p. 1236),')
t = re.sub(r'(affect intended outcomes,?)(\\u201d|\\")', lambda m: m.group(1).rstrip(",") + m.group(2) + " (p. 1599),", t)
t = t.replace("Harzing, Reiche and Pudelko (2012)", "Harzing, Reiche and Pudelko (2013)").replace("Harzing et al. (2012)", "Harzing et al. (2013)")
b = json.loads(t); p["body"] = b
log.append(f"{'ok  ' if json.dumps(b).count('(p. 1236)') and json.dumps(b).count('(p. 1599)') else 'SKIP'} C22/C30 page numbers")
rep("reporting each segment as a finding about the whole.",
    "reporting each segment as a finding about the whole. Geleilate, Magnusson, Parente and Alvarado-Vargas (2016) carried the question into emerging markets with a meta-analysis of 170 studies and found that home-country institutions shape the relationship in contrasting ways for emerging- and developed-market multinationals: the curve is not the same curve everywhere, and a result estimated on one population of firms does not transfer to another by default.", "C31 Geleilate")
rep("The mean is nearly uninformative about the design's viability, and reporting it is reporting the wrong statistic.",
    "The mean is nearly uninformative about the design's viability, and reporting it is reporting the wrong statistic. Response-rate research in organizational studies has documented how low and how variable achieved response is, for individuals and organizations alike (Baruch & Holtom, 2008) and for senior managers in particular, whose response has declined over time (Cycyota & Harrison, 2006). Harzing, Reiche and Pudelko (2013) show that the same variation is large across national frames within a single project. What that literature reports as an average, the conjunction structure of a comparative design converts into a minimum.", "C32 H1")
app("and they do not transfer without being rebuilt.", " Ghemawat (2001) makes the general point that cultural, administrative, geographic and economic distance each raise the cost of operating away from home, and recruitment channels are exposed to all four.", "C32 H2")
rep("The logic is the one Lopez, Kundu and Ciravegna used on born globals, transposed.",
    "The logic is the one Lopez, Kundu and Ciravegna (2009) used on born globals, transposed. The born-global category was defined by early and wide international activity (Knight & Cavusgil, 2004); Lopez and colleagues showed that when activity was measured by where sales actually land, most such firms were regional.", "C32 H3")
rep("The logic comes from Meyer, Li and Schotter's insistence",
    "Survey methodology has long treated data-collection mode as a determinant of both who responds and how they answer (de Leeuw, 2005), but comparative business research rarely models mode as a level in its own right. The logic here comes from Meyer, Li and Schotter's (2020) insistence", "C32 H4")
app("so every element held constant for the sake of equivalence is an element that cannot be adapted for the sake of response.",
    " There is direct evidence that tolerance for standardization is itself cultural. Newburry and Yakova (2006) found that employees from cultures high in power distance and uncertainty avoidance prefer more standardization, while those from more individualist cultures prefer less. If respondents differ in the same way, a standardized instrument will be tolerated unevenly across frames, which is the mechanism this hypothesis proposes.", "C32 H5")

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
for title, start, formal in H:
    h = head(title); end = next(j for j in range(h + 1, len(b)) if isinstance(b[j], dict))
    s_idx = next((j for j in range(h + 1, end) if isinstance(b[j], list) and b[j][0].startswith(start)), None)
    if s_idx is None: log.append(f"SKIP C33 {title}"); continue
    b.pop(s_idx); end -= 1; k = end
    while isinstance(b[k - 1], list) and b[k - 1][0].startswith("Insert "): k -= 1
    b[k:k] = [["Based on the above logic, we hypothesize:"], ["*" + formal + "*"]]; log.append(f"ok   C33 {title[:2]}")
p["body"] = b
app(" and the hypothesis is supported only if the interaction is significant in the predicted direction, not merely the main effect.",
    " Multilevel models are the approach recommended for international business hypotheses that span levels of analysis (Peterson, Arregle & Martin, 2012), and cross-classified random effects accommodate providers that operate in several frames at once (Raudenbush & Bryk, 2002).", "C40")
rep("Under H1 that number is the wrong summary statistic and a per-frame minimum should be reported alongside it.",
    "Under H1 that number is the wrong summary statistic and a per-frame minimum should be reported alongside it. Response-rate benchmarks in organizational research are averages across studies (Baruch & Holtom, 2008); for comparative designs the benchmark that matters is the weakest frame.", "C41 H1")
rep("which is one of the routes to contribution the seminar identifies.",
    "and it applies to research practice the same measurement correction Lopez, Kundu and Ciravegna (2009) applied to the born-global category (Knight & Cavusgil, 2004).", "C41 regionalization")
rep("commits the error Meyer and colleagues warn against and does so systematically.",
    "commits the error Meyer and colleagues warn against and does so systematically; it is the research-design counterpart of the ecological fallacy (Robinson, 1950), and it is the reason multilevel designs are recommended for such questions (Peterson, Arregle & Martin, 2012).", "C41 levels")
rep("If mode does dominate country, then a portion of the cross-national variation",
    "If mode does dominate country, consistent with what survey methodology would predict (de Leeuw, 2005), then a portion of the cross-national variation", "C41 H4")
rep("which is a specific and testable recommendation rather than general advice to balance the two.",
    "which is a specific and testable recommendation rather than general advice to balance the two. Because tolerance for standardization varies with national culture (Newburry & Yakova, 2006), the binding frames may also be the ones least tolerant of it.", "C41 H5")

from build_aiblac_v2_la import LA   # the Latin America section, shared with the AIB build
m = head("Managerial and practical contributions"); b[m:m] = copy.deepcopy(LA); log.append("ok   C42 Latin America section")

from build_aiblac_v2_la import NEW_REFS
r0 = head("References"); r1 = next(j for j in range(r0 + 1, len(b)) if isinstance(b[j], dict))
refs = [x[0] for x in b[r0 + 1:r1] if not x[0].startswith("Harzing")] + NEW_REFS
refs = sorted(set(refs), key=lambda r: re.sub(r"[^a-z]", "", r.lower().replace("de leeuw", "leeuw")))
b[r0 + 1:r1] = [[r] for r in refs]

d = idx("Generative artificial intelligence (Claude, Anthropic) was used")
if d:
    b[d[0]] = [b[d[0]][0].replace("No confidential, identifiable,",
      "In the revision that followed the instructor's written comments of 28 September 2026, it was also used to organise the response to each comment and to locate candidate sources; every citation added in that revision was checked against a publisher or index record before inclusion. Passages added in that revision, notably the section on Latin America and the literature added to each hypothesis, were first drafted with AI assistance and then revised by the author. No confidential, identifiable,")]
    log.append("ok   AI disclosure extended")
p["body"] = b
p["tables"] = json.loads(json.dumps(p["tables"]).replace("adding a frame leaves it unchanged or lowers it",
    "adding a frame weaker than the current minimum lowers it; adding any other frame leaves it unchanged").replace("Harzing, Reiche and Pudelko (2012)", "Harzing, Reiche and Pudelko (2013)"))
p["subtitle"] = "Formal Project Report · Draft 3"
p["ident"] = [s if not s.startswith("Draft 2") else "Draft 3 · 29 September 2026 · revised after the instructor's comments of 28 September · Report due 9 October 2026" for s in p["ident"]]

flat = json.dumps(p, ensure_ascii=False)
for bad in ("weakly", "to be confirmed", "the seminar", "by definition something", "(2012)"):
    if bad in flat: log.append(f"WARN still contains: {bad}")
json.dump(p, open(os.path.join(HERE, "geb7365_report_draft3.json"), "w"))
from build_dba_doc import build
out = os.path.join(HERE, "..", "GEB7365_International_Business", "Malik_GEB7365_ProjectReport_DRAFT3.docx")
build(p, out)
print("\n".join(log))
