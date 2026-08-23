# Handoff board

How the 🎓 Scholar and 💼 Industry agents talk. **Append-only. Newest at top. Date and sign every
entry with your lane.** Read this at the start of every session — it is the only place the other
agent's state is visible to you.

**Post when:** something in the other lane needs to change · a shared fact moves (publication status,
interview stage, a CV item resolved) · you were blocked by something the other agent owns.

**Do not** edit or delete another agent's entries. Reply beneath with a new dated entry.

Ownership boundaries and git discipline are in `../CLAUDE.md`.

---

## 2026-08-22 · 🎓 SCHOLAR — standing rule added to CLAUDE.md: which mailbox sends what

Yasir has been explicit twice now: **nothing is ever sent by an agent, and academic mail goes out
from `ymali001@fiu.edu`, not Gmail.** A message to a professor or the program office arriving from a
personal address reads wrong and can miss institutional filters.

I have added that to the standing facts in `CLAUDE.md`, immediately above the existing "draft freely,
send nothing" rule. It changes nothing about the send prohibition — that already applied to both
lanes — it records **which mailbox a drafted item is written for**, so a draft is addressed and
signed correctly before it reaches him.

💼 **Industry — one thing for you.** The rule as written says academic mail goes from the FIU
address and that industry correspondence follows its own lane's channel. If recruiter and
application mail should go from Gmail, that is already what happens and nothing changes. If any of
it should go from somewhere else, add it — the line is deliberately left open for you rather than
guessed at.

Practical note that affects both lanes: the Gmail connector in this session reaches only
`yasiramalik@gmail.com`. **We cannot read the FIU mailbox**, so anything sent to ymali001 is
invisible to us unless he forwards it. Several FIU items have already been missed that way.

— 🎓 Scholar

---

## 2026-08-20 · 🎓 SCHOLAR — claiming a new skill path: `.claude/skills/coursework/`

`CLAUDE.md` lists Scholar as owning `.claude/skills/research/` and `.claude/skills/academic-jobs/`.
Coursework was not anticipated when that table was written — Yasir is now carrying two graded DBA
courses and asked for them run as a managed track.

**I have created `.claude/skills/coursework/` and I am claiming it for the Scholar lane.** It is
squarely academic: syllabi, readings, note cards, class prep. It has no industry surface.

💼 Industry — no action needed unless you object. If you do, reply beneath rather than editing.
When `CLAUDE.md` is next revised, this path should be added to the Scholar block.

Also new and Scholar-owned: `dba/coursework/READING_LIBRARY.md` (entry point) and
`dba/coursework/COURSE_LOG.md` (append-only memory — recaps read from there rather than from a
conversation).

— 🎓 Scholar

---

## 2026-08-19 · 🎓 SCHOLAR — the DBA completion year is RESOLVED. Stop writing 2027.

`CLAUDE.md` §3 holds the completion year and GPA as unresolved and blocking both tracks, with the
rule that neither figure is asserted until the program office confirms. **For the year, that
confirmation now exists in writing.**

Yasemin Shirazi, Assistant Director of Doctoral Programs, Office of Doctoral Programs, Chapman
Graduate School — email of 26 March 2026, sent to both his FIU and personal addresses, copying
Aguirre, Leon, Lainez and Rey:

> *"As previously discussed, this is a lock step, cohort-based program. You will need to continue
> with the entirety of the program until your expected graduation, **Summer 2028**."*

That is the office that owns the answer, naming the term, unprompted. Corroborated by the Cohort
8.14 WhatsApp header ("Class of 2028") and his own 14 Aug cohort introduction.

**💼 INDUSTRY — action for you.** Any resume, cover letter, screening answer, or ATS field in
`career/applications/` that carries **2027** is wrong and is now demonstrably wrong against a
primary source. The supportable phrasing is **"expected Summer 2028."** I have not touched those
files, per the ownership contract. The Dropbox master resume needs the same fix and I cannot reach
it either.

**Still blocked, unchanged: the GPA.** No FIU communication states any figure. Daniela Leon's
11 Aug reply confirms only that enrollment verification *covers* GPA — it gives no number. The
3.81-vs-3.87 conflict stands. **Keep it `[VERIFY]` and assert nothing.**

The mechanism that settles it is the Enrollment Verification Form, which per the Office of Doctoral
Programs cannot be filed until after add/drop closes **23 August**. File it the week of 24 Aug.

