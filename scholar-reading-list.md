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

---

**Total: 46 papers across 8 sections.**

## A note on your Scholar alert

Your current "Auditor Bias" alert keyword pulls in ~50% accounting/finance auditor papers. Consider replacing it with something like:
`("algorithmic audit" OR "AI audit" OR "LLM bias" OR "fairness audit") AND (LLM OR "vision-language" OR "machine learning" OR "neural network")`
in Scholar to cut the noise at the source.
