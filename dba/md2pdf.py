"""Generic Markdown -> PDF renderer (reportlab). Handles front-matter, #/##/###/####
headings, **bold**/*italic*/`code`, bullet & numbered lists, > blockquotes,
--- rules, and GitHub-style | tables. Usage: python3 md2pdf.py FILE.md"""
import re, sys, html
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem, HRFlowable)
from reportlab.lib.enums import TA_LEFT

SRC = sys.argv[1]
OUT = SRC.rsplit(".", 1)[0] + ".pdf"
NAVY = HexColor("#1A4E8A"); ORANGE = HexColor("#B8650A"); GREY = HexColor("#5A6068")
LIGHT = HexColor("#F4F6F9")

ss = getSampleStyleSheet()
def S(name, **k):
    return ParagraphStyle(name, parent=ss["Normal"], fontName=k.get("f","Helvetica"),
        fontSize=k.get("s",10.5), leading=k.get("l",15), textColor=k.get("c",black),
        spaceAfter=k.get("sa",6), spaceBefore=k.get("sb",0), alignment=TA_LEFT)
H1=S("h1",f="Helvetica-Bold",s=19,l=23,c=NAVY,sb=6,sa=8)
H2=S("h2",f="Helvetica-Bold",s=14,l=18,c=NAVY,sb=10,sa=5)
H3=S("h3",f="Helvetica-Bold",s=12,l=16,c=ORANGE,sb=7,sa=4)
BODY=S("body",s=10.5,l=15,sa=6)
CELL=S("cell",s=8.8,l=11.5,sa=0)
CELLH=S("cellh",f="Helvetica-Bold",s=8.8,l=11.5,c=white,sa=0)
QUOTE=S("quote",s=9.8,l=14,c=GREY,sa=6)

def inl(t):
    # drop images/badges entirely
    t=re.sub(r"!\[[^\]]*\]\([^)]*\)","",t)
    # markdown link -> just the link text
    t=re.sub(r"\[([^\]]+)\]\([^)]*\)",r"\1",t)
    # strip stray html div/sub/img tags
    t=re.sub(r"</?(div|sub|sup|img)[^>]*>","",t)
    t=html.escape(t)
    t=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",t)
    t=re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)",r"<i>\1</i>",t)
    t=re.sub(r"`(.+?)`",r'<font face="Courier">\1</font>',t)
    t=re.sub(r"==(.+?)==",r'<font color="#B00020"><b>\1</b></font>',t)
    return t

raw=open(SRC,encoding="utf-8").read().split("\n")
i=0
# skip front matter
if raw and raw[0].strip()=="---":
    i=1
    while i<len(raw) and raw[i].strip()!="---": i+=1
    i+=1

story=[]; n=len(raw)
def tablerow(s): return [c.strip() for c in s.strip().strip("|").split("|")]
while i<n:
    s=raw[i].rstrip()
    st=s.strip()
    if st=="":
        i+=1; continue
    # code fence -> monospace block
    if st.startswith("```"):
        i+=1; buf=[]
        while i<n and not raw[i].strip().startswith("```"):
            buf.append(html.escape(raw[i])); i+=1
        i+=1
        story.append(Paragraph("<br/>".join(buf) or "&nbsp;",
            S("code",f="Courier",s=8.5,l=11,sa=8)))
        continue
    # html-only / image-only line -> skip if nothing left
    if (st.startswith("<") and st.endswith(">")) or re.fullmatch(r"!\[[^\]]*\]\([^)]*\)",st):
        i+=1; continue
    if st=="---":
        story.append(HRFlowable(width="100%",thickness=0.6,color=GREY,spaceBefore=6,spaceAfter=8)); i+=1; continue
    if st.startswith("#### "): story.append(Paragraph(inl(st[5:]),H3)); i+=1; continue
    if st.startswith("### "): story.append(Paragraph(inl(st[4:]),H3)); i+=1; continue
    if st.startswith("## "): story.append(Paragraph(inl(st[3:]),H2)); i+=1; continue
    if st.startswith("# "): story.append(Paragraph(inl(st[2:]),H1)); i+=1; continue
    # table
    if st.startswith("|") and i+1<n and set(raw[i+1].strip())<=set("|-: "):
        head=tablerow(st); rows=[]; i+=2
        while i<n and raw[i].strip().startswith("|"):
            rows.append(tablerow(raw[i])); i+=1
        ncol=len(head)
        data=[[Paragraph(inl(c),CELLH) for c in head]]
        for r in rows:
            r=(r+[""]*ncol)[:ncol]
            data.append([Paragraph(inl(c),CELL) for c in r])
        avail=6.9*inch
        # first col a bit narrower if many cols
        cw=[avail/ncol]*ncol
        t=Table(data,colWidths=cw,repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),NAVY),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[white,LIGHT]),
            ("GRID",(0,0),(-1,-1),0.4,GREY),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
            ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ]))
        story.append(t); story.append(Spacer(1,8)); continue
    # blockquote (collect)
    if st.startswith(">"):
        buf=[]
        while i<n and raw[i].strip().startswith(">"):
            buf.append(raw[i].strip()[1:].strip()); i+=1
        story.append(Paragraph(inl(" ".join(buf)),QUOTE)); continue
    # bullet list
    if re.match(r"^[-*] ",st):
        items=[]
        while i<n and re.match(r"^[-*] ",raw[i].strip()):
            items.append(ListItem(Paragraph(inl(raw[i].strip()[2:]),BODY),leftIndent=12)); i+=1
        story.append(ListFlowable(items,bulletType="bullet",start="•")); continue
    # numbered list
    if re.match(r"^\d+\. ",st):
        items=[]
        while i<n and re.match(r"^\d+\. ",raw[i].strip()):
            items.append(ListItem(Paragraph(inl(re.sub(r'^\d+\. ','',raw[i].strip())),BODY),leftIndent=12)); i+=1
        story.append(ListFlowable(items,bulletType="1")); continue
    story.append(Paragraph(inl(st),BODY)); i+=1

doc=SimpleDocTemplate(OUT,pagesize=LETTER,leftMargin=0.75*inch,rightMargin=0.75*inch,
    topMargin=0.7*inch,bottomMargin=0.7*inch,title=SRC)
doc.build(story)
print("wrote",OUT)
