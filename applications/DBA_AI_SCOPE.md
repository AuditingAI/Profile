# DBA Scope Expansion — Adding an AI Layer that Doubles as a Career Asset
> **Status note (2026-07-26):** this document describes a *dissertation direction under
> development*. It is not an approved topic. The approved, completed work is the qualifying
> research project *Mitigating Anchoring Bias in Long-Term Auditor Engagements* (IRB-25-0462,
> completed July 2026). Do not cite anything below as an approved dissertation or as
> IRB-approved.


Goal: make the DBA pull double duty as **academic credential + market signal**
for AI assurance / governance roles. Right now the dissertation topic
("Epistemic Drift & Sycophancy Risk in LLM-Assisted Audit Judgment") is
excellent academically but invisible commercially. The expansion below keeps
the dissertation intact and adds a public-artifact layer that recruiters,
hiring managers, and regulators will recognize.

## 1. The current state, honestly

**Strengths**
- Topic is novel, defensible, and directly aligned with what Anthropic, NIST,
  the EU AI Office, and FS regulators are publishing about.
- Mixed-methods design (the right design) is implicit in the title — make it explicit.
- You already operate at the practitioner / researcher seam (consultancy +
  doctoral work). Few candidates do.

**Gaps that limit commercial leverage**
- No public artifact yet. "DBA candidate" reads as a credential in progress;
  "DBA candidate + author of *Auditing LLMs in Regulated Settings*" reads as a thought leader.
- Methodology not visible in the resume — recruiters can't tell whether your
  research is qualitative interviews, behavioral experiments, or technical
  benchmarking. Different audiences value different answers.
