# CLAUDE.md

This file provides context for AI assistants working on this repository.

## Project Overview

**Yasir A. Malik — Personal Website**
A static portfolio site for an audit leader, DBA researcher, and AI governance strategist. Hosted on GitHub Pages with zero build dependencies.

## File Structure

```
├── index.html      # Landing / About page
├── research.html   # Research areas, dissertation, technical toolkit
├── books.html      # 15 book recommendations across 5 categories
├── style.css       # Complete stylesheet (Instrument Serif + DM Sans)
├── img/            # Image assets folder (not yet created; referenced for collage.png)
├── README.md       # Project overview and setup instructions
└── CLAUDE.md       # This file
```

**Total size**: ~1,600 lines across 5 source files. There is no JavaScript (except a JSON-LD structured data block in index.html).

## Tech Stack

- **HTML5** — semantic markup, inline SVG icons
- **CSS3** — custom properties, flexbox, grid, animations
- **Google Fonts** — Instrument Serif (display) + DM Sans (body), loaded via CSS `@import`
- **No runtime JavaScript** — only a JSON-LD `<script type="application/ld+json">` block for structured data (SEO)
- **No build tools, no package manager, no frameworks**

## Design System

### CSS Variables (`:root` in `style.css`)

| Variable | Value | Usage |
|---|---|---|
| `--color-ink` | `#1a1a1a` | Primary text |
| `--color-ink-light` | `#4a4a4a` | Body paragraphs |
| `--color-ink-muted` | `#7a7a7a` | Secondary text, labels |
| `--color-paper` | `#faf9f6` | Page background |
| `--color-paper-warm` | `#f3f1ec` | Card/highlight backgrounds |
| `--color-accent` | `#2c5f8a` | Links, headings, interactive elements |
| `--color-accent-hover` | `#1d4a6e` | Hover states |
| `--color-rule` | `#d4d0c8` | Borders, dividers |
| `--font-display` | Instrument Serif | Headings (h1, h2, h3) |
| `--font-body` | DM Sans | Body text, navigation |
| `--max-width` | `720px` | Content column width |
| `--transition` | `0.25s ease` | All interactive transitions |

### Responsive Breakpoint

Single breakpoint at **640px** (`@media (max-width: 640px)`). Below that threshold: smaller font sizes, single-column highlights grid, stacked category nav pills.

## Conventions

### HTML

- **Indentation**: 4 spaces
- **Structure**: Every page shares the same header → divider → nav → content → footer skeleton
- **Active nav**: The current page's `<a>` in `<nav>` gets `class="active"`
- **Social links**: Inline SVGs (no icon library dependency). Four links: Google Scholar, GitHub, LinkedIn, Goodreads
- **Placeholder values**: `YOUR_ID`, `YOUR_USERNAME`, `YOUR_PROFILE` — must be replaced per deployment

### CSS

- Organized in labeled sections: `/* ---- HEADER ---- */`, `/* ---- NAVIGATION ---- */`, etc.
- BEM-influenced class naming (e.g., `.book-entry`, `.book-title`, `.book-author`)
- All colors and fonts referenced through CSS variables
- Shadow system: `--shadow-sm`, `--shadow-md`, `--shadow-lg` for consistent elevation
- Shared `--radius: 10px` for border-radius consistency
- Entry animation via `@keyframes fadeIn` with staggered delays (`0.1s`, `0.15s`, `0.2s`, etc.)
- `::selection` styled with accent color tint
- `:focus-visible` outline for keyboard accessibility
- Print stylesheet hides nav/header, expands URLs inline, prevents page-break inside cards

### Book Entries (books.html)

Each book follows this exact structure:
```html
<div class="book-entry">
    <h3 class="book-title">Title</h3>
    <p class="book-author">
        by Author Name
        <a href="...">[Goodreads]</a>
        <a href="...">[YouTube]</a>
    </p>
    <p class="question">Key question the book answers?</p>
    <p>Summary paragraph with <strong>key phrases</strong> bolded.</p>
    <ul>
        <li>Bullet points with <strong>key terms</strong> highlighted</li>
    </ul>
    <p class="further-reading">Further Reading</p>
    <ul class="further-reading-list">
        <li><em>Related Book Title</em> by Author</li>
    </ul>
</div>
```

Books are grouped into 5 categories (`<section class="book-category">`), each with an `id` for anchor navigation: `audit-risk`, `leadership`, `ai-governance`, `finance`, `biography`.

### Research Cards (research.html)

Each research area uses this card structure:
```html
<div class="research-card">
    <span class="research-label research-label--dissertation">Dissertation</span>
    <h3>Card Title</h3>
    <p class="research-meta">Institution · Context</p>
    <p>Description with <strong>key phrases</strong> bolded.</p>
    <ul>
        <li>Bullet points</li>
    </ul>
</div>
```

Label modifiers: `--dissertation` (blue accent), `--interest` (muted gray).

### Skills Grid (research.html)

Uses a 2-column CSS Grid (`.skills-grid`) with `.skill-group` cards. Each group has an `<h3>` heading and a `<ul>` of skills with `·` bullet pseudo-elements.

## Adding New Pages

1. Copy the header/nav/footer skeleton from `index.html`
2. Set `class="active"` on the new page's nav link
3. Update `<nav>` links in **all** existing pages to include the new page
4. Add page-specific content between nav and footer
5. Add styles to `style.css` under a new labeled section

## Deployment

This is a GitHub Pages site. No build step is needed.

1. Push files to a repository named `USERNAME.github.io`
2. GitHub Pages serves the root directory automatically
3. All assets are relative paths (no absolute URLs except Google Fonts and external links)

## Common Pitfalls

- **No `img/` directory exists yet** — it's referenced in README but must be created before adding images
- **Placeholder links** — social links still contain `YOUR_ID` / `YOUR_USERNAME` / `YOUR_PROFILE`; do not modify these unless explicitly asked
- **No build/test/lint commands** — there is nothing to run; changes are verified by opening HTML files in a browser
- **Footer year** — currently hardcoded as `2025` in both HTML files
