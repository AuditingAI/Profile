#!/usr/bin/env python3
"""GEB 7911 final qualitative research proposal, WORKING version (due 6 Oct 2026).

Hybrid build agreed 3 Oct 2026, because the course caps AI-created content at
25% and requires it to be labelled:

  * Methodology (sections 4.1, 4.3 to 4.7) and the Proposed Timeline are drafted
    from the protocol files in dba/QUALITATIVE and Dr. Gonzalez's 1 Oct feedback.
    They are labelled AI-assisted and Yasir revises them.
  * Introduction is his Memo 4 text, carried verbatim, with each revision both
    reviewers asked for flagged in yellow at the sentence it applies to.
  * Literature Review, Role of the Researcher and Expected Contributions are
    outlines and source lists only. He writes the prose.

Yellow text is a note to Yasir and is deleted before submission.

    python3 build_geb7911_proposal.py
"""
import os, subprocess, sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_dba_doc import build

OUT_DIR = os.path.join(HERE, "..", "GEB7911_Qualitative_Research_Methods")
OUT = os.path.join(OUT_DIR, "Malik_GEB7911_Proposal_WORKING.docx")


def note(text):
    """A yellow instruction to Yasir. Deleted before submission."""
    return [{"t": "[NOTE: " + text + "]", "hl": True, "b": True}]


def ai_label(text):
    return [{"t": text, "i": True}]


H1 = lambda t: {"h1": t}
H2 = lambda t: {"h2": t}
H3 = lambda t: {"h3": t}
B = lambda t: {"bullet": t}
PB = {"pagebreak": True}

TITLE = ("When the Machine Agrees: A Phenomenological Study of How Experienced "
         "Auditors Experience AI-Generated Confirmation of Judgments Already Formed")

body = []

# ---------------------------------------------------------------- title page
body += [
    note("WORKING VERSION. Yellow text is a note to you; delete every yellow line "
         "before you submit. The title is a working title: change it if it does "
         "not sound like you."),
    "Yasir A. Malik",
    "DBA Cohort 8.14",
    "Florida International University, College of Business",
    "GEB 7911 Qualitative Research Methods in Business, Dr. Cristina Gonzalez",
    "October 6, 2026",
    PB,
]

