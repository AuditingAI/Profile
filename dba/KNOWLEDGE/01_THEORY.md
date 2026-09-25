# Theory — the six ideas the programme stands on

Each entry: **the claim · the source · the strongest objection · how I teach it in five minutes.**

The objection is not decoration. An idea you can only argue for is an idea you have not finished
learning.

---

## 1 · Anchoring-and-adjustment

**The claim.** People given a starting value adjust from it insufficiently, even when the value is
known to be arbitrary. The final judgment stays closer to the anchor than the evidence warrants.

**Source.** Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: heuristics and biases.
*Science, 185*(4157), 1124–1131.

**In audit.** The prior-year conclusion is the anchor. Current-period judgment adjusts away from it
too little. This is the foundation of the entire quantitative model — all eight interventions are
attempts to weaken it.

**The strongest objection.** The anchoring literature has taken real replication damage. Some
classic demonstrations have not held at scale, and effect sizes in the field are smaller than the lab
implies. **This matters more here than in most applications**, because the prior-year conclusion is
not arbitrary — it is genuinely diagnostic. An auditor who weights it heavily may be doing good
Bayesian updating rather than anchoring. *Distinguishing rational reliance from anchoring is the
hardest measurement problem in the whole model, and the instrument does not fully solve it.*

**Teach it in five minutes.**
> Ask the room to write down the last two digits of their phone number. Then ask them to estimate the
> year the Eiffel Tower was completed. Collect both. The correlation is usually visible and always
> uncomfortable, because everyone knows their phone number is irrelevant and it moves the estimate
> anyway.
>
> **The question that starts the argument:** *"Now — is last year's audit conclusion your phone
> number, or is it evidence?"* It is genuinely both, and the room will split. That split is the whole
> research problem.

---

## 2 · Dual-process theory

**The claim.** Judgment runs on two systems: fast, automatic, associative (System 1) and slow,
effortful, rule-governed (System 2). Biases arise when System 1's output is accepted without System 2
engaging.

**Source.** Kahneman, D. (2011). *Thinking, Fast and Slow.* Also on the shelf — `../../books.html`.

**Why the model needs it.** It supplies the *mechanism*. The eight interventions are not eight
unrelated good practices; they are eight ways of forcing System 2 engagement at a moment where System
1 would otherwise settle the question. Structured procedures, independent review and mandated
debriefs are all interrupts.

**The strongest objection.** Dual-process theory is a useful description that is very hard to
falsify. "System 2 failed to engage" can be said after any error, which makes it a label rather than
a prediction. Careful researchers treat it as a framing device, not a testable theory — and the
programme should be honest that it uses it that way.

**Teach it in five minutes.**
> Drive a familiar route and arrive with no memory of the journey. Nothing went wrong; nothing
> demanded attention. Then a child steps into the road and the whole system changes gear.
>
> **The question:** *"What is the child in an audit? What actually makes a reviewer change gear?"*
> The honest answer in most firms is: a regulator, or a mistake that already happened. Everything in
> the model is an attempt to manufacture the child.

---

## 3 · Automation bias — this is L1

**The claim.** People over-rely on automated output: they accept wrong recommendations (commission
errors) and fail to act when the system stays silent (omission errors). Documented across aviation,
clinical decision support, and process control.

**Why it is the hinge of the whole programme.** It is the bridge from a fifty-year-old human bias to
the AI question. The anchor has not disappeared — it has become automated, continuous, and it now
arrives *before* the reviewer has formed a view. That last property is the novel one, and it is what
distinguishes L1 from ordinary anchoring.

**The strongest objection.** There is a substantial literature on **algorithm aversion** — people
discarding algorithmic advice after seeing it err once, even when it outperforms them. Automation
bias and algorithm aversion are both well-evidenced and point in opposite directions. **The
programme's argument is incomplete until it says which conditions produce which**, and it does not
currently say. `[OPEN]` — this is the most serious unaddressed theoretical gap in the chain.

**Teach it in five minutes.**
> Satellite navigation into a field. Everyone has done it or watched someone do it. The road was
> visibly wrong and the instruction won.
>
> **The question:** *"Now — how many of you have ignored the sat-nav because it was wrong once?"*
> Both hands go up in the same room. **That contradiction is the live research question**, and
> teaching it as a contradiction rather than resolving it is the honest version.

---

## 4 · Sycophancy — this is L2

