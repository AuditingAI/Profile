"""Appendix slides for the GEB 7911 proposal poster: three slides, labelled as not presented.

Content comes from the author's protocol files in dba/QUALITATIVE/ (INTERVIEW_GUIDE, SAMPLING_AND_
RECRUITMENT, CODING_PLAN, TRUSTWORTHINESS). Layout only is new. Used by build_proposal_poster.py --appendix.
"""
from pptx_shim import rgb, W, H, DISP, DISPI, BODY, MONO, MONOB

BLUE=rgb("#081E3F"); GOLD=rgb("#B6862C"); INK=rgb("#14171C"); PAPER=rgb("#FCFBF8")
MUTE=rgb("#767D86"); RULE=rgb("#D8D4CB"); SOFT=rgb("#E8EDF4"); WARM=rgb("#FAF3E4")
WHITE=rgb("#FFFFFF"); BODYC=rgb("#3A4048"); TEAL=rgb("#1C6B63"); RUST=rgb("#8C3A1B"); AMBER=rgb("#8A6A1F"); DKTXT=rgb("#B9C7D8")
M = 34

def _head(d, letter, title, sub):
    d.page(PAPER)
    d.box(0, 0, W, 62, fill=BLUE)
    d.txt(f"APPENDIX {letter}  ·  NOT PRESENTED  ·  SUBMITTED FOR FEEDBACK", M, 12, MONOB, 7.5, GOLD, track=1.4)
    d.txt(title, M, 24, DISP, 21, WHITE)
    d.txt("Receiving Confirmation  ·  Yasir A. Malik  ·  GEB 7911", W - M, 14, BODY, 8.5, DKTXT, align="r")
    d.txt(sub, M, 72, DISPI, 11, BODYC)

def _col(d, x, t, w, head, items, size=11.2):
    d.txt(head, x, t, MONOB, 8.2, BLUE, track=1.1)
    d.rule(t + 12, x=x, w=w, color=GOLD, lw=1.2)
    y = t + 22
    for it in items:
        if it.startswith("**") and "**" in it[2:]:
            lead, rest = it[2:].split("**", 1)
            y += d.para(lead.strip(), x, y, w, DISP, size, INK, lead=size * 1.28) + 1
            rest = rest.strip().lstrip(",;: ").strip()
            if rest:
                y += d.para(rest, x, y, w, BODY, size - 0.6, BODYC, lead=(size - 0.6) * 1.3)
        else:
            y += d.para(it, x, y, w, BODY, size - 0.6, BODYC, lead=(size - 0.6) * 1.3)
        y += 7
    return y

def _foot(d, s):
    d.rule(H - 26, x=M, w=W - 2 * M, color=RULE)
    d.txt(s, M, H - 19, BODY, 6.8, MUTE)