# ---------------------------------------------------------------- 1 introduction
body += [
    H1("Introduction"),
    note("This section is YOUR Memo 4 text, carried over word for word. Each yellow "
         "flag sits under the sentence it applies to and says what Dr. Gonzalez "
         "(14 Sep) or Lakwantiera Braddy (13 Sep) asked for. Make the change in your "
         "own words. Target 3 to 4 double-spaced pages. The guidance asks this "
         "section to carry: a narrative hook, a short literature summary, the gap, "
         "the audiences, the purpose (script form), the RQ, the interpretive "
         "framework with four assumptions, and terminology."),
    H2("Focus and Research Problem"),
    "An auditor reviewing a multi-year engagement has always had a starting point: "
    "last year's conclusion. What has changed is that AI systems now introduce new "
    "risks into that process, including sycophancy and epistemic drift. These risks "
    "don't show up as one-time errors. They show up as a pattern that repeats every "
    "time the system is used.",
    note("Both praised this opening; keep it. Two small fixes: cite sycophancy here "
         "(Sharma et al., 2024) and either define 'epistemic drift' in Key "
         "Terminology or cut it. Write 'do not' rather than 'don't' in a formal paper."),
    "Professional standards assume a competent human reviewer sits above the AI "
    "system. Nobody has actually measured whether that reviewer's judgment survives "
    "contact with it. That matters because the auditors relying on those standards "
    "are the last check before a misjudgment reaches a client, a regulator, or a "
    "public filing.",
    note("SOFTEN (both reviewers, independently). 'Nobody has actually measured' is "
         "a categorical claim. Restate it as what the literature has mostly focused "
         "on. Cite the standard you mean (PCAOB, 2024, on supervising generative AI "
         "output; NIST AI 600-1 calls this 'human-AI configuration')."),
    "The empirical literature on AI and auditor judgment is thin, and what exists "
    "asks the wrong kind of question. Most work asks how much auditors rely on "
    "AI-generated output. That is a magnitude question, and a survey can answer it. "
    "It does not ask how auditors experience receiving that output, or how they make "
    "sense of it in the moment. That is a process question, and a survey cannot "
    "answer it. My own prior study tried to measure this by self-report and ran into "
    "the same limit every self-report measure of this kind runs into: it asks a "
    "person to notice the one thing the bias in question prevents them from "
    "noticing. The anchoring-and-adjustment literature originating with Tversky and "
    "Kahneman (1974) establishes that judgments formed from a starting point adjust "
    "insufficiently away from it, and that the effect persists even when "
    "participants are motivated toward accuracy. What that literature has not "
    "examined is what happens when the starting point is produced by a machine that "
    "also agrees with the conclusion the professional had already reached.",
    note("THREE FIXES. (1) 'asks the wrong kind of question' is the sentence both "
         "reviewers objected to. Suggested direction: the literature has focused "
         "primarily on the extent of reliance rather than the lived experience of "
         "receiving AI-generated confirmation. (2) 'That is a process question' must "
         "go: process is grounded theory. Yours is a question about experience and "
         "meaning, which is phenomenology (Gonzalez 14 Sep; class 22 Sep). (3) This "
         "paragraph is the literature summary the guidance asks for and it has one "
         "citation. Add 4 to 6 from the Literature Review list: Joyce and Biddle "
         "(1981) and Kinney and Uecker (1982) for anchoring in audit; Parasuraman "
         "and Manzey (2010) for automation bias; Commerford et al. (2022) and Koreff "
         "(2022) for what has been measured about auditor reliance on AI."),
    "This matters to two audiences. For research, it separates two things the "
    "literature currently conflates: automation bias, which is a human tendency, and "
    "sycophancy, which is a property of the system. Asking how much someone relied "
    "on a machine cannot tell those two apart. For practice, audit firms and "
    "regulators are writing AI-use policies right now on the assumption that human "
    "review is a working control. Nobody has asked the people doing that reviewing "
    "what the experience of it actually is.",
    note("Gonzalez named the automation bias versus sycophancy distinction as a "
         "strength; keep it. SOFTEN 'Nobody has asked' (same issue as above). "
         "'Conflates' also needs one citation, or soften it to 'often treats "
         "together'. Cite one policy document for 'writing AI-use policies' (PCAOB, "
         "2024 or IAASB, 2024)."),
    H2("Purpose Statement"),
    "The purpose of this phenomenological study is to understand the experience of "
    "receiving an AI-generated conclusion that confirms a judgment already formed, "
    "for experienced internal auditors, at organizations where AI-supported "
    "analytical tools are used in live engagement work. At this stage in the "
    "research, receiving AI-generated confirmation will be generally defined as the "
    "moment an AI system produces an analytical output matching a conclusion the "
    "auditor had already reached independently.",
    note("DECIDE ONE THING. This says 'internal auditors'. Your sampling plan and "
         "poster recruit across internal audit, external audit and risk assurance "
         "for maximum variation, and the RQ says 'experienced auditors'. Either drop "
         "'internal' here (recommended, it matches the RQ and the poster) or narrow "
         "the sampling. The Methodology draft assumes you drop it."),
    "Participants will be experienced internal auditors with eight or more years of "
    "practice, recurring multi-year engagement responsibility, and meaningful, "
    "direct exposure to AI-generated analytical output in the course of that work. "
    "Consistent with a phenomenological design, the site is defined by the shared "
    "professional context in which the phenomenon occurs rather than by a single "
    "named organization.",
    note("UPDATE. 'eight or more years' is now FIVE or more. Add the criterion "
         "Gonzalez asked for on 14 Sep: each participant must be able to recall a "
         "specific occasion when an AI tool reached a conclusion they had already "
         "reached. Recall is enough; they do not need to have interpreted it (her "
         "1 Oct feedback)."),
    H2("Research Question"),
    "How do experienced auditors experience and make sense of receiving an "
    "AI-generated conclusion that confirms a judgment they had already formed?",
    note("Braddy asked whether 'and make sense of' adds a second phenomenon. He did "
         "not insist. Add one sentence in your words saying why it stays: in "
         "phenomenology the meaning a person makes of an experience is part of the "
         "experience itself, not a separate process. Do not call it a process."),
    H2("Interpretive Framework and Assumptions"),
    "This study is approached from a social constructivist, inductive interpretive "
    "framework.",
    "**Ontological assumptions.** Multiple realities exist. There is no single "
    "correct account of what it is like to receive machine-generated confirmation "
    "waiting to be recovered. There are as many accounts as there are auditors who "
    "have experienced it, and the variation among them is part of the finding rather "
    "than error to be averaged away.",
    "**Epistemological assumptions.** Evidence consists of participants' own "
    "first-person descriptions of the experience, gathered through semi-structured, "
    "audio-recorded interviews. Closeness to participants is treated as a condition "
    "of knowing rather than a threat to it. The account is the data, not a proxy for "
    "something more objective sitting behind it.",
    "**Axiological assumptions.** My own values are present in this study and are "
    "stated rather than bracketed away.",
    "I am not an outsider to this setting. Fifteen years in audit and risk at "
    "Citigroup and JPMorgan Chase, and prior experience as a bank examiner for the "
    "Florida Office of Financial Regulation, give me direct familiarity with the "
    "vocabulary, pressures, and judgment calls this study asks participants to "
    "describe. That same background is also a risk: I already believe the "
    "phenomenon under study is real, which makes me more likely to hear confirmation "
    "in what a participant says than a genuinely neutral listener would. To guard "
    "against that, every occasion on which I notice myself feeling confirmed by a "
    "participant's account is logged in a confirmation hazard log kept for the "
    "duration of the study.",
    note("Both reviewers praised this paragraph; keep it. One change: remove "
         "'Fifteen years' (your no-career-length rule). For example, start with "
         "'My career in audit and risk at Citigroup and JPMorgan Chase...'. Add one "
         "clause that the hazard log records what you did about each entry, not only "
         "that you felt confirmed (Gonzalez, 1 Oct)."),
    "**Methodological assumptions.** Of the five qualitative approaches, this study "
    "uses phenomenology. The research question asks what an experience is like and "
    "how it is made sense of, which is the question phenomenology is built to "
    "answer. A grounded theory design would commit the study to generating theory "
    "it is not yet positioned to generate, and a case study design would require a "
    "bounded site this study does not have.",
    H2("Key Terminology"),
    note("These six definitions came from Memo 4, where your disclosure says AI "
         "drafted them. Reword each in your own words and add one citation per term "
         "(anchoring: Tversky & Kahneman, 1974; automation bias: Parasuraman & "
         "Manzey, 2010; sycophancy: Sharma et al., 2024; professional judgment: "
         "Bonner, 2008). Add 'epistemic drift' if you keep it in the opening. Doing "
         "this also brings the paper's AI share down."),
    {"__table__": "terms"},
    note("Memo 4 Section 6 (the larger programme) goes here, CONDENSED to two or "
         "three sentences (Braddy asked for this): the survey could not be fielded "
         "because the eligible population is about six per hundred thousand panel "
         "members; that same population can support 10 to 15 interviews. Replace "
         "the auditingai.github.io link, which is not live, with "
         "github.com/AuditingAI/Profile. DROP Memo 4 Section 7 (peer review "
         "questions); its answers now live in the Methodology below."),
    PB,
]

