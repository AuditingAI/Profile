# Literature map: the three-link chain

**Date:** 2026-10-20 · **Lane:** Scholar · **Status:** raw material for Yasir to read and rewrite. Not a chapter.

> **AI-use disclosure (FIU UGS policy).** Drafted with Claude (Anthropic) as a literature-search and organisation aid on 20 Oct 2026; sources verified as listed; synthesis and argument remain Yasir Malik's.

## Purpose

Map what the published literature does and does not show for each link of Chain v1.1 (`../../PUBLICATION_TRACKER.md`):

- **L1 Anchor.** System output arrives before the reviewer forms a view and becomes the anchor (anchoring-and-adjustment; automation bias).
- **L2 Confirm.** The model confirms the reviewer's stated position (sycophancy) while the reviewer defers to automation; both push the same way.
- **L3 Converge.** Over recurring reviews, judgments converge on each other or on model output rather than on evidence. Weakest link; untested.

Setting: audit and assurance, recurring engagements, prior-year anchoring, human review as a control.

## Contents

| File | What it is |
|---|---|
| `GAP_TABLE.md` | One row per paper, coded Tested / Partly / Not for each link, then "Where the gaps are" (draft) |
| `cards/*.md` | 29 note cards, one per verified paper: citation, DOI/URL, what was read, design, findings as stated, link, limitation, critique angle |

## Method

**Starting point.** Checked `scholar-reading-list.md`, `dba/KNOWLEDGE/01_THEORY.md`, `dba/RESEARCH_RECORD.md`, `dba/PUBLICATION_TRACKER.md` and the reference list of `Research_Paper_YMalik_SUBMISSION.md` first. Each card says whether the paper is already cited in the repo.

**Tools and databases.**
- Firecrawl research index (arXiv, PubMed, PMC, bioRxiv/medRxiv): metadata, full abstracts for arXiv items, truncated abstracts for PubMed items, and full-text passages where the arXiv text is indexed.
- Web search engine (Claude Code WebSearch), which surfaced publisher, RePEc/IDEAS, conference-proceedings, SSRN and repository records and extracted abstract text from them.
- Not reachable from this session: Crossref, JSTOR, publisher pages fetched directly, Google Scholar, Scopus, SSRN full search, AAA Digital Library. Firecrawl page scraping was out of credits. This is why several accounting papers are verified from index records rather than the publisher page.

**Search strings used** (natural-language and title queries, run 20 Oct 2026):
- `"Anchoring and adjustment in probabilistic inference in auditing"`; `"Mitigating the consequences of anchoring in auditor judgments"`; `"Anchor and adjustment heuristic effect on audit judgement" continuing audit engagements`; `prior year audit strategy anchoring continuing auditors`; `"Effects of expectations, prior involvement, and review awareness"`; `Henrizi anchoring audit judgments Switzerland`
- `"Complacency and bias in human use of automation"`; `"Automation bias: a systematic review"`; `"Does automation bias decision-making?"`
- `"Algorithm aversion: people erroneously avoid algorithms"`; `"Algorithm appreciation: People prefer algorithmic to human judgment"`
- `"Man versus machine" complex estimates auditor reliance artificial intelligence`; `Estep Griffith MacKenzie artificial intelligence financial executives`; `Libby Witz artificial intelligence independence liability`; `"Control Issues" auditor reliance artificial intelligence`; `experiment auditors rely on generative AI output large language model audit judgment`
- `Towards Understanding Sycophancy in Language Models`; `Discovering language model behaviors with model-written evaluations sycophancy`; `simple synthetic data reduces sycophancy`; `sycophantic AI users trust more, increases conviction they are right`
- `Deciding fast and slow cognitive biases AI-assisted decision-making anchoring`; `co-writing with opinionated language models`; `How human-AI feedback loops alter human judgements`; `When combinations of humans and AI are useful`
- `Generative AI enhances individual creativity but reduces collective diversity`; `Does writing with language models reduce content diversity`; `Algorithmic monoculture and social welfare`; `Picking on the same person outcome homogenization`; `AI models collapse when trained on recursively generated data`