**One obstacle worth knowing about, because it gates both of us:** AskIT incident INC00179615, an
FIU account lockout / Duo 2FA failure, shows three unlock responses in July and no closure message.
MyFIU is where tuition is paid *and* where the verification form is filed. If that login is still
broken, the GPA stays unresolved and the tuition goes unpaid — and **27 August is the date
non-payment makes him subject to being dropped from the DBA program.** That would end the academic
track and take the "doctoral candidate" line out of every industry document at the same time.

Primary source for all Fall/Spring dates now recorded at `dba/coursework/FIU_DBA_ACADEMIC_CALENDAR.md`.
Read it rather than trusting any briefing — several dates in circulation had no source behind them.

— 🎓 Scholar

---

## 2026-08-14 (evening) · 🎓 SCHOLAR — examiner wording fixed in MY lane. Yours is still wrong.

Yasir asked for the examiner line corrected everywhere. **I fixed only what Scholar owns:**

- `career/ACADEMIC_CV_YMalik.md` — profile paragraph and the experience entry
- `career/WEBSITE_CONTENT_KIT.md` — the 100-word bio and the proof-points list
- `career/FIU_Teaching_Interest_Letter.md` — the background sentence
- `career/academic/ACADEMIC_CV_v2.md` — already correct

**💼 INDUSTRY — ten files in `career/applications/` still say OCC and I did not touch them,
per the ownership contract.** They are yours to fix:

```
COMMON_ANSWERS.md
bmo-head-responsible-ai-governance/PACKAGE.md
bny-model-risk-ai-director/PACKAGE.md
goldmansachs-ai-model-validation-vp/PACKAGE.md
jpmorganchase-aiml-governance-vp/COVER_LETTER.md
jpmorganchase-aiml-governance-vp/RESUME_BRIEF.md
jpmorganchase-tech-risk-controls-director/PACKAGE.md
metlife-vp-ai-risk-governance/PACKAGE.md
morganstanley-model-validation-ed/PACKAGE.md
verisk-ai-governance-lead/PACKAGE.md
```

Replace any OCC / examiner phrasing with:

> bank examiner with the Florida Office of Financial Regulation, examining state-chartered banks
> jointly with the FDIC and the Federal Reserve Bank of Atlanta

This matters more on your side than mine: several of those cover letters **open** with the examiner
credential, and two applications have already gone out to JPMorganChase. Model-risk and audit
hiring managers know exactly which agencies supervise which charters.

Also note the master resume in Dropbox (`/Resume/Yasir_Malik_Resume_2026.docx` and `.pdf`) is
outside git entirely and almost certainly carries the old wording. Neither agent can edit it —
**Yasir has to fix that one by hand.**

---

## 2026-08-14 (later) · 🎓 SCHOLAR — examiner-agency question RESOLVED. Industry: use this wording.

Yasir clarified, and he is right: Florida OFR examiners work the **federal–state joint examination
programme**, conducting concurrent and alternating exams with federal counterparts and exchanging
confidential supervisory reports. His own 2017 resume corroborates it — *"Highly sensitive
information sharing with the related Regulatory Agencies such as Federal Deposit Insurance
Corporation (FDIC) Federal Reserve Bank of Atlanta (FRB)."*

**FDIC and Federal Reserve: keep them. State them as joint examination work, not as employment.**
Approved wording, now in the academic CV:

> Bank Examiner, Florida Office of Financial Regulation, Bureau of Bank Regulation (District II).
> Safety-and-soundness examinations of state-chartered community banks up to $3B in total assets,
> conducted on a **joint and alternating basis with the FDIC and the Federal Reserve Bank of
> Atlanta** under the federal–state supervisory programme.

This is stronger than the old three-agency list, because naming the mechanism signals someone who
understands supervisory architecture rather than someone padding a line.

**OCC: dropped, and it should stay dropped.** The OCC supervises *national* banks, which have no
state supervisor — so no federal–state joint programme exists with the OCC the way it does with the
FDIC and the Fed. Any reader who examines banks, or any hiring manager in bank regulatory risk, spots
that instantly, and it would put the two true claims in doubt. **Industry: your cover letters
currently open with "bank examiner with the OCC" — change that line.**

Employment remains Florida OFR. Federal engagement was joint examination and report exchange, plus
FDIC Corporate University training (*Introduction to Bank Examinations*, 2012).

---

## 2026-08-14 · 🎓 SCHOLAR — two documented discrepancies that affect BOTH tracks

Recovered a 2017 resume from Google Drive while rebuilding the academic CV. It surfaces two conflicts
with what the current documents claim. **Industry: read this before sending anything that describes
his regulatory background or his MBA.**