# ---------------------------------------------------------------- 2 literature
body += [
    H1("Literature Review"),
    note("YOU WRITE THIS SECTION. 3 to 4 double-spaced pages. Below is an outline "
         "and a source list only. Every source here already appears in the "
         "reference list of your research paper, so the citations are checked; you "
         "still need to read the ones you lean on before citing them. The example "
         "paper's pattern works well: for each theme, say what the literature "
         "shows, its strength, its weakness, and what that leaves open for this "
         "study. Close with a paragraph that states the gap in the softened form."),
    H3("2.1 Anchoring on a prior conclusion in audit judgment"),
    B("The question to answer: what do we already know about auditors carrying a "
      "starting point forward?"),
    B("Tversky & Kahneman (1974); Joyce & Biddle (1981); Kinney & Uecker (1982); "
      "Henrizi, Himmelsbach & Hunziker (2021); Furnham & Boo (2011)"),
    B("Mechanism worth naming: selective accessibility, where people test the "
      "anchor by looking for evidence that fits it (Strack & Mussweiler, 1997; "
      "Mussweiler & Strack, 1999). This is the closest thing in the literature to "
      "your 'confirmation' moment."),
    B("Weakness to point out: almost all of it is experimental, and the anchor is a "
      "number or a prior-year figure, never a machine conclusion."),
    H3("2.2 Automation bias: the human side"),
    B("Parasuraman & Manzey (2010) for complacency and automation bias; Dowling & "
      "Leech (2007) for audit decision aids."),
    B("What it leaves open: the work studies whether people miss automation errors, "
      "not what it is like when the automation agrees with them and is right."),
    H3("2.3 What has been measured about auditors and AI"),
    B("Commerford, Dennis, Joe & Ulla (2022): auditors discount AI evidence that "
      "CONTRADICTS management relative to the same evidence from a human specialist. "
      "Useful contrast: they studied disagreement; you study agreement."),
    B("Koreff (2022): reliance on analytics conclusions varies with the input. "
      "Fedyk et al. (2022): firm-level AI investment and audit quality. Estep, "
      "Griffith & MacKenzie (2024): how financial executives respond to AI in audit."),
    B("Field and practitioner evidence: Kokina et al. (2025); Fotoh & Mugwira "
      "(2025); Emett et al. (2025); Eulerich et al. (2024)."),
    B("CHECK BEFORE YOU WRITE THE GAP: open Kokina et al. (2025) and Fotoh & "
      "Mugwira (2025) and note their method. If either interviewed auditors about "
      "their experience, say so and narrow your gap to the specific moment of "
      "confirmation. This is the check your RB02 runbook asks for, and it is the "
      "first thing a reviewer will test."),
    H3("2.4 Sycophancy: the system side"),
    B("Sharma et al. (2024) and Perez et al. (2023) on language models agreeing with "
      "the user; Fanous et al. (2025) on measuring it."),
    B("Glickman & Sharot (2025) on human and AI feedback loops changing human "
      "judgment; Lee et al. (2025) on knowledge workers reporting less critical "
      "effort with generative AI; Messeri & Crockett (2024) on illusions of "
      "understanding."),
    B("The point this subsection sets up: when the tool agrees, a human tendency and "
      "a system property point the same way, and a measure of reliance cannot tell "
      "them apart. That is your strongest original argument; make it in your words."),
    H3("2.5 Professional skepticism and the reviewer"),
    B("Nelson (2009); Hurtt et al. (2013); Peecher, Solomon & Trotman (2013); "
      "Trotman & Yetton (1985) and Ramsay (1994) on review."),
    B("Regulatory expectation that a human supervises AI output: PCAOB (2024); "
      "IAASB (2024); NIST (2024, AI 600-1)."),
    H3("2.6 Synthesis and the gap"),
    B("One paragraph. Suggested shape: the literature has examined the extent and "
      "direction of reliance, mostly by experiment and archive, and has examined "
      "sycophancy as a property of models; it has examined much less how "
      "experienced auditors experience the moment an AI tool confirms what they had "
      "already concluded. Keep it to what you have read."),
    B("Optional: a small figure of the concepts the literature offers, with a line "
      "saying the analysis stays open to what participants describe (the example "
      "paper does this with its Figure 1)."),
    PB,
]

