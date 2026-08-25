# 📓 NotebookLM Playbook — DBA Paper Material Extraction

**Who this is for:** Yasir — for working through Dr. Ray's "find more sources, summarize, identify gaps" assignment using NotebookLM, without losing focus.

**ADD-first design rules of this doc:**
- Every step has a ⏱ time estimate
- Every step has a single **action verb** at the top
- Every step has a **"You're done when…"** finish line
- Copy-paste prompts are in code blocks — just click → paste → send
- Skip-ahead links at the top so you don't get lost
- One screen per step. If a step feels long, it's split.

**Estimated total time first pass:** 60–90 minutes to set up + 15–20 minutes per construct after that.

---

## 🎯 What you'll get out of this

By the end of Phase 1 (Setup), you'll have a NotebookLM workspace that contains all 47 verified sources from your paper plus any new PDFs you add. By the end of Phase 2 (Extract), you'll have copy-paste-ready paragraphs of grounded, cited content for every construct in Chapter 2. By the end of Phase 3 (Study), you'll have an audio "Deep Dive" podcast of your own paper that you can listen to on a walk to internalize it.

**Why NotebookLM (not ChatGPT/Claude) for this:**
- NotebookLM **only answers from sources you upload** — it cannot invent fake citations. This is exactly what Dr. Ray demanded.
- Every response shows the **exact passage** it came from, so verification is one click.
- It has free **Audio Overview** that generates a podcast about your sources — gold for ADD-friendly studying.

---

## 🗺️ Skip ahead

