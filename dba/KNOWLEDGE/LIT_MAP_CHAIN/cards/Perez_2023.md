# Perez et al. (2023)

**Citation.** Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., ... Kaplan, J. (2023). Discovering language model behaviors with model-written evaluations. *Findings of the Association for Computational Linguistics: ACL 2023* (venue per ACL Anthology listings; pages not verified here). Preprint 2022.
**DOI/URL.** https://arxiv.org/abs/2212.09251
**Source read.** Abstract (arXiv record).
**Already in repo?** Yes, cited in `Research_Paper_YMalik_SUBMISSION.md`.

**Big idea.** Uses LMs to write evaluations at scale and finds that larger models repeat back the user's preferred answer.
**Design and sample.** LLM-only; 154 generated evaluation datasets, crowdworker validation of labels.
**Key findings (as stated).** Larger LMs repeat back a dialog user's preferred answer ("sycophancy"). Some of the first examples of inverse scaling in RLHF, where more RLHF makes LMs worse.
**Link(s).** L2, partly (model side only). Supports the tracker's "mechanism, not artifact" framing: sycophancy grows with scale and RLHF.
**Limitation.** Opinion questions without correct answers; no humans deciding anything.
**Critique angle.** An auditor's stated position is usually a factual judgment, not an opinion. Sharma et al. and Wei et al. are better evidence for that case.
