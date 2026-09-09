import json

spec = {
 "title": "Learning Memo 4 · Proposal Introduction",
 "subtitle": "Working Draft",
 "ident": [
   "Yasir A. Malik",
   "Florida International University · College of Business",
   "Doctor of Business Administration · Cohort 8.14",
   "GEB 7911 · Qualitative Research Methods · Instructor: Dr. Cristina Gonzalez",
   "September 7, 2026",
 ],
 "double_spaced": False,
 "body": [
  {"h2": "1. Focus and Research Problem"},

  ["An auditor reviewing a multi-year engagement has always had a starting point: last year's "
   "conclusion. What has changed is that AI systems now introduce new risks into that process, "
   "including sycophancy and epistemic drift. These risks don't show up as one-time errors. They "
   "show up as a pattern that repeats every time the system is used."],

  ["Professional standards assume a competent human reviewer sits above the AI system. Nobody has "
   "actually measured whether that reviewer's judgment survives contact with it. That matters "
   "because the auditors relying on those standards are the last check before a misjudgment reaches "
   "a client, a regulator, or a public filing."],

  ["The empirical literature on AI and auditor judgment is thin, and what exists asks the wrong "
   "kind of question. Most work asks ",
   {"t":"how much","i":True},
   " auditors rely on AI-generated output. That is a magnitude question, and a survey can answer "
   "it. It does not ask ",
   {"t":"how","i":True},
   " auditors experience receiving that output, or how they make sense of it in the moment. That "
   "is a process question, and a survey cannot answer it. My own prior study tried to measure this "
   "by self-report and ran into the same limit every self-report measure of this kind runs into: "
   "it asks a person to notice the one thing the bias in question prevents them from noticing. "
   "The anchoring-and-adjustment literature originating with Tversky and Kahneman (1974) "
   "establishes that judgments formed from a starting point adjust insufficiently away from it, "
   "and that the effect persists even when participants are motivated toward accuracy. What that "
   "literature has not examined is what happens when the starting point is produced by a machine "
   "that also agrees with the conclusion the professional had already reached."],

  ["This matters to two audiences. For research, it separates two things the literature currently "
   "conflates: automation bias, which is a human tendency, and sycophancy, which is a property of "
   "the system. Asking how much someone relied on a machine cannot tell those two apart. For "
   "practice, audit firms and regulators are writing AI-use policies right now on the assumption "
   "that human review is a working control. Nobody has asked the people doing that reviewing what "
   "the experience of it actually is."],

  {"h2": "2. Purpose Statement"},

  ["The purpose of this phenomenological study is to understand the experience of receiving an "
   "AI-generated conclusion that confirms a judgment already formed, for experienced internal "
   "auditors, at organizations where AI-supported analytical tools are used in live engagement "
   "work. At this stage in the research, receiving AI-generated confirmation will be generally "
   "defined as the moment an AI system produces an analytical output matching a conclusion the "
   "auditor had already reached independently."],

  ["Participants will be experienced internal auditors with eight or more years of practice, "
   "recurring multi-year engagement responsibility, and meaningful, direct exposure to "
   "AI-generated analytical output in the course of that work. Consistent with a phenomenological "
   "design, the site is defined by the shared professional context in which the phenomenon occurs "
   "rather than by a single named organization."],

  {"h2": "3. Research Question"},

  [{"t":"How do experienced auditors experience and make sense of receiving an AI-generated "
        "conclusion that confirms a judgment they had already formed?","b":True}],

  {"h2": "4. Interpretive Framework and Assumptions"},

  ["This study is approached from a social constructivist, inductive interpretive framework."],

  [{"t":"Ontological assumptions.","b":True},
   " Multiple realities exist. There is no single correct account of what it is like to receive "
   "machine-generated confirmation waiting to be recovered. There are as many accounts as there "
   "are auditors who have experienced it, and the variation among them is part of the finding "
   "rather than error to be averaged away."],

  [{"t":"Epistemological assumptions.","b":True},
   " Evidence consists of participants' own first-person descriptions of the experience, gathered "
   "through semi-structured, audio-recorded interviews. Closeness to participants is treated as a "
   "condition of knowing rather than a threat to it. The account is the data, not a proxy for "
   "something more objective sitting behind it."],

  [{"t":"Axiological assumptions.","b":True},
   " My own values are present in this study and are stated rather than bracketed away."],

  ["I am not an outsider to this setting. Fifteen years in audit and risk at Citigroup and JPMorgan "
   "Chase, and prior experience as a bank examiner for the Florida Office of Financial Regulation, "
   "give me direct familiarity with the vocabulary, pressures, and judgment calls this study asks "
   "participants to describe. That same background is also a risk: I already believe the phenomenon "
   "under study is real, which makes me more likely to hear confirmation in what a participant says "
   "than a genuinely neutral listener would. To guard against that, every occasion on which I "
   "notice myself feeling confirmed by a participant's account is logged in a confirmation hazard "
   "log kept for the duration of the study."],

  [{"t":"Methodological assumptions.","b":True},
   " Of the five qualitative approaches, this study uses phenomenology. The research question asks "
   "what an experience is like and how it is made sense of, which is the question phenomenology is "
   "built to answer. A grounded theory design would commit the study to generating theory it is "
   "not yet positioned to generate, and a case study design would require a bounded site this "
   "study does not have."],

  {"h2": "5. Key Terminology"},
 ],

 "table": {
  "rows": [
   ["Term", "Definition"],
   ["Anchoring", "The tendency to rely too heavily on an initial reference point when forming a judgment, and to adjust insufficiently away from it."],
   ["Automation bias", "The tendency to over-trust or defer to output from an automated system, even when independent evidence should prompt further scrutiny."],
   ["Sycophancy", "A tendency in AI systems to agree with or affirm a user's stated position rather than challenge it. This is a property of the model, not a human bias."],
   ["Professional judgment", "The application of relevant training, knowledge, and experience to reach a well-reasoned conclusion under conditions of uncertainty."],
   ["Recurring engagement", "An audit relationship that continues across multiple annual periods with the same client, in which prior-period conclusions remain available as reference points."],
   ["AI-generated conclusion", "An analytical output produced by an AI system, such as a flagged item, a risk score, or a suggested conclusion, that a reviewer can accept, adjust, or reject."],
  ]
 },

 "appendix": [
  {"h2": "Reference"},
  ["Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. "
   "Science, 185(4157), 1124-1131."],

  {"h2": "Disclosure of Artificial Intelligence Use"},
  ["AI (Claude) was used to organise this document against the assignment's five prescribed "
   "components and to draft the terminology definitions and structural language. The research "
   "problem, purpose, research question, interpretive framework, and the positionality reflection "
   "are my own."],
 ],
}
json.dump(spec, open('memo4.json','w'))
print("spec written")