def add(d):
    cw = (W - 2 * M - 2 * 16) / 3
    xs = [M, M + cw + 16, M + 2 * (cw + 16)]

    # ---- A · who and how ------------------------------------------------------------
    _head(d, "A", "Sampling and the interview", "Every participant must have lived the phenomenon, not merely hold views about it.")
    _col(d, xs[0], 94, cw, "ELIGIBILITY · ALL FOUR", [
        "**1. Five or more years** in audit, internal audit or risk assurance",
        "**2. Recurring or multi-year engagements**, where prior-period work is the anchoring context",
        "**3. Uses or has used AI or analytics tools** that produce conclusions, findings or risk ratings",
        "**4. Can recall a specific occasion** when such a tool reached a conclusion they had already reached",
        "Criterion 4 is the study. A candidate who meets 1 to 3 and fails 4 has not lived the phenomenon, and their data would be opinion.",
        "**Maximum variation within the criterion:** Big Four, mid-tier and in-house internal audit; external and internal; senior associate to partner or CAE; several industries."])
    _col(d, xs[1], 94, cw, "HOW MANY, AND WHEN TO STOP", [
        "**Criterion sample of 10 to 15.** Saturation is a stopping rule, not a target.",
        "Stop after three consecutive interviews that add no new surviving meaning unit.",
        "Below 10, do not stop regardless of apparent saturation. Above 15, stop and report why saturation did not arrive, which is itself a finding.",
        "**Pilot first.** The protocol is piloted, and pilot testers cannot become participants.",
        "**Channel:** professional networks, association chapters and referral chains, not general research panels, which held about 6 eligible auditors per 100,000 in the author's prior study."])
    _col(d, xs[2], 94, cw, "THE INTERVIEW · 60 MINUTES", [
        "**Q1 (textural):** What have you experienced when an AI tool reached the same conclusion you had already reached?",
        "**Q2 (structural):** What situations or circumstances have typically influenced how you experienced that?",
        "**Grounding move:** before anything else, the participant silently recalls one specific occasion. If none comes, the screen failed and the interview ends courteously.",
        "Body: the occasion (20 min) · prior-year conclusion versus AI answer (10) · confirmation as evidence (10) · when to stop looking (8) · under review (5).",
        "**Never asked:** \"Why did you...?\" (produces a defence) · \"Would you say you were anchored?\" (supplies the construct)."])
    _foot(d, "Source: the author's protocol files, dba/QUALITATIVE/INTERVIEW_GUIDE.md and SAMPLING_AND_RECRUITMENT.md. Nothing has been fielded; zero participants; IRB modification not yet submitted.")

    # ---- B · analysis ------------------------------------------------------------------
    _head(d, "B", "Data analysis", "Creswell and Poth's five analysis activities, carried out through Moustakas-style phenomenological steps in NVivo.")
    _col(d, xs[0], 94, cw, "THE FIVE ACTIVITIES", [
        "**1. Managing and organising the data.** Verbatim transcripts, pseudonyms at transcription, encrypted storage, one NVivo project.",
        "**2. Reading and memoing.** A reflexive memo before each listen-back, and emergent ideas memoed from the first transcript.",
        "**3. Describing and classifying codes into themes.** Horizontalisation, then meaning units, then clusters.",
        "**4. Developing and assessing interpretations.** A mandatory disconfirming pass before anything is written up.",
        "**5. Representing the data.** Textural, structural and composite descriptions, quoting rather than paraphrasing."])
    _col(d, xs[1], 94, cw, "THE PHENOMENOLOGICAL STEPS", [
        "**Epoché first.** Four written commitments, including the author's stake in the answer, set down before the first interview.",
        "**Horizontalisation.** Every significant statement listed, each given equal weight.",
        "**Meaning units and themes.** Statements reduced to non-overlapping units, then clustered.",
        "**Textural (what) and structural (how, in what context) descriptions,** for each participant and then across all of them.",
        "**Composite essence.** Two rules: no causal language, and no frequency claims such as \"most participants\"."])
    _col(d, xs[2], 94, cw, "THE AI BOUNDARY", [
        "**AI may:** transcribe audio · format and tabulate what the author has already coded · check prose for clarity and grammar · act as an adversary (\"what have I missed?\") · find literature.",
        "**AI may not:** assign a code or meaning unit · name a theme · write any part of a description · decide what a participant meant · decide when saturation is reached.",
        "**Why the line sits here:** the study examines what happens when a machine reaches a conclusion first and a human agrees with it. Letting a model propose themes and then agreeing with them would reproduce the phenomenon inside its own analysis.",
        "Every AI use is logged with date, tool, request and outcome (FIU Graduate School AI policy; GEB 7911 limits)."])
    _foot(d, "Source: dba/QUALITATIVE/CODING_PLAN.md. The analysis plan follows the course's prescribed activities rather than a self-invented procedure, as asked in Week 6.")

    # ---- C · validation, and the questions for feedback ------------------------------------
    _head(d, "C", "Validation, and where feedback would help most", "Chapter 10: at least two strategies, drawn from more than one lens. This design uses seven.")
    _col(d, xs[0], 94, cw, "THE RESEARCHER'S LENS", [
        "**Reflexivity and the confirmation hazard log.** The author is a career auditor who built an AI review tool: insider access and insider bias at once. Every moment of feeling confirmed by a participant's account is logged, because that is the study's own phenomenon happening to the researcher.",
        "**Negative case analysis.** Actively seek auditors who distrusted or overrode the AI's agreement.",
        "**Outsider review.** Every third transcript read cold by a second person asking \"where is the researcher in this data?\""])
    _col(d, xs[1], 94, cw, "THE PARTICIPANT'S AND THE READER'S LENS", [
        "**Member checking.** Each participant receives their own textural description, not the raw transcript, and is asked what is wrong or missing.",
        "**Thick description.** Firm type, function, engagement, tool category and the moment of agreement, so a reader can judge transfer.",
        "**Audit trail.** Protocol written before data collection, an append-only decision log, dated codebook versions and the hazard log: the study's own workpapers.",
        "**Falsification conditions** stated in advance of any participant."])
    y = 94
    d.box(xs[2] - 6, y - 8, cw + 12, 408, fill=WARM, stroke=GOLD, r=3)
    _col(d, xs[2], y, cw, "QUESTIONS FOR DR. GONZALEZ", [
        "**1. Is criterion 4 too narrow?** Requiring a recalled occasion of AI agreement may make 10 participants hard to reach. Would you keep it strict, or allow a closely related occasion?",
        "**2. Member checking on the textural description** rather than the transcript: acceptable for this proposal, or should the transcript also go back to participants?",
        "**3. One outsider reviewer** reading every third transcript: enough, given how close the author is to the phenomenon?",
        "**4. Is the AI boundary drawn in the right place** for the course's 25% limit and labelling rule?"])
    _foot(d, "Source: dba/QUALITATIVE/TRUSTWORTHINESS.md; Creswell and Poth, Chapter 10. Slides prepared with AI assistance for layout and organisation; the design and every decision in it are the author's.")
