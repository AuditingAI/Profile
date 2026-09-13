# The Sunday Scholar sweep · what runs automatically, and what only you can do

**Set up 13 September 2026.** Trigger `trig_01CCan5ZW6sHUwNX16WijEjQ`.
**Fires every Sunday, 8:00 AM ET.** First run: **Sunday 20 September.**
Push and email notification both on. Each firing starts a fresh session.

---

## What it does without you

| Step | |
|---|---|
| 1 | Reads the week's Google Scholar alert emails |
| 2 | Triages each hit against the three-link chain in `../PUBLICATION_TRACKER.md` |
| 3 | Captures survivors in the row format in `SCHEMAS.md`, with a resolving URL or not at all |
| 4 | Ranks by value: recruitment precedent first, then L3 evidence, then AI-and-audit empirics, then Chapter 2 construct rows |
| 5 | Appends to `../../scholar-reading-list.md` and the research brief, dated, append-only |
| 6 | Commits and pushes as `[scholar]` |
| 7 | Reports a table, the single best find, and one next action |

**It reports the signal-to-noise ratio every week**, including on weeks when nothing survives. That
number is the thing that tells you whether the alert set is working, and a quiet week reported
honestly is worth more than a manufactured find.

---

## 🔴 Two things it cannot do, and both are on you

### 1 · It has no Gmail access as created, so it cannot read the alerts

The routine was created from this session, and the system would not pass a connector grant through
to it. The warning was explicit: **"this trigger stores no MCP connectors, so the sessions it fires
will run without connector tools."**

**Without Gmail it cannot read the Scholar alert emails, which is the entire input.** It will still
fire, still read the repo, and still report, but on an empty inbox.

**The fix, ten seconds:** open the routine in **claude.ai → Routines**, find **📚 Sunday Scholar
sweep**, and attach **Gmail**. Do this before 20 September or the first run is a no-op.

### 2 · The four replacement alerts still do not exist

**This is the real bottleneck and it has been open since 7 September.** Google Scholar alerts are a
manual web action. No tool in any session can create them.

The existing "Auditor Bias" alert fired **25 times in 35 days** and returned roughly **250 results,
of which one was relevant**. The pipeline is healthy. The query is wrong. A sweep of a bad alert set
is a well-run search of the wrong literature.

**Ten minutes at `scholar.google.com/scholar_alerts`. Paste these four, in this order:**

**1. This one first. It hunts the counter-evidence, which matters most:**
```
"algorithm aversion" OR "algorithmic appreciation" expert judgment
```
**2.**
```
sycophancy OR "sycophantic" "language model"
```
**3.**
```
"model collapse" OR "self-consuming" OR "recursive training" language model
```
**4.**
```
auditor "professional skepticism" "artificial intelligence" reliance
```

Search the string, click **Create alert** (envelope icon), confirm the address is
**`yasiramalik@gmail.com`**, repeat. **Keep "Auditor Bias" running** as well; it is cheap and it
occasionally lands something real.

**Why alert 1 is first.** It looks for evidence that AI assistance sometimes *improves* expert
judgment. That is the finding that would most damage the argument, which is exactly why it should be
hunted deliberately rather than waited for. A research pipeline that only searches for confirmation
is a demonstration of the thing the dissertation is about.

---

## Where the AI side gets its context, and what is missing

You asked what else you have to do so the sweep has more to work with, particularly on the research
and the AI. Three things, in order of value.

| | What | Why it matters | Who |
|---|---|---|---|
| 🔴 1 | **Attach Gmail to the routine** | Without it the sweep reads nothing | You, 10 seconds |
| 🔴 2 | **Create the four alerts** | Without them it reads the wrong literature | You, 10 minutes |
| 🟡 3 | **RB02 has never been run** | `RESULTS/` is empty. The AI-and-audit empirical papers in `../00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §7 are still marked *"none read in full."* **That is the largest honesty gap in the repo** | Run `/airun RB02`, or paste `CONTEXT_PACK.md` into Perplexity |

**On item 3.** The sweep finds what arrives. RB02 goes and looks. They are different jobs and only
the first is automated. The chain's weakest link is L3, a committee will push there, and nothing in
`RESULTS/` currently answers it.

**A fourth, smaller one.** `CONTEXT_PACK.md` is what any other model reads to understand this
research cold. It is the file that decides what ChatGPT, Perplexity, Gemini or NotebookLM believe
about the work, including the hard "what is NOT claimed" section. **When the research changes, that
file changes**, or every other model you use is working from a stale picture. It was last touched in
August, and the qualitative arm and the GEB 7365 model have both moved since.

---

## Existing coverage this replaces

The Scholar sweep was **section 5 of "Monday roll-up, properties, LLC and research"**
(`trig_013A1LtfqAUbEZcCJ6nxTCMu`, Mondays 7:00 AM ET), behind four sections on rent status, water
bills, tenant leads and HELOC figures.

**That is why it never landed.** Research was competing with a landlord brief for attention in the
same message. The Monday roll-up still runs and still covers the properties. Research now has its
own morning.
