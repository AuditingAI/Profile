# -*- coding: utf-8 -*-
"""
GEB 7365 Formal Project Report, Draft 1.

Format is Prof. Newburry's, from Session 4 (8/10 September 2026), slides 17-27:
  Introduction 2-3 pp · Literature Review 5 pp · Hypotheses 1+ p each ·
  Methodology ~5 pp · Results NOT required · Discussion & Conclusions ~5 pp ·
  References immediately after main text · Tables and Figures at the end, with
  "Insert Table X About Here" markers in the body. 30 pages maximum, due 9 Oct.

Built with build_dba_doc.py (FIU coursework builder, no consulting wordmark).
"""
import json

TITLE = ("Feasibility as a Parameter: When Comparative Research on Narrow "
         "Specialist Professional Populations Can and Cannot Be Executed")

spec = {
 "title": TITLE,
 "subtitle": "Formal Project Report · Draft 1",
 "ident": [
   "Yasir A. Malik",
   "Florida International University · College of Business",
   "Doctor of Business Administration · Cohort 8.14",
   "GEB 7365 · International Business Theory and Practice · Instructor: Prof. William Newburry",
   "Draft 1 · September 11, 2026 · Report due October 9, 2026",
 ],
 "double_spaced": True,
 "body": [

  # ================= INTRODUCTION =================
  {"h1": "Introduction"},

  ["Comparative international business research rests on a requirement that is rarely stated as a "
   "requirement. To compare a phenomenon across countries, a researcher must reach the same "
   "population in every country in the design, at the same time, with an instrument that means the "
   "same thing in each place. When the population is a general one, this requirement is "
   "demanding but routine. When the population is a narrow professional specialty, it becomes "
   "something else. This paper is about what that something else is, and about the fact that it "
   "can be calculated in advance rather than discovered after the money is spent."],

  ["The received wisdom treats sampling difficulty as an execution problem. It belongs to "
   "fieldwork, to budget, to the quality of local partners, and it surfaces in published work as "
   "a limitation paragraph near the end of the method section. The methodological literature on "
   "international survey research is considerably more sophisticated than that, and Harzing, "
   "Reiche and Pudelko (2012) document response variation across national frames in detail, but "
   "its orientation is managerial. Cross-national variation is a nuisance to be reduced through "
   "better translation, better incentives, better contact protocols, and better local "
   "relationships. The implicit model is that effort and money convert into responses at a rate "
   "that differs by country but is always positive and always improvable."],

  ["The gap is that nobody has asked what happens to this picture when the target population is "
   "rare. For a population present at a few members per hundred thousand, the conversion of "
   "effort into responses is governed less by protocol quality than by arithmetic that is fixed "
   "before the first contact is made. More importantly, that arithmetic does not add across "
   "national frames. It compounds, and it compounds in one direction only. A design that is "
   "marginal in one country is not four times harder in four countries. It can be structurally "
   "impossible in four countries while remaining marginal in each one taken separately. That "
   "distinction is invisible to a literature that reports sampling as a limitation, because a "
   "limitation is by definition something discovered afterward."],

  ["The research question this paper proposes to begin answering is therefore: under what "
   "conditions is a comparative, multi-country design targeting a narrow specialist professional "
   "population feasible at all, and where is the threshold at which a survey design must be "
   "abandoned in favour of a different method?"],

  ["The intended contribution is to move sampling feasibility from the status of a limitation to "
   "the status of a parameter. A parameter is estimated before a study is designed and it "
   "constrains the design; a limitation is confessed after the study has failed. The claim here "
   "is that for narrow populations the relevant quantities are observable in advance. Commercial "
   "research panels expose estimated reachable counts on their audience-configuration interfaces "
   "before any commitment is made, and published response rates by country are available. Those "
   "two inputs, combined with an eligibility screen, determine feasibility. A secondary "
   "contribution follows from the first and is the more useful one for practice. Where the "
   "arithmetic rules out a survey it does not rule out the study. The same twenty reachable "
   "participants who cannot sustain a comparative survey can sustain a phenomenological design. "
   "The threshold at which one method fails and another becomes appropriate is locatable before "
   "resources are committed, and locating it is a service to the field rather than an admission "
   "about one project."],

  ["This is a contribution to an existing conversation rather than a new one. The regionalization "
   "literature established that firms described as global are substantially home-region bound "
   "(Rugman & Verbeke, 2004), and that ventures described as born global may be better described "
   "as born regional (Lopez, Kundu, & Ciravegna, 2009). This paper extends the same suspicion, "
   "that the label and the reality diverge, from the firms under study to the research "
   "infrastructure used to study them. If commercial research panels are themselves firms, and "
   "firms are regionally bound, then the infrastructure on which comparative research depends "
   "should be regionally bound in the same way and for the same reasons. That is an empirical "
   "question and it has not been asked."],

  # ================= LITERATURE REVIEW =================
  {"h1": "Literature Review"},

  ["Four streams bear on the question. The first documents the phenomenon without modelling it. "
   "The second supplies the theoretical mechanism for why research infrastructure should be "
   "regionally bounded. The third supplies the levels of analysis at which feasibility is "
   "determined. The fourth supplies the tension between standardization and response that sits at "
   "the centre of any comparative instrument."],

  {"h2": "International survey research and the management of response variation"},

  ["Harzing, Reiche and Pudelko (2012) provide the most detailed available account of what "
   "actually happens when a single instrument is fielded across national frames. Their project "
   "response rates range from four percent in China to roughly fifteen percent in Spain, with a "
   "figure of forty-seven percent in Korea obtained by telephone through a survey company rather "
   "than by the instrument used elsewhere. The orientation of this work is practical. It tells a "
   "researcher what to expect and what to do about it."],

  ["Two features of that dataset matter more than the paper's own emphasis suggests. The first is "
   "the spread. A four-fold difference between the best and worst frame is not noise around a "
   "mean; it is a difference in kind, and any design that requires a threshold in every frame is "
   "governed by the worst of them. The second is the Korean observation. A change of mode moved "
   "the response rate by roughly five times more than the entire spread attributable to country. "
   "If that pattern generalises, then the variable the comparative literature treats as central, "
   "national context, is dominated by a variable it treats as incidental, instrument mode. The "
   "present paper takes that inversion seriously enough to hypothesise it."],

  {"h2": "Regionalization and the gap between the label and the reality"},

  ["Rugman and Verbeke (2004) examined the sales of the largest multinationals and found that the "
   "overwhelming majority were home-region oriented rather than global. The theoretical mechanism "
   "is not simply distance. Firm-specific advantages developed in a home region transfer within "
   "that region at low cost because the supporting institutions, customer expectations and "
   "distribution structures are similar, and transfer across regions only by being rebuilt. The "
   "label global describes an aspiration; the sales data describe a region."],

  ["Lopez, Kundu and Ciravegna (2009) applied the same test to firms that appear international "
   "from inception. Their Costa Rican software cases are international from day one in the sense "
   "the born-global literature intends, yet their activity concentrates regionally. The "
   "contribution is the demonstration that a firm can satisfy the formal definition of a category "
   "while failing the substantive one, and that the discrepancy is detectable only by measuring "
   "where the activity actually lands rather than where the firm says it operates."],

  ["The extension proposed here is direct. A commercial research panel is a firm. It recruits its "
   "membership through channels that are themselves institutionally embedded: professional "
   "associations, employment platforms, advertising networks and payment infrastructures that "
   "differ by region. There is no reason to expect the resulting membership to be regionally "
   "neutral, and considerable reason grounded in this literature to expect it to be home-region "
   "concentrated. For a general population the concentration may be immaterial because the "
   "population is abundant everywhere. For a specialty present at a few per hundred thousand, a "
   "modest regional skew in recruitment is the difference between a reachable frame and an "
   "unreachable one."],

  {"h2": "Levels of analysis and the agency of local units"},

  ["Meyer, Li and Schotter (2020) argue that the subsidiary is not an instrument of headquarters "
   "but an actor with its own agency, embedded simultaneously in the internal network of the firm "
   "and in an external national context, and that research on it must be explicitly multi-level "
   "and dynamic. Their agenda is a corrective to designs that treat the country as the only level "
   "that matters."],

  ["The parallel to research design is exact and has not been drawn. Feasibility is determined at "
   "several levels at once: at the population level by prevalence, at the infrastructure level by "
   "panel coverage, at the instrument level by mode and length, and at the design level by the "
   "strictness of the eligibility screen. These levels are not nested cleanly and they are not "
   "interchangeable. A researcher who attributes a failed frame to the country has committed the "
   "error Meyer and colleagues describe, which is to assign to one level a result produced at "
   "another. The Korean telephone datum is precisely such a case."],

  {"h2": "Control, coordination, and the standardization tension"},

  ["Zeng and colleagues (2023) review the mechanisms by which multinationals control and "
   "coordinate dispersed units, and separate the two. Control is the imposition of a common "
   "standard from the centre; coordination is the alignment of units that retain discretion. The "
   "two are not the same instrument and they trade off, because tightening the first reduces the "
   "local adaptation on which the second depends."],

  ["Comparative survey research faces this tradeoff in an unusually pure form. Measurement "
   "equivalence requires that the instrument be as nearly identical as possible across frames, "
   "which is control. Achieving response requires adaptation to local norms of length, channel, "
   "incentive, sponsorship and language register, which is coordination. Every increment of "
   "standardization purchased for the sake of comparability is paid for in response, and the "
   "payment is heaviest in exactly the frames that were weakest to begin with. The literature "
   "treats equivalence and response as separate methodological concerns. They are the two sides "
   "of one tradeoff, and for a narrow population the tradeoff binds."],

  {"h2": "The recurring lesson: measuring one thing while believing another was measured"},

  ["A final stream is relevant less for its content than for its shape. Contractor, Kundu and Hsu "
   "(2003) resolved three decades of contradictory findings on multinationality and performance "
   "by showing that the field had been sampling different segments of a single sigmoid curve and "
   "reporting each segment as a finding about the whole. Mezias (2002) made progress on the "
   "liability of foreignness only by abandoning aggregate performance measures, which confound "
   "advantages with disadvantages, in favour of labour lawsuit judgments, which isolate one "
   "disadvantage. Ghemawat (2001) showed that country portfolio analysis measures market size "
   "while being used as though it measured opportunity, and that firms which solve geographic "
   "distance routinely conclude they have solved distance."],

  ["In each case the obstacle was not the theory but what the field was able to measure, and on "
   "whom. This paper takes that problem as its subject rather than as a limitation paragraph. The "
   "question of who can actually be reached, in which frames, and what follows for the design, is "
   "treated here as a first-order research question in international business methodology."],

  # ================= HYPOTHESES =================
  {"h1": "Hypotheses Development"},

  ["Five hypotheses follow. The first is analytic and states the structure of the problem. The "
   "remaining four are empirical and each draws its theoretical logic from one of the streams "
   "above."],

  {"h2": "H1. The binding-frame hypothesis"},

  ["In a comparative design that requires a minimum usable sample in every national frame, joint "
   "feasibility is determined by the least feasible frame rather than by the mean across frames. "
   "Adding a national frame to such a design weakly decreases joint feasibility and can never "
   "increase it."],

  ["The theoretical logic does not depend on any citation and should be clear without one. A "
   "comparative claim is a conjunction. To say that a relationship differs between Spain and "
   "China is to assert something about Spain and something about China, and the assertion fails "
   "if either component fails. The design therefore requires that every frame clear its threshold "
   "simultaneously. An average cannot satisfy a conjunction. A design with one excellent frame "
   "and one hopeless frame has a respectable mean and no comparison."],

  ["The consequence is asymmetric in a way that is easy to miss. Because the requirement is set "
   "by the minimum, and because a set's minimum can only fall or stay level when an element is "
   "added, every additional country weakly worsens the design and no additional country can "
   "improve it. Breadth, which the field treats as a virtue in comparative work, is therefore "
   "purchased at a price that rises faster than the number of frames. This is not a claim about "
   "difficulty. It is a claim about structure, and it means that the common practice of "
   "describing a design as more ambitious because it covers more countries misstates what has "
   "been done: the design has not become more ambitious, it has become more fragile."],

  ["Worked against the empirical inputs described in the method section, the magnitude is large. "
   "A single-frame design in the most favourable country requires roughly nineteen million panel "
   "members to yield thirty usable responses. Adding four more countries, one of which is the "
   "least favourable, raises the requirement in every frame to roughly seventy-two million while "
   "the mean response rate across the design falls only from about fifteen percent to about nine "
   "percent. The mean is nearly uninformative about the design's viability, and reporting it is "
   "reporting the wrong statistic."],

  ["Insert Table 1 About Here"],
  ["Insert Table 2 About Here"],
  ["Insert Figure 1 About Here"],

  {"h2": "H2. The regional bounding hypothesis"},

  ["The observable prevalence of a narrow specialist professional population on a commercial "
   "research panel is higher within the panel provider's home region than outside it, controlling "
   "for the size of the national frame."],

  ["The theoretical logic is the mechanism Rugman and Verbeke identify, applied to a firm whose "
   "product is access to people. A panel provider builds its membership through recruitment "
   "channels that are institutionally specific: professional associations, employment platforms, "
   "advertising markets, payment rails and reputational networks. Each of these is denser and "
   "cheaper to work within the region where the provider originated, because the provider's own "
   "advantages in that region are the advantages Rugman and Verbeke describe, and they do not "
   "transfer without being rebuilt."],

  ["The reason this should bite harder for specialists than for general populations is that "
   "specialist recruitment runs through narrower channels. A general consumer panel can be "
   "assembled almost anywhere through broad advertising. A panel containing experienced internal "
   "auditors is assembled through professional bodies and industry networks whose reach is "
   "national or regional by construction. The rarer the specialty, the more the panel depends on "
   "exactly the channels least likely to have been rebuilt outside the home region. The "
   "prediction is therefore not merely that coverage is uneven but that its unevenness increases "
   "as the target population narrows."],

  {"h2": "H3. The born-regional design hypothesis"},

  ["Published studies that describe themselves as cross-national achieve national coverage that "
   "is more regionally concentrated than their stated design implies, and the discrepancy "
   "increases with the narrowness of the target population."],

  ["The logic is the one Lopez, Kundu and Ciravegna used on born globals, transposed. A study "
   "satisfies the formal definition of cross-national by including frames from several countries. "
   "Whether it satisfies the substantive definition depends on where the achieved responses "
   "actually land, which is a different measurement and is rarely reported with enough "
   "granularity to check."],

  ["The mechanism connecting this to H2 is straightforward. If panel coverage is regionally "
   "bounded, then achieved responses will concentrate in the frames where coverage is best, which "
   "will be the frames within the provider's home region. Researchers who set a global target and "
   "accept the responses that arrive will produce a sample that is formally multinational and "
   "substantively regional, without any decision having been made to that effect. The "
   "concentration is a property of the infrastructure, not of the research design, which is "
   "precisely why it goes unremarked. For a narrow population the effect should be larger, "
   "because the weakest frames contribute close to nothing and the sample collapses onto the "
   "strongest ones."],

  {"h2": "H4. The mode dominance hypothesis"},

  ["Variance in achieved response attributable to data-collection mode exceeds variance "
   "attributable to country."],

  ["The logic comes from Meyer, Li and Schotter's insistence that outcomes be assigned to the "
   "level that produced them. Response is an outcome of an encounter between a person and a "
   "request. The properties of that encounter, whether the request arrives by telephone from a "
   "human being or by email from a platform, how long it claims to take, who appears to be "
   "asking, are properties of the instrument, not of the country. National context shapes the "
   "encounter, but it does so through norms that are themselves mode-specific: the norm governing "
   "an unsolicited telephone call is not a weaker or stronger version of the norm governing an "
   "unsolicited email, it is a different norm."],

  ["The reason to expect mode to dominate rather than merely to matter is that mode changes the "
   "cost structure of compliance for the respondent, while country changes only the disposition "
   "toward it. A telephone request from a person imposes a social cost on refusal that an email "
   "does not impose in any country. The single available datum is consistent with this: the "
   "forty-seven percent obtained by telephone in Korea exceeds the entire country spread in the "
   "same project by roughly a factor of five. One observation is not evidence, which is why this "
   "is a hypothesis and not a finding, but it is the observation that makes the hypothesis worth "
   "testing. If it holds, a substantial part of what the comparative literature has attributed to "
   "national context is an artefact of instrument selection."],

  {"h2": "H5. The standardization tension hypothesis"},

  ["The degree of instrument standardization across national frames is negatively associated with "
   "achieved response rate, and the association is stronger in frames with lower baseline "
   "response."],

  ["The logic is Zeng and colleagues' separation of control from coordination. Standardization is "
   "control: a common instrument imposed from the centre so that responses are comparable. "
   "Response depends on coordination: adaptation of length, channel, sponsorship, incentive and "
   "language register to what each frame will actually tolerate. These draw on the same "
   "instrument and pull it in opposite directions. Every element held constant for the sake of "
   "equivalence is an element that cannot be adapted for the sake of response."],

  ["The interaction is the part that matters for design. In a strong frame, standardization costs "
   "response that the frame can afford to lose. In a weak frame, the same standardization is "
   "applied to a frame that had no margin, and it is the weak frames that bind the design under "
   "H1. Standardization therefore damages a comparative design at precisely the point where the "
   "design is already most vulnerable, which means the equivalence-response tradeoff is not "
   "linear in its consequences and cannot be managed by trading a uniform amount of one for the "
   "other."],

  ["Insert Table 3 About Here"],

  # ================= METHODOLOGY =================
  {"h1": "Methodology"},

  {"h2": "Study context"},

  ["The empirical setting is the set of commercial research panels used in academic and "
   "commercial survey work, and the specialist professional occupations that comparative business "
   "research targets. The setting is unusual in one respect that makes the study possible. Panel "
   "providers expose an audience-configuration interface that returns an estimated reachable "
   "count once screening criteria are entered, before any commitment is made and at no cost. The "
   "quantity this study needs as its dependent variable is therefore observable in advance and is "
   "quotable, rather than having to be inferred from completed studies. This is what makes "
   "feasibility a parameter rather than a limitation, and it is the practical basis of the whole "
   "project."],

  ["The unit of analysis is the country-panel-occupation cell: one specialist occupation, on one "
   "panel provider, in one national frame. The sampling plan is to populate a matrix of at least "
   "six specialist occupations across at least eight national frames on at least three panel "
   "providers of differing regional origin, which gives a target of roughly one hundred and "
   "forty-four cells. Panel providers are selected to vary on home region deliberately, because "
   "H2 is unidentifiable if every provider originates in the same place."],

  ["The author's own study supplies one fully documented validating case. A panel of 334,976 "
   "members returned approximately twenty eligible participants under the study's screening "
   "criteria, a prevalence of about six per hundred thousand, and of twenty-three raw responses "
   "four survived screening. Cost per usable response is documented. Any model proposed here must "
   "reproduce that case from its own inputs, and a model that cannot do so is rejected."],

  {"h2": "Variable measures"},

  ["The dependent variable is reachable usable sample, defined as the estimated number of "
   "responses that would survive eligibility screening and data-quality exclusion in a given "
   "cell. It is computed as the product of frame size, observed prevalence, expected response "
   "rate and screen survival. Where achieved response rates are observable from published "
   "studies, achieved response rate is used as a second dependent variable for H4 and H5."],

  ["The independent variables follow the hypotheses. For H2, region concordance is a binary "
   "indicator of whether the national frame falls within the panel provider's home region, with "
   "region defined on the triad classification used by Rugman and Verbeke. For H3, coverage "
   "discrepancy is the difference between the regional concentration implied by a study's stated "
   "design and the concentration of its achieved responses, computed as a Herfindahl-style index "
   "over regions. For H4, mode is a categorical variable distinguishing telephone, email or "
   "platform panel, face to face, and mixed. For H5, standardization is an index constructed over "
   "whether the instrument held constant its item wording, length, incentive structure, "
   "sponsorship presentation and contact protocol across frames."],

  ["Control variables are population prevalence, frame size, eligibility strictness measured as "
   "the number of conjunctive screening criteria, incentive value expressed in purchasing power "
   "parity, field period length, and year of fielding. Eligibility strictness is included because "
   "it is the one term in the feasibility identity that is under the researcher's control, and "
   "any finding that does not separate it from the terms that are not under control would be "
   "uninterpretable."],

  {"h2": "Statistical method"},

  ["H1 is an analytic claim rather than an inferential one and is treated accordingly. It is "
   "established by demonstration and probed by sensitivity analysis over the full plausible range "
   "of prevalence, response and screen-survival values, reporting the region of the parameter "
   "space in which a comparative design remains viable. This is the appropriate treatment because "
   "the claim is about the structure of a conjunction and would not be made more true by a "
   "p-value. Reporting a significance test for it would misrepresent a deductive result as an "
   "empirical one."],

  ["H2 through H5 are tested with hierarchical linear models, with cells nested within national "
   "frames and frames nested within regions, and with random intercepts at the frame and provider "
   "levels. The nesting is not a statistical convenience; it is the substantive structure that "
   "Meyer and colleagues argue must be modelled explicitly, and ignoring it would attribute to "
   "countries the variance that belongs to providers. For H5 the standardization-by-baseline "
   "interaction is the term of interest, and the hypothesis is supported only if the interaction "
   "is significant in the predicted direction, not merely the main effect."],

  ["Where the instrument yields a scale rather than a single observable, reliability is "
   "established before use. The standardization index is the only constructed scale in the "
   "design; its internal consistency will be reported, and the individual components will be "
   "reported separately as well, because an index that conceals a divergent component would hide "
   "exactly the tradeoff the hypothesis concerns."],

  ["No data have been collected for this project. The design above is what the project proposes, "
   "and the preliminary evidence reported in the discussion comes from the author's prior study "
   "and from published response rates, not from fieldwork conducted for this paper."],

  # ================= DISCUSSION =================
  {"h1": "Discussion and Conclusions"},

  ["The expected pattern across the five hypotheses is a single one stated five ways: that the "
   "feasibility of comparative research on rare populations is determined by structural "
   "properties of the research infrastructure that are observable in advance, and that the "
   "profession's habit of treating these properties as execution problems has caused them to be "
   "discovered late and reported as limitations."],

  ["H1 is expected to hold by construction, and the contribution lies in its magnitude rather "
   "than its direction. The demonstration that the mean response rate across a design is nearly "
   "uninformative about that design's viability, while the minimum is decisive, has an immediate "
   "consequence for how comparative work should be reported. Studies currently report an overall "
   "response rate. Under H1 that number is the wrong summary statistic and a per-frame minimum "
   "should be reported alongside it."],

  ["H2, if supported, would establish that the regionalization thesis applies to research "
   "infrastructure and not only to the firms that infrastructure is used to study. This is the "
   "most consequential of the four empirical hypotheses, because it implies that comparative "
   "findings in the field carry a regional signature imported from the panels rather than from "
   "the phenomena. If it is not supported, the more likely explanation is that the major "
   "providers have converged on similar global recruitment channels, which would itself be worth "
   "documenting and would bound the claim usefully."],

  ["H3, if supported, would show that the divergence between stated and achieved coverage is "
   "systematic rather than incidental, and that it scales with population narrowness. The "
   "practical yield is a reporting standard: achieved coverage by frame, reported as a matter of "
   "course, in the way that response rates already are."],

  ["H4 is the hypothesis most likely to be wrong and the most valuable if it is right. It rests "
   "on a single observation from one study, which is not evidence. If mode does dominate country, "
   "then a portion of the cross-national variation the field has interpreted substantively is "
   "methodological, and comparative designs should be matched on mode before they are compared on "
   "context. If it does not hold, the finding still disciplines the literature by establishing "
   "that the Korean datum was idiosyncratic, which is worth knowing because that datum currently "
   "sits in a widely cited source without qualification."],

  ["H5, if supported, would identify the equivalence-response tradeoff as a design decision with "
   "an interaction rather than a uniform cost, and would show that standardization is most "
   "damaging where the design is already weakest. The prescription that follows is not to abandon "
   "equivalence but to concentrate adaptation in the binding frames, which is a specific and "
   "testable recommendation rather than general advice to balance the two."],

  {"h2": "Theoretical contributions"},

  ["The principal theoretical contribution is to reposition sampling feasibility as a parameter "
   "of a comparative design rather than a limitation of a completed one. This changes what is "
   "knowable and when. A parameter is estimated in advance and constrains the design space; a "
   "limitation is a retrospective account of why a design did not work. The paper supplies the "
   "identity that links the observable quantities to reachable sample and demonstrates that the "
   "quantities are available before commitment."],

  ["The second contribution extends the regionalization argument to a new object. Rugman and "
   "Verbeke, and Lopez, Kundu and Ciravegna, established that the gap between a firm's stated "
   "geographic scope and its realised scope is systematic. This paper proposes that the same gap "
   "exists for research infrastructure and, by extension, for the studies built on it. That is an "
   "instance of using an existing theory to look at a new phenomenon, which is one of the routes "
   "to contribution the seminar identifies."],

  ["The third contribution is a levels-of-analysis correction. By separating population, "
   "infrastructure, instrument and design as distinct determinants of feasibility, the framework "
   "makes it possible to state which level produced a failed frame. The current convention, which "
   "attributes such failures to the country, commits the error Meyer and colleagues warn against "
   "and does so systematically."],

  {"h2": "Managerial and practical contributions"},

  ["For researchers the yield is a pre-commitment test. Before a comparative design is funded, "
   "the reachable sample in the weakest intended frame can be computed from quantities that cost "
   "nothing to obtain. A design that fails this test fails before money is spent rather than "
   "eighteen months afterward. The author's own case is the argument for why this matters: the "
   "constraint was discovered after fielding, and the cost of that discovery was the study."],

  ["The second practical yield is the method-switch threshold. The framework identifies the point "
   "at which a population that cannot sustain a survey can still sustain an interview-based "
   "design, and it locates that point in advance. This reframes a class of research problems "
   "currently treated as failures. A population of twenty reachable participants is a failed "
   "survey and a well-powered phenomenological study, and knowing which of those two a project is "
   "before it begins is the difference between a contribution and a write-off."],

  ["For organisations commissioning multi-country research the implication is a procurement one. "
   "A vendor proposal covering eight markets should be evaluated on its weakest market, and the "
   "regional origin of the panel should be treated as material information about coverage rather "
   "than as a corporate detail."],

  {"h2": "Limitations"},

  ["The feasibility model holds prevalence constant across countries, and it almost certainly is "
   "not constant. No cross-national prevalence data for specialist professional populations "
   "currently exists, which is why obtaining it is the empirical contribution the project "
   "proposes rather than an assumption it can rely on. Until that data exists, the model's "
   "cross-national figures should be read as illustrating a structure, not as estimating a "
   "quantity."],

  ["The response rates used come from a single study, one instrument and one period. They are the "
   "best available and they are not sufficient. Treating them as a general country characteristic "
   "would commit the level-of-analysis error the paper itself identifies, and H4 exists in part "
   "to test whether that error is being made."],

  ["The model treats national response rates as independent. They are not; frames within a region "
   "share institutional conditions and will correlate, which means the true joint feasibility of "
   "a multi-frame design is worse than an independence assumption implies in some configurations "
   "and better in others. Estimating the correlation structure requires the data the project "
   "proposes to collect."],

  ["Finally, panel audience-configuration estimates are vendor-supplied and are not audited. They "
   "are the same numbers researchers currently rely on when commissioning work, so using them "
   "does not introduce a new exposure, but a systematic comparison of estimated against achieved "
   "counts is a necessary validation step and is not yet part of the design."],

  {"h2": "Conclusion"},

  ["Comparative international business research has treated the question of who can be reached as "
   "a matter of execution. For general populations that treatment is harmless. For narrow "
   "specialist populations it is not, because the arithmetic that governs reachability compounds "
   "across national frames in one direction and is decided by the weakest frame rather than the "
   "average one. The quantities involved are observable before a study is fielded. Making them "
   "part of the design, rather than part of the confession, is a small change in practice and a "
   "substantial change in what the field can claim to have compared."],

  # ================= REFERENCES =================
  {"h1": "References"},

  ["Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international "
   "expansion: The link between multinationality and performance in the service sector. Journal "
   "of International Business Studies, 34(1), 5-18."],
  ["Ghemawat, P. (2001). Distance still matters: The hard reality of global expansion. Harvard "
   "Business Review, 79(8), 137-147."],
  ["Harzing, A.-W., Reiche, B. S., & Pudelko, M. (2012). Challenges in international survey "
   "research: A review with illustrations and suggested solutions for best practice. European "
   "Journal of International Management."],
  ["Lopez, L. E., Kundu, S. K., & Ciravegna, L. (2009). Born global or born regional? Evidence "
   "from an exploratory study in the Costa Rican software industry. Journal of International "
   "Business Studies, 40(7), 1228-1238."],
  ["Meyer, K. E., Li, C., & Schotter, A. P. J. (2020). Managing the MNE subsidiary: Advancing a "
   "multi-level and dynamic research agenda. Journal of International Business Studies, 51(4), "
   "538-576."],
  ["Mezias, J. M. (2002). Identifying liabilities of foreignness and strategies to minimize their "
   "effects: The case of labor lawsuit judgments in the United States. Strategic Management "
   "Journal, 23(3), 229-244."],
  ["Rugman, A. M., & Verbeke, A. (2004). A perspective on regional and global strategies of "
   "multinational enterprises. Journal of International Business Studies, 35(1), 3-18."],
  ["Zeng, R., Grogaard, B., & Steel, P. (2023). Navigating MNE control and coordination: A "
   "critical review and directions for future research. Journal of International Business "
   "Studies, 54(9), 1599-1622."],

  {"pagebreak": True},

  # ================= TABLES AND FIGURES =================
  {"h1": "Tables and Figures"},

  {"h2": "Table 1. Panel frame required for 30 usable responses, by country"},
  {"__table__": "t1"},
  ["Note. Response rates from Harzing, Reiche and Pudelko (2012), Illustration 7. Prevalence of "
   "5.97 per 100,000 and screen survival of 0.174 are from the author's own study. Korea's rate "
   "was obtained by telephone through a survey company rather than by the instrument used in the "
   "other frames and is reported separately for that reason."],

  {"h2": "Table 2. What a design requires as national frames are added"},
  {"__table__": "t2"},
  ["Note. Target is 30 usable responses in every frame in the design. The binding rate is the "
   "minimum response rate among the frames included. The mean falls by roughly a third while the "
   "requirement rises by roughly a factor of four, which is the asymmetry H1 predicts."],

  {"h2": "Table 3. Hypotheses, theoretical source, and test"},
  {"__table__": "t3"},

  {"h2": "Figure 1. The binding-frame effect"},
  {"image": "/home/user/Profile/dba/coursework/GEB7365_International_Business/figures/fig1_feasibility_cliff.png",
   "width_in": 6.3,
   "alt": "Combination bar and line chart. Blue bars show the panel members required in every "
          "national frame to yield 30 usable responses, rising from 18.8 million for a design "
          "covering Spain alone to 72.2 million for a design covering Spain, Germany, Japan, the "
          "United Kingdom and China. An orange line shows the binding response rate falling from "
          "15.4 percent to 4.0 percent as countries are added. A grey line shows the mean "
          "response rate falling only from 15.4 percent to 9.2 percent over the same designs. "
          "The gap between the two lines is the point of the figure: the mean barely moves while "
          "the requirement quadruples, because the design is priced by its worst frame.",
   "caption": "Figure 1. Adding a national frame prices the design by its worst frame, not its "
              "average one. Response rates from Harzing et al. (2012); prevalence and screen "
              "survival from the author's own study."},

  # ================= AI DISCLOSURE =================
  {"h1": "Disclosure of Artificial Intelligence Use"},

  ["Generative artificial intelligence (Claude, Anthropic) was used to organise this draft, to "
   "format it to the required structure, to produce Figure 1 from the author's own model code, "
   "and to check the prose for clarity and grammar. The research question, the theoretical "
   "argument, the hypotheses and their justification, and the interpretation of the empirical "
   "inputs are the author's own. The figures reported derive from the author's own study records "
   "and from published sources cited in the text. No confidential, identifiable, or restricted "
   "data was provided to any artificial intelligence system. This disclosure is made in "
   "accordance with the FIU University Graduate School policy on artificial intelligence use and "
   "the course syllabus."],
 ],

 "tables": {
   "t1": [
     ["Country", "Response rate", "Panel frame required"],
     ["China", "4.0%", "72,229,200"],
     ["United Kingdom", "5.2%", "55,560,923"],
     ["France", "6.6%", "43,775,273"],
     ["Japan", "10.4%", "27,780,462"],
     ["Germany", "11.1%", "26,028,541"],
     ["Nordic countries", "11.3%", "25,567,858"],
     ["Australia / New Zealand", "12.7%", "22,749,354"],
     ["Spain", "15.4%", "18,760,831"],
     ["Korea (telephone)", "47.0%", "6,147,166"],
   ],
   "t2": [
     ["Design", "Mean response rate", "Binding rate", "Frame required in EACH country"],
     ["Spain", "15.4%", "15.4%", "18,760,831"],
     ["+ Germany", "13.2%", "11.1%", "26,028,541"],
     ["+ Japan", "12.3%", "10.4%", "27,780,462"],
     ["+ United Kingdom", "10.5%", "5.2%", "55,560,923"],
     ["+ China", "9.2%", "4.0%", "72,229,200"],
   ],
   "t3": [
     ["", "Hypothesis", "Theoretical source", "Test"],
     ["H1", "Joint feasibility is set by the least feasible frame, not the mean; adding a frame "
            "weakly decreases it", "Analytic; conjunction structure", "Demonstration plus "
            "sensitivity analysis over the parameter space"],
     ["H2", "Specialist prevalence on a panel is higher inside the provider's home region",
            "Rugman & Verbeke (2004)", "Hierarchical model; region concordance indicator"],
     ["H3", "Studies described as cross-national achieve regionally concentrated coverage, "
            "increasing with population narrowness", "Lopez, Kundu & Ciravegna (2009)",
            "Coverage discrepancy index across published studies"],
     ["H4", "Mode explains more variance in response than country does",
            "Meyer, Li & Schotter (2020)", "Variance decomposition across levels"],
     ["H5", "Standardization is negatively associated with response, more so in weak frames",
            "Zeng et al. (2023)", "Standardization by baseline-response interaction"],
   ],
 },
}

json.dump(spec, open('geb7365_report.json', 'w'))
print("spec written")
