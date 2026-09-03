# Harzing, Reiche & Pudelko (2012) — what Bill sent, and what it does to your project

**Received 3 September 2026**, from Prof. Newburry after the call: *"Here is the article I mentioned
that may help as a start."*

> Harzing, A.-W., Reiche, B. S., & Pudelko, M. (2012). Challenges in international survey research:
> A review with illustrations and suggested solutions for best practice. *European Journal of
> International Management.* 41 pp.

---

## The headline: your contribution survives, and it is now sharper

**The question that mattered was whether this paper already makes your argument. It does not.**

| | Harzing et al. (2012) | Your project |
|---|---|---|
| **Unit** | Mostly **organisations** — MNCs, subsidiaries. Respondents reached *through* firms | **Individuals in a rare profession**, reached directly |
| **Access treated as** | A set of practical obstacles with workarounds: buy a database (D&B, Hoover's), use local collaborators, address the letter to the right director | A **structural property measurable in advance**. No workaround changes prevalence |
| **Response rate** | Something to **maximise** — 61 mentions, an operational target | One of two **parameters**, alongside prevalence |
| **Prevalence** | Not treated | The whole point |
| **The words "elite", "hard-to-reach"** | **Zero occurrences in 41 pages** | The population definition |
| **Output** | Best-practice suggestions per research stage | A **threshold**: where a comparative survey stops being viable at all |

**They map the terrain. You are asking a different question about one corner of it.**

---

## The sentence in their paper that hands you your gap

> *"Overall response rates have been found to differ significantly, both across different professions
> and occupational groups as well as across countries."*  — §4

**They name both variables and never multiply them.** Response rate varies by profession. Response
rate varies by country. What happens when a narrow profession is sampled across several countries at
once is not asked, and that is your project in one sentence — **stated in the words of the paper your
professor handed you.**

That is the strongest possible position to argue a gap from. You are not claiming the field ignored
the problem; you are showing that a leading review identified both halves and stopped short of the
product.

---

## The numbers you can now use — and the model they unlock

Their own project 2, Illustration 7:

| Country | Response rate |
|---|---|
| Korea *(telephone, via survey company)* | **47%** |
| Spain | 15.4% |
| Australia / NZ | 12.7% |
| Nordic countries | 11.3% |
| Germany | 11.1% |
| Japan | 10.4% |
| France | 6.6% |
| UK | 5.2% |
| **China** | **4.0%** |
| **Overall** | **13.8%** — **9.6% excluding Korea** |

**This is the missing parameter for your study model, and it is empirical rather than assumed.**

You already have prevalence: roughly **six eligible per hundred thousand** in your own auditor
screen. Harzing gives you country-level response rate, ranging roughly **4% to 15%** in ordinary
conditions. Reachable respondents per country is prevalence × frame × response rate — and a
comparative design needs **all** countries to clear the bar simultaneously, so the joint probability
is the product, not the average.

**That is your Slide 4 — the study model.** Two parameters, one multiplication, and a curve that
crosses the viability line. `../../RISK_QUANT/feasibility.py` already computes the first half.

**And it gives you a hypothesis that falls out of the reading rather than being asserted:**

> The reachable sample for a specialist professional population declines faster than linearly as
> national frames are added, because prevalence and response rate compound multiplicatively rather
> than averaging.

**Note the Korea line carefully.** 47% by telephone through a survey company against 9.6% for
everything else — that is a *method* effect nearly five times the size of the *country* effects
around it. Worth one sentence: if switching instrument moves the number more than switching country
does, then "which country" may be the wrong question and "which instrument, at what prevalence" the
right one. That is a defensible reading of their own data and it is friendly to their paper rather
than a critique of it.

---

## What to do with it

- [ ] **Read it properly.** 41 pages, and §2 and §4 are the ones that matter. The rest — translation,
      equivalence, common method variance — is useful background but not your argument
- [ ] **It replaces Harzing (1997) as paper #1** on the runway. Same author, more recent, directly
      cross-national, and handed to you by the person grading you
- [ ] Pull the response-rate table into the model
- [ ] Keep §2 for the literature summary — it is the citation that establishes the problem exists

---

## The reply to Bill — send today, keep it short

**From `ymali001@fiu.edu`.** He wrote a two-line email. A long reply reads as needy; a same-day
short one reads as someone already working.

> **Subject:** Re: [his subject line]
>
> Dear Professor Newburry,
>
> Thank you — and thank you for the call. The Harzing paper is exactly the right starting point.
>
> Section 4 in particular gave me something I did not have. Their observation that response rates
> differ both across professions and across countries names both of the variables I have been
> working with, and their own country figures — around four to fifteen percent outside the telephone
> sample — give me the second parameter empirically rather than by assumption. I had prevalence from
> my own screening; I did not have response rate.
>
> That combination is, I think, the model: reachable sample as prevalence multiplied by response
> rate, compounding across national frames rather than averaging. I will bring a first version of it
> to the next session.
>
> Thanks again,
> Yasir A. Malik

**Why it is this short.** It does three things and stops: thanks him, proves you read it by naming a
specific section and what it changed, and commits to a deliverable. It does not summarise the paper
back to him — he wrote the email, he knows what is in it.

**One judgement call:** it says "I will bring a first version to the next session." Only send that if
you will. He will remember.