- [Phase 1 — Set up the notebook (one-time, ~30 min)](#phase-1--set-up-the-notebook-one-time-30-min)
- [Phase 2 — Extract more material per construct (~20 min each)](#phase-2--extract-more-material-per-construct-20-min-each)
- [Phase 3 — Study what you have (the ADD gold)](#phase-3--study-what-you-have-the-add-gold)
- [Prompt library (every prompt, copy-paste)](#prompt-library)
- [Troubleshooting](#troubleshooting)

---

## Phase 1 — Set up the notebook (one-time, ~30 min)

### Step 1.1 — **Open** NotebookLM ⏱ 1 min

1. Go to **https://notebooklm.google.com**
2. Sign in with your **yasiramalik@gmail.com** account
3. Click **"+ Create new"** (top-left)
4. Name the notebook: **`DBA — Anchoring Bias Paper`**

✅ **You're done when** you see an empty notebook with a "Sources" panel on the left.

---

### Step 1.2 — **Upload** your own paper as the anchor source ⏱ 2 min

1. In the **Sources** panel (left), click **"+ Add"**
2. Choose **"Upload"**
3. Select **`Research_Paper_YMalik_v4.docx`** from your computer
   - Don't have it? Download from: https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_v4.docx (click *Download raw file*)
4. Wait for the green checkmark (~20 seconds)

✅ **You're done when** the file appears in the Sources panel with a checkbox next to it.

> 💡 **Why this matters:** Your own paper becomes a source. Now NotebookLM can answer questions like *"What does my paper claim about RA?"* and you can compare new findings to your current text.

---

### Step 1.3 — **Add** the 5 most important anchor papers as PDFs ⏱ 15 min

Grab the PDFs of these five papers (one Scholar click each), then upload all five to NotebookLM. **These are the canonical foundations your committee will expect to see grounded in the actual text.**

| # | Paper | Why this one | Scholar search to paste |
|---|---|---|---|
| 1 | **Tversky & Kahneman (1974)** *Science* — Judgment under uncertainty | The origin of anchoring | `Tversky Kahneman 1974 judgment under uncertainty heuristics biases` |
| 2 | **Joyce & Biddle (1981)** *JAR* — Anchoring in auditing | First anchoring-in-audit experiments | `Joyce Biddle 1981 anchoring adjustment probabilistic inference auditing` |
| 3 | **Kinney & Uecker (1982)** *TAR* — Mitigating anchoring | Most-cited audit-anchoring study | `Kinney Uecker 1982 mitigating consequences anchoring auditor judgments` |
| 4 | **Nelson (2009)** *AJPT* — Professional skepticism review | The skepticism map your model sits in | `Nelson 2009 model literature review professional skepticism auditing` |
| 5 | **Francis (2011)** *AJPT* — Audit-quality framework | The framework that justifies your two mediators | `Francis 2011 framework understanding researching audit quality` |

**How to grab each PDF (the routine for all 5):**

1. Open https://scholar.google.com
2. Paste the search string from the table above
3. Click the first result
4. Look for the **`[PDF]`** link on the right side of the result, OR click the title and look for a "Download PDF" link
5. If no PDF: check **FIU library** (https://library.fiu.edu) → it has full-text access to AJPT, TAR, JAR, etc.
6. Drag each PDF into NotebookLM's **Sources** panel

✅ **You're done when** all 5 papers show green checkmarks in the Sources panel (6 sources total counting your own paper).

> 💡 **ADD tip:** Don't try to read these. You're just uploading them. NotebookLM will read them for you.

---

### Step 1.4 — **Verify** the notebook works ⏱ 2 min

In the chat box at the bottom of NotebookLM, paste this and hit Enter:

```
List every source currently in this notebook, one per line, in the format:
"[number]. Author (Year) — short title"
```

✅ **You're done when** you see a numbered list of 6 sources. If anything is missing, re-upload it.

---

### Step 1.5 — **Generate** the first study tool: Audio Overview ⏱ 5 min (mostly waiting)

This is the ADD-superpower step.

1. In the right-hand panel, find **"Audio Overview"** (sometimes labeled "Deep Dive Conversation")
2. Click **"Customize"** (don't just click Generate yet)
3. Paste this customization prompt:

```
Focus on anchoring bias in long-term auditor engagements. Explain to a doctoral
student preparing a research proposal: (a) what anchoring bias is, (b) why it
matters specifically for auditors who return year after year to the same client,
(c) the eleven-construct model in Yasir Malik's paper, and (d) what gaps remain
in the literature that this study addresses. Keep it conversational and around
15-20 minutes. Pretend the listener has ADD — keep the energy up, signpost
clearly, and recap key points twice.
```

4. Click **Generate**
5. **Walk away.** It takes 5–10 minutes. Come back when your phone dings.

✅ **You're done when** you see a play button and can listen to a ~15-min podcast about your own paper.

> 💡 **Why this is the ADD gold:** Listen to it on a walk tomorrow morning. Your committee meeting prep just became cardio.

---

## Phase 2 — Extract more material per construct (~20 min each)

Repeat this loop for each of the 11 constructs in your paper. **You do NOT have to do all 11 today** — pick the two you feel weakest on and start there.

### The loop (memorize this — it's the whole game)

> **Search → Upload → Ask → Paste**
>
> 1. **Search** Scholar for 2-3 new papers on the construct (10 min)
> 2. **Upload** their PDFs to NotebookLM (2 min)
> 3. **Ask** NotebookLM the 4-prompt set below (5 min)
> 4. **Paste** the answers into the right section of your markdown master (3 min)

---

### Step 2.1 — **Search** Scholar for new sources ⏱ 10 min

Pick a construct (e.g., **Training & Awareness — TA**). Open the **"Optional further reading"** box for that construct in your paper to see what I already suggested. Then in Google Scholar, run **2 of these searches** (not all — just 2):

```
"bias training" auditors effectiveness experiment

"debiasing" training "decision making" transfer durability

professional skepticism training intervention audit
```

For each search:
1. Sort by **"Cited by"** (high to low) — find papers cited ≥50 times
2. Pick the **top 2** that look most relevant to *your* construct definition
3. Click the **[PDF]** link or use the FIU library to download

**Target:** 2–4 PDFs per construct.

✅ **You're done when** you have 2-4 new PDFs saved on your computer.

> 💡 **ADD tip:** Set a 10-min timer. When it goes off, stop searching even if you found "only" 2 papers. 2 good ones beats 8 vague ones.

---

### Step 2.2 — **Upload** to NotebookLM ⏱ 2 min

1. Drag the new PDFs into the NotebookLM Sources panel
2. Wait for green checkmarks
3. Take a screenshot of the Sources panel so you have a record of what's in there

✅ **You're done when** the new PDFs show green checkmarks.

---

### Step 2.3 — **Ask** NotebookLM the 4-prompt set ⏱ 5 min

These four prompts are **tested** to give you copy-paste-ready paragraphs in the academic voice your paper is already written in. **Run them one at a time, in order.** Wait for each answer before sending the next.

#### Prompt A — Define and summarize each new source

```
For each of the new sources I just added (NOT my own paper, NOT the 5 anchor
papers from before), give me ONE academic paragraph in this exact format:

"Author (Year), in [Journal Name], [verb: showed/demonstrated/argued/found]
that [main finding]. The study [method in one clause]. The implication for
[Training & Awareness as a debiasing intervention in long-term auditor
engagements] is [implication in one clause]."

Replace [Training & Awareness ...] with whichever construct I'm working on
when I tell you. Do NOT invent details — if a paper doesn't report a method,
say so. Do NOT include sources I didn't just add.
```

✅ **You should get back** a paragraph per new paper, in the exact voice of your existing Ch.2.

---

#### Prompt B — Find contradictions and gaps

```
Across ALL sources in this notebook (including my own paper and the 5 anchor
papers), what does the literature DISAGREE about regarding [Training & Awareness]?
Be specific:
- Where do authors contradict each other?
- Where does evidence point in opposite directions?
- What does the literature NOT address that a critical reader would ask?

Format the answer as 3-5 bullets, each starting with "Contradiction:" or "Gap:".
Cite which source(s) each bullet draws on, in (Author, Year) format.
```

✅ **You should get back** 3-5 bullets, each tagged Contradiction or Gap with source citations. **This is exactly what Dr. Ray meant by "give me your critical voice."**

---

#### Prompt C — Write the synthesis paragraph

```
Write a 120-150 word paragraph I can paste directly into the section of my
paper on [Training & Awareness]. Requirements:
- Integrate AT LEAST 2 of the new sources I just added
- Reference at least 1 contradiction from the previous answer
- End with a sentence that takes a defensible position (e.g., "The defensible
  reading of the literature is that...")
- Use the in-text citation style (Author, Year)
- Match this voice: academic but not stiff, declarative, no hedging fluff

Do NOT use sources outside this notebook. Do NOT use phrases like "in conclusion"
or "in summary." Start with a substantive sentence, not a meta-sentence.
```

✅ **You should get back** a paragraph that drops directly into your paper. **Read it once. If it's accurate, paste it.** If not, run Prompt C again with a tweak.

---

#### Prompt D — Generate the new reference-list entries

```
For each of the new sources I just added, give me a formatted APA reference
list entry in this exact style:

Author, A. B., & Author, C. D. (Year). Title of the article. *Journal Name,
Volume*(Issue), pages.

Use italics ONLY for the journal name and volume. Use the en-dash for page
ranges. Do NOT include DOIs. Do NOT include URLs. If you do not know a field
(e.g., exact pages), write [page range unconfirmed] rather than inventing one.
```

✅ **You should get back** clean APA entries to add to your Verified Reference Pool. **If you see `[page range unconfirmed]`, go back to the PDF's first page and find the page numbers yourself — don't push unverified info into the paper.**

---

### Step 2.4 — **Paste** into your paper ⏱ 3 min

1. Open `Research_Paper_YMalik_v4_master.md` in any text editor (VS Code, Notepad, even Google Docs)
2. Find the section for the construct you just worked on (e.g., **"## 2.4  Training & Awareness (TA)"**)
3. Paste the synthesis paragraph from **Prompt C** at the end of the construct's narrative (just before the "Optional further reading" box)
4. Scroll to the bottom — **Verified Reference Pool** — and paste the new entries from **Prompt D** alphabetically
5. **Save the file**

✅ **You're done when** the file is saved and the new content is in two places: the construct section AND the reference pool.

> 💡 **Don't worry about regenerating the .docx today.** Edit the markdown master through all 11 constructs first, then regenerate the .docx once at the end. (Or ask me to do it.)

---

### Step 2.5 — **Repeat** for the next construct ⏱ start a new 20-min timer

Mark the construct you just did with a ✅ on this list. **Two per session is plenty.**

- [ ] 2.4 Training & Awareness (TA)
- [ ] 2.5 Rotation of Auditors (RA)
- [ ] 2.6 Use of Analytical Tools (AT)
- [ ] 2.7 Structured Auditing Processes (SAP)
- [ ] 2.8 Feedback & Reflection (FR)
- [ ] 2.9 Independent Reviews (IR)
- [ ] 2.10 Regulatory & Professional Guidance (RPG)
- [ ] 2.11 Performance Metrics & Incentives (PMI)
- [ ] 2.12 Auditor Judgment Quality (AJQ)
- [ ] 2.13 Audit Process Rigor (APR)
- [ ] 2.3 Reduction in Anchoring Bias (RAB)

---

## Phase 3 — Study what you have (the ADD gold)

You don't *only* need to **write** the paper. You need to **own** it well enough to defend it in a committee meeting. NotebookLM has features built for exactly that.

### Tool 1 — **Study Guide** (auto-generated flashcards & key terms)

In NotebookLM's right-hand panel, click **"Study Guide"** → **Generate**.

You'll get:
- Key terms & definitions
- Short-answer quiz questions
- An essay-question prompt

**ADD use:** Print it. Stick it on the wall. Quiz yourself once a day for 5 minutes.

---

### Tool 2 — **Mind Map** (visualize the whole literature)

Click **"Mind Map"** → **Generate**.

NotebookLM will produce a clickable, expandable mind map of every concept in your sources. Click any node to expand it.

**ADD use:** This is what to screen-share when your brain freezes in the committee meeting. You can navigate the literature visually instead of from memory.

---

### Tool 3 — **Audio Overview** (you already made one — make more)

Generate one **per construct** when you really need to internalize that section. Use this customization prompt template:

```
Focus only on [CONSTRUCT NAME] as a debiasing intervention in long-term auditor
engagements. Walk a doctoral student through: (a) the operational definition,
(b) the theoretical mechanism by which it would reduce anchoring bias, (c) the
two main contradictions in the literature, and (d) the hypothesis stated in
Yasir Malik's paper. About 8 minutes. Keep energy high, recap twice, signpost
clearly.
```

**ADD use:** Listen to one a day for 11 days. By day 11 you've internalized your own model.

---

### Tool 4 — **Briefing Doc** (auto-generated executive summary)

Click **"Briefing Doc"** → **Generate**.

NotebookLM writes a 2-page executive summary of all your sources. **Use it as the foundation for your Chapter 1 introduction rewrite** later in the semester.

---

### Tool 5 — **Video Overview** (narrated slide deck of your paper)

New in April 2026. Click **"Video Overview"** in the Studio panel → **Generate**.

NotebookLM produces a narrated slide presentation summarizing your sources with on-screen visuals. **This is your committee-meeting prep deck.** You can screen-share this in the meeting if you blank, or watch it on 1.5x the night before to refresh.

---

### Tool 6 — **Interactive Mode** (raise your hand during the podcast)

While the Audio Overview is playing, click **"Join"** (or the hand-raise icon). Speak or type a question. The two AI hosts pause, answer using only your sources, and resume the discussion.

**ADD use:** This is the killer feature. When your mind wanders mid-podcast and you snap back with *"wait — what's the difference between AJQ and APR again?"*, just ask. You don't lose your place; you get the answer and the podcast keeps going.

---

## Prompt library

Every prompt from this playbook, in one block, for fast access. Paste any of these directly into NotebookLM's chat.

### Setup prompts

```
List every source currently in this notebook, one per line, in the format:
"[number]. Author (Year) — short title"
```

### Per-construct extraction prompts

```
For each of the new sources I just added (NOT my own paper, NOT the 5 anchor
papers from before), give me ONE academic paragraph in this exact format:

"Author (Year), in [Journal Name], [verb: showed/demonstrated/argued/found]
that [main finding]. The study [method in one clause]. The implication for
[CONSTRUCT] as a debiasing intervention in long-term auditor engagements is
[implication in one clause]."

Do NOT invent details — if a paper doesn't report a method, say so.
```

```
Across ALL sources in this notebook, what does the literature DISAGREE about
regarding [CONSTRUCT]? Be specific:
- Where do authors contradict each other?
- Where does evidence point in opposite directions?
- What does the literature NOT address that a critical reader would ask?

Format as 3-5 bullets, each starting with "Contradiction:" or "Gap:".
Cite sources in (Author, Year) format.
```

```
Write a 120-150 word paragraph I can paste directly into the section of my
paper on [CONSTRUCT]. Requirements:
- Integrate AT LEAST 2 of the new sources I just added
- Reference at least 1 contradiction from the previous answer
- End with a sentence that takes a defensible position
- Use in-text citation style (Author, Year)
- Match this voice: academic but not stiff, declarative, no hedging fluff

Do NOT use sources outside this notebook.
```

```
For each of the new sources I just added, give me a formatted APA reference
list entry in this exact style:

Author, A. B., & Author, C. D. (Year). Title of the article. *Journal Name,
Volume*(Issue), pages.

Italicize ONLY journal name and volume. Use en-dash for page ranges.
No DOIs, no URLs. If you don't know a field, write [unconfirmed] — do not invent.
```

### Hypothesis-development prompts (use these for Chapter 3 work)

```
Based on the sources in this notebook, argue the theoretical relationship
between [CONSTRUCT A] (origin) and [CONSTRUCT B] (destination). Structure:
1. One sentence defining the origin construct
2. One sentence defining the destination construct
3. 2-3 sentences arguing the mechanism by which A would affect B
4. Cite at least 2 sources for the mechanism
5. End with: "Thus, Hypothesis [N] states that [A] is positively associated with [B]."

Match the voice of section 3.4 of my paper.
```

```
For the mediated relationship [CONSTRUCT A] -> [MEDIATOR] -> Reduction in
Anchoring Bias, argue why [MEDIATOR] is the appropriate conduit (not the other
mediator). Structure:
1. State the mechanism the mediator captures
2. Explain why this intervention's effect operates through THIS mediator rather
   than the alternative
3. End with: "Thus, Hypothesis [N] states that [MEDIATOR] mediates the
   relationship between [A] and the Reduction in Anchoring Bias."

3-4 sentences total. Cite at least 1 source.
```

### Cross-cutting sanity-check prompts

```
Read my paper (Research_Paper_YMalik_v4.docx in this notebook). For each
in-text citation in my paper, check whether the cited source SUPPORTS the
claim I make about it, based on the other sources in this notebook. Flag
any claims where the cited source seems mis-paraphrased or over-claimed.
List them as: "Section X.Y: claim '...' attributed to (Author, Year) —
[CORRECT / NUANCED / NOT SUPPORTED]" with a one-line explanation.
```

```
Read my paper. Identify the THREE weakest arguments in Chapter 2 and the
THREE weakest hypotheses in Chapter 3, based on the supporting literature in
this notebook. For each, suggest one specific source from this notebook that
would strengthen it, and one sentence I should add.
```

---

## Troubleshooting

### "NotebookLM said something that contradicts my paper."
**Good.** That's exactly what Dr. Ray meant by finding contradictions. Investigate: open the source NotebookLM cited (it shows the passage), read the actual claim, and decide whether to update your paper or push back.

### "NotebookLM is citing something I didn't upload."
You shouldn't see this. NotebookLM is grounded only in uploaded sources. If you do see something suspicious, click the citation chip — it should open the source passage. If it doesn't, re-prompt with: *"You may only cite sources I have uploaded to this notebook. Re-answer using only those sources."*

### "A PDF I uploaded shows as 'failed' or just sits there."
- File too large (>200 MB): rare for journal PDFs, but if so, crop to just the article pages
- Image-only PDF (scan): run it through https://tools.pdf24.org/en/ocr-pdf first
- Restricted/encrypted PDF: open it in Preview/Acrobat, **File → Export → PDF**, re-upload the export

### "I can't find the PDF on Scholar."
1. Try **FIU library** (https://library.fiu.edu) — it has full-text access to AJPT, TAR, JAR, CAR, AOS
2. Email the corresponding author. They almost always respond within 48 hours and will send you the PDF directly.
3. Last resort: cite from the abstract + Google Scholar excerpt only — but flag with `[abstract-only verification]` in your draft, and remove the flag once you secure the full PDF.

### "I lost track of where I am."
Open this playbook. Scroll to the construct checklist in Step 2.5. Pick the next unchecked construct. Set a 20-min timer. Go.

---

## Quick reference — what each prompt gives you, at a glance

| Prompt | What you paste back into the paper | Where it goes |
|---|---|---|
| **A** Per-source summary | Individual sentences | Inside construct sections |
| **B** Contradictions & gaps | Critical-voice bullets | Inside construct sections (paragraph 2 of each) |
| **C** Synthesis paragraph | The whole paragraph | End of construct narrative, before the box |
| **D** APA entries | Reference-list lines | Verified Reference Pool (alphabetical) |
| Hypothesis prompt 1 | Direct-effect argument | One of §§ 3.4.1, 3, 5, 7, 9, 11, 13, 15 |
| Hypothesis prompt 2 | Mediated-effect argument | One of §§ 3.4.2, 4, 6, 8, 10, 12, 14, 16 |
| Sanity-check prompt | Flag list of risky claims | Use as a revision worklist; don't paste |

---

## When you finish a session

1. Save `Research_Paper_YMalik_v4_master.md`
2. Commit it to your branch with a message like `"Add NotebookLM-extracted citations for TA and RA"`
3. Or send me what you've got and I'll regenerate the .docx and push for you
4. **Stop.** Don't try to do a third construct. Two-per-session is the sustainable pace.

---

## One more thing — about your ADD and this work

This playbook is designed so you can pick it up after a one-week gap and know exactly what to do next. The construct checklist tells you where you are. The four prompts tell you what to do. The pasted output tells you where it goes. There is no "remembering what you were thinking last time" step.

If you only ever do Phase 1 + listen to the Audio Overview once, you'll still come out ahead of where you are now. If you do two constructs a week for five weeks, you're done.

Now stop reading this and go do **Step 1.1**.
