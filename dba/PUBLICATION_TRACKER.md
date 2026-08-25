# Publication Tracker — from passed exam to citable work

**What this file is for.** Two things at once: a record of where each publishable output stands, and
a standing argument about the causal chain that sits at the top of the research. The chain is not
settled and must not be treated as settled — every literature sweep tests it, and this file records
what survived and what did not.

**Reviewed:** every Friday sweep (`/research`), and on every commit that touches the extension.
**Last review:** 2026-08-10.

---

## Part 1 — The chain at the top of the house

Everything below the chain — instrument, sample, analysis — only matters if the chain holds. So the
chain gets argued first, and re-argued as AI capability moves. A link that cannot be defended gets
demoted to "conjecture" in the manuscript rather than quietly carried.

**Chain v1.1** (revised 2026-08-10 — see the change note at the end of this section)

```
AI tool enters recurring review work
        ↓  L1
system output becomes the anchor — automated, continuous, arriving before the reviewer forms a view
        ↓  L2
the model confirms the position the reviewer has already stated rather than challenging it
        ↓  L3
successive models reprocess the same work; conclusions converge on each other, not on evidence
        ↓
recurring professional judgment degrades while every individual model passes its own validation
```

### Link-by-link status

| | Claim | Support | Strongest challenge | Status |
|---|---|---|---|---|
| **L1** | System-generated output functions as an anchor, and does so continuously and at scale | Anchoring-and-adjustment is among the most replicated findings in judgment research; the qualifying study's own model is built on it | Classic anchoring effects have taken replication damage in adjacent literatures; effect sizes in expert populations are smaller than in student samples | **Defensible**, but must be argued with expert-population evidence specifically, not lab-undergraduate evidence |
| **L2** | The model agrees with a stated position rather than challenging it | Sycophancy is documented and named in the LLM literature; vendors publish on mitigating it | Sycophancy is a moving target — successive model generations are explicitly trained against it. A 2026 claim may not hold in 2028 | **Time-sensitive.** Must be dated and re-tested each sweep, never stated as a fixed property of "AI" |
| **L3** | Successive models reprocessing the same work converge on each other rather than on evidence | Model-collapse and synthetic-data-contamination results; **and now** *How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer Review* (2026) — cross-model peer review is this link, instrumented by someone else | Most evidence is about training corpora, not about professionals reading model output. The step from "models degrade on synthetic data" to "auditors converge because models converge" is an inference, not a finding | **Weakest link.** This is where a committee will push |
| **Whole** | The three compound in recurring professional review | — | AI assistance sometimes *improves* judgment (see the adversarial flag in `scholar-reading-list.md`, Aug 10) | **Untested. Say so.** No findings exist yet |

### Standing challenges — carried forward until answered

1. **The improvement case.** A 2026 study found AI assistance reduced bias in a judgment task. Lay
   readers, different domain — but the argument must engage it rather than route around it.
2. **The moving-target problem.** L2 describes current model behaviour. A dissertation defended in
   2028 against 2026 model behaviour is a dated dissertation. The defensible framing is
   *mechanism*, not *artifact*: sycophancy arises from optimising on human approval, and that
   pressure persists across generations even as each generation is patched.
3. **L3's inferential gap.** Model-to-model convergence is documented. Auditor-to-auditor convergence
   *via* models is not. Closing this is the single highest-value empirical contribution available —
   and it is the one thing a well-designed study could actually measure.

### Change log

- **v1.1 (2026-08-10)** — L3 upgraded from "conjecture" to "weakest link, externally supported"
  after the cross-model peer-review paper surfaced. Added the improvement-case challenge. Added the
  moving-target framing for L2.
- **v1.0 (2026-07)** — chain first stated in the qualifying manuscript's dissertation-transition
  section. Praised by the advisor as sound research judgment; no link individually defended.

---

## Part 2 — Publication pipeline

Ranked by how close each is to submittable, not by how interesting it is.

### P1 · The recruitment-feasibility note — **closest to ready**

**Claim:** specialist professional populations cannot be reached through standard research
infrastructure at any price. Applying eligibility criteria to a panel of 334,976 returned roughly
twenty eligible people — about six per hundred thousand.

**Why it is publishable:** it is a complete, negative, methodological finding with a hard number
behind it. Researchers designing auditor studies are currently budgeting against assumptions this
result falsifies. The advisor already judged the reflection on it sound.

**What exists:** the finding, the screening protocol (`03_Data/clean_and_screen.py`), the exclusion
log, the platform's own eligibility figure, and the cost record.

**What is missing:** a target venue, a 3,000–4,000 word write-up, and a decision on how much
platform detail can be disclosed without breaching terms.

**Status:** 🟡 **draft v1 written** (2026-08-10, ~3,400 words) — `P1_Feasibility_Note/MANUSCRIPT_DRAFT_v1.md` · **Blocking:** 4 items in `P1_Feasibility_Note/SUBMISSION_CHECKLIST.md` — advisor sign-off (incl. co-authorship), platform terms, IRB aggregate-reporting confirmation, and reconciling the exact n against the course manuscript's deliberate hedge · **Owner:** Yasir

