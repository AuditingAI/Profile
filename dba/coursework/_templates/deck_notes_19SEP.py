# -*- coding: utf-8 -*-
"""Toastmasters speaking notes, one block per slide, for the GEB 7365 deck.

Structure per slide is fixed on purpose so the eye lands in the same place
every time: a clock, the words to say, the physical cue, and the single
keyword that slide exists to deliver. Opening 10 percent, body 80, close 10.
"""

NOTES = [
# 1 TITLE
"""[0:00 - 0:25]   OPENING   Block 1 of 6

>> DO NOT START WITH YOUR NAME. Start with the number.

SAY:
"I screened three hundred and thirty four thousand people."
    ... hold two full seconds. Look at one face. ...
"I got four."

"That is not bad luck. That is arithmetic, and every bit of it
 was visible before I spent a cent."

ROADMAP:
"Five elements. The topic. The model. Five hypotheses and why each
 one follows. How I would test it. And my evidence, which is that
 failure."

>> CUE: stand still. Hands at your sides. The pause is the hook.
>> KEYWORD: arithmetic, not bad luck.
""",

# 2 ELEMENT 1 TOPIC
"""[0:25 - 1:15]   OPENING   Element 1

SAY:
"To compare something across countries you have to reach the same
 people in every country, at the same time, with an instrument that
 means the same thing in each place. Nobody writes that down as a
 requirement. It just sits there."

"For a general population it is a fieldwork problem. Money and effort
 turn into responses. The rate differs by country, but it is always
 positive and always improvable."

"For a rare population it is not a fieldwork problem at all. It is
 arithmetic that was fixed before the first contact. And it does not
 add across borders. It compounds, in one direction."

>> CUE: point left box, then right box. Two gestures, no more.
>> KEYWORD: fieldwork problem on the left, design parameter on the right.
""",

# 3 ELEMENT 1 GAP AND QUESTION
"""[1:15 - 1:55]   OPENING ends here   Element 1

SAY:
"Received wisdom says sampling difficulty is an execution problem.
 It belongs to budget and local partners, and it shows up in print as
 a limitation paragraph at the end."

"The gap is that nobody asked what happens when the population is
 rare. The quantities that decide it are observable before you field
 anything."

THE QUESTION, read it slowly off the slide:
"Under what conditions is a comparative multi-country design on a
 narrow specialist population feasible at all, and where must a survey
 give way to another method?"

THE CONTRIBUTION, land this one:
"To move feasibility from a limitation to a parameter."

>> SIGNPOST OUT LOUD: "That is the topic. Now the model."
>> KEYWORD: parameter, not limitation.
""",

# 4 ELEMENT 2 MODEL
"""[1:55 - 3:10]   BODY 1   Element 2

SAY:
"Reachable usable sample is a product, not a sum. Four terms."

Walk them left to right, one breath each:
"Frame size. How many people the panel has.
 Times prevalence. How rare the specialty is.
 Times response rate. Who answers.
 Times screen survival. Who gets through eligibility."

"And here is the part that matters. Each of those is decided at a
 different level. Frame size is population. Prevalence is
 infrastructure. Response is the instrument. Screen survival is my
 own design. Blaming a failed country for all four assigns to one
 level what another one produced."

"All four are readable on the panel's own interface, free, before
 anyone commits a dollar. That is why it is a parameter."

>> CUE: four fingers, then close the hand on "product, not a sum."
>> KEYWORD: four terms, four different levels.
""",

# 5 BINDING FRAME
"""[3:10 - 4:40]   BODY 1   Element 2   *** THE CENTRAL SLIDE ***

>> ASK THE ROOM FIRST. Then wait. Do not answer your own question.

"How many of you have read a comparative paper that reported one
 overall response rate?"

    ... wait for hands. Count them out loud if you like. ...

"That is the number I am telling you is wrong."

SAY:
"Add four countries to a design. The mean response rate barely moves,
 fifteen point four down to nine point two. Looks survivable."

"But the panel you need in each frame goes from eighteen point eight
 million to seventy two point two million. A factor of four."

"The design is priced by its worst frame, not its average one. An
 average cannot satisfy a conjunction."

>> CUE: this is where you stand still. Do not walk.
>> KEYWORD: the average hides it, the worst frame decides it.
>> SIGNPOST: "That is the model. Now the hypotheses."
""",

# 6 FIVE HYPOTHESES
"""[4:40 - 5:20]   BODY 2   Element 3

>> DO NOT READ ALL FIVE. Name them and move. You have a slide each
>> for the ones that matter.

SAY:
"Five hypotheses, and each one takes its logic from one of this
 week's four papers, not from my own intuition."

"H1 is the binding frame. H2 and H3 come from regionalization.
 H4 is level of analysis. H5 is standardization against response."

"I will take H1 on its own, then H2 and H3 together, then H4 and H5."

>> CUE: run your hand down the column once. Do not read the boxes.
>> KEYWORD: five hypotheses, four papers, one argument.
""",

# 7 H1
"""[5:20 - 6:10]   BODY 2   Element 3   H1

SAY:
"To say a relationship differs between Spain and China is to assert
 something about Spain AND something about China. That is a
 conjunction. It fails if either half fails."

"So a design with one excellent frame and one hopeless frame has a
 respectable mean and no comparison at all."

"And because a minimum can only fall or stay level when you add an
 element, every extra country weakly worsens the design. No extra
 country can improve it."

LAND IT:
"Breadth is treated as a virtue in comparative work. A design covering
 more countries has not become more ambitious. It has become more
 fragile."

>> CUE: two hands apart on "Spain AND China," then bring them together.
>> KEYWORD: a comparison is a conjunction, not an average.
""",

# 8 H2 H3
"""[6:10 - 7:10]   BODY 2   Element 3   H2 and H3

>> THIS IS THE SLIDE THAT MAKES IT INTERNATIONAL BUSINESS. Say so.

SAY:
"Rugman and Verbeke looked at the three hundred and eighty largest
 multinationals with usable sales data. Three hundred and twenty were
 home-region oriented, averaging eighty point three percent of sales
 at home. Nine were global. Nine."

"Their mechanism is specific. Upstream advantages in technology
 travel. Downstream advantages like branding are location-bound."

"Now apply that to a research panel. A panel is a firm whose entire
 product is a downstream asset. Its membership, and its standing with
 that membership. Survey software is a commodity, so there is almost
 no upstream advantage to carry abroad."

"By their own logic a panel should be MORE home-region bound than a
 manufacturer, not less."

"And it bites harder for specialists. A consumer panel is built by
 broad advertising anywhere. A panel of experienced auditors is built
 through professional bodies, and those are national by construction."

>> IF ASKED about the seven institutional types: say you are raising it
>> with the professor rather than quietly revising after the deadline.
>> KEYWORD: a panel is a firm, and its product is entirely downstream.
""",

# 9 H4 H5
"""[7:10 - 8:00]   BODY 2   Element 3   H4 and H5

SAY H4:
"Response is what happens when a person meets a request. Whether that
 request arrives by telephone from a human being or by email from a
 platform is a property of the instrument, not of the country."

"Mode changes the cost of refusing. Country only changes the
 disposition toward it."

"My one datum: Harzing's forty seven percent in Korea was telephone,
 and it beats the entire country spread in the same project by about
 five times. One observation is not evidence. It is why this is a
 hypothesis and not a finding."

SAY H5, and be careful here:
"Zeng and colleagues name standardization as a control mechanism,
 against coordination by mutual adjustment. They do NOT claim the two
 trade off. They say the interaction is understudied."

"Proposing that equivalence and response pull against each other is my
 conjecture about a gap they name. It is not a finding I am borrowing."

>> CUE: saying what is yours and what is theirs is the most credible
>> thing in the talk. Do not rush it.
>> SIGNPOST: "That is the why. Now how I would test it."
""",

# 10 DATA COLLECTION
"""[8:00 - 8:45]   BODY 3   Element 4   data sources

SAY:
"Panel providers expose an audience-configuration interface. You enter
 your screening criteria and it returns an estimated reachable count,
 before any commitment, at no cost. That single fact is what makes
 feasibility a parameter rather than a confession."

"The unit of analysis is one occupation, on one provider, in one
 national frame. Six occupations by eight frames by three providers is
 roughly a hundred and forty four cells."

"Providers are chosen to vary on home region, deliberately. H2 is
 unidentifiable otherwise."

"And the validating case is my own study. A model that cannot
 reproduce three hundred and thirty four thousand to twenty to four is
 rejected."

>> SAY THE DISCLAIMER OUT LOUD, do not let them read it:
>> "No data has been collected for this project. This is the design."
>> KEYWORD: free, before commitment, on the vendor's own interface.
""",

# 11 VARIABLE MEASURES
"""[8:45 - 9:30]   BODY 3   Element 4   variable measures

>> THIS SLIDE IS SCORED. The rubric asks for variable measures
>> explicitly. Walk the table, do not wave at it.

SAY:
"Dependent variable is the reachable usable sample, the product of the
 four terms, read off the interface."

"Second dependent variable for H4 and H5 is the achieved response
 rate, taken from published method sections."

"H2 is measured as region concordance, binary, against the triad,
 from incorporation and headquarters filings."
"H3 is coverage discrepancy. Stated regional coverage minus achieved."
"H4 is mode, categorical, coded by two readers."
"H5 is a standardization index over wording, length, incentive,
 sponsorship and protocol."

"Controls are prevalence, frame size, eligibility strictness as a
 count of conjunctive screens, incentive at purchasing power parity,
 field period and year."

>> CUE: one finger down the left column. Four beats.
>> KEYWORD: every measure has a named source. Nothing is assumed.
""",

# 12 ANALYSIS PLAN
"""[9:30 - 10:15]   BODY 3   Element 4   method

SAY:
"Two different kinds of claim need two different treatments."

"H1 is analytic. It is established by demonstration and probed with a
 sensitivity analysis across the plausible range, reporting the region
 of the parameter space where a comparative design stays viable."

"I am deliberately not putting a p-value on H1. The claim is about the
 structure of a conjunction. A p-value would present a deductive
 result as an empirical one."

"H2 through H5 are inferential. Hierarchical linear models. Cells
 nested in frames, frames nested in regions, random intercepts at
 frame and provider level."

"The nesting is not a convenience. It is the structure Meyer and
 colleagues argue has to be modelled, and ignoring it attributes to
 countries the variance that belongs to providers, which is the exact
 error this paper is about."

"H5 is supported only by the interaction, not the main effect."

"Software is R with lme4, Stata as a cross-check, everything versioned
 in git."

>> KEYWORD: two kinds of claim, two treatments.
""",

# 13 TIMEFRAME
"""[10:15 - 10:45]   BODY 3   Element 4   timeframe

SAY:
"Nine months, four phases."

"And the thing I want you to notice is what is missing. There is no
 recruitment step anywhere on this chart."

"The constraint that ended my qualifying study was recruitment. This
 design does not have one. The measurements already exist on the
 platforms. The work is gathering them systematically rather than
 obtaining them."

"No human subjects at any phase. I still intend to confirm the
 exemption with the IRB office before Phase 1 rather than assume it."

>> CUE: trace the timeline left to right once with a flat hand.
>> SIGNPOST: "That is the design. Now what I actually have."
>> KEYWORD: no recruitment step at all.
""",

# 14 PRELIMINARY EVIDENCE
"""[10:45 - 11:40]   EVIDENCE   Element 5

>> SLOW DOWN. This is the most honest slide in the talk and honesty
>> is what gets remembered.

SAY:
"No data has been collected for this project. What I have is the
 qualifying study, which was designed to test something else entirely
 and failed for exactly the reason this project is about."

"Three hundred and thirty four thousand nine hundred and seventy six
 panel members screened."
    ... pause ...
"About twenty eligible."
"Four usable, out of twenty three raw starts."
"That is about six per hundred thousand."

NOW SAY WHAT IT CANNOT DO:
"H1 it bears on directly. It supplies the prevalence and screen
 survival terms the whole model runs on."
"H2 it says nothing about. One provider, one home region. The
 comparison H2 needs does not exist in my data."
"H4 only weakly. My instrument was one mode, so mode could not be
 separated from anything."

"This is one case, fully documented. It is not evidence that the
 pattern generalises. That is what the design is for."

>> KEYWORD: say what your evidence cannot do.
""",

# 15 DOES NOT CLAIM
"""[11:40 - 12:20]   EVIDENCE   the limits, stated first

>> PUT THIS BEFORE THE Q AND A ON PURPOSE. Say that out loud.

SAY:
"I would rather state the limits than be handed them."

"One. Prevalence is held constant across countries in the model. It
 almost certainly is not. No cross-national prevalence data for these
 populations exists, which is why obtaining it is the contribution
 rather than an assumption."

"Two. The response rates come from one study. One instrument, one
 period. Treating them as a general country characteristic would
 commit the very level-of-analysis error the paper identifies."

"Three. The rates are treated as independent and they are not. Frames
 inside a region share institutional conditions and will correlate."

"Four. The panel estimates are vendor-supplied and unaudited. They are
 the same numbers researchers already rely on, so this adds no new
 exposure, but estimated against achieved is a validation step that is
 not in the design yet, and it should be."

>> KEYWORD: the weakest part is the unit, and H1 being analytic.
""",

# 16 CLOSE
"""[12:20 - 13:00]   CLOSE   Block 6 of 6

>> NO NEW MATERIAL. Return to the one message and stop.

SAY:
"A parameter is worked out before a design. A limitation is confessed
 after it fails."

"Comparative international business has treated who can be reached as
 a matter of execution. For general populations that is harmless. For
 narrow specialist populations it is not, because the arithmetic
 compounds in one direction and the weakest frame decides it."

"All of these numbers are visible before you field anything."

THE LAST SENTENCE. Land it and stop:
"Making them part of the design instead of part of the confession is a
 small change in practice and a large change in what we can claim to
 have compared."

AND THE SECOND IMPLICATION, if you have the time:
"Where the arithmetic rules out a survey, it does not rule out the
 study. Twenty reachable participants are a failed survey and a well
 powered phenomenological one."

>> STOP. Do not say "so, yeah, that's it." Say "Thank you. Questions."
>> KEYWORD: parameter before, limitation after.
""",
]
