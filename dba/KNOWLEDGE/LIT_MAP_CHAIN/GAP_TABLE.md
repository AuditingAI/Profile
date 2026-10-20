# Gap table: the three-link chain against the literature

Built 2026-10-20. One row per verified card in `cards/`. Method and verification notes in `README.md`.

**Coding rule.** *Tested* = the study measures the link's mechanism directly (system or model output moving a human judgment for L1; a model confirming a stated user position, with or without the human response, for L2; judgments or outputs converging across people or rounds for L3). *Partly* = a component or analogue (human-supplied anchor, model side only, single round, theory only, or analogy). *Not* = does not bear on the link. Codes describe what each paper measured, not whether its result supports the chain.

| Citation | Population | Design | L1 anchor | L2 confirm | L3 converge | One-line relevance |
|---|---|---|---|---|---|---|
| Joyce & Biddle (1981), *JAR* | Auditors | Experiments | Partly | Not | Not | Founding evidence that auditors anchor; anchor is human-set (not read beyond purpose) |
| Kinney & Uecker (1982), *TAR* | Auditors (not verified) | Not verified | Partly | Not | Not | Anchoring mitigation in audit; **unread**, cite for nothing specific yet |
| Presutti (1995), *MAJ* | Auditors (public firm and government) | Experiment | Partly | Not | Not | Prior-year results in continuing engagements; prior-year info appeared to weaken anchoring |
| Tan (1995), *JAR* | Auditors | Experiments | Partly | Not | Not | Prior involvement aligns judgment with prior-year papers; review awareness as moderator (dissertation abstract only) |
| Fay, Jenkins & Popova (2015), *MAJ* | Auditors (n = 64) | 2x2 experiment | Partly | Not | Not | Continuing auditors anchor on prior-year audit strategy |
| Henrizi et al. (2021), *JAAR* | Auditors (n = 85) | Experiment | Partly | Not | Not | Recent expert replication; firm size, experience and bias knowledge moderate |
| Skitka, Mosier & Burdick (1999), *IJHCS* | Students (per secondary source) | Simulation experiment | Tested | Not | Not | Automation as heuristic replacement for vigilant search; omission and commission errors |
| Parasuraman & Manzey (2010), *Human Factors* | Mixed, incl. experts | Review and model | Tested | Not | Not | Automation bias in naive and expert users, not prevented by training |
| Goddard, Roudsari & Wyatt (2012), *JAMIA* | Clinicians (reviewed studies) | Systematic review | Tested | Not | Not | Better on average, new errors from over-reliance |
| Dietvorst, Simmons & Massey (2015), *JEP: General* | Lay | 5 experiments | Partly | Not | Not | Algorithm aversion after seeing errors: the counter-mechanism to L1 |
| Logg, Minson & Moore (2019), *OBHDP* | Lay, plus forecasting professionals | 6 experiments | Partly | Not | Not | Lay appreciation of algorithms; experts and self-vs-algorithm choices rely less |
| Commerford et al. (2022), *JAR* | Auditors | Experiment | Partly | Not | Not | Auditors discount contradictory AI evidence vs human specialist: aversion, not anchoring |
| Estep, Griffith & MacKenzie (2024), *RAST* | Financial executives | Survey and experiment | Partly | Not | Not | Client managers book larger adjustments when both sides use AI |
| Libby & Witz (2024), *CAR* | Jurors (per secondary description) | Experiment | Not | Not | Not | Liability context; AI use may reduce perceived independence harm (weakly verified) |
| Rastogi et al. (2022), *PACM HCI (CSCW)* | Crowdworkers (n = 47, Exp. 1) | 2 experiments | Tested | Not | Not | AI prediction as explicit anchor; more time, more adjustment |
| Rosbach et al. (2026), *MELBA* | Pathology experts (n = 28) | Within-subject experiment | Tested | Not | Not | Experts anchor on AI; worse under time pressure; experience reduces dependence |
| Perez et al. (2023), *Findings of ACL* | LLM-only | Model-written evaluations | Not | Partly (model side) | Not | Larger and more RLHF-trained models repeat the user's preferred answer |
| Sharma et al. (2024), *ICLR* | LLM-only, plus human preference data | Model evaluations and preference analysis | Not | Partly (model side, plus human preference) | Not | Sycophancy general across assistants; humans prefer agreeing answers |
| Wei et al. (2023), arXiv **[preprint]** | LLM-only | Model evaluations and fine-tuning | Not | Partly (model side) | Not | Models agree with known-false user claims; sycophancy is patchable |
| Cheng et al. (2026), *Science* | LLMs plus lay participants (N = 2,405) | Model audit plus 3 preregistered experiments | Not | Tested | Partly | Models affirm users; people trust them more and grow more convinced |
| Batista & Griffiths (2026), arXiv **[preprint]** | Lay (n = 557) | Bayesian analysis plus experiment | Not | Tested | Partly | Sycophancy raises confidence without progress toward truth |
| Jakesch et al. (2023), *CHI* | Lay (N = 1,506) | Online experiment | Tested | Not | Partly | Opinionated assistant shifts what people write and believe |
| Glickman & Sharot (2025), *Nat. Hum. Behav.* | Lay (n = 1,401) | Series of experiments | Tested | Not | Partly | Human-AI feedback loop amplifies bias; users underestimate AI influence |
| Doshi & Hauser (2024), *Science Advances* | Lay writers (n = 293) plus evaluators | Preregistered experiment | Partly | Not | Partly | Better individual output, more similar collective output |
| Padmakumar & He (2024), *ICLR* | Lay writers | Controlled experiment | Not | Not | Partly | Feedback-tuned model homogenises co-written essays |
| Kleinberg & Raghavan (2021), *PNAS* | None (theory) | Formal model | Not | Not | Partly | Shared algorithm can lower collective accuracy while helping each user |
| Bommasani et al. (2022), *NeurIPS* | Model-only | Benchmark experiments | Not | Not | Partly | Shared data and models homogenise outcomes across decision-makers |
| Shumailov et al. (2024), *Nature* | Model-only | Simulation and training experiments | Not | Not | Partly (analogy only) | Recursive training loses distribution tails |
| Vaccaro, Almaatouq & Malone (2024), *Nat. Hum. Behav.* | Mixed (106 studies) | Meta-analysis | Partly | Not | Not | Human plus AI worse than best alone in decision tasks |

