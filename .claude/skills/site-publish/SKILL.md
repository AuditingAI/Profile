---
name: site-publish
description: Add or update a page on Yasir's personal site (the Profile repo / auditingai.github.io). Use this whenever the user wants to publish, add, write up, or put something on the site — a research finding, a project write-up, a new section, a case study, a speaking or teaching page, a services page. Also use it when they say "put this on the site", "add a page for", "get this on the git", "make this public", or ask to update the nav or an existing page. It carries the site's design system, the cross-linking steps that are easy to forget, and the rules about what must never go public. Prefer this over writing HTML from scratch, because a hand-rolled page will silently drift from the house style and miss the nav/sitemap updates that make it reachable.
---

# Publishing to the site

This site is Yasir A. Malik's public professional presence. It is read by
recruiters, potential clients, academic collaborators, and — because he is
currently in active litigation — potentially by opposing counsel. Every page
added here is a permanent public artifact tied to his real name.

That context drives everything below. The design rules keep the site coherent;
the guardrails keep it from doing damage.

## Before writing anything: the publication test

Ask what would happen if the least friendly plausible reader found this page.
Most content passes easily. Some does not, and the cost of getting it wrong is
high enough to be worth a deliberate check.

**Never publish:**

- **Anything about the litigation.** Trial dates, filings, strategy, the
  opposing party, settlement posture, counsel-fee questions. Even framed as
  general commentary, a page that reveals he is in a matrimonial action hands
  information to the other side for no gain.
- **Anything about employment separation, unemployment claims, or job-search
  status.** A site that reads as "currently between roles" undercuts the
  authority the site exists to establish.
- **Business planning internals.** Pricing strategy, "don't chase deals right
  now", revenue targets, bandwidth constraints, which clients to pursue. These
  are decisions, not credentials.
- **Financial specifics.** Account details, property financials, holds or
  disputes, income figures.
- **Third-party private information.** Tenants, family members, clients,
  colleagues — names, situations, or documents.
- **Research findings that are not yet defended.** The DBA is in progress. It is
  accurate and impressive to describe *what the research investigates*. It is
  fabrication to state what it *found*. Describe questions, methods, and status;
  never invent results, effect sizes, or conclusions.

**Safe to publish**, and what the site is for: professional history and
credentials, research questions and areas of focus, completed and shipped work
(the Citi RAG audit QA tool and its "Delivers with Pride" award is the strongest
example), teaching and speaking, book recommendations and written commentary,
frameworks and methodology he actually uses.

When something sits on the line, the useful move is to name the concern in one
sentence and offer the version that is safe, rather than either publishing it
quietly or refusing the whole request. Usually there is a legitimate page hiding
inside a request that as-stated would be a mistake.

## The design system

The site is deliberately restrained: warm paper, a single blue accent, a serif
display face against a clean sans. Zero build step, zero JavaScript, zero
dependencies beyond one Google Fonts import. New pages match this exactly —
a page in a different visual language reads as bolted on.

Everything lives in `style.css` at the repo root. Use the existing tokens and
classes rather than writing new CSS; the vocabulary below covers nearly every
page you would need to build.

**Tokens** (defined in `:root`):

| Token | Value | Use |
|---|---|---|
| `--color-ink` | `#1a1a1a` | Headings, primary text |
| `--color-ink-light` | `#4a4a4a` | Body paragraphs |
| `--color-ink-muted` | `#7a7a7a` | Meta text, captions |
| `--color-paper` | `#faf9f6` | Page background |
| `--color-paper-warm` | `#f3f1ec` | Card and highlight backgrounds |
| `--color-accent` | `#2c5f8a` | Links, labels, interactive |
| `--color-accent-hover` | `#1d4a6e` | Hover states |
| `--color-rule` | `#d4d0c8` | Dividers, borders |
| `--font-display` | Instrument Serif | `h1`–`h3` |
| `--font-body` | DM Sans | Everything else |
| `--max-width` | `720px` | Content column |
| `--radius` | `10px` | Card corners |

**Existing classes** worth reaching for before inventing anything:
`.container` `.site-name` `.site-tagline` `.social-links` `.divider`
`.page-hero` `.page-title` `.page-subtitle` `.section-heading` `.intro`
`.research-section` `.research-intro` `.research-card` `.research-label`
`.research-label--dissertation` `.research-label--interest` `.skills-grid`
`.skill-group` `.highlights` `.highlight-item` `.highlight-number`
`.highlight-label` `.book-category` `.book-entry` `.category-nav`
`.back-to-top`

If a page genuinely needs something new, add a page-scoped `<style>` block in
the head that builds on the tokens, the way a one-off section would — don't
edit `style.css` for a single page's needs, since that stylesheet is shared by
every page and a change there can shift layouts you aren't looking at.

**Page skeleton.** Copy the structure from `research.html`, which is the
cleanest example: `<div class="container">` wrapping a `<header>` with site name,
tagline, and social links; an `<hr class="divider">`; the `<nav>`; the page
content; and a `<footer>`. Set `class="active"` on the current page's nav link.
Indentation is 4 spaces.

## The steps that get forgotten

A new page is not published until it is reachable. These four things are what
separate "the file exists" from "someone can find it," and skipping any of them
produces a page that is live but effectively invisible.

1. **Add the page to the nav in every existing page**, not just the new one.
   Currently that means `index.html`, `research.html`, and `books.html`. A nav
   that differs between pages is the most visible possible sign of a site that
   isn't maintained.
2. **Add it to the footer links** where the site uses them.
3. **Add a `<url>` entry to `sitemap.xml`** with today's date as `lastmod`, so
   search engines index it.
4. **Fill in the metadata**: `<title>`, `<meta name="description">`, and the
   Open Graph `og:title` / `og:description` / `og:type` tags. The OG tags are
   what render when a link is shared on LinkedIn, which is exactly how this site
   gets seen.

## Before committing

Run these checks. They take seconds and catch the errors that are embarrassing
rather than merely wrong.

```bash
# Placeholders — the site has shipped with these before
grep -rn "YOUR_ID\|YOUR_USERNAME\|YOUR_PROFILE\|TODO\|Lorem ipsum" *.html

# Every internal link resolves
for f in *.html; do
  grep -oE 'href="[a-zA-Z0-9_.-]+\.html' "$f" | sed 's/href="//' | sort -u | \
  while read t; do [ -f "$t" ] || echo "BROKEN: $f -> $t"; done
done

# Stylesheet reference present on the new page
grep -c 'href="style.css"' <newpage>.html
```

Also confirm the footer copyright year is current — it has gone stale before.

## Git

The repo has a real history of concurrent work: **another session has rewritten
this branch mid-task before**, replacing the entire site. Before committing,
`git fetch` and check whether the remote has moved.

If the remote has commits you don't have, **stop and show the user what changed
rather than merging or force-pushing.** A force-push here destroys someone's
work, and a mechanical merge of two different site versions produces a broken
hybrid — mismatched stylesheet filenames, nav links to sections that exist in
only one version. This has already happened once; it is not a hypothetical.

Otherwise: commit with a descriptive message, push to the current working branch
with `git push -u origin <branch>`, and do not open a pull request unless asked.

## Working alongside other tools

Yasir works across several AI tools. Keep everything here in plain, portable
form — standard HTML, standard CSS, markdown skills — so any tool can read the
repo and continue the work. Avoid anything that only one toolchain understands.