**Verification rule.** A paper became a card only if its authors, year, title and venue were confirmed in at least one record actually reached (research index, publisher, proceedings, RePEc, or author vita). Each card states exactly what was read: full abstract, partial abstract, full-text passages, or bibliographic record only. Findings are quoted or closely paraphrased only from that text. No page numbers or statistics were added that were not seen. Where a volume or page range was not seen, it is left out or marked "not verified".

**Coding rule for the gap table** is stated at the top of `GAP_TABLE.md`.

## Read before citing

- **Thinly verified cards** (record only, no abstract read): Kinney & Uecker (1982), Libby & Witz (2024). Tan (1995) rests on the author's related dissertation abstract. Skitka et al. (1999) and Joyce & Biddle (1981) on partial abstracts. Read these before relying on them for any finding.
- **Preprints** (labelled on their cards): Wei et al. (2023), Batista & Griffiths (2026). Doshi & Hauser and Rastogi et al. figures were read in the arXiv versions of published papers; check them against the published versions.
- **Published vs preprint numbers differ** for Cheng et al. (2026). Use the *Science* figures.
- **Repo items that need a look.** The submission manuscript's Glickman & Sharot entry gives issue and pages that were not re-verified here.

## Leads, unverified (not carded)

| Lead | What is known | Why not carded |
|---|---|---|
| McMillan, J. J., & White, R. A. (1993). Auditors' belief revisions and evidence search: The effect of hypothesis frame, confirmation bias, and professional skepticism. *The Accounting Review, 68*(3), 443-465 | Cited in secondary sources; title wording varies ("confirmation" vs "confirmation bias"); one source spells the author "McMillian" | No primary record or abstract reached. Main candidate for audit confirmation bias; verify first |
| Commerford, B., Eilifsen, A., Hatfield, R., Holmstrom, K., & Kinserdal, F. "Control issues: How providing input affects auditor reliance on artificial intelligence." *Contemporary Accounting Research* (listed as 2024, forthcoming) | University and NHH pages list it; summaries say auditors are more hesitant to rely on AI than on human specialists | Volume, issue and DOI not confirmed; abstract not read. Highly relevant to L1 direction |
| Callahan & Hill (2001, year per a search summary). "Planned audit hours: Do auditors use a same as last year strategy?" Emerald DOI 10.1016/S1474-7979(01)04077-7 | Title seen in search; a summary says auditors did not use a same-as-last-year strategy for planned hours | Authors, venue and abstract not confirmed. Potential counter-evidence to prior-year anchoring |
| Dell'Acqua et al. (2023). "Navigating the jagged technological frontier" (HBS working paper) | Known working paper on consultants using GPT-4 | Not reached in any index this session |
| Estep, Griffith, MacKenzie & Csere (2025), *Current Issues in Auditing* | Listed on a faculty page as a shorter version | Not confirmed as the same study |
| "How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer Review" (2026) | Already in `scholar-reading-list.md` (10 Aug) as L3 support | Not re-verified here; full text still to obtain per the reading list |
| Candidates surfaced but not carded, all arXiv preprints: "Reactive Writers" (arXiv 2603.10374, AI co-writing seeds ideas writers do not notice); "Be Friendly, Not Friends" (arXiv 2502.10844, sycophancy and user trust, N = 224); "Who Does What in AI Auditing?" (arXiv 2609.24986, 71 AI auditors relied more on AI assessments) | Abstracts seen in the research index | Out of scope for this pass or adjacent (AI auditing, not financial audit); candidates for a second pass |

## Rules carried from the repo

No DBA completion year or GPA appears in this folder. Nothing here describes the chain as having findings. Every interpretive sentence in `GAP_TABLE.md` is marked as a draft for Yasir to rewrite.
