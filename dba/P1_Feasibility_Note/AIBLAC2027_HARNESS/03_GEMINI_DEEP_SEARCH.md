# Brief for Gemini · Deep Research with Google Scholar · AIB-LAC 2027, ID 69

**How Yasir uses this:** open Gemini, turn on **Deep Research**, paste the **Context block** once, then paste **one
search at a time**. Save each answer as `RESULTS/GEMINI_S<number>_<date>.md`. Gemini searches; it does not write the paper.

---

## Context block (paste first)

> You are a research librarian for a doctoral student. Your only job is to find and capture published sources.
> Do not write prose for the paper, do not summarise beyond one sentence per source, and do not give opinions.
>
> **The paper.** "Feasibility as a Parameter: When Comparative International Research on Narrow Specialist
> Professional Populations Can and Cannot Be Executed." Accepted for an interactive session at the AIB Latin America
> and the Caribbean Chapter conference, 2027. It argues that for rare professional populations (for example, audit
> specialists), the reachable usable sample is the product of frame size, specialist prevalence, response rate and
> screen survival, and that a multi-country comparison is only as feasible as its least feasible country. It proposes
> reading reachable counts from commercial panel providers' audience tools before a study is fielded. No data have
> been collected.
>
> **Five hypotheses.**
> H1 Binding frame: joint feasibility is set by the least feasible national frame; adding a frame cannot raise it.
> H2 Regional bounding: a specialist population's prevalence on a commercial panel is higher in the provider's home region.
> H3 Born-regional design: studies that call themselves cross-national achieve more regionally concentrated coverage
> than they state, more so for narrow populations.
> H4 Mode dominance: data-collection mode explains more variance in response than country does.
> H5 Standardization tension: more instrument standardization goes with lower response, more so where response is already low.
>
> **Already cited, do not return these:** Baruch & Holtom (2008); Cohen (1988); Contractor, Kundu & Hsu (2003);
> Cuervo-Cazurra, Newburry & Park (2016); Cycyota & Harrison (2006); Geleilate et al. (2016); Ghemawat (2001);
> Harzing, Reiche & Pudelko (2013); Hermans et al. (2017); Hofstede (2001); Knight & Cavusgil (2004); Lopez, Kundu &
> Ciravegna (2009); Mezias (2002); Newburry & Yakova (2006); Peterson, Arregle & Martin (2012); Raudenbush & Bryk
> (2002); Robinson (1950); Rugman & Verbeke (2004); Zeng, Grogaard & Bjorkman (2023).
>
> **Rules.**
> 1. Peer-reviewed journal articles, scholarly books and working papers from recognised institutions only.
> 2. Every row needs a DOI or a stable publisher URL that you opened and that resolves. If you cannot open it, drop the row.
> 3. Never invent a citation, author, year, page or finding. If a field is not stated in the source, write `not reported`.
> 4. Quote the one sentence that supports the row, in quotation marks, with the page number if shown.
> 5. Include sources that **contradict** the hypothesis. Mark them `contradicts`.
> 6. Prefer 2010 onward; include older work only if it is the standard reference.
> 7. Return at most 12 rows per search, best first. Fewer good rows beat more weak ones.
>
> **Output: one Markdown table per search, exactly these columns:**
> `citation` (APA 7) | `url` (DOI link) | `access` (open / paywalled) | `relation` (supports / contradicts / method / context)
> | `hypothesis` (H1 to H5 or General) | `key_sentence` (verbatim quote) | `why_it_matters` (one sentence)
> | `read_state` (always `lead`) | `captured` (today's date, Gemini Deep Research)
>
> After the table, list under "Could not verify" anything you found but could not open.

---

## The six searches (paste one at a time)

**S1 · Rare and hard-to-reach professional populations (General).**
> Find studies and methods papers on sampling rare, low-prevalence or hard-to-reach professional or elite populations
> in survey research: executives, auditors, physicians, specialists. I need reported eligibility or incidence rates,
> screen-out rates and achieved sample sizes. Include work on online panel incidence and feasibility estimation.

**S2 · H1 Binding frame: multi-country survey feasibility.**
> Find papers on cross-national or multi-country survey design in international business and management where the
> achieved sample differed sharply by country, where countries were dropped for insufficient sample, or that discuss
> minimum per-country sample requirements and measurement invariance sample needs. Include methods reviews of
> cross-cultural survey research in JIBS, JWB, MIR, IBR and Organizational Research Methods.

**S3 · H2 Regional bounding: online panel coverage by country.**
> Find research on the composition, coverage and data quality of commercial online research panels and crowdsourcing
> platforms (for example Prolific, MTurk, Qualtrics panels, CloudResearch, Dynata) across countries or regions,
> especially evidence that panel membership is concentrated in the provider's home region, and work on recruiting
> professionals or business-to-business samples through panels.

**S4 · H3 Born-regional design: stated versus achieved country coverage.**
> Find reviews or bibliometric studies of sample composition in international business research: which countries
> and regions samples actually come from, the dominance of single-region or triad samples, and gaps between stated
> scope and achieved scope. Include reviews of Latin America's representation in IB research.

**S5 · H4 Mode dominance: survey mode versus country effects.**
> Find meta-analyses and methods studies comparing response rates and data quality across data-collection modes
> (web, mail, telephone, face to face, panel) and across countries, especially any that estimate how much variance
> is due to mode versus country. Include response-rate meta-analyses in organizational and management research since 2008.

**S6 · H5 Standardization tension: equivalence versus response.**
> Find research on the trade-off between instrument standardization or measurement equivalence and local adaptation
> in cross-national surveys: translation and back-translation, emic versus etic design, and any evidence linking
> standardized instruments to lower response or data quality in some countries.

---

## After each search (Yasir, 2 minutes)
1. Copy Gemini's table into `RESULTS/GEMINI_S<number>_<date>.md`.
2. Tell Codex: "run C4 on S<number>" so the links are checked.
3. Read the top three. Only what you have read can be marked `read`.
