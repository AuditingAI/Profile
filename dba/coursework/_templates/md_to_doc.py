#!/usr/bin/env python3
"""Turn one of the academic markdown documents into a Word file.

A narrow markdown reader, not a general one. It handles what these documents
actually use: headings, paragraphs, bullet lists, pipe tables, horizontal rules
and **bold**. Anything it does not recognise passes through as body text rather
than being dropped, because silently losing a line from a CV is worse than
rendering it plainly.

Sections whose heading begins "Notes for Yasir" are working notes rather than
part of the document, so they are cut along with everything under them.

    python3 md_to_doc.py INPUT.md OUTPUT.docx "Title" "Subtitle" ["ident", ...] [--linebreaks] [--centered] [--logo PNG] [--email X] [--phone X] [--pdf]
"""
import json, re, subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

def convert(path, linebreaks=False):
    raw = open(path, encoding="utf-8").read().split("\n")
    # Each of these documents opens with a title, a byline and a working note,
    # then a horizontal rule. The Word file takes its masthead from the spec,
    # so everything above that rule would print twice.
    lines = raw
    if raw and raw[0].startswith("# "):
        for k, l in enumerate(raw[:14]):
            if re.fullmatch(r"\s*([-*_])\1{2,}\s*", l):
                lines = raw[k + 1:]
                break
    body, table, para, i, skip = [], [], [], 0, False

    def flush_table():
        if not table:
            return
        rows = []
        for r in table:
            if re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", r):   # the |---|---| divider
                continue
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            rows.append(cells)
        if rows:
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            key = "t%d" % len(TABLES)
            TABLES[key] = rows
            body.append({"__table__": key})
        table.clear()

    def flush_para():
        # a markdown paragraph runs until a blank line, so emphasis that spans
        # two source lines only closes once the whole paragraph is joined
        if para:
            body.append([" ".join(para)])
            para.clear()

    def add_line(text):
        """In line-break mode every source line is its own paragraph.

        A CV uses the line break to separate the degree from the institution
        from the date, so joining those into a paragraph destroys the entry.
        Prose does the opposite and needs the join. The one case both share is
        emphasis opened on one line and closed on the next, so a line is held
        back only while its asterisks are unbalanced.
        """
        para.append(text)
        if not linebreaks:
            return
        if ("".join(para).count("*") % 2 == 0) or len(para) >= 4:
            flush_para()

    TABLES = {}
    while i < len(lines):
        ln = lines[i].rstrip()
        i += 1
        h = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if h:
            flush_para()
            flush_table()
            text = _plain(h.group(2))
            # working notes are not part of the document
            if text.lower().startswith("notes for yasir"):
                skip = True
                continue
            skip = False
            lvl = len(h.group(1))
            if lvl == 1:
                body.append({"h1": text})
            elif lvl == 2:
                body.append({"h2": text})
            else:
                body.append({"h3": text})
            continue
        if skip:
            continue
        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            flush_para()
            table.append(ln)
            continue
        flush_table()
        if not ln.strip():
            flush_para()
            continue
        if re.fullmatch(r"\s*([-*_])\1{2,}\s*", ln):      # horizontal rule
            flush_para()
            continue
        b = re.match(r"^\s*[-*+]\s+(.*)$", ln)
        if b:
            flush_para()
            body.append({"bullet": b.group(1).strip()})
            continue
        n = re.match(r"^\s*\d+\.\s+(.*)$", ln)
        if n:
            flush_para()
            body.append({"bullet": n.group(1).strip()})
            continue
        add_line(ln.strip())
    flush_para()
    flush_table()
    return body, TABLES

def _plain(s):
    """Headings carry no runs, so emphasis and links are reduced to their text."""
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    return s.replace("**", "").replace("*", "").replace("`", "").strip()

def main():
    valued = {"--email", "--phone", "--logo"}
    args, skip = [], False
    for a in sys.argv[1:]:
        if skip: skip = False; continue
        if a in valued: skip = True; continue
        if a.startswith("--"): continue
        args.append(a)
    src, out, title, subtitle = args[0], args[1], args[2], args[3]
    ident = args[4:]
    body, tables = convert(src, linebreaks=("--linebreaks" in sys.argv))
    # links and code ticks do not survive into Word; keep the text, drop the markup
    def clean(x):
        if isinstance(x, str):
            x = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", x)
            return x.replace("`", "")
        if isinstance(x, list):
            return [clean(v) for v in x]
        if isinstance(x, dict):
            return {k: clean(v) for k, v in x.items()}
        return x
    # contact details are filled here, at build time, from flags. They never
    # live in the repository (CLAUDE.md), so the markdown keeps {{EMAIL}} and
    # {{PHONE}} and only the delivered file carries the real values.
    fills = {}
    for flag, key in (("--email", "{{EMAIL}}"), ("--phone", "{{PHONE}}")):
        if flag in sys.argv:
            fills[key] = sys.argv[sys.argv.index(flag) + 1]
    def fill(x):
        if isinstance(x, str):
            for k, v in fills.items(): x = x.replace(k, v)
            return x
        if isinstance(x, list): return [fill(v) for v in x]
        if isinstance(x, dict): return {k: fill(v) for k, v in x.items()}
        return x
    logo = sys.argv[sys.argv.index("--logo") + 1] if "--logo" in sys.argv else None
    masthead = "centered" if "--centered" in sys.argv else "side"
    spec = {"title": title, "subtitle": subtitle, "ident": fill(ident),
            "double_spaced": False, "logo": logo, "masthead": masthead,
            "logo_alt": "The Reference Mark, Yasir A. Malik's personal mark",
            "tables": fill(clean(tables)), "body": fill(clean(body))}
    tmp = out + ".json"
    json.dump(spec, open(tmp, "w"))
    subprocess.check_call([sys.executable, os.path.join(HERE, "build_dba_doc.py"), tmp, out])
    os.remove(tmp)
    if "--pdf" in sys.argv:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir",
                        os.path.dirname(os.path.abspath(out)), out],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)

if __name__ == "__main__":
    main()