# ---------------------------------------------------------------- 3 methodology
body += [
    H1("Methodology"),
    ai_label("AI-assisted draft. Sections 4.3 to 4.7 were drafted with "
             "Claude (Anthropic) from my own research protocol and the instructor's "
             "feedback, then revised by me. Sections 4.1 and 4.2 are my own writing."),
    note("KEEP the italic label above in the final version: the course requires "
         "AI-written text to be labelled. Revise every paragraph in your voice; the "
         "more you rewrite, the lower the AI share. 4.1 and 4.2 are yours to write."),
    H2("4.1 Research Design"),
    note("YOU WRITE THIS, half a page. It keeps the AI share under the 25% cap, and "
         "you have already written most of it: expand your 'Methodological "
         "assumptions' paragraph from the Introduction. Cover: phenomenology "
         "describes what people who lived the same experience share about it "
         "(Creswell & Poth, 2024; Moustakas, 1994); one line each on why not "
         "grounded theory (process and theory generation) and case study (bounded "
         "site); the site is the shared professional context, not one organization; "
         "transferability through rich description, no generalization."),
    H2("4.2 Role of the Researcher"),
    note("YOU WRITE THIS. 3 to 4 paragraphs, first person. Most of it already exists "
         "in your own words: your axiology paragraph in the Introduction and the "
         "epoché in your protocol. Cover: (1) insider position, an asset and a risk, "
         "with no career-length number; (2) bracketing in practice: a reflexive memo "
         "before each listen-back, leading questions flagged in the transcript "
         "margin; (3) the confirmation hazard log and why feeling confirmed by a "
         "participant is the phenomenon itself happening inside the study; (4) the "
         "insider and outsider pairing after Gioia and Chittipeddi (1991): their "
         "design, not their analysis method. Name the risk that auditors may "
         "describe more careful practice to a researcher than they actually follow."),
    H2("4.3 Participants and Sampling"),
    "Participants will be selected by criterion sampling, because phenomenology "
    "requires that every participant has lived the experience under study rather "
    "than holding views about it (Creswell & Poth, 2024). To be eligible, a person "
    "must have five or more years in internal audit, external audit, or risk "
    "assurance; must have worked recurring engagements in which a prior-period "
    "conclusion is available as a reference point; must use or have used AI or "
    "automated analytical tools that produce conclusions, findings, or risk ratings; "
    "and must be able to recall a specific occasion when such a tool reached a "
    "conclusion they had already reached themselves. The last criterion carries the "
    "study. A candidate who meets the first three but cannot recall an occasion has "
    "not lived the phenomenon and is not enrolled.",
    "Participants need to recall the experience, not to have interpreted it. They do "
    "not need to have thought of it as confirmation, reassurance, or bias. That "
    "meaning is for the interview to explore, so the screening question does not "
    "name or frame it. Before recruitment opens, the screening question will be "
    "tested informally with a small number of people in my professional network to "
    "learn whether experienced auditors can name a specific occasion. Those people "
    "will not become participants.",
    "Recruitment will draw on my first-degree professional network and then on "
    "referrals. Every referred person passes the same screen. To keep variation "
    "across settings, the sample will deliberately include different kinds of "
    "organizations, both internal and external audit, and a range of seniority and "
    "industries, with no more than two participants from any one firm. A commercial "
    "research panel will not be used. When the quantitative study was fielded, a "
    "panel of 334,976 members returned about twenty eligible people, which is too "
    "few for a survey but enough to recruit an interview study through a network.",
    "The plan is 10 to 15 participants. The decision to stop will rest on the depth "
    "and richness of the accounts rather than on saturation as an automatic rule. As "
    "a guide, stopping will be considered when the accounts already gathered are full "
    "enough to support textural and structural descriptions, when three consecutive "
    "interviews add no new meaning unit, and when the external reviewer agrees. The "
    "judgment and its reasons will be recorded on the day it is made.",
    H2("4.4 Data Collection"),
    "Data will come from one semi-structured interview per participant, of about 60 "
    "minutes, held by video call and audio-recorded with consent. The guide follows "
    "Creswell and Poth's (2024) two broad phenomenological questions: what the "
    "participant has experienced when an AI tool reached the conclusion they had "
    "already reached, and what situations or circumstances have typically shaped how "
    "they experienced it. Before the first question, each participant is asked to "
    "take a moment and bring one specific occasion to mind. The interview then "
    "follows that occasion: what they had concluded before the tool produced its "
    "output, how sure they were, what the tool said, what they did next, and what it "
    "was like to see it agree. Probes follow the participant rather than a fixed "
    "order.",
    "Recordings will be transcribed verbatim. Pseudonyms are assigned at "
    "transcription and firm, client, and engagement names are removed. I will write "
    "a reflexive memo after each interview and before listening back to it.",
    H2("4.5 Data Analysis"),
    "Analysis will follow the modified Stevick-Colaizzi-Keen method described by "
    "Moustakas (1994) and Creswell and Poth (2024), organized within the data "
    "analysis spiral of managing and organizing the data, reading and memoing, "
    "describing and classifying codes into themes, developing and assessing "
    "interpretations, and representing the data.",
    "**Managing and organizing.** Transcripts and memos are held in NVivo on an "
    "encrypted device under a named file plan, one file per participant, with the "
    "audit trail kept alongside and nothing stored in any public location. **Reading and memoing.** Each transcript is read in full more than "
    "once, and memos record first impressions and any moment I notice myself "
    "agreeing with a participant. **Describing and classifying.** Every statement "
    "about the experience is listed with equal weight (horizontalization), reduced "
    "to non-repeating meaning units in language close to the participant's own, and "
    "grouped into themes named in words a participant would recognize. A unit that "
    "does not fit is set aside in a visible list rather than dropped. **Developing "
    "and assessing interpretations.** A textural description sets out what "
    "participants experienced, quoted throughout, and a structural description sets "
    "out the conditions in which they experienced it, such as deadline pressure, the "
    "review hierarchy, and engagement history. Before the composite description of "
    "the essence is written, every transcript is re-read only for material that "
    "contradicts it, including accounts of checking harder when the tool agreed. "
    "**Representing.** Findings will be written as a narrative with extended "
    "quotation, without frequency counts or causal claims.",
    "Coding will be done by me. NVivo stores and organizes the codes I assign; its "
    "automated coding features will not be used, and AI tools will not assign codes, name themes, write "
    "descriptions, or decide what a participant meant. Letting a model propose "
    "themes and then agreeing with them would reproduce, inside the analysis, the "
    "experience the study examines. Any use of AI, for example checking prose for "
    "clarity, is logged with the date, the tool, and what was done with the output.",
    H2("4.6 Trustworthiness and Validation"),
    "Trustworthiness is addressed through Lincoln and Guba's (1985) criteria and "
    "Creswell and Miller's (2000) validation strategies, using the participant, "
    "reviewer, and researcher lenses.",
    "**Member checking.** Each participant receives their own textural description, "
    "not the transcript, as a chance to consider whether it represents what they "
    "experienced and to add context. Responses and how each was considered are "
    "recorded. Member checking informs the credibility of the individual "
    "descriptions; it does not validate the structural interpretations or the "
    "composite description. **External review.** A reviewer with no stake in the "
    "argument will examine a few transcripts chosen on purpose, including one that "
    "challenges an emerging interpretation, together with the matching analytic "
    "memos, so that the review looks at how I move from accounts to meaning units, "
    "themes, and interpretations. **Researcher reflexivity.** The confirmation "
    "hazard log records each occasion on which I felt confirmed by an account and "
    "what I did about it, for example returning to the transcript for contradicting "
    "material or rewording a probe for the next interview. Each entry is "
    "cross-referenced in the audit trail to the decision it affected. **Audit "
    "trail.** The protocol was written and dated before any data collection, and "
    "each design decision is logged as it is made.",
    H2("4.7 Ethical Considerations"),
    "No participant will be approached before IRB approval. The existing approval "
    "(IRB-25-0462) covers an anonymous online survey, so an interview study with "
    "audio recording requires a modification or a new protocol, and the IRB will be "
    "asked which applies. Consent will be recorded verbally, with separate consent "
    "for audio recording. The main risk to participants is professional: some may "
    "describe practices their organization would not endorse. Pseudonyms, removal "
    "of identifying detail at transcription, encrypted storage, deletion of "
    "recordings after transcription and member checking, and the right to withdraw "
    "any passage without giving a reason all address that risk. No recording, "
    "transcript, or identifier will be uploaded to a public AI platform, consistent "
    "with the FIU University Graduate School AI policy.",
    PB,
]

