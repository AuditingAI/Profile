# Pre-IRB critique of the phenomenological protocol

**Date:** 20 October 2026
**Scope:** Review of the L2 phenomenology design before the IRB modification is drafted. Reviewed:
`PROTOCOL_phenomenology.md`, `INTERVIEW_GUIDE.md`, `SAMPLING_AND_RECRUITMENT.md`, `CODING_PLAN.md`,
`TRUSTWORTHINESS.md`, `AUDIT_TRAIL.md`, `README.md` (this directory); `../KNOWLEDGE/03_METHOD.md`; the
GEB 7911 Week 8 prep and delivery script, Dr. Gonzalez's feedback of 7 Sep, 14 Sep and 1 Oct, the
proposal skeleton, and the methodology sections in `../coursework/_templates/build_geb7911_proposal.py`.
The research question taken as current is the GEB 7911 version: *"How do experienced auditors
experience and make sense of receiving an AI-generated conclusion that confirms a judgment they had
already formed?"*
**Not in scope:** the protocol itself is not edited. Nothing here is a finding; nothing has been fielded.

> Critique drafted with Claude (Anthropic) on 20 Oct 2026 as review feedback; all design decisions and
> revisions are Yasir Malik's and remain subject to his committee and Dr. Gonzalez.

Log this use in `AUDIT_TRAIL.md` under `AI` if you act on any of it.

---

## 2 · Summary verdict

**The design is strong where most student phenomenologies are weak.** One bounded moment, stated
precisely (protocol §2). A criterion screen that tests for lived experience rather than opinion. A
falsification table written before data (§6). An AI boundary that is principled, not just compliant.
Hard limits on causal and frequency language at the essence step. Dr. Gonzalez's three October
changes (recall not interpretation, depth over saturation, purposive external review with memos) are
already in the course proposal. The confirmation hazard log is a genuine methodological contribution
and both reviewers said so.

**What would stop or damage it is mostly in the plumbing, not the idea.** Ranked by risk to IRB
approval first, then to credibility:

| # | Issue | Why it matters | Where |
|---|---|---|---|
| **1** | **Participant content is routed into a public repository.** The hazard log ("what was said"), screening decisions (`SAMPLING` tag), and leading-question flags are all specified to go in `AUDIT_TRAIL.md`, which is public and whose git history cannot be cleanly rewritten. `CODING_PLAN.md` also plans to commit "de-identified, quotable extracts" here | Directly contradicts the confidentiality controls the IRB will be told about. In a population this small (about 20 eligible in a 334,976 panel), a quote plus a setting detail can identify someone (deductive disclosure; Kaiser, 2009) | `TRUSTWORTHINESS.md` §4, `AUDIT_TRAIL.md` tags, `CODING_PLAN.md` last paragraph |
| **2** | **Professional confidentiality and insider recruitment are under-specified.** The interview asks for a specific live-engagement episode, which invites client facts, employer-proprietary tool details and, for any former examiner, confidential supervisory information. Recruitment starts in your first-degree network, which includes former Citi and JPMorgan colleagues and, potentially, users of the Citi AI review tool you built. The opening script promises "nothing identifies you or your firm", which a recorded interview cannot promise | IRB will ask about power relationships, conflict of interest and accurate confidentiality language. A participant who describes your own tool is evaluating your work to your face | `INTERVIEW_GUIDE.md` opening; `SAMPLING_AND_RECRUITMENT.md` §4, §5 |
| **3** | **The study is not yet one study.** The protocol still carries the old "reliance" RQ; the proposal intro says internal auditors with eight or more years while sampling says five or more years across internal, external and risk assurance; the skeleton still describes grounded-theory coding and survey open-text data. Methodologically, Moustakas's transcendental epoché and invariant essence sit beside a social-constructivist "multiple realities" stance, IPA-flavoured "make sense of" wording, and a statement that bracketing is "not achievable". Three Moustakas steps are missing or thin (see §3) | The modification must describe exactly one RQ, one population and one analytic tradition. A methods reviewer will test coherence first | Protocol §1, §3, §4; proposal builder; `PROPOSAL_SKELETON.md` |
| **4** | **The interview guide leaves the episode after Section A.** Sections B to E move to abstraction, norms and hypotheticals ("is that evidence?", "checked anyway", "deserves more scrutiny", "would anyone notice if it moved?"). Several presuppose the answer. Separately, your public writing, LinkedIn posts and this repository describe the sycophancy and automation-bias argument to the very network you recruit from | Leading and normative questions produce the textbook answer an experienced auditor gives a former senior colleague, which is the data least able to separate experience from professional self-presentation | `INTERVIEW_GUIDE.md` B to E; recruitment channel |
| **5** | **AI touching participant data is not settled or approved.** Transcription tool is `[VERIFY]`; `CODING_PLAN.md` lets AI "act as an adversary" and "format, reorder and tabulate what I have already coded", both of which would expose participant data and the second of which edges into interpretation; NVivo and Zoom both ship AI assistants; committee approval of AI use (FIU UGS §3.2, §5.1) is recorded as not yet obtained | FIU policy forbids identifiable data on public AI platforms and requires committee approval and Methods disclosure. The IRB will want each tool named | `CODING_PLAN.md` AI boundary and Tooling; `../00_Execution/FIU_AI_POLICY_2026.md` §4 |

