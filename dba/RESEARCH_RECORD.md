# Research record — the evidence base

**What this file is.** One sourced account of the research programme, written so it can feed three
very different documents without any of them inventing anything. It is **not** a résumé and must not
be pasted into one whole. It is the pile of verified facts a résumé draws from.

**Why it exists separately.** Three audiences want three different sentences about the same work. A
hiring manager in model risk, a search committee, and a prospective advisory client will each reject
the other two's phrasing. The facts do not change. The framing does. Keeping them apart at the source
is what stops the framing drifting into claims.

**Last verified:** 25 September 2026 · **Primary sources:** `RESEARCH.md`, `dba/PUBLICATION_TRACKER.md`,
`dba/STUDY_OVERVIEW.md`, `dba/00_Execution/IRB_STATUS_2026-08-28.md`, `dba/RISK_QUANT/`,
`dba/QUALITATIVE/`, `dba/coursework/`.

---

## 0 · The identity line, in its verified form

> **Yasir A. Malik** · Doctor of Business Administration candidate, Florida International University,
> Chapman Graduate School of Business · Cohort 8.14
> Audit and risk at **Citigroup** (2012–2015, and July 2021 onward) and **JPMorgan Chase** (2015 to June 2021)
> Former bank examiner, **Florida Office of Financial Regulation**

No career-length number appears anywhere. Yasir's instruction to the Industry lane on 12 September
2026 was no tenure figure at all, fifteen included. The institutions and the dates carry it.

**Three things that are wrong elsewhere and must not be repeated.**

| Wrong | Right | Why it matters |
|---|---|---|
| Bank Examiner, **OCC** | **Florida Office of Financial Regulation** | Removed on 2026-08-14. Industry confirmed on 25 September that it is already gone from `main`; the earlier flag here was stale |
| **20+ years** / two decades | **No career-length number.** Institutions and dates only | Yasir, 12 September, to Industry: no "20 years", no "15 years". Fixed on the Industry branch; still live on `main` until that branch merges |
| A **GPA** or a **completion year** | Neither, until the program office confirms | `CLAUDE.md` §3. The record shows 3.81 against a claimed 3.87, and Summer 2028 against a claimed 2027 |

---

## 1 · The programme in one paragraph

An auditor reviewing a multi-year engagement has always worked from an anchor: last year's
conclusion. Anchoring-and-adjustment is among the most replicated findings in judgment research.
What changed is that the anchor is now produced by a system — automatically, continuously, and
before the reviewer has formed a view — and when the reviewer states a position, the system tends to
agree with it. The programme argues a three-link chain and is explicit that only the first link is a
human cognitive bias.

| | Claim | What kind of thing it is | Status |
|---|---|---|---|
| **L1** | System output functions as an anchor: automated, continuous, arriving first | **Automation bias** — a human cognitive bias | Defensible, but must be argued from expert-population evidence, not undergraduate lab samples |
| **L2** | The model agrees with a stated position rather than challenging it | **Sycophancy** — model behaviour, not a human bias | Time-sensitive. Argue the mechanism, not the artifact: it arises from optimising on human approval, and that pressure survives each generation's patch |
| **L3** | Successive systems reprocess earlier machine-influenced work and converge on each other rather than on evidence | **Recursive epistemic drift** — a property of a system of models | **Weakest link.** Model-to-model convergence is documented; auditor-to-auditor convergence *via* models is not. This is the inferential gap |

**Nothing in the chain has been tested.** No findings exist for the AI extension.

---

## 2 · Chronology, with the evidence for each entry

| When | What happened | Evidence |
|---|---|---|
| Jun 2026 | Instrument built and IRB approved. 11 constructs, 55 items, 16 hypotheses | **IRB-25-0462** · `dba/STUDY_OVERVIEW.md` |
| Jul 2026 | Fielded. A commercial panel of **334,976** screened against eligibility returned roughly **20** eligible. **23** raw responses, **4** survived screening. Prevalence near **6 per 100,000** | `dba/03_Data/clean_and_screen.py`, the exclusion log, the platform's own eligibility figure |
| 26 Jul 2026 | Manuscript submitted. ~16,200 words, Chapters 1 to 6 plus references and Appendix A | `dba/Research_Paper_YMalik_SUBMISSION.md` |
| 26 Jul 2026 | **Qualifying examination passed.** Advisor's words: *"demonstrates sound research judgment"* | Advisor correspondence |
| 27 Jul 2026 | Five advisor directives converted into a work plan | `dba/00_Execution/Rey_Final_Feedback_Dissertation_Plan.md` |
| Jul 2026 | Three-link chain stated, v1.0 — asserted, not argued | `dba/PUBLICATION_TRACKER.md` |
| 10 Aug 2026 | Chain argued link by link, v1.1. First external support for L3 surfaced | `dba/PUBLICATION_TRACKER.md`, `scholar-reading-list.md` |
| 10 Aug 2026 | **P1 manuscript draft v1**, ~3,400 words | `dba/P1_Feasibility_Note/MANUSCRIPT_DRAFT_v1.md` |
| Aug–Sep 2026 | Feasibility calculator built. Reproduces the failed study from its own rates and shows a survey at this prevalence needed a frame near **9.6 million** | `dba/RISK_QUANT/feasibility.py` |
| Aug–Sep 2026 | Phenomenological protocol written for L2: sampling, interview guide, coding plan, trustworthiness criteria, append-only audit trail, falsification conditions stated before any data exists | `dba/QUALITATIVE/` |
| Aug–Sep 2026 | Model-agnostic research runbooks and a capture schema that refuses unsourced claims and runs an adversarial pass on its own output | `dba/AI_RUNBOOKS/` |
| Sep 2026 | GEB 7365 project: feasibility as a design parameter. Five hypotheses, a multi-level design, and a stated level of analysis | `dba/coursework/GEB7365_International_Business/` |
| Sep 2026 | GEB 7911 qualitative proposal: the L2 phenomenology, with a positionality statement and a confirmation hazard log | `dba/coursework/GEB7911_Qualitative_Research_Methods/` |

