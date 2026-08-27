# FIU University Graduate School — AI guidelines

**Source:** *Guidelines for the Use of AI in Graduate Research, Theses, and Dissertations*, FIU
University Graduate School. Circulated by **Dr. René M. Price**, Associate Dean UGS / Associate VP
Research and Economic Development.
**Official copy:** https://gradschool.fiu.edu/wp-content/uploads/2026/01/Guidance-for-the-Effective-and-Responsible-use-of-AI-in-Dissertations.pdf
**Also at:** gradschool.fiu.edu → Current Students → Research Integrity

**Status: binding.** This is university policy, above the course syllabi and above Dr. Rey's
instruction. Both remain in force — programs *may* set stricter standards, and the stricter one wins.

---

## 1 · The thing worth noticing first

UGS §7, *Risks and Limitations of Generative AI*, lists as an unavoidable property of LLMs:

> **"Obsequiousness: Tendency to agree, reinforce user assumptions, or provide overly confident
> answers."**

**That is L2.** Sycophancy, named as a documented risk, in an official Florida International
University policy document, signed by the Associate Dean of the Graduate School.

The same section also names:

| UGS §7 | The chain |
|---|---|
| **Obsequiousness** — agrees, reinforces user assumptions | **L2 — sycophantic confirmation** |
| **Poor self-awareness** — "the model does not know what it does not know" | Supports L1 and L3 |
| **Confabulations** — confidently presenting fabricated facts | The verification burden the whole programme argues for |
| **Bias** — outputs reproduce training-data bias | Context for the programme |
| **Randomness** — responses vary by prompt or session | Reproducibility problem the runbook schemas address |

**Why this matters beyond compliance.** The L2 link has been argued from model-evaluation
literature and never from an institutional source. This is one — and it is Yasir's own university,
which makes it usable in the practice section of the dissertation and in front of a committee that
answers to the same graduate school.

⚠️ **It does not make L2 established.** A policy document naming a risk is not empirical evidence
that the risk operates in audit judgment. It is a citable institutional acknowledgement that the
phenomenon is real and recognised. Say it that way and nothing else.

---

## 2 · What is now required of every submission

| Requirement | UGS § |
|---|---|
| **Disclose all AI use** — research, writing, data analysis, coding, graph making, figure creation, **exam preparation** | 3.1 |
| **Preserve original unedited drafts** | 3.1, 6 |
| Disclosure names the **specific tools**, the **purpose and scope**, and the **components produced with AI** | 5.2 |
| Disclosure appears in the **preliminary pages** (Acknowledgements or Preface) of every proposal draft, every thesis/dissertation draft, and the final ETD | 5.3 |
| AI used in **data analysis** must also appear in the **Methods section** | 5.3 |
| AI used in **figures or visualisations** must be **cited in the figure caption** | 5.3 |
| The committee **reviews and approves** the AI use | 3.2, 5.1 |

**Never:** upload confidential, sensitive, identifiable, proprietary or restricted data to public AI
platforms (§9). Comply with IRB, HIPAA, FERPA. Check the FIU prohibited-technologies list:
https://security.fiu.edu/resources/prohibited-technologies/

---

## 3 · Where this repository already complies

| Requirement | Where it is already met |
|---|---|
| **Preserve original unedited drafts** | ✅ **Git history.** Every draft is timestamped and immutable, and force-push is prohibited. This is stronger than the requirement asks for — most students cannot demonstrate draft provenance at all |
| Log AI use as it happens | ✅ `../QUALITATIVE/AUDIT_TRAIL.md`, tagged `AI`, dated |
| Bound what AI may touch | ✅ `../QUALITATIVE/CODING_PLAN.md` — AI may not assign a code, name a theme, or write any interpretation |
| Verify everything | ✅ `../AI_RUNBOOKS/SCHEMAS.md` — resolving URLs required, `read_state: lead` until read in full |
| No identifiable data to public platforms | ✅ `CODING_PLAN.md` — no transcript, recording or linking key ever leaves the local machine |

**The audit trail was built before this policy arrived and happens to satisfy it.** That is worth
saying to a committee.

---

## 4 · What still has to change

- [ ] **Write the disclosure statement** into the preliminary pages of the qualitative proposal
      before it goes to Dr. Gonzalez. Template in §5 below.
- [ ] **Ask Dr. Rey to review and approve** the AI use — §3.2 makes committee approval a
      requirement, not a courtesy. Nothing in the record shows this has been done.
- [ ] **Check the DBA programme handbook** for programme-specific standards. §1 says programmes may
      add stricter rules and the student must follow both.
- [ ] **Check the prohibited-technologies list** before any new tool enters the workflow.
- [ ] **Figure captions** — any chart generated with AI assistance needs the tool cited in the
      caption. That includes the deck figures if they enter a submitted document.

---

## 5 · Disclosure statement — draft, to be completed honestly

⚠️ **This is a template. Complete it truthfully before use — an inaccurate disclosure is worse than
none.** The bracketed parts are the parts only Yasir can fill.

> **Artificial Intelligence (AI) tools were utilized in the preparation of this
> [proposal / dissertation].**
>
> **Claude (Anthropic), via Claude Code,** was used to organise source material, draft and format
> research infrastructure documents, and produce data visualisations and figures. It was also used
> to check quotations and reported figures against the source PDFs.
>
> **[NAME ANY OTHER TOOL — e.g. NotebookLM, ChatGPT, Perplexity]** was used for
> **[STATE THE PURPOSE HONESTLY]**.
>
> AI assistance was **not** used to generate the research questions, the analytic decisions, the
> interpretation of data, or the argument. Coding, theme naming and all interpretive work were
> performed by the author; the boundary is documented in `dba/QUALITATIVE/CODING_PLAN.md` and every
> instance of AI use is dated in `dba/QUALITATIVE/AUDIT_TRAIL.md`.
>
> Original unedited drafts are preserved in the version history of the public repository
> `github.com/AuditingAI/Profile`.
>
> **All AI use was reviewed and approved by my committee.** ← ⚠️ **DO NOT INCLUDE THIS SENTENCE
> UNTIL IT IS TRUE.** Ask Dr. Rey first.

---

## 6 · The uncomfortable symmetry, stated plainly

This programme argues that professionals defer to systems that agree with them, and that the
deference is hard to see from inside. The university has now told every graduate student, in
writing, that these systems are obsequious.

**The disclosure requirement and the research question are the same problem.** A study of AI-induced
deference, drafted with AI assistance, has to be able to show where the line was — which is what the
audit trail and the coding boundary exist for. That is not a compliance detail. It is the
methodological core of the qualitative arm, and it should be said out loud in the proposal rather
than left for a committee member to notice.
