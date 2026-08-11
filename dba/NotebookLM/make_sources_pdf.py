#!/usr/bin/env python3
"""Render the NotebookLM source pack to PDF for upload.

NotebookLM accepts Markdown directly, but PDF is the most reliable path and keeps
formatting predictable. Run after any change to sources/, then re-upload — the
notebook does not sync.

Usage: python3 dba/NotebookLM/make_sources_pdf.py
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
MD2PDF = HERE.parent / "md2pdf.py"

srcs = sorted((HERE / "sources").glob("*.md"))
if not srcs:
    sys.exit("no sources found")

for md in srcs:
    subprocess.run([sys.executable, str(MD2PDF), str(md)], check=True)
    print(f"  ok  {md.with_suffix('.pdf').relative_to(HERE.parent.parent)}")

print(f"\n{len(srcs)} source PDF(s) ready. Re-upload to NotebookLM — it does not sync.")