**The claim.** Language models tend to agree with a position a user has already stated, adjusting
their answer toward the user's expressed view rather than toward the evidence. It is a property of
how the models are trained to be helpful, not a bug in a particular one.

⚠️ **This is not a cognitive bias.** It is model behaviour. Calling it one is the fastest way to lose
the argument in front of an examiner, and it is the single most common error made when describing
this work.

**Why it is different from L1.** L1 is a human failing in the presence of a machine. L2 is a machine
failing in the presence of a human. They compound: a reviewer predisposed to accept system output
meets a system predisposed to confirm.

**The strongest objection.** Sycophancy is well-documented in model evaluations and **not documented
at all in professional audit settings.** The jump from benchmark behaviour to what happens in a real
review is exactly the kind of inference this programme criticises other people for making. That is
why the qualitative arm exists and why it describes rather than tests. See `../QUALITATIVE/`.

**Teach it in five minutes.**
> Type into any chatbot: *"I think this contract clause is unenforceable — am I right?"* Then open a
> fresh window and type: *"I think this contract clause is enforceable — am I right?"* Same clause.
> Watch what happens.
>
> **The question:** *"If a junior analyst did that, what would you call it?"* The room will say
> something unflattering. Then: *"So what do we call it when the tool does it, and why do we trust
> the tool more?"*

---

## 5 · Recursive epistemic drift — this is L3

**The claim.** When successive systems reprocess work that earlier systems influenced, the outputs
converge on each other rather than on evidence. The evidentiary basis thins while the apparent
consensus strengthens.

**Related, not identical: model collapse** — the documented degradation when generative models are
trained on their own outputs. L3 is the *organisational* analogue: not models trained on model
output, but judgments built on judgments that a model shaped.

**Why it is the most interesting and the weakest link.** It is a system-level property, and it is the
only one of the three that would show up as *increasing* confidence and *decreasing* diversity at the
same time — which is what makes it dangerous and hard to notice from inside.

**The strongest objection.** It is entirely argued. No design in this programme tests it, and none is
proposed — see `../QUALITATIVE/README.md`, which scopes it out for a stated reason. Anything said
about L3 must be flagged as an argument, every time.

**Teach it in five minutes.**
> A photocopy of a photocopy of a photocopy. Everyone knows what happens. Now make it worse: each
> copy comes back sharper-looking than the last, because the machine cleans up the noise it does not
> recognise.
>
> **The question:** *"How would you know, from inside, that this was happening?"* The honest answer is
> that you probably would not, which is the point.

---

## 6 · The prevalence constraint

**The claim.** For a low-prevalence specialist population, the binding constraint on empirical work is
not budget, effort, or design quality. It is the number of eligible people who exist in the frame
you chose — and it is knowable *before* fielding.

**The evidence.** This programme's own: ~20 eligible out of 334,976 panel members, near six per
hundred thousand. Roughly $1,000 spent for four usable responses.

**Why it belongs among the theories.** Because it generalises. It is not an anecdote about one study;
it is a statement about the relationship between population definition and method choice, and it is
the one original contribution the programme currently has. See `04_THE_FAILURE.md` and
`../RISK_QUANT/FEASIBILITY_MODEL.md`.

**The strongest objection.** One case. The generalisation is argued from a single failed study on a
single platform, and the field may already know this and simply not publish it — publication bias
against reporting recruitment failure would produce exactly the silence being observed. **RB01 exists
to find out.** See `../AI_RUNBOOKS/perplexity/RB01_recruitment_precedent.md`.

**Teach it in five minutes.**
> *"I want to survey 100 left-handed neurosurgeons. What is my first move?"* The room will say design
> the instrument, get IRB, find a panel.
>
> **The correct first move is arithmetic:** how many left-handed neurosurgeons exist in the frame? If
> the answer is twenty, no instrument and no budget saves you, and you have just learned that your
> question needs interviews rather than a survey.
>
> **The line to land on:** *"I paid a thousand dollars to learn something that was on the screen for
> free, before I spent anything."*

---

## Open items

- [ ] **The automation bias / algorithm aversion contradiction** (§3) is unresolved and is the
      programme's most serious theoretical gap. Needs a boundary-conditions account.
- [ ] `[VERIFY]` Kahneman (2011) chapter references before citing specific pages.
- [ ] Sycophancy needs a primary citation from the model-evaluation literature, read in full — not a
      secondary description. Assigned to `RB02`.
- [ ] Model collapse needs the same. Currently held on general knowledge, which is not a source.