---

## 3 · Outputs ledger, with honest status

| Output | What it is | Status |
|---|---|---|
| Qualifying manuscript | ~16,200 words, complete, Ch. 1–6 | ✅ Submitted, examination passed |
| Survey instrument | 55 items, 11 constructs, IRB-approved, fielded | ✅ Built and proven |
| Data screening record | Script, exclusion log, cost record | ✅ Complete |
| **P1 · feasibility manuscript** | *Six in One Hundred Thousand* — specialist populations cannot be recruited from general research panels | 🟡 **Draft v1.** Four items block submission: advisor sign-off including co-authorship, platform terms, IRB aggregate-reporting confirmation, and reconciling the exact n |
| **P2 · conceptual extension** | The three-link chain argued from literature with a research agenda | ⬜ Not started. P1 goes first |
| **P3 · dissertation** | — | ⬜ Blocked on a recruitment strategy, which is the advisor's explicit order |
| Feasibility calculator | Turns the finding into a reusable instrument | ✅ Working |
| Qualitative protocol | Full phenomenological design | ✅ Written · ⛔ Nothing fielded, zero participants, IRB modification not submitted |
| Research runbooks | Portable, model-agnostic pipeline | ✅ Working |
| **Peer-reviewed publications** | — | **None to date** |

**A passed qualifying examination is not a publication.** The gap between "the work is good" and
"the work is citable" is one drafted manuscript, and P1 is the one that closes it fastest.

---

## 4 · Capabilities demonstrated, each tied to an artifact

This is the section a résumé actually draws from. Every line has something behind it.

| # | Capability | The artifact that proves it |
|---|---|---|
| 1 | **Measurement design and psychometrics.** Multi-construct instrument design; exploratory factor analysis with principal axis factoring and direct oblimin rotation; reliability analysis; confirmatory and structural models specified for the next stage | 11 constructs, 55 items, 16 hypotheses, fielded under IRB-25-0462 |
| 2 | **Research governance and ethics.** Protocol approval, amendment tracking, participant protection, institutional AI-use policy compliance and disclosure | IRB-25-0462 and a four-item IRB status file that records what is unsubmitted |
| 3 | **Feasibility quantification.** Reachable sample modelled as a product of frame size, prevalence, response rate and screen survival; validated by reproducing the study that produced it | `dba/RISK_QUANT/feasibility.py` |
| 4 | **Qualitative method.** Phenomenological design: criterion sampling, interview protocol, horizontalisation through to composite description, trustworthiness criteria mapped to procedures, append-only audit trail | `dba/QUALITATIVE/` |
| 5 | **AI governance and model risk.** A defensible separation of automation bias from sycophancy from epistemic drift, argued against its own strongest objections and dated because the middle link moves | The chain, v1.1, with a link-by-link challenge table |
| 6 | **Research pipeline engineering.** A model-agnostic capture schema, provenance on every row, a rule that a source is a lead until it has been read in full, and an adversarial pass against the pipeline's own output | `dba/AI_RUNBOOKS/` |
| 7 | **Reproducible analysis tooling.** Python for screening and analysis; document and figure builders driven from a single specification so two outputs cannot drift | `dba/03_Data/`, `dba/coursework/_templates/` |
| 8 | **Evidentiary discipline.** Nothing asserted without a primary source; unresolved items carry a `[VERIFY]` tag and are claimed nowhere; the public record includes what did not work | This repository, and the failure written into its front page |

---

## 5 · The same fact, in three voices

**Use one column. Never two.** The academic CV and the industry résumé must not appear in the same
message, application or email — an industry recruiter reading the academic CV sees someone leaving
for academia, and a department chair reading the industry résumé sees a consultant passing through.

