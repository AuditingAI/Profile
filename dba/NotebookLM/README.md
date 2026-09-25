# NotebookLM — setup and the daily study loop

## First, the honest answer on connecting it

**NotebookLM cannot be connected to Claude.** It has no public API and no MCP server. Nothing built
here can read from your notebook or write into it. The integration is manual and one-directional:
files are generated here, you upload them there.

That is a real limitation, and it has one practical consequence — **the notebook goes stale silently.**
The previous pack sat unchanged from 24 July while the exam result, five directives, the argued
chain, and a drafted manuscript all landed. A notebook that quietly describes a five-week-old state
of the work is worse than no notebook, because you will study from it and believe it.

So: **re-upload whenever `sources/` changes.** The date at the top of every source file tells you
whether what you are studying is current.

---

## Setup — once, about ten minutes

1. Go to notebooklm.google.com and create a notebook: **"DBA — Anchoring Bias & AI Judgment Risk."**
2. Upload the three files from `sources/` (PDF versions are in this folder; NotebookLM also accepts
   Markdown directly).
   - `01_THE_STUDY_AND_THE_FINDING` — the model, the method, what happened, what is not claimed
   - `02_THE_ARGUMENT_AND_ITS_CHALLENGES` — the chain, link by link, with every objection
   - `03_WHAT_IS_OWED_AND_TO_WHOM` — the five directives, the pipeline, the sequencing
3. Add the qualifying manuscript (`../Research_Paper_YMalik_SUBMISSION.pdf`) as a fourth source when
   you want depth. Keep it separate — it is long, and NotebookLM cites per source, so mixing the
   summary and the full manuscript makes citations harder to trace.

**Why three focused sources rather than one large one:** NotebookLM attributes every answer to a
source. Separate files mean an answer about the argument cites the argument file, and you can see at
a glance whether a claim came from the study record or from the reasoning layer. One merged document
destroys that signal.

---

## The daily loop — fifteen minutes

**Do it in this order. The order is the point: retrieve before you read.**

**1 · Answer before opening anything (5 min).** Take one question from §5 of Source 2 and answer it
out loud, from memory, before looking. Retrieval practice is what builds recall; re-reading feels
productive and mostly is not.

**2 · Check yourself against the sources (5 min).** Ask NotebookLM the same question. Compare. The
gap between your answer and the source is the only part worth studying.

**3 · Push on one weak point (5 min).** Use a challenge prompt below. You are not looking for
agreement — you are looking for the thing you cannot yet answer.

**Friday, instead of the above:** generate an Audio Overview of Source 2 and listen to it while
doing something else. Hearing your own argument spoken back by a third party is the fastest way to
notice which parts sound thin.

---

## Prompts that actually earn their keep

NotebookLM is grounded in your sources, so it is genuinely good at interrogating them and poor at
inventing beyond them. Use it for the former.

**To rehearse a defense:**
> Act as a sceptical dissertation committee member in accounting. Ask me the five hardest questions
> about the L3 link in the chain, one at a time. Wait for my answer before the next question.

**To find your own gaps:**
> What claims in these sources are asserted without supporting evidence? List them and say what
> evidence each would need.

**To force honesty:**
> Where do these sources overstate what the data supports? Quote the specific sentences.

**On the directives:**
> Using Source 3, what is the shortest path from where the work is now to satisfying Directive 5?
> What has to happen first?

**For the weakest link:**
> Design a study that would test whether professionals reading model output converge on each other.
> What would be measured, and what result would falsify the claim?

**Study guide / briefing doc / timeline** — NotebookLM's built-in generators work well on Source 1
(factual, structured). They work less well on Source 2, which is an argument rather than a body of
facts; interrogate that one with questions instead.

---

## Two cautions

**NotebookLM will not tell you when you are wrong about something outside its sources.** It is
grounded, which means it is confident within the notebook and silent beyond it. Everything in these
sources came from this project — if a claim is wrong here, it will be wrong there too, consistently
and persuasively. That is worth noticing given what you research.

**Do not paste NotebookLM output into the dissertation.** Dr. Rey's instruction is explicit: AI
supports brainstorming, organisation, and clarity — not synthesis, interpretation, or the argument
itself. Use it to test whether you can defend the reasoning. The reasoning has to be yours.

---

## Keeping it current

Regenerate the PDFs after any change to `sources/`:

```
python3 dba/NotebookLM/make_sources_pdf.py
```

Then re-upload. NotebookLM does not sync — an old upload stays old forever.

**Last generated:** 11 August 2026 · chain v1.1 · P1 draft v1