**1. Bank examiner agency — the important one.**
The 2017 resume lists **Florida Office of Financial Regulation only** (West Palm Beach, 2011–2012,
Bureau of Bank Regulation District II). The current academic CV says "OCC, Federal Reserve, and
FDIC." The website kit says "OCC and Florida OFR." The only federal item documented anywhere is
**FDIC Corporate University training** — *Introduction to Bank Examinations*, March 2012 — which is
training, not service.

→ **Neither agent should claim OCC or Federal Reserve examiner service until Yasir produces
documentation.** Industry cover letters currently lead with "bank examiner with the OCC." That
should change to Florida OFR, or the claim needs evidence. Overstating federal service is
disqualifying in a way an omission is not, and banks verify.

**2. MBA GPA.** 2017 resume says **3.71**; current academic CV says **3.8**. Add this to the existing
DBA-year and DBA-GPA discrepancies. The pending FIU enrollment verification covers GPA and should
settle all of them.

**Also recovered — genuinely good news for the academic track.** Four documented FIU graduate
appointments from 2010–2011 that were missing from every current document: Capital Markets Lab
Graduate Assistant (Employee Financial Literacy Program); Student-Athlete Academic Center Resident
Tutor in corporate finance and accounting; Sector Manager, Student Managed Investment Fund; and
instructional-support materials for FIN 6644. Plus FIU Ignite 100% Graduate Assistantship (2011) and
President of PakSA (2010). Corroborated by archived payroll forms and a full instructor-side course
folder with answer keys.

This materially strengthens the teaching case. No effect on the industry track.

**Scholar state unchanged otherwise:** P1 drafted not submitted · zero publications · teaching
statement still does not exist · zero academic applications sent.

---

## 2026-08-13 · 🎓 SCHOLAR — opening the board

**Track split confirmed by Yasir.** Scholar takes the doctorate — research, publications, and
academic/faculty appointments. Industry takes corporate roles. Two windows, one repo,
`CLAUDE.md` is the contract.

### Shared state, current as of today

**Publication status — this is the one Industry should watch.**
P1, *"Six in One Hundred Thousand: Why Specialist Professional Populations Cannot Be Recruited from
General Research Panels,"* draft v1 written, ~3,400 words, `dba/P1_Feasibility_Note/`.
**Not submitted.** Four blocking items in that folder's checklist.
→ *Industry:* once it is submitted somewhere, "manuscript under review" becomes usable in cover
letters. **Not before.** Nothing may describe it as under review, forthcoming, or published until
this entry says so.

**🚨 CV verification — blocks BOTH tracks, and nobody has resolved it.**
- DBA completion year: CV says **2027**; the approved 2024–25 evaluation records **Summer 2028**
- GPA: CV shows a **range**, 3.81–3.87, with a `[CONFIRM]` tag

Neither agent asserts either figure anywhere. Academic search committees verify degree dates and a
discrepancy is disqualifying; banks verify education too. **One call to the FIU DBA program office
clears both.** This has been open since 29 July.

**Research substance available to Industry.** The argument chain in `dba/PUBLICATION_TRACKER.md`
(chain v1.1, argued link by link) is what makes an industry cover letter distinctive — most
AI-governance candidates cannot articulate a mechanism. Quote it; do not edit it. Current state: L1
defensible, L2 time-sensitive, **L3 is the weak link and is where the empirical contribution lies.**

**Referral pipeline that touches both lanes.**
- **Dr. Juan C. Rey (FIU)** — passed Yasir in July. Letter drafted (`career/FIU_Teaching_Interest_Letter.md`),
  **blocked on the CV items above**. Scholar owns this thread.
- **Asad Rana** — Google referral request, resume sent 7 Aug, no reply as of 13 Aug. Industry's
  thread; flagging only so Scholar does not double-contact.

### Asks

**→ Industry:** post interview and offer stages here as they move. A live offer changes how hard
the academic track should push, and the academic calendar (postings open Aug–Oct for next fall) is
running now.

**→ Industry:** if you learn the DBA year or GPA from any source, post it here immediately. It
unblocks the FIU letter and every academic application.

**→ Yasir:** the program-office call is the highest-leverage thing available to either agent. It is
blocking the warmest referral you have.

### Scholar's current state — no action needed from Industry

| | |
|---|---|
| P1 | Draft v1, 4 blocking items, not submitted |
| P2 conceptual paper | Not started — waits for P1 |
| Dissertation | Blocked on the recruitment strategy (advisor Directive 5) |
| Teaching statement | **Does not exist.** Most postings require it. |
| Academic applications sent | Zero |
| Publications | **Zero.** This is the binding constraint on the whole academic track. |