| The fact | **Professional** (model risk, audit, assurance) | **Academic** (search committee) | **Business** (advisory, consulting) |
|---|---|---|---|
| The three-link chain | Built a risk taxonomy separating human automation bias from model sycophancy from system-level epistemic drift, mapped to review controls | Develops a conceptual model of recursive epistemic degradation in professional judgment, with each link stated against its strongest counter-evidence | Diagnoses why AI-assisted review can pass every model validation and still degrade the judgment it was meant to support |
| The failed survey | Identified, quantified and documented a structural sampling constraint before budget commitment, converting a project risk into a pre-flight check | Negative methodological finding: specialist professional populations at ~6 per 100,000 prevalence cannot be reached through general research infrastructure at any price | Built a go/no-go calculator that prices a study's weakest market before anyone signs a vendor contract |
| The instrument | Designed and fielded a 55-item control-effectiveness instrument across eight intervention categories under institutional ethics approval | Multi-construct measurement model, 11 constructs and 16 hypotheses, EFA with PAF and oblimin rotation, higher-order models specified | Turned eight commonly claimed audit-quality controls into something a firm can actually measure rather than assume |
| The qualitative pivot | Redesigned the study around what the population can supply rather than what the method preferred | Method as a function of population feasibility rather than of researcher preference; phenomenological protocol with falsification conditions stated in advance | Twenty reachable people is a failed survey and a well-powered interview study. Knowing which you have is worth more than the budget |
| The runbooks | Governance tooling for AI-assisted research: provenance on every claim, adversarial review of the tool's own output | A working demonstration of the L2 argument: a pipeline that refuses to confirm its operator | A repeatable research process that does not quietly agree with whoever is paying for it |
| The public repository | Working record with auditable decisions, versioned, with unresolved items flagged rather than smoothed | Open research practice: the record includes the study that did not work, and why | Evidence of how the work is actually done, not a portfolio of finished things |

---

## 6 · What must never be claimed

Taken from `CLAUDE.md` and enforced everywhere.

- ❌ A DBA completion year, or a GPA, until the program office confirms them
- ❌ That the dissertation is complete
- ❌ That the AI extension has findings. It has an argument
- ❌ Peer-reviewed publications. There are none to date
- ❌ Teaching evaluations. There are none
- ❌ Professional memberships that are unconfirmed
- ❌ Contact details, salary figures, or the PID anywhere in this public repository

**And one positive obligation.** The recruitment failure is the strongest thing in the record
because it is documented, quantified and unflattering. Every version of every document should carry
it. A record that lists only what worked is a brochure, and reviewers in all three audiences can
tell the difference.

---

## 7 · Where each document gets built

| Document | Lane | Location |
|---|---|---|
| Academic CV, research statement, teaching statement | 🎓 **Scholar** | `career/academic/`, `career/ACADEMIC_CV_YMalik.md` |
| Professional résumé, model risk and audit leadership | 💼 **Industry** | `career/applications/` — **not Scholar's to write** |
| Business and advisory positioning | 💼 **Industry** | `career/applications/`, `career/AUTOMATION_ROADMAP.md` |
| This record | 🎓 Scholar | `dba/RESEARCH_RECORD.md` — the shared factual source all three draw from |

A handoff entry has been posted so the Industry agent can build the professional and business
versions from this record rather than from memory.

---

## 8 · References

Verified against the reference list of the submitted manuscript, where each carries a DOI.

- Commerford, B. P., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man versus machine: Complex estimates and auditor reliance on artificial intelligence. *Journal of Accounting Research, 60*(1), 171–201.
- Creswell, J. W., & Poth, C. N. (2024). *Qualitative inquiry and research design: Choosing among five approaches* (5th ed.). SAGE.
- Fotoh, L. E., & Mugwira, T. (2025). Exploring the impact of generative AI on professional skepticism in auditing.
- Glickman, M., & Sharot, T. (2025). How human-AI feedback loops alter human perceptual, emotional and social judgements.
- Kokina, J., Blanchette, S., Davenport, T. H., & Pachamanova, D. (2025). Challenges and opportunities for artificial intelligence in auditing: Evidence from the field. *International Journal of Accounting Information Systems, 56*, 100734.
- Murikah, W., Nthenge, J. K., & Musyoka, F. M. (2024). Bias and ethics of AI systems applied in auditing: A systematic review.
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410.
- Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., & Bowman, S. R., et al. (2024). Towards understanding sycophancy in language models. *ICLR.*
- Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131.

---

## 9 · Two things to reconcile before anyone relies on them

1. **The AIB Latin America dates.** `RESEARCH.md` records a submission window of 20 November 2026.
   The 19 September residency minutes record a conference-portal deadline of 30 September 2026 with
   notifications mid-November and the conference on 3 to 5 March 2027 in San Juan. One of those is
   the paper track and one is the consortium. **Confirm which before citing either.**
2. **The public integrity items.** `README.md` and `index.html` still carry the OCC line, a GPA, a
   2027 completion year and a twenty-year tenure. All four are wrong or unconfirmed, all four are
   public, and all four sit in the Industry lane. They are on the handoff board.