# ---------------------------------------------------------------- 4 contributions
body += [
    H1("Expected Contributions"),
    note("YOU WRITE THIS. One page. The points below are prompts, not text. Pick "
         "three or four and argue them in your own voice; this is where the course "
         "most wants to hear you."),
    B("Scholarship: describes the lived experience of AI confirmation, which "
      "experimental and archival work on reliance does not reach."),
    B("Scholarship: separates automation bias (human) from sycophancy (system) in "
      "the one situation where they point the same way and cannot be told apart by "
      "measuring reliance."),
    B("Practice: tests from the inside the assumption in firm and regulatory AI "
      "policies that human review is a working control; what reviewers say they do "
      "when the tool agrees could inform review guidance and training."),
    B("Method: the confirmation hazard log as a reflexive control for any study where "
      "the researcher holds a prior position, shown changing decisions rather than "
      "only recording them."),
    B("Programme: this is the second link of your three-link chain. Say in one line "
      "how its findings will feed the dissertation's quantitative work."),
    B("Limitations to name briefly: a small, network-recruited sample; self-report "
      "of a moment that may have been tidied in memory; possible description of more "
      "careful practice than is followed; no generalization claimed."),
]

# ---------------------------------------------------------------- 5 timeline
body += [
    H1("Proposed Timeline"),
    ai_label("AI-assisted draft, built from my research protocol and revised by me."),
    "The study is planned to run from October 2026 to June 2027. Data collection "
    "and analysis run in parallel, so each interview is memoed and coded before the "
    "next is held.",
    {"__table__": "timeline"},
    note("Check the dates against your own calendar and the dissertation work. Do "
         "not add a completion date for the DBA anywhere in this paper."),
    PB,
]

