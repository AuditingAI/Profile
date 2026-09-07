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
   "it asks a person to notice the one thing the bias in question prevents them from noticing."],

  ["This matters to two audiences. For research, it separates two things the literature currently "
   "conflates: automation bias, which is a human tendency, and sycophancy, which is a property of "
   "the system. Asking how much someone relied on a machine cannot tell those two apart. For "
   "practice, audit firms and regulators are writing AI-use policies right now on the assumption "
   "that human review is a working control. Nobody has asked the people doing that reviewing what "
   "the experience of it actually is."],

  {"h2": "2. Purpose Statement"},

  ["The purpose of this phenomenological study is to understand how experienced auditors experience "
   "and make sense of receiving an AI-generated conclusion that confirms a judgment they had "
   "already formed. Participants will be experienced auditors, with eight or more years in "
   "internal audit roles, recurring multi-year engagement responsibility, and meaningful, direct "
   "exposure to AI-generated analytical output in the course of that work. The phenomenon under "
   "study is the experience of encountering machine-generated confirmation of a prior professional "
   "judgment."],

  {"h2": "3. Research Question"},

  [{"t":"How do experienced auditors experience and make sense of receiving an AI-generated "
        "conclusion that confirms a judgment they had already formed?","b":True}],

  {"h2": "4. Interpretive Framework and Assumptions"},

  ["This study is approached from a constructivist interpretive framework. Constructivism holds "
   "that multiple realities exist and that meaning is constructed through individuals' lived "
   "experience. In this study, that means auditors' own accounts of what it is like to receive "
   "AI-generated confirmation are the data itself, not a proxy for a single correct account waiting "
   "to be recovered. Evidence will be gathered through semi-structured, audio-recorded interviews."],

  ["I am not an outsider to this setting. Fifteen years in audit and risk at Citigroup and JPMorgan "
   "Chase, and prior experience as a bank examiner for the Florida Office of Financial Regulation, "
   "give me direct familiarity with the vocabulary, pressures, and judgment calls this study asks "
   "participants to describe. That same background is also a risk: I already believe the phenomenon "
   "under study is real, which makes me more likely to hear confirmation in what a participant says "
   "than a genuinely neutral listener would. To guard against that, every occasion on which I "
   "notice myself feeling confirmed by a participant's account is logged in a confirmation hazard "
   "log kept for the duration of the study."],

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
  {"h2": "Disclosure of Artificial Intelligence Use"},
  ["AI (Claude) was used to organise this document against the assignment's five prescribed "
   "components and to draft the terminology definitions and structural language. The research "
   "problem, purpose, research question, interpretive framework, and the positionality reflection "
   "are my own."],
 ],
}
json.dump(spec, open('memo4.json','w'))
print("spec written")
