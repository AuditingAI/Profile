# Shumailov, Shumaylov, Zhao, Papernot, Anderson & Gal (2024)

**Citation.** Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature, 631*, 755-759.
**DOI/URL.** https://doi.org/10.1038/s41586-024-07566-y · precursor preprint https://arxiv.org/abs/2305.17493
**Source read.** Abstract of the 2023 preprint ("The curse of recursion") in full; the Nature abstract only in truncated form. Findings below are from the preprint abstract.
**Already in repo?** Yes, cited in `Research_Paper_YMalik_SUBMISSION.md`. Meets part of the `01_THEORY.md` open item ("model collapse needs a primary source").

**Big idea.** Training on model-generated content makes successive models lose the tails of the original distribution.
**Design and sample.** Model-only: VAEs, Gaussian mixture models and LLMs.
**Key findings (as stated, preprint abstract).** Use of model-generated content in training causes irreversible defects in resulting models, where tails of the original content distribution disappear ("model collapse").
**Link(s).** L3, analogy only. Not evidence about human reviewers.
**Limitation.** Training dynamics, not judgment.
**Critique angle.** The "tails disappear" result maps onto audit: rare, unusual items are exactly what convergence would lose. Use as metaphor with that caveat stated every time.