# ---------------------------------------------------------------- references
body += [
    H1("References"),
    note("Every entry below is from your research paper's verified reference list "
         "or a standard methods text. Delete any you do not end up citing, and add "
         "page numbers for direct quotations."),
]
REFS = [
    "Bonner, S. E. (2008). *Judgment and decision making in accounting.* Prentice Hall.",
    "Commerford, B. P., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man versus machine: Complex estimates and auditor reliance on artificial intelligence. *Journal of Accounting Research, 60*(1), 171-201. https://doi.org/10.1111/1475-679X.12407",
    "Creswell, J. W., & Miller, D. L. (2000). Determining validity in qualitative inquiry. *Theory Into Practice, 39*(3), 124-130.",
    "Creswell, J. W., & Poth, C. N. (2024). *Qualitative inquiry and research design: Choosing among five approaches* (5th ed.). SAGE Publications.",
    "Dowling, C., & Leech, S. A. (2007). Audit support systems and decision aids. *International Journal of Accounting Information Systems, 8*(2), 92-116.",
    "Emett, S. A., Eulerich, M., Lipinski, E., Prien, N., & Wood, D. A. (2025). Leveraging ChatGPT for enhancing the internal audit process: A real-world example from Uniper, a large multinational company. *Accounting Horizons, 39*(2), 125-135. https://doi.org/10.2308/HORIZONS-2023-111",
    "Estep, C., Griffith, E. E., & MacKenzie, N. L. (2024). How do financial executives respond to the use of artificial intelligence in financial reporting and auditing? *Review of Accounting Studies, 29*(3), 2798-2831. https://doi.org/10.1007/s11142-023-09771-y",
    "Eulerich, M., Sanatizadeh, A., Vakilzadeh, H., & Wood, D. A. (2024). Is it all hype? ChatGPT's performance and disruptive potential in the accounting and auditing industries. *Review of Accounting Studies, 29*(3), 2318-2349. https://doi.org/10.1007/s11142-024-09833-9",
    "Fanous, A., Goldberg, J., Agarwal, A. A., Lin, J., Zhou, A., Daneshjou, R., & Koyejo, S. (2025). *SycEval: Evaluating LLM sycophancy* (arXiv:2502.08177). arXiv. https://doi.org/10.48550/arXiv.2502.08177",
    "Fedyk, A., Hodson, J., Khimich, N., & Fedyk, T. (2022). Is artificial intelligence improving the audit process? *Review of Accounting Studies, 27*(3), 938-985. https://doi.org/10.1007/s11142-022-09697-x",
    "Fotoh, L. E., & Mugwira, T. (2025). Exploring large language models in external audits: Implications and ethical considerations. *International Journal of Accounting Information Systems, 56*, 100748. https://doi.org/10.1016/j.accinf.2025.100748",
    "Furnham, A., & Boo, H. C. (2011). A literature review of the anchoring effect. *The Journal of Socio-Economics, 40*(1), 35-42.",
    "Gioia, D. A., & Chittipeddi, K. (1991). Sensemaking and sensegiving in strategic change initiation. *Strategic Management Journal, 12*(6), 433-448.",
    "Glickman, M., & Sharot, T. (2025). How human-AI feedback loops alter human perceptual, emotional and social judgements. *Nature Human Behaviour, 9*(2), 345-359. https://doi.org/10.1038/s41562-024-02077-2",
    "Henrizi, P., Himmelsbach, D., & Hunziker, S. (2021). Anchoring and adjustment effects on audit judgments: Experimental evidence from Switzerland. *Journal of Applied Accounting Research, 22*(4), 598-621. https://doi.org/10.1108/JAAR-01-2020-0011",
    "Hurtt, R. K., Brown-Liburd, H., Earley, C. E., & Krishnamoorthy, G. (2013). Research on auditor professional skepticism: Literature synthesis and opportunities for future research. *Auditing: A Journal of Practice & Theory, 32*(Supplement 1), 45-97.",
    "International Auditing and Assurance Standards Board. (2024). *Technology position and focus area resources.* https://www.iaasb.org/focus-areas/technology",
    "Joyce, E. J., & Biddle, G. C. (1981). Anchoring and adjustment in probabilistic inference in auditing. *Journal of Accounting Research, 19*(1), 120-145.",
    "Kinney, W. R., Jr., & Uecker, W. C. (1982). Mitigating the consequences of anchoring in auditor judgments. *The Accounting Review, 57*(1), 55-69.",
    "Kokina, J., Blanchette, S., Davenport, T. H., & Pachamanova, D. (2025). Challenges and opportunities for artificial intelligence in auditing: Evidence from the field. *International Journal of Accounting Information Systems, 56*, 100734. https://doi.org/10.1016/j.accinf.2025.100734",
    "Koreff, J. (2022). Are auditors' reliance on conclusions from data analytics impacted by different data analytic inputs? *Journal of Information Systems, 36*(1), 19-37. https://doi.org/10.2308/ISYS-19-051",
    "Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.* https://doi.org/10.1145/3706598.3713778",
    "Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic inquiry.* SAGE Publications.",
    "Messeri, L., & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. *Nature, 627*(8002), 49-58. https://doi.org/10.1038/s41586-024-07146-0",
    "Moustakas, C. (1994). *Phenomenological research methods.* SAGE Publications.",
    "Mussweiler, T., & Strack, F. (1999). Hypothesis-consistent testing and semantic priming in the anchoring paradigm: A selective accessibility model. *Journal of Experimental Social Psychology, 35*(2), 136-164.",
    "National Institute of Standards and Technology. (2024). *Artificial intelligence risk management framework: Generative artificial intelligence profile* (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1",
    "Nelson, M. W. (2009). A model and literature review of professional skepticism in auditing. *Auditing: A Journal of Practice & Theory, 28*(2), 1-34.",
    "Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381-410. https://doi.org/10.1177/0018720810376055",
    "Peecher, M. E., Solomon, I., & Trotman, K. T. (2013). An accountability framework for financial statement auditors and related research questions. *Accounting, Organizations and Society, 38*(8), 596-620.",
    "Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., et al. (2023). Discovering language model behaviors with model-written evaluations. In *Findings of the Association for Computational Linguistics: ACL 2023* (pp. 13387-13434). https://doi.org/10.18653/v1/2023.findings-acl.847",
    "Public Company Accounting Oversight Board. (2024). *Spotlight: Staff update on outreach activities related to the integration of generative artificial intelligence in audits and financial reporting.* https://pcaobus.org/documents/generative-ai-spotlight.pdf",
    "Ramsay, R. J. (1994). Senior/manager differences in audit workpaper review performance. *Journal of Accounting Research, 32*(1), 127-135.",
    "Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. In *Proceedings of the Twelfth International Conference on Learning Representations (ICLR).* https://arxiv.org/abs/2310.13548",
    "Strack, F., & Mussweiler, T. (1997). Explaining the enigmatic anchoring effect: Mechanisms of selective accessibility. *Journal of Personality and Social Psychology, 73*(3), 437-446.",
    "Trotman, K. T., & Yetton, P. W. (1985). The effect of the review process on auditor judgments. *Journal of Accounting Research, 23*(1), 256-267.",
    "Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124-1131.",
]
body += REFS