**Next tier, fix before submission but lower risk:**

6. **Saturation language survives in four places** after Dr. Gonzalez asked for it to go:
   `TRUSTWORTHINESS.md` §3 (dependability row), the 26 Aug `AUDIT_TRAIL.md` entry (history, so leave it
   and add a superseding entry), `CODING_PLAN.md` ("decide when saturation is reached") and
   `../KNOWLEDGE/03_METHOD.md` §4. `SAMPLING_AND_RECRUITMENT.md` §3 still says "above 15, report why
   saturation did not arrive". See §5 below.
7. **The external reviewer gates the stopping decision but is not yet recruited**, and whether they
   must be named on the IRB protocol is an open question.
8. **Concurrent analysis plus hazard-log-driven probe changes means the guide will evolve mid-study.**
   That is legitimate, but the guide needs version numbers and a record of which participant had which
   version.
9. **A precondition to confirm with Dr. Rey:** the skeleton records Dr. Gonzalez saying the
   dissertation stays quantitative and the qualitative work is for the course proposal, and that the IRB
   is "wired for quantitative". Before drafting a modification, confirm that this arm will actually be
   fielded, under whose supervision, and as part of what.

---

## 3 · Alignment check against Moustakas (1994)

Moustakas presents transcendental phenomenology as epoché, transcendental-phenomenological reduction,
imaginative variation and synthesis, and gives the modified Stevick-Colaizzi-Keen and van Kaam
procedures for analysis. Creswell & Poth (2024) present a simplified version of that procedure. Your
protocol names the modified Stevick-Colaizzi-Keen method, so that is the yardstick here. Check step
wording against your own copy of Moustakas before quoting it; no page numbers are given below because
none were verified.

