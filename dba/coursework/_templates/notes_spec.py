# -*- coding: utf-8 -*-
"""Talking notes, 19 September. Short lines, plain words, one block per slide."""
import json, re
B=lambda t:{"t":t,"b":True}

spec = {
 "title": "Talking Notes",
 "subtitle": "GEB 7365 Project Presentation · 16 slides · 12 minutes of talking",
 "ident": [
   "Yasir A. Malik · DBA Cohort 8.14",
   "Prof. William Newburry · 19 September 2026",
 ],
 "double_spaced": False,
 "body": [

  {"h1": "Before you start"},
  ["Say the roadmap out loud. It takes fifteen seconds and it scores the "
   "well-organised box before you have said anything else."],
  [B("“Five elements. The topic and my contribution. The model. Five hypotheses and why each one "
     "follows. How I would study it. And what evidence I already have, which is my own failed study.”")],
  ["Then breathe. You know this better than anyone in the room."],

  {"h1": "Slide 1 and 2 · Open"},
  ["Forty five seconds."],
  ["To compare anything across countries you have to reach the same people in every country, at the "
   "same time, with an instrument that means the same thing everywhere."],
  ["For ordinary people that is hard but normal. For a rare profession it is something else."],
  [B("That something else is the whole project.")],

  {"h1": "Slide 3 · The contribution"},
  ["Seventy seconds. Walk the five boxes. Land on the last one."],
  [B("“I want to move sampling feasibility from being a limitation to being a parameter.”")],
  ["A parameter is worked out before you design, and it limits what you can design."],
  ["A limitation is what you confess afterwards."],

  {"h1": "Slide 4 · The model"},
  ["A minute."],
  ["Reachable sample is four things multiplied together, not added."],
  ["Frame size. Prevalence. Response rate. Screen survival."],
  ["Each one is decided at a different level. That matters because when a country fails, people "
   "blame the country. Usually the country is not what failed."],

  {"h1": "Slide 5 · The big chart"},
  ["Seventy seconds. This is your best slide. Slow down."],
  ["Add four countries and the panel you need in every single country goes from nineteen million to "
   "seventy two million."],
  ["The average response rate barely moves. Fifteen percent down to nine."],
  [B("“The average is almost useless. The worst country decides everything.”")],
  [B("↓ ASK THE ROOM HERE ↓")],
  ["“How many of you have read a comparative paper that reported one overall response rate? "
   "That is the number I am saying is wrong.”"],
  ["That question is a scored box. You cannot get it any other way."],

  {"h1": "Slide 6 · Five hypotheses"},
  ["A minute. Read H1 and H2 properly. Say the other three in a few words each."],
  ["Do not read the whole slide. They can read. Reading it is how you lose the room."],

  {"h1": "Slide 7 · Why H1 works"},
  ["Just under a minute."],
  ["Saying a relationship differs between Spain and China means claiming something about both. If "
   "either one fails, the claim fails."],
  ["An average cannot do that job."],
  [B("So every country you add makes the study more fragile, not more ambitious.")],

  {"h1": "Slide 8 · H2, the one to be ready for"},
  ["Seventy seconds. This is where a question is most likely."],
  ["Rugman and Verbeke found 320 of 380 big multinationals sell mostly in their home region. Eighty "
   "percent of sales."],
  ["Their reason is specific. Technology travels. Branding does not."],
  ["A research panel is nothing but branding. Its members, and its standing with them. The software "
   "is a commodity."],
  [B("“So by their own logic, a panel should be MORE home region bound than a factory. Nobody has "
     "checked.”")],

  {"h1": "Slide 9 · H4 and H5"},
  ["Fifty seconds. Quick."],
  ["How you ask may matter more than where you ask."],
  ["Harzing got forty seven percent in Korea, by telephone. That beats the entire country spread by "
   "five times."],
  ["One number is not evidence. That is why it is a hypothesis and not a finding."],

  {"h1": "Slide 10 · Where the data comes from"},
  ["Just under a minute."],
  ["Panel companies show you an estimated reachable count before you pay anything. Free."],
  [B("That is the whole trick. It is why feasibility can be a parameter instead of an excuse.")],
  ["One occupation, one provider, one country. About a hundred and forty four of those."],

  {"h1": "Slide 11 · What gets measured"},
  ["Just under a minute. They score this separately, so be precise and do not rush."],
  ["Dependent variable is reachable usable sample."],
  ["Each independent variable belongs to one hypothesis."],
  ["Controls include eligibility strictness, which is just how many screening criteria you stack up. "
   "That is the only term the researcher actually controls."],

  {"h1": "Slide 12 · The analysis"},
  ["A minute. Also scored separately. Be exact."],
  ["Two kinds of claim, two treatments."],
  ["H1 is logical, so it gets demonstration and sensitivity testing. A p-value would not make it "
   "more true."],
  ["H2 to H5 get hierarchical models. Cells inside countries, countries inside regions."],
  ["For H5 it is the interaction that matters, not the main effect."],

  {"h1": "Slide 13 · Timeline"},
  ["Forty five seconds."],
  ["Nine months."],
  [B("“The thing that killed my last study was recruitment. This design has no recruitment step "
     "at all.”")],

  {"h1": "Slide 14 · Your evidence"},
  ["Seventy seconds. The most memorable thing you will say. Pause after the big number."],
  ["“My evidence is my own failed study.”"],
  [B("“A panel of 334,976 people.”"), "  ... pause two seconds ..."],
  ["“About twenty were eligible. Four were usable.”"],
  ["Then say what it does not do:"],
  ["It supports H1 directly. It says nothing about H2, because I had one provider in one region. It "
   "barely touches H4, because I used one instrument."],
  [B("Saying what your evidence cannot do is the most credible thing in the talk. Do not skip it.")],

  {"h1": "Slide 15 · Limits"},
  ["Forty seconds. Read them briskly. Do not apologise for them."],

  {"h1": "Slide 16 · Close"},
  ["Thirty five seconds."],
  [B("“A parameter is worked out before a design. A limitation is confessed after it fails.”")],
  ["“These numbers are all visible before you field anything. Making them part of the design "
   "instead of part of the confession is a small change in practice and a big change in what we can "
   "claim to have compared.”"],

  {"h1": "If you run out of time"},
  ["Cut slide 9 and slide 15. You can answer H4 and H5 if asked, and the limits fit in one sentence "
   "at the close."],

  {"h1": "Three questions you will probably get"},

  {"h2": "“Isn't this just a methods paper?”"},
  ["“The dependent variable is cross national. Which countries can be reached, and why coverage "
   "differs. H2 is what makes it international business, because it applies the regional thesis to a "
   "new kind of firm.”"],

  {"h2": "“Your prevalence comes from one study in one country.”"},
  ["“Agreed. There is no cross national prevalence data, which is exactly why getting it is the "
   "contribution rather than an assumption. Held constant, the model isolates the response rate "
   "effect. The figures show a structure. They do not estimate a quantity.”"],

  {"h2": "“What if the big panels have all gone global?”"},
  ["“Then H2 fails, and that is worth publishing, because it shows where the regional argument "
   "stops applying.”"],

  {"h1": "Last thing"},
  ["Do not read the slides. Look at faces. Stand where they can see you."],
  [B("You have done the work. Go and say it.")],
 ],
}

def md(n):
    if isinstance(n,str):
        if "**" not in n: return n
        parts=re.split(r"\*\*(.+?)\*\*",n); out=[]
        for i,sg in enumerate(parts):
            if sg: out.append({"t":sg,"b":True} if i%2 else sg)
        return out
    if isinstance(n,list):
        flat=[]
        for x in n:
            r=md(x)
            flat.extend(r) if isinstance(r,list) and isinstance(x,str) else flat.append(r)
        return flat
    return n
spec["body"]=[md(i) for i in spec["body"]]
json.dump(spec, open('notes.json','w')); print("spec written")
