# Reading List — Algorithmic Auditing of AI/LLMs

A curated subset of the broader filtered list (`scholar-links-filtered.md`), selected for methodological depth and topical breadth. Read in roughly this order: foundations → methodology → sub-area deep-dives.

## 1. Start here — surveys & foundational frameworks (read first, ~5 papers)

These give you the landscape and vocabulary.

- **[Human-Centered and Participatory AI Auditing](https://link.springer.com/content/pdf/10.1007/978-981-97-8440-0_102-1.pdf)** — WH Deng, K Holstein, M Eslami, Handbook of Human-Centered AI, 2026
  *Why: Authoritative survey from the CMU/HCI auditing group; defines participatory audit methodology and the trade-offs in user-driven auditing.*
- **[A Systematic Review on Human Roles, Solutions, and Methodological Approaches to Address Bias in AI](https://www.cise.ufl.edu/~eragan/papers/Hashky_CSUR_2026.pdf)** — A Hashky, ED Ragan, 2025
  *Why: Comprehensive taxonomy of bias-mitigation solutions across the AI lifecycle — best one-stop survey for orienting yourself.*
- **[Bias in Large Language Models: Origin, Evaluation, and Mitigation](https://search.proquest.com/openview/f9ec704bb302a28cc072da406da0ad01/1)** — G Yufei et al., Electronics, 2026
  *Why: Documented, reproducible review of LLM bias origins, eval methods, and mitigations.*
- **[Fairness at Risk: Where Bias Emerges in Machine Learning](https://onlinelibrary.wiley.com/doi/pdf/10.1111/exsy.70265)** — OP Albuquerque et al., Expert Systems, 2026
  *Why: Maps bias sources across the ML lifecycle into a taxonomy that spans all development stages, including cognitive bias.*
- **[A Comprehensive Review of Bias in AI, ML, and DL Models: Methods, Impacts, and Future Directions](https://link.springer.com/article/10.1007/s11831-025-10483-6)** — A Kumar et al., Archives of Computational Methods in Engineering, 2025
  *Why: Springer review tracing how bias propagates through the full AI lifecycle with attention to scalable fairness auditing.*

## 2. Audit methodology & frameworks (~8 papers)

Frameworks for HOW to audit AI systems — these are the methodological backbone.

- **[Beyond Bias Detection: Community Auditors and Normative Reasoning in AI Oversight](https://dl.acm.org/doi/pdf/10.1145/3788042)** — C Jackson et al., CSCW (PACM HCI), 2026
  *Why: Reframes algorithmic auditing to include normative judgment by community auditors — major venue (PACM HCI).*
- **[The Audit Gap: Why Existing Assurance Frameworks Fail for AI Systems and What Comes Next](https://www.researchgate.net/profile/Ali-Shaik-3/publication/405022752_The_Audit_Gap_Why_Existing_Assurance_Frameworks_Fail_for_AI_Systems_and_What_Comes_Next/links/6a0c821c9d7cce6f5c759a85/The-Audit-Gap-Why-Existing-Assurance-Frameworks-Fail-for-AI-Systems-and-What-Comes-Next.pdf)** — AS Shaik, 2026
  *Why: Sharp critique of control-based audit frameworks (NYC LL144, ISO) and what's missing in evaluation depth.*
- **[A Scalable Entity-Based Framework for Auditing Bias in LLMs](https://arxiv.org/pdf/2601.12374)** — A Elbouanani, A Tuo, A Popescu, arXiv 2601.12374, 2026
  *Why: Uses named entities as probes to measure structural disparities — a clean scalable audit methodology.*
- **[Auditing Fairness under Model Updates: Fundamental Complexity and Property-Preserving Updates](https://arxiv.org/pdf/2601.05909)** — A Ajarra, D Basu, arXiv 2601.05909, 2026
  *Why: Tackles the underexplored problem of how fairness audits hold up under continual model updates.*
- **[BiAxisAudit: A Novel Framework to Evaluate LLM Bias Across Prompt Sensitivity and Response-Layer Divergence](https://arxiv.org/pdf/2605.09041)** — J Gan, J Dong, S Li, arXiv 2605.09041, 2026
  *Why: Empirical finding that task format alone explains as much bias variance as model choice; 63.6% of signals appear in only one coding layer — important for audit design.*
- **[The Dice Roll Method: A Standardized Protocol for Measuring Stochastic Bias in Large Language Model Outputs](https://www.researchsquare.com/article/rs-8980233/latest)** — D Żatuchin, 2026
  *Why: Formalizes the repeated-prompt method as an audit protocol with minimum methodological standards.*
- **[Quantifying the Gaps: A Systematic Taxonomy of Bias and Imbalance in 96 Multilingual AI Benchmarks & Datasets](https://www.researchgate.net/profile/Sankalp-Jajee/publication/399995100_Quantifying_the_Gaps_A_Systematic_Taxonomy_of_Bias_and_Imbalance_in_96_Multilingual_AI_Benchmarks_Datasets/links/69726a71ac604d40d0e50a42/Quantifying-the-Gaps-A-Systematic-Taxonomy-of-Bias-and-Imbalance-in-96-Multilingual-AI-Benchmarks-Datasets.pdf)** — S Jajee, T Shaw, V Soni, 2026
  *Why: Meta-audit of 96 multilingual benchmarks themselves — essential context before trusting any LLM eval.*
- **[Automating Auditing of Personalization Systems at Scale with Large Language Models](https://www.charapodimata.com/files/Auditing_with_LLMs-april2026.pdf)** — A Morosini, SH Cen, A Ilyas, A Madry et al., 2026
  *Why: Madry-group (MIT) framework using LLMs to scale platform audits; addresses the Hawthorne-effect problem in audit research.*

## 3. LLM bias audits (~9 papers)

Empirical audits of large language model biases — political, demographic, cultural, sycophancy, etc.

- **[Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor](https://arxiv.org/pdf/2604.27633)** — P Törnberg, M Schimmel, arXiv 2604.27633, 2026
  *Why: Shows that "political bias" measurements partly reflect sycophancy toward the auditor — methodologically important caveat for the whole field.*
- **[Redirected, Not Removed: Task-Dependent Stereotyping Reveals the Limits of LLM Alignments](https://arxiv.org/pdf/2604.02669)** — D Kumar et al., arXiv 2604.02669, 2026
  *Why: Audits 7 commercial/open-weight LLMs with ~45K prompts across 9 bias types including under-studied axes (caste, linguistic, geographic).*
- **[Evidence of political bias in search engines and language models before major elections](https://arxiv.org/pdf/2603.23474)** — Í Damião et al., arXiv 2603.23474, 2026
  *Why: Privacy-preserving, bot-and-proxy audit methodology applied to four LLMs/search engines before elections — concrete findings, replicable design.*
- **[Different demographic cues yield inconsistent conclusions about LLM personalization and bias](https://sharathg.cis.upenn.edu/assets/pdf/76_hrfUAAAAJ_FAceZFleit8C.pdf)** — M Tonneau et al., 2026
  *Why: Demonstrates that audit conclusions about LLM bias depend heavily on which demographic cues are used — methodological warning.*
- **[Sima AIunty: Caste Audit in LLM-Driven Matchmaking](https://arxiv.org/pdf/2603.29288)** — A Naik, S Kar, V Sharma, A Rajadesingan, K Saha, arXiv 2603.29288, 2026
  *Why: Controlled audit of caste bias (Brahmin → Dalit) in LLM matchmaking — concrete findings on an under-audited axis.*
- **[Race and Gender in LLM-Generated Personas: A Large-Scale Audit of 41 Occupations](https://arxiv.org/pdf/2510.21011)** — I van der Linden et al., arXiv 2510.21011, 2025
  *Why: Large-N occupational bias audit with a clean regression framework for separating systematic skew from amplification.*
- **[Which English Do LLMs Prefer? Triangulating Structural Bias Towards American English in Foundation Models](https://arxiv.org/pdf/2604.04204)** — MT Nayeem, D Rafiei, arXiv 2604.04204, 2026
  *Why: Audits six major pretraining corpora directly, grounding LLM dialect bias in data-level evidence.*
- **[How Can You Tell if Your Large Language Model Could Be a Closet Antisemite? An Explainability-Based Audit Framework for Implicit Bias](https://ojs.aaai.org/index.php/AAAI/article/view/41181/45142)** — A Dutta, R Fayyazi, S Yang, AR KhudaBukhsh, AAAI 2026
  *Why: AAAI paper introducing an explainability-based audit that doesn't require harmful-request compliance — clever methodological move.*
- **[Language Models Generate Widespread Intersectional Biases in Narratives of Learning, Labor, and Love](https://conference2025.eaamo.org/conference_information/accepted_papers/papers/language_models_generate_widespread_intersectional_biases.pdf)** — E Shieh et al., EAAMO 2025
  *Why: 500K-story dataset enabling intersectional bias audit — released for replication; top-tier venue (EAAMO).*

## 4. Vision-language & text-to-image audits (~6 papers)

VLM/CLIP/T2I model bias audits.

- **[Locating Demographic Bias at the Attention-Head Level in CLIP's Vision Encoder](https://arxiv.org/pdf/2603.11793)** — A Yasser et al., arXiv 2603.11793, 2026
  *Why: Mechanistic fairness audit using projected residual streams + CAVs + bias-augmented TextSpan — moves from "is the model biased" to "where in the network."*
- **[T2I-BiasBench: A Multi-Metric Framework for Auditing Demographic and Cultural Bias in Text-to-Image Models](https://arxiv.org/abs/2604.12481)** — N Jaiswal et al., arXiv 2604.12481, 2026
  *Why: Unified 13-metric framework jointly capturing demographic, cultural, and element bias in T2I — a reusable benchmark.*
- **[Breaking Language Barriers or Reinforcing Bias? A Study of Gender and Racial Disparities in Multilingual CLIP](https://www.researchgate.net/profile/Zahraa_Al_Sahili/publication/391911086_Breaking_Language_Barriers_or_Reinforcing_Bias_A_Study_of_Gender_and_Racial_Disparities_in_Multilingual_Contrastive_Vision_Language_Models/links/68c482989534473a6d4a8adb/Breaking-Language-Barriers-or-Reinforcing-Bias-A-Study-of-Gender-and-Racial-Disparities-in-Multilingual-Contrastive-Vision-Language-Models.pdf)** — Z Al Sahili, I Patras, M Purver
  *Why: First systematic audit of four multilingual CLIP variants — clean comparative design.*
- **[Bias at the End of the Score](https://arxiv.org/pdf/2604.13305)** — SA Magid, G Guo, E Tureci, A Dharmasiri et al., arXiv 2604.13305, 2026
  *Why: Large-scale audit of reward-model robustness w.r.t. demographic biases during T2I training and generation — connects RM design to downstream bias.*
- **[Surgeons Are Indian Males and Speech Therapists Are White Females: Auditing Biases in Vision-Language Models for Healthcare Professionals](https://arxiv.org/pdf/2510.06280)** — ZH Siddiqui et al., arXiv 2510.06280, 2025
  *Why: Healthcare-specific VLM audit with operational risk framing — concrete findings across multiple vision models.*
- **[Generative AI So White: Racial Biases in AI Imagery Across the United States and China](https://journals.sagepub.com/doi/pdf/10.1177/10755470261428542)** — Z Wang et al., Science Communication, 2026
  *Why: Scalable cross-national auditing protocol for T2I; expands the unit of analysis from text to visual infrastructure.*

## 5. High-stakes deployed AI audits (~6 papers)

Audits of AI in hiring, lending, healthcare, criminal justice, education.

- **[Auditing demographic bias in AI-based emergency police dispatch: a cross-lingual evaluation of eleven large language models](https://arxiv.org/pdf/2605.01451)** — W Guey, W Zhang, P Bougault, Y Wang, B Ucar, arXiv 2605.01451, 2026
  *Why: LLM-DispatchBias framework auditing 11 LLMs cross-lingually for a clearly high-stakes deployment.*
- **[EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage](https://arxiv.org/pdf/2605.03998)** — RJ Young, AM Matthews, arXiv 2605.03998, 2026
  *Why: First comprehensive fairness audit of LLM ED triage with a multi-step clinical reasoning probe.*
- **[Who Invests, Who Gets Funded: Gender and Racial Bias in LLM-Generated Investment Advice](https://link.springer.com/article/10.1007/s10551-026-06251-6)** — Y Wang, K Gu, Journal of Business Ethics, 2026
  *Why: Two-sided audit framework applied to multiple LLMs (GPT-4 Turbo baseline) with concrete asymmetric findings.*
- **[Beyond Single-Attribute Fairness: A Cross-Jurisdictional Intersectional Audit of Criminal Justice Risk Assessment Systems](https://openreview.net/pdf?id=YBvXVPix9G)** — ND Nair, Bridge between AI and Law workshop, 2025
  *Why: Operationalizes EU AI Act Article 24 / US disparate impact doctrine as a real intersectional audit — bridges legal and technical.*
- **[Auditing LLMs for Algorithmic Fairness in Casenote-Augmented Tabular Prediction](https://arxiv.org/pdf/2604.19204)** — XQ Lee, E Nwankwo, A Zhou, arXiv 2604.19204, 2026
  *Why: Audits multi-class error disparities for LLM-augmented housing-placement prediction — high-stakes and concrete.*
- **[ABLEIST: Intersectional Disability Bias in LLM-Generated Hiring Scenarios](https://arxiv.org/pdf/2510.10998)** — M Phutane, H Jung, M Kim, T Mitra, A Vashistha, arXiv 2510.10998, 2025
  *Why: 2,820-scenario audit across six LLMs spanning disability × gender × nationality × caste with a new taxonomy — Vashistha group at Cornell.*

## 6. LLM-as-judge & evaluator bias (~4 papers)

Audits of using LLMs to evaluate other systems.

- **[Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering](https://arxiv.org/pdf/2604.16790)** — Z Zhao, A Esmaeili, F Fard, arXiv 2604.16790, 2026
  *Why: Shows LLM-judge decisions are highly sensitive to prompt biases even when underlying code is unchanged — crisp finding.*
- **[Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/pdf/2604.23178)** — SK Soumik, arXiv 2604.23178, 2026
  *Why: Systematic eval of bias-mitigation strategies in LLM-judge pipelines — useful complement to the Zhao et al. audit.*
- **[A Scoping Review of LLM-as-a-Judge in Healthcare and the MedJUDGE Framework](https://arxiv.org/pdf/2604.25933)** — C Li et al., arXiv 2604.25933, 2026
  *Why: Surveys positional, verbosity, and self-preference biases in LLM-judges, with a tiered framework for healthcare deployment.*
- **[When AI Becomes Its Own Biggest Fan: Self-Preference Bias in AI-Assisted Peer Review](https://ieeexplore.ieee.org/abstract/document/11512087/)** — J Shi, J Lee, LZ Xu, T Ow, Y Wang, IEEE Trans. Engineering Management, 2026
  *Why: Empirical evidence of self-preference bias under self- vs. cross-review conditions with audit-trigger design.*

## 7. Audit tools & techniques (~5 papers)

Mechanistic interpretability, steering vectors, head-level localization, counterfactual frameworks.

- **[Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions](https://arxiv.org/pdf/2605.15217)** — J Tripathy, M Buckmann, arXiv 2605.15217, 2026
  *Why: Combines steering experiments with a classic credit-decision audit to mechanistically probe latent bias even when outputs look fair.*
- **[Measuring Mechanistic Independence: Can Bias Be Removed Without Erasing Demographics?](https://arxiv.org/pdf/2512.20796)** — Z Shan, A Mueller, arXiv 2512.20796, 2025
  *Why: Uses sparse-autoencoder feature ablations in Gemma-2-9B to test whether bias features are independent from demographic recognition.*
- **['I Know You Are Discriminatory!': Automated Substantiating for Individual Fairness Auditing of AI Systems](https://dl.acm.org/doi/pdf/10.1145/3757414)** — Y Liu, Q Cao, H Shen, K Zhang, Y Wu, X Cheng, PACM HCI, 2025
  *Why: Top-venue framework producing substantiated individual-fairness audits — evaluated with auditors, developers, and regulators.*
- **[How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles](https://arxiv.org/pdf/2604.07650)** — C Kuai et al., arXiv 2604.07650, 2026
  *Why: Statistical framework + entanglement-aware reweighting for verifier ensembles — addresses a real gap in multi-judge audits.*
- **[Scrutinizing Systemic Risks in Personalized Recommender Systems Through Sock-Puppet Auditing of VLOPs](https://dl.acm.org/doi/pdf/10.1145/3795516)** — L Bekavac, J Strecker-Bischoff, K Garcia, S Mayer et al., ACM TWeb, 2026
  *Why: Sock-puppet audit methodology applied to Very Large Online Platforms — important technique for platform-level audits.*

## 8. Borderline but worth knowing (~3 papers)

Cross-cutting work on governance, regulation that intersects with audit methodology.

- **[Audit Trails and AI Transparency: Regulatory Compliance under the EU AI Act](https://www.researchgate.net/profile/Athanasios-Davalas/publication/401946334_International_Journal_of_Social_Science_and_Economic_Research_Audit_Trails_and_AI_Transparency_Regulatory_Compliance_under_the_EU_AI_Act/links/69b4122fa5bf176ab54f5702/International-Journal-of-Social-Science-and-Economic-Research-Audit-Trails-and-AI-Transparency-Regulatory-Compliance-under-the-EU-AI-Act.pdf)** — M Grivokostopoulou, A Davalas, M Tsiogka, 2026
  *Why: Useful distinction between audit-trail logging (technical feature) and bias audit (external procedure) — clarifies a common conflation.*
- **[A practical framework for operationalising responsible and equitable artificial intelligence in health care](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(25)00139-6/fulltext)** — ML Welch et al., The Lancet Digital Health, 2026
  *Why: Top-tier venue (Lancet Digital Health) with concrete recommended auditing practices for healthcare AI.*
- **[Understanding and Mitigating Unintended Bias in Medical AI Systems](https://assets.pubpub.org/c99608f92-d70f-46c1-a72c-df272215f13e/p59ca6018-7725-43a3-8dc6-991479dc6bf6/udb8b0293-3c81-4a66-a8c2-c82afb5d27a5/Tyner-Monroe_et_al._(2026)_Just_Accepted-11775576076298.pdf)** — S Tyner-Monroe, B Rakova, JY Kim, M Sendak, S Balu et al., Harvard Data Science Review, 2026
  *Why: Introduces a Unintended Bias Risk Matrix grounded in empirical AI-testing experience — practical, from a recognizable group.*

## 9. Auditor judgment, audit quality & AI reliance in the audit profession (~16 papers)

New cluster surfaced by the "Auditor Bias" alert backlog (3 Aug – 6 Sep 2026): papers about the accounting/assurance audit profession itself — auditor cognitive bias, professional skepticism, and AI reliance in audit/assurance — as distinct from the algorithmic-fairness-audit literature in sections 1–8 above. Direct hits on the dissertation's own intersection (auditor judgment × AI reliance), not just papers that happen to contain the word "audit."

- **[Professional Judgment and AI Disclosure Governance in Audit and Sustainability Assurance: Public Evidence from the UK Big Four](https://www.mdpi.com/1911-8074/19/9/675)** — R Krasteva-Hristova, Journal of Risk and Financial Management, 2026
  *Why: Discusses AI misjudgment as a candidate cause in statutory audit failure and the PCAOB's amendments to AS 1105/AS 2301 — closest direct hit yet to the dissertation's core question.*
- **[The Effect of Generative AI on Audit Judgment Quality through Professional Scepticism and Governance](https://journal.nexuspublishing.co.id/jsmb/article/download/9/37)** — D Wirianto, S Krisnawati, Journal of Strategic Management & Business Nexus, 2026
  *Why: Tests algorithm aversion and automation bias as explanations for a non-significant AI-utilisation/professional-scepticism link — names two of the dissertation's own constructs directly.*
- **[Artificial Intelligence (AI), Audit Quality, and the Future of Professional Judgment: Policy and Governance Challenges in Auditing-A Systematic Literature Review](https://cspub-ijcisim.org/index.php/ijcisim/article/download/3899/3147)** — G Odoch, International Journal of Computer Information Systems …, 2026
  *Why: Systematic review whose title is almost a paraphrase of the dissertation's own framing — explainability crisis for auditors, algorithmic bias threatening audit objectivity.*
- **[Digital Transformation in the Audit Process in Nigeria: Balancing Artificial Intelligence, Cybersecurity, and Professional Skepticism](https://www.researchgate.net/profile/Adamu-Idris-Adamu/publication/412123505)** — OO Ekundayo, TS Orshi, SN Odunko, ACCOUNTING AND FINANCE, 2026
  *Why: Auditor training gaps and systematic model bias set directly against professional skepticism in a live audit-process context.*
- **[Exploration on Application of Large Language Models in Unstructured Audit Materials](https://hbem.net/index.php/ojs/article/download/57/55)** — W Li, Highlights in Business, Economics and Management, 2026
  *Why: Names hallucination, bias, transparency, and reliability as the open risks of generative AI in high-risk audit scenarios.*
- **[LLM: Usage of ChatGPT and AI Tools. An academic analysis from an auditor's perspective.](https://iampoojatheauditor.com/LLMs-and-ChatGPT-An-Auditors-Perspective.pdf)** — P Singh, 2026
  *Why: Practitioner-authored piece on LLM bias replication and the audit-methods needed for known/unknown risk in AI-assisted audit work.*
- **[Artificial Intelligence and Audit Effectiveness in Global Accounting: A Big Four Analysis](https://www.researchgate.net/profile/Saad-Saadouni/publication/411038897)** — S Saadouni, S Habbani, 2026
  *Why: Big Four-scoped look at AI perpetuating historical bias in flagging client risk characteristics — directly on the AI-reliance-in-audit question.*
- **[AI in Risk Management and Certification: Implications for Auditors and Assurance](https://link.springer.com/chapter/10.1007/978-3-032-35506-5_3)** — M van der Meulen, P Myrseth, … Conference on Computer Safety, Reliability, and …, 2026
  *Why: Conformity-auditor perspective on AI-tool adoption, competency gaps, and governance guidance needs.*
- **[The Role of AI-Assisted Accounting Information Systems in Enhancing Audit Effectiveness](https://ejournal.uhb.ac.id/index.php/globeforum/article/download/2451/1282)** — GB Kristianto, E Saraswati, Globe Forum, 2026
  *Why: Ties audit effectiveness explicitly to auditor-level factors alongside AI-assisted accounting information systems.*
- **[The effect of aggregating performance information on confirmation bias in subjective performance evaluations](https://www.sciencedirect.com/science/article/pii/S1044500526000181)** — JW Bentley, KM Stubbs, Management Accounting Research, 2026
  *Why: Experimental design has auditors preparing audit work on a client under a confirmation-bias manipulation — core auditor-judgment-bias methodology, no AI required.*
- **[Mental Health-Focused Intervention for Enhancing Professional Judgment in National Auditors: A Cognitive Bias Perspective](https://academic.oup.com/schizophreniabulletin/article/52/Supplement_2/S14/8762226)** — J Che, W Liu, Schizophrenia Bulletin, 2026
  *Why: RCT (n=120 practicing national auditors) testing whether cognitive-bias-awareness training improves professional judgment quality.*
- **[The effect of providing an opportunistic opportunity in financial statements, auditor certification, and financial reporting on the type of audit error](https://www.jmaak.ir/article_24467_en.html?lang=en)** — S Bozorgmehrian, Journal of Management Accounting and Auditing …, 2026
  *Why: Auditor confirmation bias tested directly against Type I/II audit error rates on the Tehran Stock Exchange.*
- **[Conspiracy illusion and auditors' professional skepticism: the moderating roles of tolerance for ambiguity and religious attitude](https://www.emerald.com/jaoc/article-abstract/doi/10.1108/JAOC-02-2026-0116/1390369)** — S Molavi, A Bazrafshan, Journal of Accounting & Organizational Change, 2026
  *Why: Integrates cognitive bias and motivated reasoning into professional-skepticism research with auditor-training implications.*
- **[Bridging the expectation performance gap in fraud detection: A systematic review of external auditors' responsibilities, audit failures, and regulatory responses](https://iessociety.org/index.php/IJBM/article/download/368/155)** — EOND Ocansey, E Peprah, International Journal of Business and Management …, 2026
  *Why: Systematic review naming auditor independence, professional competence and scepticism as the drivers of the audit expectation gap.*
- **[AI Security Risks in Enterprise Workflows: A Governance Architecture for the Validation Gap, Anchoring Bias, and Knowledge Staleness](https://www.pst-journal.org/wp-content/uploads/2026-2-3.pdf)** — L Botero, Power System Technology, 2026
  *Why: Names anchoring bias and automation bias explicitly, and proposes a governance/audit layer to counteract them — adjacent AI-governance framing rather than audit-profession specific.*
- **[Ask–Audit–Apply: A Framework for Clinical Reasoning with Artificial Intelligence](https://link.springer.com/article/10.1007/s11606-026-10741-8)** — A Jenkins, K Eisenberg, RC Ziegelstein, Journal of General Internal Medicine, 2026
  *Why: Anchoring bias, premature closure, and automation bias in AI-assisted professional judgment — clinical domain, but the identical cognitive-bias/AI-reliance mechanism the dissertation studies.*
- **[Auditing Implicit Sycophancy](https://books.google.com/books?hl=en&lr=lang_en&id=oNEAEgAAQBAJ&oi=fnd&pg=PA201&dq=Auditor+Bias&ots=JHELmcJ71G)** — T Han, B Xu, H Zhang, Y Lu, … Intelligence: The First Workshop on EI …, 2026
  *Why: Structured audit framework (DESG) for detecting implicit sycophancy — sycophancy is one of the dissertation's own named constructs.*

---

**Total: 62 papers across 9 sections.**

## A note on your Scholar alert

Your current "Auditor Bias" alert keyword pulls in ~50% accounting/finance auditor papers. Consider replacing it with something like:
`("algorithmic audit" OR "AI audit" OR "LLM bias" OR "fairness audit") AND (LLM OR "vision-language" OR "machine learning" OR "neural network")`
in Scholar to cut the noise at the source.

---

## Jun–Jul 2026 alert triage (2026-07-16, pre-submission sweep)

29 "Auditor Bias" alerts reviewed (Jun 1 – Jul 16). **Verdict: no impact on Ch. 1–4** — no new work on anchoring or process interventions in human auditor judgment. ~80% of alerts now concern algorithmic/AI-bias auditing (LLM audits, fairness auditing, AI-driven digital audit governance) — supports the Future Research AI/LLM bridge narrative only. Single human-auditor item (Tampubolon 2026, overconfidence/ethical decisions, minor venue) judged not citation-worthy for the qualifying manuscript.

---

## Jul 9–22, 2026 alert triage (2026-07-23 sweep, pre-final-submission)

10 "Auditor Bias" alerts reviewed (Jul 9–22). **Verdict: no impact on Ch. 1–4 — the human-auditor anchoring literature in the manuscript remains current.** All 10 are algorithmic/AI-bias auditing (bucket b): HR bias audits, generative-AI cross-engine bias measurement, education fairness, text-to-image cultural bias, and unrelated domains (satellite precipitation XAI, sports gender bias).

**One standout for the dissertation AI bridge:**
- **Artificial intelligence and bias in banking and financial services: a comprehensive review and future research agenda** — N Krey, G Rancati, J Parajuli, RV Srivastava, *International Journal of Bank Marketing*, 2026.
  *Why: comprehensive review + research agenda at exactly the AI × bias × financial-services intersection where the dissertation extension (AI/LLM audit tools and anchoring in bank audit risk) will sit. Candidate anchor citation for the dissertation proposal's motivation section.*

---

## Jul 21 – Aug 9, 2026 alert triage (2026-08-10 sweep)

9 "Auditor Bias" alerts reviewed. **8 rejected at the relevance gate, 1 accepted.** Rejected set is
the same pattern as the last three sweeps: L2 speaking-assessment fairness, volatility-forecast
auditing, spatial fairness in algorithmic decisions, e-recruitment cultural bias, generative
recommender fairness, skills-based job matching, HR algorithmic auditing. All are *algorithmic
auditing* — machines being audited — not *human auditor judgment*.

### Accepted — and it is the most relevant paper this alert has ever returned

- **How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer Review Under
  Identity Disclosure and Cross-Lingual Conditions** — O EFT, 2026.
  *Why it matters:* this is the dissertation extension chain, already partly instrumented by someone
  else. "Cross-model peer review" is **recursive epistemic drift** — successive models reprocessing
  the same work and converging on each other. "Auditor bias under identity disclosure" is adjacent to
  **sycophantic confirmation** — the model's output shifting toward the position it believes the
  counterparty holds. Five named mechanisms give the extension a citable vocabulary instead of
  three phrases invented in this repo.
  *Action:* obtain the full text before drafting the extension section. Check whether the five
  mechanisms map onto the three-link chain, and whether any is measured rather than asserted —
  a measured mechanism is a scale the dissertation could adapt.

### Adversarial flag (Pass 5 — never bury these)

- **AI-Powered Browsers Are Broadly Accurate News Summarizers That Reduce Political Bias and Negative
  Affect** — Y Xia, D Batorski, E Wertz, M Mamakos, L Li et al., arXiv 2026.
  *Why it matters:* evidence pointing the **other way** — AI assistance reducing rather than
  amplifying bias in a judgment task. Different domain and a lay-reader task rather than a
  professional-judgment one, so it is not fatal. But an argument that AI degrades professional
  judgment has to engage with the case that it sometimes improves it, or a committee member will
  raise it first.

### Recruitment precedent (Pass 3 — the binding constraint)

**None found.** Fourth consecutive sweep with no study that successfully recruited auditors or a
comparable specialist population. Directive 5 remains unserved by the literature sweep.

### The alert query itself is the problem

Eight of nine rejected, and the same ratio held across the Jun–Jul and Jul 9–22 sweeps: roughly
**80–90% of what "Auditor Bias" returns is algorithmic-audit work**, because Scholar reads "auditor"
as "the thing auditing a model." The sweep is not failing; the query is mis-pointed.

**Replace the single alert with two, so the two literatures stop competing in one inbox:**

1. Human-auditor judgment — the qualifying study's literature, and where Directive 5's recruitment
   precedent would appear:
   `("anchoring bias" OR "professional skepticism" OR "audit judgment" OR "auditor judgment") AND (auditor OR audit OR assurance)`

2. The dissertation extension — where the accepted paper above came from:
   `("automation bias" OR "algorithmic appreciation" OR sycophancy OR "model collapse" OR "epistemic drift") AND (LLM OR "large language model" OR "AI assistant")`

Keep "Auditor Bias" running for one month alongside them to confirm nothing is lost, then retire it.

## 10. External framing for L2/L3 — not peer-reviewed, leads only (added 9 Sep 2026)

Jennifer Kinne, jenniferkinne.com. Essays, not papers. Read for framing and for the sources she
cites; do not cite the posts themselves. Assessment: `dba/00_Execution/KINNE_2026-09-09.md`.

| Post | Date | Why | State |
|---|---|---|---|
| Silent Reinforcement: AI Systems and the Epistemic Vulnerability of Users | 17 Jul 2025 | "Cognitive integrity, the preservation of human reasoning quality over time" — candidate L3 outcome construct | lead |
| Optimizing Against the Gradient: RLHF, MDL Compression, and the Structural Inevitability of Epistemic Drift | 2026 | A mechanism for L3; uses the exact term the Scholar audit found zero times | lead |
| The Measurement Problem in AI Risk: Why Output Variance Doesn't Capture Epistemic Drift | 2026 | The construct-11 critique at field level | lead |
| The Wrong Variable | 17 Jul 2026 | The L2 framing: the question is what happens to the human | lead |
| In the Absence of Reason | 14 May 2026 | Governance frameworks as unexamined; the practice-section critique | lead — **body not yet obtained** |
| Naming is Not Explaining | 2026 | Anti-anthropomorphism discipline | lead |
