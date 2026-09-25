# -*- coding: utf-8 -*-
"""GEB 7911 Learning Memo Week 6. Chapter 9 concepts, read against the article itself.

Every page reference was checked against the published PDF in the repo.
"""
import json

FIG = "/home/user/Profile/dba/coursework/GEB7911_Qualitative_Research_Methods/figures/memo6_rhetoric.png"

spec = {
 "title": "Learning Memo Week 6 · Writing Strategies in a Grounded Theory Article",
 "subtitle": "Gerlach & Cenfetelli (2020), Constant Checking Is Not Addiction, MIS Quarterly 44(4), 1705-1732",
 "ident": [
   "Yasir A. Malik",
   "Florida International University · College of Business",
   "Doctor of Business Administration · Cohort 8.14",
   "GEB 7911 · Qualitative Research Methods in Business · Instructor: Dr. Cristina Gonzalez",
   "September 22, 2026",
 ],
 "double_spaced": False,

 "tables": {

  "overall": [
   ["Section", "What it does", "Chapter 9 reading"],
   ["Abstract and epigraph, p. 1705",
    "States the phenomenon, names the received label, announces the replacement construct. A quotation from a news report sits above the Introduction.",
    "The opening of the overall structure is doing rhetorical work before any argument is made."],
   ["Introduction and literature, pp. 1705-1709",
    "Builds the opponent in detail, then dismantles it. Technology addiction is given its fullest statement and then shown to rest on a circular classification.",
    "An overall structure organised around a contest, not around a gap."],
   ["Research Method, pp. 1709-1710",
    "Procedure at fine grain: 90 participants, two techniques, line-by-line open coding, Atlas.ti, constant comparison, theoretical saturation.",
    "The scientific format borrowed intact. This is the part a quantitative reader recognises."],
   ["Findings, pp. 1710-1719",
    "Construct defined first, then causes, then situations, then consequences. Eight numbered propositions are distributed through it.",
    "The grounded theory variant: the theory is built in front of the reader rather than reported."],
   ["Discussion, implications, limitations, pp. 1719-1721",
    "Contributions to three literatures, then practical implications addressed to designers, businesses and users, then four limitations.",
    "The closing returns to the audience question the opening raised."],
   ["Appendices A and B, pp. 1727-1732",
    "The question set, and four tables of further participant quotes organised by theme.",
    "Evidence moved out of the argument so the argument can stay readable."],
  ],

  "embedded": [
   ["Device", "Where it appears", "What it buys the authors"],
   ["Epigraph",
    "Above the Introduction, quoting a news report on the American Psychological Association's phrase “constant checker” (Shanker 2017), p. 1705",
    "The everyday vocabulary enters the paper in someone else's voice, so the authors never have to adopt it."],
   ["Scare quotes",
    "“technology addiction,” “behavioral addictions,” the “discovery” of addiction to “Argentine tango,” p. 1707",
    "A claim is reported and withheld at the same time. The punctuation carries the disagreement."],
   ["Metatext and signposting",
    "“In what follows, we first develop and define the construct” (p. 1710); “Up to this point, we have reported … We now move to a different perspective” (p. 1716)",
    "The reader is told the shape of the argument at every seam, which is how a long inductive paper stays navigable."],
   ["Data structure diagram",
    "Table 1, first-order codes, second-order categories and themes, p. 1711",
    "A Gioia presentational device inside a Glaserian study. The reader can audit the climb from data to theme on one page."],
   ["Numbered propositions",
    "Eight of them, indented and set apart, for example Proposition 4 on reward timing, p. 1716",
    "The authority of hypothesis formatting without the claim. They are never called hypotheses, because they are outputs and not inputs."],
   ["Overview figure",
    "Figure 1, A Theory of IT-Mediated State-Tracking, p. 1720",
    "The theory becomes an object a reader can hold, and a future quantitative researcher can operationalise."],
   ["Formal definition",
    "IT-mediated state-tracking defined in the abstract and again in the findings",
    "Repetition of the exact wording is how a new construct gets installed."],
   ["Quote appendix",
    "Appendix B, four tables, pp. 1728-1732",
    "Depth of evidence demonstrated without slowing the argument, and it answers the reader who suspects cherry-picking."],
  ],

  "quotes": [
   ["Kind of quote", "Example from the article", "What it is doing"],
   ["Short, eye-catching",
    "“If you pull out your phone to check Twitter while waiting for the light to change, or read e-mails while brushing your teeth …” (Shanker 2017), p. 1705",
    "Opens the paper on recognition rather than on argument. The reader is in the phenomenon before page one ends."],
   ["Embedded in the authors' own sentence",
    "“A reason for participants' ‘constant’ performance of state-tracking behaviors …”, p. 1715; participants motivated to “stay connected to” or be “up to date on” work, p. 1708",
    "Single words lifted from data and from prior studies, carried inside the analyst's syntax. Cheap, fast, and it keeps the participant's wording visible."],
   ["Long block quotation, analysed",
    "The Outlook quote, ten lines, ending “now that [checking] was worth it!” (#26, 31f), p. 1715",
    "Given room because it carries the reward-timing mechanism. Chapter 9's warning applies and the authors observe it: a long quote is followed by analysis, never left to speak alone."],
   ["Block quotation from the literature, used against its source",
    "Turel et al.'s six criteria for technology addiction, block quoted with a page citation, p. 1707",
    "The unusual move. Block quoting is normally deference. Here the opposing position is quoted in full precisely so it can be refuted in full."],
   ["The one-line block quote",
    "“You cannot say per se ‘I only check every tenth message’” (#73, 29f), p. 1716",
    "A participant sentence set apart as a punchline. Length is doing rhetorical work: the brevity is the argument."],
   ["Tabulated quotes",
    "Appendix B, grouped under each second-order category, pp. 1728-1732",
    "Quotation as an evidentiary appendix rather than as narrative."],
  ],

  "audience": [
   ["Audience", "How the text encodes for them", "Where"],
   ["Information systems scholars",
    "Construct definition, propositions, contributions framed against named literatures, and the abbreviation IS used as an in-group shorthand.",
    "Abstract, Discussion, pp. 1719-1720"],
   ["Representation theory specialists",
    "An argument that the construct extends the theory's neglected external view.",
    "p. 1720"],
   ["Library and information science scholars",
    "The authors reach into LIS for information-seeking theory and then tell LIS that its positive view of accessibility is incomplete.",
    "pp. 1714, 1720"],
   ["Designers and platform builders",
    "“designers could provide users with opportunities to define events … combined with filter techniques and notifications.”",
    "p. 1720"],
   ["Businesses that depend on online services",
    "A short passage on what better understanding of state-tracking is worth commercially.",
    "p. 1721"],
   ["Users themselves",
    "“We recommend to mindfully customize ITs they are using and perhaps refrain from creating shortcuts or bookmarks.” Second person advice, in a research article.",
    "p. 1721"],
   ["The public conversation, and the people who write it",
    "“our study makes the case for much more careful usage of the addiction label when dealing with or talking and writing about users who use IT excessively.”",
    "p. 1721"],
  ],
 },

 "body": [

  ["The title of this article makes a negative claim. Constant checking is not addiction. A negative "
   "claim carries a burden that a positive one does not, because the authors must unseat an "
   "established reading before their own has anywhere to stand. Reading the article against "
   "Chapter 9 of Creswell and Poth, what struck me is that almost every writing decision in it is "
   "shaped by that burden. The rhetoric is not packaging around the findings. It is how the "
   "argument advances."],

  ["Page references below are to the published article, which I read in full for this memo."],

  {"h2": "1 · The overall writing structure"},

  ["The macro structure is the conventional scientific sequence, and Creswell and Poth would call "
   "this the overall rhetorical structure of the study. What is interesting is that a grounded "
   "theory paper can keep that sequence at all. Introduction, literature, method, findings, "
   "discussion, limitations. The quantitative reader is never disoriented. Inside that familiar "
   "frame, three things have been quietly swapped: the literature review argues against a "
   "construct rather than establishing one, the findings build a theory rather than test it, and "
   "hypotheses are replaced by propositions that arrive at the end rather than the beginning."],

  {"__table__": "overall"},

  ["One structural choice is worth naming on its own. The opponent is built up before it is knocked "
   "down. Technology addiction gets its fullest and fairest statement on pages 1706 and 1707, "
   "including a block quotation of its six defining criteria, before the criticism arrives. A "
   "weaker paper would have summarised the opposing view in a sentence. Giving it room is what "
   "makes the refutation land."],

  {"h2": "2 · The embedded writing structures"},

  ["Embedded structures are the smaller narrative devices working inside the overall frame. This "
   "article uses at least eight, and they are unusually easy to see because the authors are "
   "consistent."],

  {"__table__": "embedded"},

  {"image": FIG, "width_in": 5.8,
   "alt": "A four-panel diagram showing how the article's argument advances in four moves, the label, "
          "the doubt, the evidence and the replacement, with the Chapter 9 writing device that carries "
          "each move, and a band below listing three devices that run through all four: first person "
          "plural, metatext at every seam, and procedural reflexivity.",
   "caption": "Figure 1. The four rhetorical moves, and the device that carries each one."},

  {"h2": "3 · Quotes"},

  ["Chapter 9 distinguishes short eye-catching quotations, quotations embedded in the analyst's own "
   "narrative, and longer block quotations that require analysis around them. All three appear "
   "here, and the article adds two variants that the chapter does not need to anticipate."],

  {"__table__": "quotes"},

  ["The handling conventions are as revealing as the types. Every participant quotation closes with "
   "an identifier of the form (#26, 31f): a case number, an age, and a sex. Nothing else. No "
   "pseudonyms, no occupations, no vignettes. The participants are evidence rather than characters, "
   "which is a defensible choice for a study building a general construct and a costly one for any "
   "study that wanted the reader to know a person."],

  ["Inside the quotations, the authors intervene visibly. Square brackets clarify referents that the "
   "speaker left implicit, as in “I have it [smartphone] in my hand so many times a day” and "
   "“now that [checking] was worth it!” Ellipses compress. Exclamation marks and false "
   "starts are left in. The reader can see where the analyst's hand has been, which is the point."],

  ["Every long quotation is sandwiched. A lead-in sentence tells the reader what the speaker is "
   "about to demonstrate, and an interpretation follows. On page 1715, for instance: "
   "“One user was frequently state-tracking her emails at work and reflected on the ever-present "
   "possibility of an important incoming email.” The quote is then read for the reader rather "
   "than left to the reader. This is efficient and it is also a transfer of interpretive authority "
   "away from the participant, and it is worth noticing which of those two you are buying."],

  ["The most honest sentence about quotation in the whole article is in Appendix B, where the "
   "authors write that the tables present “snippets of participants' statements outside of the "
   "statements' context,” and that information not shown may have informed the coding. That is "
   "a limitation of quotation as evidence, stated by the people it disadvantages."],

  {"h2": "4 · Audience"},

  ["Chapter 9 treats audience as something the writing encodes rather than something the writer "
   "merely has in mind. By that test this article is written for at least seven audiences, and it "
   "signals each one differently."],

  {"__table__": "audience"},

  ["The seventh is the one I did not expect. The paper is partly addressed to the discourse itself, "
   "to journalists, clinicians and commentators who use the word addiction loosely. The authors "
   "argue that “calling someone an addict has significant and potentially dangerous consequences "
   "for the individual and the treatment of the associated behaviors” (p. 1721). That is a "
   "qualitative study making a claim about vocabulary as an intervention, which is only possible "
   "because the study went after a label rather than a variable."],

  {"h2": "5 · Reflexivity"},

  ["This is where the article is most interesting and most limited at once. Creswell and Poth treat "
   "reflexivity as the researcher's presence in the text: who they are, what they bring, and how "
   "that shapes interpretation. Gerlach and Cenfetelli position themselves thoroughly, but almost "
   "entirely as procedure rather than as persons."],

  ["What they do disclose is substantial. They state that grounded theory “requires researchers to "
   "manage preconceptions” and that they “began our study with an open mind, without seeking "
   "any preconceived relationships in the data” (p. 1709). They admit that most participants came "
   "“through our personal and professional networks,” and then treat that admission as a design "
   "problem rather than a confession: 24 further respondents were recruited through Mechanical Turk "
   "specifically “to see whether a non-convenience sample would generate different insights” "
   "(p. 1709). They ran anonymous surveys alongside interviews to test for interview bias, and "
   "report the comparison (p. 1709). In the limitations they even offer a judgement in their own "
   "voice: they “felt that our participants were generally very self-critical” (p. 1721)."],

  ["What is absent is any account of who these two researchers are. There is no positionality "
   "statement, no axiology, no disclosure of the authors' own relationship to constant checking, "
   "and no reflection on the fact that two information systems academics studying device use are "
   "themselves heavy device users. The first person plural runs through the entire article, so the "
   "authors are visible as actors at every step, and invisible as people throughout."],

  ["I do not think this is an oversight. It reads as a disciplinary norm: MIS Quarterly rewards "
   "procedural transparency and does not ask for biography. But our 18 September session made the "
   "opposite point about axiology, that disclosing the researcher's values and background is part "
   "of what makes an inductive claim auditable. Both cannot be fully right, and the gap between "
   "them is a real choice a doctoral student has to make rather than a box to tick."],

  ["There is one moment where the absence shows. The authors write that they began “with an open "
   "mind, without seeking any preconceived relationships.” Chapter 9 would ask how a reader is "
   "supposed to assess that. Managing preconceptions is demonstrated by naming them and then "
   "showing what was done about them. Asserting an open mind is the one reflexive claim in the "
   "article that the article gives the reader no way to check."],

  {"h2": "What I am taking into my own proposal"},

  ["First, build the opponent before knocking it down. My own study has a received reading to "
   "displace, and this article is a model for giving that reading its full strength first."],

  ["Second, choose the quote convention deliberately rather than by default. (#26, 31f) suits a "
   "study building a general construct. A phenomenological study asking about lived experience "
   "needs the reader to know a person, so the identifier and the quote length both have to change."],

  ["Third, write the positionality statement this article does not have. Not because the article is "
   "wrong for its journal, but because my method and my topic both make my own relationship to the "
   "phenomenon part of the evidence rather than a distraction from it."],

  {"h2": "References"},

  ["Creswell, J. W., & Poth, C. N. (2024). Qualitative inquiry and research design: Choosing among "
   "five approaches (5th ed.). SAGE Publications. Chapter 9."],

  ["Gerlach, J. P., & Cenfetelli, R. T. (2020). Constant checking is not addiction: A grounded "
   "theory of IT-mediated state-tracking. MIS Quarterly, 44(4), 1705-1732."],

  {"h2": "Disclosure of Artificial Intelligence Use"},

  ["Generative artificial intelligence (Claude, Anthropic) was used to organise this memo, to build "
   "the figure, to format the tables, and to check the prose for clarity and grammar. The selection "
   "of passages from the article, the application of the Chapter 9 concepts, the reading of the "
   "article's reflexivity as procedural rather than personal, and the conclusions drawn for my own "
   "proposal are my own. No confidential, identifiable, or restricted data was provided to any "
   "artificial intelligence system. This disclosure is made in accordance with the FIU University "
   "Graduate School policy on artificial intelligence use and the course syllabus."],
 ],
}

json.dump(spec, open('memo6.json','w'))
print("spec written")