| Moustakas step | What the protocol does | Gap | Suggested fix |
|---|---|---|---|
| **Epoché** | §3 lists four commitments (insider, prior model, stake, pressure to produce) and four procedures; step 1 of §4 revisits it | The four commitments are *judgments about* the phenomenon, which is reflexivity. The Stevick-Colaizzi-Keen variant starts with the researcher's own **full description of his own experience** of the phenomenon, analysed by the same steps. You have one (the Citi episode in the Week 8 script: "did I check, or did I just feel confirmed?") and it is not written as a description. The step 1 stopping rule ("names at least one view that changed") can be satisfied by manufacturing a change | Before interview 1, write your own experiential description of that episode, in the first person, with no theory words. Run it through horizonalization to essence privately and keep it out of the composite. Add a short epoché memo **before** each interview, not only before each listen-back. Replace the step 1 stopping rule with "memo written and dated before the interview" |
| **Phenomenological reduction: horizonalization** | Step 2; every statement listed flat with a locator | Sound. Not stated that it is done per transcript, nor how statements that followed a leading question are treated | State "per participant". Carry the `LEADING` flag into the horizon list as a column so those statements stay visible and can be weighed at clustering |
| **Invariant constituents / meaning units** | Step 3; non-repetitive, non-overlapping; keep/reject examples ban theory vocabulary | Sound. The ban on "anchored" and "automation bias" as unit labels is exactly right | Add a mechanical check: search unit labels for theory terms (anchor, bias, sycophancy, complacency, reliance, skepticism) before clustering |
| **Clusters of meaning / themes** | Step 4; named in participant language; parked list reported; single-participant clusters allowed | Sound. The risk is that cluster names drift toward the three-link chain | Give the external reviewer the parked list and the cluster names together; ask specifically which cluster names they could predict from your published argument |
| **Individual textural description** | Step 5 reads as a group-level description; member checking (TRUSTWORTHINESS §1) presupposes individual ones | The Moustakas sequence writes a textural description **for each participant** before any composite | Make step 5 explicitly per participant. That document is what goes to member check |
| **Imaginative variation / structural description** | Step 6 operationalised as a list of contextual pressures: deadline, review hierarchy, tool familiarity, engagement history, firm culture | This is a factor list. It invites "deadline pressure led to..." which your own step 7 rule forbids. Imaginative variation is a reflective procedure: varying frames of reference to separate what is essential to the experience from what is incidental | For each participant's textural themes, ask and record: would this still be *this* experience if the tool had disagreed, if a colleague rather than a tool had concurred, if there were no deadline, if no reviewer would ever see it? Use structural lenses such as time, setting, relation to self and others, the tool as an object, and causality *as the participant experienced it* `[VERIFY the list against Moustakas's chapter on imaginative variation]`. Keep the variations considered in the analytic memo |
| **Individual textural-structural description** | Not present | Missing step between steps 6 and 7 | Add a per-participant synthesis of what and how, before the composite |
| **Composite description / essence** | Step 7; invariant structure, exceptions stated, no causal or frequency language | Strong limits. Unresolved tension with the stated social-constructivist paradigm ("as many accounts as auditors") | One sentence in the design section: the essence claimed is the shared structure across *these* participants' accounts, offered for transferability, not a universal truth about auditors |
| **Researcher's own experience as data** | Hazard log and memos | Covered under epoché above | As above |

**Traditions, stated plainly.** The design currently borrows from three places: Moustakas (analysis,
epoché, essence), a hermeneutic or reflexive stance ("bracketing is not having no views"; the hazard
log as interpretive evidence), and Gioia & Chittipeddi (insider/outsider architecture). "Make sense
of" is also the signature phrase of IPA, where the researcher's interpretation of the participant's
sense-making is the point (Smith, Flowers & Larkin, 2022). Two defensible routes, and the choice is
yours with Dr. Gonzalez:

- **Stay with Moustakas (lower cost, matches the course and Creswell & Poth).** Say that epoché is
  pursued as a repeated discipline whose success is partial, and that the reflexive procedures support
  it rather than replace it. Keep "make sense of" and be ready with your existing answer: meaning-making
  is part of the experience, not a second process. Keep Gioia as reflexivity design only, as you do.
- **Move to a hermeneutic approach (van Manen, 1990) or IPA.** Then fore-understanding is used, not
  set aside, and the hazard log becomes an analytic resource. But the analysis steps, the essence claim
  and the course alignment all change. Not recommended this late unless Dr. Gonzalez prefers it.

Either way, delete the grounded-theory and Gioia-coding remnants (first-order/second-order codes,
aggregate dimensions, constant comparison as an analysis method) from `PROPOSAL_SKELETON.md` before any
of it is reused.

---

## 4 · Interview guide review

**Principles applied.** Phenomenological questions stay experience-near: what happened, what it was
like, in this occasion. Episodic or critical-incident questioning (Flanagan, 1954; Flick, 2000) keeps
the participant in one concrete event and asks for a contrasting event, rather than for general views.
Questions that ask what *should* happen, what *usually* happens, or whether something *counts as*
evidence produce professional self-presentation, which an experienced auditor does fluently.

### 4.1 Question-by-question

| Current wording | Verdict | Reason | Suggested wording to adapt |
|---|---|---|---|
| Opening: "Everything is confidential, the recording stays with me, nothing identifies you or your firm" | **Revise** | Over-promises. A recording identifies the speaker; a transcription service or reviewer may handle data; confidentiality has limits | "I'll protect what you tell me as far as I can: names of people, firms and clients come out when I transcribe, and the recording is deleted after [step]. Please don't name clients or describe anything your firm or a client would treat as confidential. Keep it general and I'll steer us if we get close." |
| Grounding move: "think of one specific time an AI tool told you something you'd already concluded yourself" | **Keep, add one line** | Good episodic anchor. Recall favours dramatic episodes | Add: "It can be small and ordinary. It doesn't need to be memorable." |
| Q1 "What have you experienced when an AI tool reached the same conclusion you had already reached?" | **Revise** | General framing invites a summary of many occasions | "Tell me about that time, starting wherever it starts for you." |
| Q2 "What situations or circumstances have typically influenced how you experienced that?" | **Revise** | "Typically" generalises; "influenced" is causal (your own vocabulary list bans it) | "What was going on around that moment: the stage of the work, the timing, who else was involved, what the tool was in general terms?" |
| A "Take me through that one. Where were you, what were you working on?" | **Keep** | Experience-near, concrete | |
| A "What had you concluded, before the tool said anything?" | **Keep, add probe** | Establishes the prior judgment the phenomenon requires | Add: "How had you arrived there?" (not "why") |
| A "How sure were you at that point?" | **Keep, add probe** | Useful, but invites hindsight | Add: "Is that how it felt then, or how it looks now?" |
| A "Then what did the tool say?" | **Revise lightly** | Add the sensory and material detail | "What did the tool give you, and how did it appear: on screen, in a report, in a list?" |
| A "What was the next thing you did?" | **Keep** | | |
| A "What was it like to see it agree with you?" | **Keep, mirror their word** | The central question. "Agree" is your word; if they said "matched", "backed me up" or "landed in the same place", use theirs | "What was it like when you saw it [their word]?" Then silence |
| A "What did you notice yourself thinking?" | **Keep, widen** | | "...thinking, or feeling?" |
| A "Did anything change about how the workpaper got written up?" | **Revise** | Closed yes/no; and invites disclosure of a possible documentation deficiency, which is a professional-risk question | "What happened with that piece of work afterward?" |
| B "Think about the prior-year conclusion... Is seeing that the same as seeing the AI's answer, or different?" | **Revise, move late** | Researcher-introduced comparison in an either/or frame; imports the anchoring theory. It is the hinge, so keep the topic but ask it only after Section A is exhausted and only if they have not raised it | "On that engagement, was anything else already on the file before the tool's output, such as last year's work? How did that sit with you at the time?" Mark it in the transcript as a researcher-introduced topic |
| B "Say more about the difference." | **Keep** | Only if they named one; your note "never supply one" is right | |
| B "If you had to explain to a new associate why one deserves more scrutiny than the other" | **Drop** | Presupposes one deserves more scrutiny; hypothetical; invites the training-manual answer | |
| C "When the tool agrees with you, is that evidence?" | **Drop or revise** | "Evidence" is a defined term in auditing standards, so it elicits the normative answer; closed question | "In that moment, what did the tool's answer mean to you?" |
| C "Is it different evidence from a colleague agreeing with you?" | **Revise** | Presupposes it is evidence; abstract comparison | "Can you think of a time a colleague or reviewer landed where you had? Tell me about that one." Let any comparison come from them |
| C "Has there been a time you went and checked anyway? What made that one different?" | **Revise** | "Anyway" implies not checking is the default | "Tell me about another time a tool reached the same conclusion you had. What happened that time?" (contrast episode) |
| D "How do you know when you've looked at an AI output enough?" | **Revise** | General and normative | "On that occasion, how did your work on that item come to a close?" |
| D "Has that point moved since you started using these tools?" | **Drop** | Presupposes a threshold; change over time is a process question and L3 territory, which you scoped out | |
| D "Is there anyone who would notice if it moved?" | **Drop** | Implies a control failure or concealment; leading; raises professional risk for the participant | |
| E "When you review work you know was AI-assisted, does anything change in how you review it?" | **Drop** (or use only if their episode was as reviewer) | A different phenomenon: someone else's AI-assisted work, not a tool confirming your own judgment | |
| E "Would you be able to tell?" | **Drop** | Closed capability question | |
| Closing "Is there anything I should have asked and didn't?" | **Keep** | | |
| Closing "Is there anything you've said that you'd want me to leave out?" | **Keep** | Good ethics practice | |
| *(new, closing)* | **Add** | Records exposure to your argument without priming during the interview | "Before we finish: have you seen anything I've written or posted about this topic?" Note the answer in the private log |

Removing B3, D2, D3, E1 and E2 frees roughly 15 minutes. Spend them on Section A and on one contrast
episode; that is where the textural description comes from.

### 4.2 Probes for the remembered episode

Add these to the five-probe table. All stay inside the one occasion:

- "Where were you in the engagement: planning, fieldwork, wrap-up, a deadline?"
- "What were you looking at when the result came up?"
- "Just before you saw it, what was on your mind?"
- "What did you say to yourself, if anything, in the moment?"
- "What did you do in the next few minutes?"
- "Was anyone else involved or nearby?"
- "Is that how it seemed then, or how it looks to you now?" (separates the lived moment from later sense-making, which your RQ treats as part of the experience but which should be distinguishable in the data)
- "Walk me through it as if I'd never seen an audit file." (counters insider shorthand: "you know how it is")
- "You said [their word]. What was [their word] like?"
- "Was there ever a time it went differently?" (opens the contrast episode)

### 4.3 Leading or priming wording to remove everywhere

- **Never use with participants, in recruitment messages, the consent form, the study title or the
  interview:** bias, sycophancy, automation bias, anchoring, confirmation bias, complacency,
  over-reliance, deference, "permission to stop".
- **Use only after the participant does:** rely, trust, check, skeptical, evidence, agree, confirm.
- **Consent-form title:** the proposal title "When the Machine Agrees" is fine for the paper but frames
  the answer for a participant. A neutral working title for IRB materials, for example "Auditors'
  experiences with AI-generated conclusions", describes the purpose accurately without supplying the
  meaning. Ask the IRB whether this level of description counts as full disclosure; it should, since it
  is accurate and general, but they decide.
- **Your public footprint.** This repository, the public site and your LinkedIn posts state the
  argument. Participants come from that network. Consider pausing public posts on the L2 argument
  while interviews run, and record each participant's exposure (closing question above).
- **The hazard log can itself shape questions.** When an entry leads you to reword a probe, version
  the guide and note which participants had which version.

---

## 5 · Sample adequacy

### 5.1 Why "saturation" is a contested stopping rule here

Saturation comes from grounded theory, where it is tied to theoretical sampling and to a developing
theory's categories. Transplanted to other designs it usually becomes code saturation: no new codes
appear. Guest, Bunce & Johnson (2006) found that in 60 interviews from two West African countries most
themes appeared within the first twelve and the elements of metathemes by six, but in a fairly
homogeneous sample with a structured guide and codebook thematic analysis. Hennink & Kaiser's (2022)
systematic review of empirical saturation tests reports saturation within roughly 9 to 17 interviews,
mostly with homogeneous populations and narrow objectives (figures checked only through secondary
summaries; confirm against the article). Braun & Clarke (2021) argue that saturation fits
coding-reliability approaches, not interpretive ones, and that sample-size judgments are partly made in
the analysis, not fixed beforehand.

For phenomenology the problem is sharper. The aim is a sufficiently rich description of a shared
structure, not exhaustion of codes. Every account adds *some* variation, so "nothing new" is never
strictly true, and "no new meaning unit for three interviews" measures the researcher's coding habits
as much as the data. That is why Dr. Gonzalez asked you not to position saturation as an automatic
rule. Malterud, Siersma & Guassora (2016) offer a rationale that fits: **information power**, where a
sample holding more information relevant to the aim needs fewer participants, judged on five
dimensions (aim, sample specificity, use of established theory, quality of dialogue, analysis
strategy), assessed at planning and revisited during data collection.

Your "three consecutive interviews" guide can stay as **one piece of evidence** in the decision, as
your 1 Oct revision already says. Remove it from the places listed in §2 item 6 where it still reads as
the rule.

### 5.2 Draft paragraph

> **DRAFT for Yasir to rewrite in his own words. Not for submission as written.**
>
> The study plans 10 to 15 participants. The number is justified by information power (Malterud,
> Siersma, & Guassora, 2016) rather than by saturation, which originates in grounded theory and fits a
> phenomenological aim poorly. Three of the five dimensions favour a smaller sample. The aim is narrow:
> one bounded moment, the receipt of an AI-generated conclusion matching a judgment already formed. The
> sample is dense in specificity, because every participant must recall a specific occasion of that
> moment, not merely use AI tools. The interviews are expected to carry strong dialogue, because the
> interviewer shares the participants' professional language. Two dimensions pull the other way. The
> analysis does not apply an established theory; existing theory is bracketed. And the analysis is
> cross-case, seeking a structure that holds across deliberately varied settings (internal and
> external audit, firm size, seniority, industry), which requires enough accounts from each setting to
> see what is invariant. On balance a moderate sample is indicated, consistent with the 10 to 15 range.
> The final number will be decided by whether the accounts are rich enough to support individual and
> composite textural and structural descriptions. That judgment, its reasons, and the external
> reviewer's view will be recorded on the day it is made.

Check the 5th-edition Creswell & Poth chapter on data collection for any range they give for
phenomenology and cite it only from your own copy.

### 5.3 Recording the stopping decision

Use one entry per decision point (after interview 10, then after each later one). Keep the full entry
in the **private** analytic log; post only the dated decision and reason, with no participant content,
in the public `AUDIT_TRAIL.md`.

| Field | Content |
|---|---|
| Date, interviews completed | e.g. "after P10" |
| Information power re-rated | Each of the five dimensions: as planned, or changed, and why (e.g. dialogue quality weaker than expected in two interviews) |
| Variation achieved vs planned | Settings, seniority, external vs internal; any setting with too few accounts |
| Richness check | For each emerging textural theme: is it described from at least one detailed episode, with context, from more than one setting? Which themes are thin? |
| New meaning in recent interviews | The "three consecutive" evidence, stated as evidence, not as the rule |
| Disconfirming material | Any account that does not fit; whether more such accounts are needed |
| Reviewer's view | Date, what they reviewed, agree or disagree, and why |
| Decision and reason | Stop or continue, in your words |

Set the IRB-approved maximum to cover screen-outs and withdrawals (for example up to 15 interviews,
with screening contacts counted separately), and replace "above 15, report why saturation did not
arrive" with "at the approved maximum, stop and report the sufficiency judgment and any thin themes as
a limitation".

---

## 6 · Trustworthiness and researcher position

### 6.1 What the confirmation hazard log should capture

Keep it, as both reviewers advised, and move it out of the public repository. Suggested fields:

| Field | Note |
|---|---|
| Entry ID, date, time relative to interview | During, same day, at transcription, during analysis |
| Participant pseudonym and transcript locator | Private log only |
| What was said | Private log only. Never in the public trail |
| What I felt confirmed about | Which part of the chain or which expectation, in a sentence |
| Was a leading or researcher-introduced question just before it? | Links to the `LEADING` flag |
| What I did about it | Returned to transcript for contradicting material; flagged unit for reviewer; reworded a probe (record guide version); nothing, with reason |
| What happened later | Did the related meaning unit survive clustering? Did the reviewer read it differently? |
| Cross-reference | The analytic decision it affected |

**Add the mirror entry.** Log moments of feeling *disconfirmed*, surprised or irritated by an account
as well. The reaction to disconfirmation (discounting, probing harder, explaining it away) shapes
analysis just as much, and logging only confirmation makes the log one-sided by design.

**The public trail** keeps a one-line, content-free record: "2026-xx-xx · HAZARD · entry H-07 logged
privately; action: unit flagged for reviewer". That preserves the timestamped evidence that the log
existed and changed decisions, which is its value to confirmability, without exposing participants.

### 6.2 Bracketing versus reflexivity

Moustakas's epoché aims at setting aside prior judgments so the phenomenon can be seen freshly.
Reflexivity, from constructivist and hermeneutic traditions, assumes prior understanding cannot be set
aside and instead makes it visible and accountable. The literature disagrees about what bracketing is,
who does it, and when (Tufford & Newman, 2012), and insider researchers occupy a space between insider
and outsider rather than one pole (Dwyer & Buckle, 2009).

Your protocol already leans reflexive ("not having no views, which is not achievable"), while claiming
a transcendental essence. That is workable if said out loud: epoché as a practice attempted before each
interview and each analysis step, with reflexive procedures as the evidence of how far it succeeded.
The hazard log fits this framing well, because it records the moments epoché failed and what was done.

Two insider-specific risks worth naming in the proposal:

- **Shared shorthand.** Participants who know you will under-describe ("you know how it is"). The
  "as if I'd never seen an audit file" probe addresses this.
- **Social desirability toward a known senior figure.** Former colleagues may present careful
  practice to you specifically. The external reviewer should be asked to look for this, and the
  limitation should be stated.

---

## 7 · IRB modification checklist

**Before drafting**
- [ ] Confirm with Dr. Rey that this arm will be fielded, under whose supervision, and its relation to
      the dissertation (see §2 item 9)
- [ ] Ask the FIU IRB office: modification to IRB-25-0462 or new protocol (already an open item)
- [ ] Ask whether the screening-question pre-test with non-participants needs approval before it runs
- [ ] Confirm human-subjects training is current for you and anyone who will see data
- [ ] Settle one RQ, one population definition (internal, external or both; years) and update the
      protocol and proposal to match
- [ ] Decide compensation (`SAMPLING_AND_RECRUITMENT.md` §6)

**Recruitment**
- [ ] Recruitment messages and referral script attached, in neutral language (§4.3 word list)
- [ ] Exclusion or disclosure rule for: current or former direct reports; anyone who used or was
      affected by an AI tool you built or oversaw; anyone you currently supervise or are being hired by
- [ ] Two-per-firm cap stated; no recruitment through employer channels
- [ ] Conflict-of-interest statement: prior employment, authorship of an AI review tool at Citi, public
      writing on the topic

**Consent**
- [ ] Purpose stated accurately and generally, without the study's theoretical vocabulary
- [ ] Procedures: one interview of about 60 minutes, video call, audio recording, optional member check
- [ ] Risks: professional and reputational exposure; breach of confidentiality
- [ ] Accurate confidentiality language, including its limits (replace "nothing identifies you")
- [ ] Explicit instruction not to disclose client names, nonpublic client or employer information, or
      confidential supervisory information; interviewer will redirect
- [ ] Right to skip, stop, and withdraw passages after member check, with the date after which
      withdrawal is no longer possible (once analysis is aggregated)
- [ ] Consent to de-identified quotation in the dissertation and publications, as a separate choice
      (consider Kaiser's (2009) post-interview check of how each participant wants material used)
- [ ] If consent is verbal: request a waiver of documentation of consent; 45 CFR 46.117(c)(1)(i) fits
      where the consent form would be the only link to the participant and the main risk is a
      confidentiality breach; give an information sheet in advance
- [ ] Separate, recorded consent to audio recording at the start of the recording (Florida treats
      recording of a private conversation as all-party consent, Fla. Stat. § 934.03; participants in
      other states make explicit consent the safe default)
- [ ] Debrief offer: a short plain summary at study end

**Data handling**
- [ ] Video platform named; cloud recording, automatic transcripts and built-in AI assistants **off**
      unless approved; audio-only recording; camera optional
- [ ] Transcription method named: manual, an FIU-approved service, or an offline tool; **no public AI
      platform** (FIU UGS §9; check FIU's prohibited-technologies list)
- [ ] Storage: encrypted, FIU-approved location `[VERIFY with FIU IT/IRB]`; linking key stored
      separately
- [ ] Retention and destruction dates checked against FIU IRB requirements before promising "delete
      after member check" or "destroy key at close"
- [ ] **Nothing about participants in this public repository**: split `AUDIT_TRAIL.md` into a public
      design log and a private analytic log (hazard entries, screening decisions, leading flags,
      stopping evidence); drop the plan to commit quotable extracts until publication
- [ ] Setting descriptions reported at aggregate level; no per-participant table combining firm type,
      seniority, industry and tool
- [ ] Member-check documents sent through FIU email or another approved secure channel
- [ ] External reviewer: sees de-identified material only; confidentiality agreement; ask whether
      they must be named on the protocol
- [ ] Plan for incidental disclosures of possible misconduct: redirect, do not transcribe the detail;
      describe the plan to the IRB

**AI use**
- [ ] List every AI use that touches participant data (ideally only an approved transcription tool,
      or none)
- [ ] Narrow `CODING_PLAN.md`: the "adversary" role runs on your memos and de-identified cluster
      labels only, never on transcripts; "format, reorder and tabulate" done locally without AI, or
      dropped
- [ ] NVivo AI features off and stated
- [ ] Committee review and approval of AI use obtained and recorded (UGS §3.2, §5.1) before data
      collection; disclosure drafted for the preliminary pages and the Methods section

---

## 8 · References verified for this critique

Verified on 20 Oct 2026 by web search for bibliographic details and, where noted, the claim used.
Page numbers inside books were **not** verified, and none are given.

- Braun, V., & Clarke, V. (2021). To saturate or not to saturate? Questioning data saturation as a
  useful concept for thematic analysis and sample-size rationales. *Qualitative Research in Sport,
  Exercise and Health, 13*(2), 201 to 216. https://doi.org/10.1080/2159676X.2019.1704846
- Creswell, J. W., & Poth, C. N. (2024). *Qualitative inquiry and research design: Choosing among five
  approaches* (5th ed.). SAGE. *SAGE lists January 2024; some library catalogs record 2025. Chapter
  numbers not verified: check your copy.*
- Dwyer, S. C., & Buckle, J. L. (2009). The space between: On being an insider-outsider in qualitative
  research. *International Journal of Qualitative Methods, 8*(1), 54 to 63.
  https://doi.org/10.1177/160940690900800105
- Flanagan, J. C. (1954). The critical incident technique. *Psychological Bulletin, 51*(4), 327 to 358.
  https://doi.org/10.1037/h0061470
- Flick, U. (2000). Episodic interviewing. In M. W. Bauer & G. Gaskell (Eds.), *Qualitative
  researching with text, image and sound: A practical handbook*. SAGE. *Chapter pages not verified.*
- Guest, G., Bunce, A., & Johnson, L. (2006). How many interviews are enough? An experiment with data
  saturation and variability. *Field Methods, 18*(1), 59 to 82. https://doi.org/10.1177/1525822X05279903
- Hennink, M., & Kaiser, B. N. (2022). Sample sizes for saturation in qualitative research: A
  systematic review of empirical tests. *Social Science & Medicine, 292*, 114523. *Details and the 9 to
  17 interview finding confirmed only through secondary summaries; read the article before citing.*
- Kaiser, K. (2009). Protecting respondent confidentiality in qualitative research. *Qualitative Health
  Research, 19*(11), 1632 to 1641. https://doi.org/10.1177/1049732309350879
- Malterud, K., Siersma, V. D., & Guassora, A. D. (2016). Sample size in qualitative interview studies:
  Guided by information power. *Qualitative Health Research, 26*(13), 1753 to 1760.
  https://doi.org/10.1177/1049732315617444
- Moustakas, C. (1994). *Phenomenological research methods*. SAGE. *Contents include a chapter on
  epoché, phenomenological reduction, imaginative variation and synthesis. The list of structural
  lenses in §3 is flagged `[VERIFY]` against that chapter.*
- Smith, J. A., Flowers, P., & Larkin, M. (2022). *Interpretative phenomenological analysis: Theory,
  method and research* (2nd ed.). SAGE. *Some sources date it 2021.*
- Tufford, L., & Newman, P. (2012). Bracketing in qualitative research. *Qualitative Social Work,
  11*(1), 80 to 96. *Article confirmed (online first 2010, doi 10.1177/1473325010368316); print volume
  and pages not confirmed.*
- van Manen, M. (1990). *Researching lived experience: Human science for an action sensitive
  pedagogy*. State University of New York Press.
- U.S. Department of Health and Human Services. Protection of Human Subjects, 45 C.F.R. § 46.117(c)
  (waiver of documentation of informed consent, 2018 requirements).
- Fla. Stat. § 934.03 (interception and disclosure of wire, oral or electronic communications).
  *General information only; confirm current text and its application with the FIU IRB.*

**Cited in your files, not re-verified here:** Creswell & Miller (2000); Lincoln & Guba (1985);
Gioia & Chittipeddi (1991).