# ---------------------------------------------------------------- disclosure
body += [
    PB,
    H1("Disclosure of Artificial Intelligence Use"),
    note("Required by the FIU University Graduate School AI policy and the course's "
         "labelling rule. Update it to match what you actually end up keeping."),
    "Generative AI (Claude, Anthropic) was used in preparing this proposal in four "
    "ways. It drafted the Participants and Sampling, Data "
    "Collection, Data Analysis, Trustworthiness, and Ethical Considerations sections "
    "of the Methodology, and the Proposed Timeline, from decisions already recorded "
    "in my own research protocol and from the instructor's feedback; those sections "
    "are labelled in the text and I revised them. It organized an outline and a "
    "source list for the Literature Review and Expected Contributions, which I "
    "wrote. It compiled the reference list from sources I had already gathered, and "
    "it formatted the document. The research problem, purpose statement, research "
    "question, interpretive framework and assumptions, literature review, research "
    "design, role of the researcher, expected contributions, and every methodological decision are "
    "my own. No participant data exists, and none was shared with any AI tool.",
]

TABLES = {
    "terms": [
        ["Term", "Definition"],
        ["Anchoring", "The tendency to rely too heavily on an initial reference point when forming a judgment, and to adjust insufficiently away from it."],
        ["Automation bias", "The tendency to over-trust or defer to output from an automated system, even when independent evidence should prompt further scrutiny."],
        ["Sycophancy", "A tendency in AI systems to agree with or affirm a user's stated position rather than challenge it. This is a property of the model, not a human bias."],
        ["Professional judgment", "The application of relevant training, knowledge, and experience to reach a well-reasoned conclusion under conditions of uncertainty."],
        ["Recurring engagement", "An audit relationship that continues across multiple annual periods with the same client, in which prior-period conclusions remain available as reference points."],
        ["AI-generated conclusion", "An analytical output produced by an AI system, such as a flagged item, a risk score, or a suggested conclusion, that a reviewer can accept, adjust, or reject."],
    ],
    "timeline": [
        ["Phase", "Activities", "Period"],
        ["1. Approval", "IRB modification or new protocol; consent and recording language; confirm transcription service and external reviewer", "October to December 2026"],
        ["2. Preparation", "Test the screening question informally; finalize the interview guide; recruit the external reviewer", "December 2026"],
        ["3. Recruitment", "Network outreach and referrals; screening; scheduling", "January to February 2027"],
        ["4. Interviews and early analysis", "10 to 15 interviews; transcription and reflexive memos; horizontalization and meaning units as each transcript is ready; hazard log kept", "January to March 2027"],
        ["5. Analysis", "Themes; textural and structural descriptions; disconfirming re-read; decision on stopping recorded", "March to April 2027"],
        ["6. Validation", "Member checking on individual descriptions; external review of selected transcripts with memos", "April to May 2027"],
        ["7. Write-up", "Composite description; findings narrative; limitations; audit trail closed", "May to June 2027"],
    ],
}

spec = {
    "title": TITLE,
    "subtitle": None,
    "ident": [],
    "double_spaced": True,
    "body": body,
    "tables": TABLES,
}

build(spec, OUT)

# APA title page: centre everything above the first page break.
d = Document(OUT)
for p in d.paragraphs:
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if 'type="page"' in p._p.xml:
        break
d.save(OUT)

subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir",
                OUT_DIR, OUT], check=True, capture_output=True)
print("wrote", OUT.replace(".docx", ".pdf"))