---

### P2 · The conceptual extension paper

**Claim:** the three-link chain above, argued from literature, with a research agenda.

**Why it is publishable:** conceptual papers with a clear causal argument and a testable agenda are
publishable in practitioner-academic venues, and this one now has external support at L3.

**What is missing:** L1 argued with *expert*-population anchoring evidence; L2 framed as mechanism
rather than artifact; L3's inferential gap stated honestly rather than smoothed over; and the
improvement case engaged. All four are listed above.

**Status:** ⬜ not started · **Blocking:** P1 should go first — a negative methodological finding is
easier to place and establishes a publication record before a conceptual argument · **Owner:** Yasir

---

### P3 · The dissertation itself

**Blocking, in the advisor's explicit order:** a comprehensive recruitment strategy *before* writing
resumes. Four literature sweeps have produced **zero** recruitment precedent. P1 is not a detour from
this — writing up the feasibility finding forces the recruitment problem to be solved on paper, which
is exactly what Directive 5 asks for.

**Status:** ⬜ blocked on recruitment strategy

---

## Part 3 — Progression

| Stage | Date | Evidence |
|---|---|---|
| Instrument built, IRB approved | Jun 2026 | IRB-25-0462 · 11 constructs, 55 items, 16 hypotheses |
| Fielded; collection failed | Jul 2026 | 23 raw → 4 valid · ~6 eligible per 100,000 |
| Manuscript submitted | 26 Jul 2026 | `Research_Paper_YMalik_SUBMISSION.md` |
| **Qualifying examination passed** | 26 Jul 2026 | Advisor: *"demonstrates sound research judgment"* |
| Five directives converted to a work plan | 27 Jul 2026 | `00_Execution/Rey_Final_Feedback_Dissertation_Plan.md` |
| Chain stated | Jul 2026 | v1.0 — asserted, not argued |
| Chain argued link-by-link | 10 Aug 2026 | v1.1 — this file |
| First external support for L3 | 10 Aug 2026 | Cross-model peer-review paper, `scholar-reading-list.md` |
| Recruitment strategy | — | ⬜ **blocking everything downstream** |
| First submission | — | ⬜ P1 is the candidate |

**Citable output to date: none.** A passed qualifying examination is not a publication. The gap
between "the work is good" and "the work is citable" is one drafted manuscript, and P1 is the one
that closes it fastest.

---

## How this file stays honest

- Every Friday sweep tests the chain against what arrived that week. Support **and** contradiction
  get recorded; the adversarial pass exists precisely so this file cannot become a highlight reel.
- A link that survives a sweep unchanged still gets its date bumped, so "defensible" never silently
  means "unexamined since last year."
- L2 is dated by construction. Model behaviour moves; a claim about it that carries no date is a
  claim that will quietly become false.
- Nothing here is described as a finding until data exists. The extension has **no findings**.

---

## P4 — AIB Latin America 2027 · the first real submission window

*Source: GEB 7365 class session, 21 August 2026 — "AIB Latin America Conference Overview", Prof.
William Newburry. Meeting notes in Notion.*

**Academy of International Business, Latin America Chapter** · San Juan, Puerto Rico ·
**3–5 March 2027**

| Track | Deadline | Requires | Verdict |
|---|---|---|---|
| Paper (competitive) | **3 Sep 2026** | Completed research and data | **Not viable.** Four valid responses; the AI extension is argued, not tested |
| **Poster / interactive** | **20 Nov 2026** | No completed data required | **This is the target** |

The class was explicitly steered toward interactive and poster sessions for exactly this situation.

**Why this matters to this tracker.** GEB 7365's project brief asks for "a manuscript that can be
submitted to a top academic conference in international business," and the instructor devoted a
session to one conference. The course project and the conference submission are the same artifact.
The Formal Project Report is due 7–9 October; the poster deadline is 20 November. **A revision pass,
not a second project.**

**The Latin America requirement is not a blocker.** The class was told a regional angle can be added
via a comparison or a regional framework such as GLOBE. P1's finding — eligibility prevalence near
six per hundred thousand on a general panel — extends directly: whether that prevalence is worse in
Latin American panels, and what it implies for anyone attempting a comparative IB survey across the
region, is a Latin America question with US evidence already in hand.

Candidate tracks: **International Strategy**, or **Teaching & Learning** framed as doctoral research
methods. Ten tracks exist; each has two chairs and 2–3 peer reviewers per paper.

**Costs to know before committing.** The corresponding author is expected to review **10–20**
submitted papers, landing in the same window as coursework. FIU offers partial travel funding but
the process was described as cumbersome — start the paperwork early.

**What alumni actually got from it**, per the session: every speaker named networking and mentorship
above the CV line. One is now mentored by a full professor in France; one met the researcher they
had cited throughout their dissertation; a classmate co-authored there and is in second-round
journal review. Several said outside feedback led them to substantially revise their research
question and model. Given that chain link L3 is the acknowledged weak one, that is the more
valuable outcome than the submission itself.

**Status:** not submitted. No abstract drafted. Decision to target 20 November recorded 21 Aug 2026.
