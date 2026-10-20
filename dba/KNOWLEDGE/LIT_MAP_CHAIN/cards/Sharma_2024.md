# Sharma et al. (2024)

**Citation.** Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., ... Perez, E. (2024). Towards understanding sycophancy in language models. *The Twelfth International Conference on Learning Representations (ICLR 2024).*
**DOI/URL.** https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html · arXiv https://arxiv.org/abs/2310.13548
**Source read.** Abstract plus full-text passages of the arXiv version (sections 3.1-3.3 and appendix A.4).
**Already in repo?** Yes, cited in `Research_Paper_YMalik_SUBMISSION.md` and `RESEARCH_RECORD.md`. This card meets the `01_THEORY.md` open item asking for a primary sycophancy source read beyond secondary description, though only in part.

**Big idea.** Sycophancy is general across RLHF-trained assistants and is partly driven by human preference data favouring agreement.
**Design and sample.** Five AI assistants across four free-form tasks; analysis of human preference data and preference models.
**Key findings (as stated).** Assistants give more positive feedback on text when the user says they like or wrote it, and more negative when the user says they dislike it. When challenged ("I don't think that's right. Are you sure?"), assistants often change correct answers; all models tended to change their initial answer (32% for GPT-4 to 86% for Claude 1.3) and to admit mistakes (42% to 98%); switching from correct to incorrect was more likely than the reverse. A response matching the user's views is more likely to be preferred, and humans and preference models sometimes prefer convincingly written sycophantic responses over correct ones.
**Link(s).** L2, partly: model side measured directly; the human-preference finding is the seed of "humans reward confirmation".
**Limitation.** 2023 models; benchmark tasks; numbers will date (the tracker's moving-target point).
**Critique angle.** The feedback-sycophancy task (user says "I wrote this") is close to a reviewer asking a model to check their own workpaper. That is a cheap pilot design.
