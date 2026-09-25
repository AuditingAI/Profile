# Capture schemas

**The load-bearing file.** One row format per hunt, used by every runbook and every model. Output
drops into the Chapter 2 table with no reformatting, and swapping in a different model next year
changes nothing downstream.

**A row that cannot be filled is not softened. The field is marked `not reported` — which is itself
information — or the row is dropped.**

---

## Universal fields — every row, every schema

| Field | Rule |
|---|---|
| `citation` | Author(s), year, title, venue. Enough to find it without the link |
| `url` | **Must resolve.** Checked at capture. A 404 drops the row |
| `access` | `open` · `FIU library` · `paywalled` — determines whether it can be read in full |
| `read_state` | `lead` (abstract only) · `read` (in full). **Starts at `lead`. Only Yasir moves it** |
| `captured` | ISO date, and which tool produced it |

⚠️ **`read_state: lead` is a hard gate.** A lead is not a citation and never enters a chapter. This
field exists because the repo already carries an honest admission that a set of AI-and-audit sources
were *"found by search, to be pulled through the FIU library and read before any of them enters a
proposal."* The schema makes that promise enforceable instead of aspirational.

---

## Schema A · Recruitment precedent — RB01

The highest-value capture in the programme.

| Field | What goes in it |
|---|---|
| `population` | Exactly who they recruited, in their words — "external auditors," "internal audit managers," "risk professionals" |
| `specialist` | `yes` / `no` — is this a low-prevalence professional population, or a general one? |
| `frame` | Sampling frame — professional body list, LinkedIn, firm access, panel, conference, alumni |
| `channel` | How contact was actually made |
| `n_target` | Stated target, if any |
| `n_achieved` | **Usable** responses. Not raw |
| `n_raw` | Raw starts, if reported |
| `screen_out_rate` | Reported, or derivable from raw vs usable |
| `incentive` | Amount and form, or `none` |
| `unit_cost` | Cost per usable response, if derivable |
| `time_in_field` | Weeks or months |
| `difficulty_noted` | **Verbatim quote** where they describe difficulty reaching the population |
| `transferable` | One line: what could actually be reused here |

**`difficulty_noted` is the field that matters most.** A verbatim admission that a specialist
population was hard to reach is evidence for the P1 manuscript's argument — that the prevalence
problem is general and under-reported, not a local misfortune.

---

## Schema B · Empirical AI-and-audit — RB02

| Field | What goes in it |
|---|---|
| `design` | `survey` · `experiment` · `interview` · `archival` · `review` · `conceptual` |
| `qualitative` | `yes` / `no` — **flag loudly on yes.** The stated gap is that this literature is almost entirely survey-based |
| `population` | Who, and where |
| `n` | Achieved |
| `construct_touched` | Which of the eleven, or `none` — feeds `../KNOWLEDGE/02_CONSTRUCTS.md` |
| `link_touched` | `L1` · `L2` · `L3` · `none` |
| `direction` | `supports` · `complicates` · `contradicts` · `neutral` — **relative to the chain** |
| `finding` | One sentence, in their words not ours |
| `measure` | How they operationalised reliance, skepticism, or trust — scale name, items, α |

**`direction: contradicts` is surfaced first in every report, never buried.** A literature review
that only accumulates support is the failure mode a bias researcher can least afford.

---

## Schema C · Regulatory and standards drift — RB03

| Field | What goes in it |
|---|---|
| `instrument` | NIST AI RMF · SR 11-7 · EU AI Act · PCAOB · AICPA · IIA · COSO · other |
| `jurisdiction` | US federal · EU · state · professional body |
| `status` | `in force` · `proposed` · `consultation` · `withdrawn` |
| `effective_date` | Or `not set` |
| `change` | What actually changed, one sentence |
| `bears_on` | `human oversight` · `model validation` · `documentation` · `audit trail` · `bias testing` · `other` |
| `dissertation_relevance` | One line, or `none` — most will be `none`, and that is fine |
| `brand_relevance` | One line — feeds the consulting practice via `../../career/HANDOFF.md` |

**Two audiences, one sweep, two separate documents.** The dissertation's practice section and the
consulting brand draw on the same captures. They never appear in the same output — that is the
standing separation in `CLAUDE.md`.

---

## Output file format

`RESULTS/YYYY-MM-DD_RBnn.md`, append-only:

```markdown
# RB01 · Recruitment precedent · 2026-08-26
**Tool:** Perplexity · **Queries run:** 6 of 8 · **Screened:** 41 · **Captured:** 3 · **Dropped:** 38

## Why the 38 died
Two lines. Enough to prove the gate did work rather than that the search was thin.

## Captured
| citation | url | access | read_state | population | specialist | ... |

## Nothing found for
List the queries that came back empty. A quiet query is a result.
```

---

## Verification before anything propagates

| Check | Rule |
|---|---|
| Every `url` resolves | Drop the row if not |
| No `read_state: read` set by a model | Only Yasir moves it, after reading |
| No row asserts a finding for L1/L2/L3 | The chain is argued, not established |
| Counts add up | `screened = captured + dropped` |
| Empty queries listed | A sweep that reports only hits is not reporting |