- No tie to the existing AI auditing literature (Mökander et al.'s three-layer
  framework, Anthropic's RSP, NIST GenAI Profile). Citing these in your
  dissertation framing positions you inside the conversation.

## 2. Proposed scope additions — pick 2 or 3, not all four

### A. Empirical sycophancy-drift benchmark (highest leverage)

Build a small but publishable benchmark — say **100–200 audit scenarios** —
that measures the gap between (a) an auditor's unaided judgment, (b) the
auditor's judgment after LLM assistance, and (c) ground-truth. Publish it.

- **Why it matters for your career:** a published benchmark is the single
  most cited artifact in AI safety / evals work. The Anthropic Trust &
  Safety, OpenAI Preparedness, and NIST AI evals teams all hire on benchmark
  authorship.
- **Tractability:** doable inside the dissertation; collaborate with FIU
  accounting faculty for the auditor cohort.
- **Suggested name / framing:** *Audit Judgment Drift Benchmark (AJDB)*.
- **Output:** dataset on Hugging Face + arXiv preprint + 1 conference paper
  (AI & Ethics, FAccT, or NeurIPS Safety workshop).

### B. The three-layer audit framework, applied to a regulated FS deployment

Mökander, Schuett, Floridi, et al. (2023) proposed a three-layer LLM audit
model (governance / model / application). No one has translated it to a
**bank-supervisory** context yet. You are the right person to do it.

- **Why it matters:** gives bank examiners a vocabulary they
  don't currently have, and gives you a co-authoring opportunity with the
  original authors.
- **Output:** white paper / law-review-style essay co-published with one of
  the named authors, plus a 1-page regulator brief.
- **Career signal:** establishes you as the bridge between AI audit theory
  and supervisory practice — exactly the niche the Citi MD role is built around.

### C. Practitioner playbook — open-sourced

Take your *Audit the Algorithm* methodology, anonymize, and release a
GitHub-hosted **AI Audit Playbook** with:

- Control library mapped to NIST AI RMF + SR 11-7 + ISO/IEC 42001.
- Workpaper templates for governance / model / application audits.
- Evaluation scripts (Python) for bias, drift, sycophancy, jailbreak,
  hallucination.

- **Why it matters:** every recruiter you talk to will Google you. Code on
  GitHub answers the "is this person actually technical?" question instantly.
- **Tractability:** much of this exists in your client work — the lift is
  redaction + packaging, not net-new creation.

### D. A teaching artifact (lowest priority, highest signaling-per-hour)

Convert the dissertation framing into a **short FIU course or executive
education module**: *AI Audit & Governance for Financial Services*. Even
one cohort (10–15 students or executives) gives you:

- A second public artifact (syllabus, recorded lectures).
- "Adjunct faculty" or "guest lecturer" line that hits hiring managers' bias
  filters in a useful way.
- A defensible reason to be on LinkedIn weekly without it feeling forced.

## 3. Reframing the dissertation title (small change, big effect)

Current: *Epistemic Drift & Sycophancy Risk in LLM-Assisted Audit Judgment*.

The risk of this title for non-academic audiences: "epistemic" is
philosophy-coded, and "sycophancy" doesn't land outside AI safety. Two
alternative framings that keep the substance and travel better:

- **For regulator and big-tech audiences:** *Auditing the Auditor: Measuring
  and Controlling LLM-Induced Judgment Drift in Regulated Decision-Making*.
- **For frontier-lab audiences (Anthropic, OpenAI):** *Sycophancy and
  Epistemic Drift in High-Stakes LLM Assistance: A Benchmark and Control
  Framework for Audit Judgment*.

Both keep "sycophancy" in the second-position phrase — important for AI
safety SEO — but lead with what the work *does* (measurement + control)
rather than what it studies (drift).

## 4. Suggested coursework / cert additions during the DBA

Pick the ones that *also* show up on the Citi MD / Anthropic / Google JDs:

- **IAPP AIGP** — AI Governance Professional. ~4 weeks. The credential.
- **CIA Part 1** — Internal Audit credential, ~6 weeks. Closes the most-cited resume gap.
- **MLOps fundamentals** — one of the free Google or AWS MLOps specializations. Just enough to defend "MLOps awareness" on the resume.
- **Optional: GIAC GAII** (AI ethics-focused) or **AICPA AI in Audit** — only if budget allows.

Decline: a second master's, generic AI bootcamps you've already exceeded,
and any cert that doesn't appear in target JDs.

## 5. Publication calendar (12 months)

A realistic cadence that doesn't require you to leave your job:

| Month | Output | Audience |
|---|---|---|
| 1 | LinkedIn long-form: "What we mean when we say an LLM is sycophantic — and why auditors should care" | Recruiter-visible signal |
| 3 | arXiv preprint: short benchmark proposal (1500 words) | Anthropic / NIST / OpenAI eval teams |
| 6 | Co-authored white paper applying three-layer audit framework to FS supervision | Regulators, FS CAEs |
| 9 | Open-source AI Audit Playbook v0.1 on GitHub | Hiring managers, peer practitioners |
| 12 | Conference paper submission (AI & Ethics, FAccT, or workshop at NeurIPS) | Academic credibility |

If you only do **one**, do the benchmark + arXiv preprint at month 3. It is
the single highest-leverage move for both your dissertation and your career.

## 6. How this maps back to the three target lanes

- **Citi MD / Guardian DAACA / FS AI Assurance** → items B (three-layer
  framework applied to FS) + C (playbook) hit hardest.
- **Google AI Compliance** → items A (benchmark) + C (playbook) demonstrate
  scaled, repeatable, evidence-driven program design.
- **Anthropic / frontier labs** → item A (benchmark) is the single most
  important artifact. Lab hiring runs on evals authorship.

## 7. What to do this week

1. Pick one of (A, B, C) — recommend **A** + **C**, defer B and D.
2. Reserve a calendar block — 4 hrs Saturday for the next 8 weeks.
3. Tell your DBA chair you intend to expand scope to include a published
   benchmark; get their sign-off before sinking work in.
4. Draft the LinkedIn long-form (month 1 in the table above). Even unpublished,
   the draft sharpens the rest of the work.