**Counts (29 papers).** L1: 7 tested, 12 partly. L2: 2 tested, 3 partly. L3: 0 tested, 9 partly. Auditor samples: 7 papers, all L1 partly; audit-adjacent samples (executives, jurors): 2. None of the nine touches L2 or L3.

---

## Where the gaps are

*Draft for Yasir to rewrite. Descriptive only; the chain has no findings.*

1. **No auditor study puts system output before the auditor's own view.** Every audit-sample anchoring paper here uses a human-supplied anchor (prior-year results, prior-year strategy, experimenter numbers). The one auditor-AI experiment reached (Commerford et al., 2022) presents AI as contradictory evidence after management's estimate, and auditors discount it. Expert anchoring on AI output does exist, but in pathology (Rosbach et al., 2026).
2. **L2 has no professional-sample evidence at all.** Sycophancy is measured on models (Perez; Sharma; Wei) and its human effects only on lay participants in interpersonal or abstract tasks (Cheng; Batista & Griffiths). No study found has a professional state a position on evidence and then measures whether model confirmation changes the final judgment.
3. **L1 and L2 have never been tested together.** No paper found combines a reviewer's deference to system output with a model that confirms the reviewer's stated position, which is the "push the same way" claim.
4. **L3 has no direct test.** Convergence evidence is single-round homogenisation with lay writers (Doshi & Hauser; Padmakumar & He), formal or model-only work (Kleinberg & Raghavan; Bommasani et al.), and model collapse as analogy (Shumailov et al.). None is recurring, none uses professionals, and none separates convergence on the model from convergence on evidence. Glickman & Sharot and Batista & Griffiths come closest on mechanism (loops, confidence without accuracy).
5. **Direction of reliance is unresolved for experts.** Auditors discounted AI (Commerford), experienced forecasters discounted algorithms (Logg), and aversion follows visible errors (Dietvorst), while experts still anchored on AI in pathology (Rosbach). Candidate boundary conditions named in these sources: input objectivity, expertise, time pressure, and whether errors are visible. This bears directly on the open item in `01_THEORY.md` §3.

Also worth recording: the prior-year anchoring evidence itself is mixed (Presutti 1995 found prior-year information weakened anchoring; Fay et al. 2015 found continuing auditors anchor).

**Search limitation.** A targeted search for peer-reviewed experiments on auditors using generative AI returned only a PCAOB conference proposal, practitioner pieces and regulator papers. That is weak evidence of absence: accounting databases (SSRN full search, AAA Digital Library, Scopus) were not queried directly from this session.
