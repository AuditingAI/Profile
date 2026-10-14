"""Adjunct / lecturer application package, 14 Oct 2026 (Scholar lane).

Renders the academic CV and one cover letter per posting to PDF, all under the same Audit Lens
header. Contact details never live in this public repo: they are read from the environment at
build time (CV_EMAIL, CV_PHONE) and default to the {{EMAIL}} / {{PHONE}} placeholders.

    CV_EMAIL=... CV_PHONE=... python3 career/academic/builders/build_adjunct_package.py OUT_DIR

The letters are drafts in Yasir's voice for him to edit; nothing here is sent or submitted.
"""
import os, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "out")
OUT.mkdir(parents=True, exist_ok=True)
EMAIL = os.environ.get("CV_EMAIL", "{{EMAIL}}")
PHONE = os.environ.get("CV_PHONE", "{{PHONE}}")
CHROME = os.environ.get("CHROME", "chromium")

cv = (HERE / "academic_cv.html").read_text()
# Lift the header and its styles from the CV so the letters can never drift from it.
style = re.search(r"<style>(.*?)</style>", cv, re.S).group(1)
sig = re.search(r'(<div class="sig">.*?</div>\s*</div>)', cv, re.S).group(1) + "</div>"  # close .sig
sig = sig.replace('<div class="kicker">Curriculum Vitae</div>', '<div class="kicker">Audit &middot; Risk &middot; Governance</div>')

LETTER_CSS = """
  @page { size: Letter; margin: 0.55in 0.75in 0.6in; }
  body { font-size: 10.3pt; line-height: 1.38; }
  .date { margin: 18px 0 12px; }
  .to { margin-bottom: 14px; }
  .lt p { margin-top: 9px; text-align: left; }
  .close { margin-top: 16px; }
"""

LETTERS = {
    "Stevens_SchoolOfBusiness_Adjunct": dict(
        to="Faculty Search Committee<br>School of Business<br>Stevens Institute of Technology<br>Hoboken, NJ 07030",
        re_="Adjunct Instructor, School of Business (posted as &ldquo;Fall 2026 Adjunct, School of Business&rdquo;)",
        body=[
            "I am applying for the adjunct opening in the Stevens School of Business. I am a doctoral candidate in Business Administration at Florida International University, past the qualifying examination, and I have spent fifteen years inside the control systems of large banks: as a state bank examiner, in capital and controls at JPMorgan Chase, and most recently as Vice President and Audit Manager in Citi Internal Audit. I live in Newark, a short trip from Hoboken, and I am available from the Spring 2027 term.",
            "Stevens teaches business through technology, and that is the ground I work on. At Citi I designed and deployed a retrieval-augmented AI assistant for audit review, and I wrote the governance framework proposal it ran under, against the NIST AI Risk Management Framework and federal model risk guidance. My doctoral research asks what happens to professional judgment when an AI tool agrees with the reviewer, the moment that human review is least likely to catch an error. I would bring both sides of that into a classroom: how to build with AI, and how to govern and audit what gets built.",
            "I am prepared to teach auditing and internal control, enterprise risk management, financial institutions and regulation, accounting information systems, and AI governance and responsible AI in business. I have also written a full course outline, <i>AI Agents for Business Applications</i>, which I would be glad to share.",
            "My teaching record is applied rather than long. At FIU I held graduate appointments delivering financial-literacy instruction in the College of Business&rsquo;s markets lab and tutoring corporate finance and accounting; in 2025 I gave an invited guest lecture to the International MBA on AI and the political economy; and for more than a decade I trained and coached auditors on methodology and judgment. Your posting prefers a Ph.D.; I hold an MBA and a B.Sc. from the London School of Economics, and my DBA is in progress.",
            "My CV is attached, and faculty references at FIU are listed on it. Thank you for your consideration. I would welcome the chance to talk about the courses you need covered.",
        ],
    ),
    "CUNY_CSI_Management_Lecturer": dict(
        to="Search Committee, Lecturer in Management<br>The Lucille and Jay Chazanoff School of Business<br>College of Staten Island, The City University of New York<br>Staten Island, NY 10314",
        re_="Lecturer or Doctoral Lecturer, Management",
        body=[
            "I am applying for the Lecturer position in Management at the College of Staten Island. I am a doctoral candidate in Business Administration at Florida International University, past the qualifying examination, and I apply at the Lecturer rank; I would expect to be considered for Doctoral Lecturer once the degree is conferred.",
            "A lecturer line is a teaching commitment, and I want to make one. I have spent fifteen years managing risk and control inside large organisations: as a state bank examiner, as a programme manager and risk control manager at JPMorgan Chase, where I ran planning across more than fifty stakeholders in five functions, and as Vice President and Audit Manager at Citi, where I led audits across more than fifteen business units and reported to the Board Audit Committee. Those are management problems before they are technical ones, and they make good cases for students who will work inside large organisations.",
            "I am prepared to teach principles of management, risk management and internal control, business ethics and corporate governance, management of information systems and AI in organisations, and international business, the last drawing on my training at the London School of Economics, my work in Dubai, and a conference paper now under review with the Academy of International Business, Latin America and Caribbean Chapter. My research asks how AI tools change professional judgment, which gives students a current and concrete way into decision-making in organisations.",
            "My classroom record is applied: graduate appointments at FIU in markets-lab instruction and in corporate finance and accounting tutoring, an invited International MBA guest lecture in 2025, and more than a decade of training and coaching professional staff. I live in Newark, within easy reach of the campus.",
            "My CV is attached, with FIU faculty references. Thank you for your consideration.",
        ],
    ),
    "Touro_LCW_Management_Adjunct": dict(
        to="Office of the Dean<br>Lander College for Women, Touro University<br>New York, NY",
        re_="Management Adjunct Professor, Lander College for Women",
        body=[
            "I am applying for the Management adjunct position at Lander College for Women. I am a doctoral candidate in Business Administration at Florida International University, past the qualifying examination, with fifteen years of management experience in banking, most recently as Vice President and Audit Manager in Citi Internal Audit. I live in Newark and am available from the Spring 2027 term.",
            "Undergraduates in a management major benefit most from someone who can show them how organisations actually run. I have led audit teams across more than fifteen business units at Citi, managed cross-functional programmes at JPMorgan Chase, examined banks for the State of Florida, and founded and still run a small real-estate business. I can bring that into courses in principles of management, business ethics and corporate governance, risk management, and international business, and into the newer question of how companies should adopt and govern AI, which is the subject of my doctoral research.",
            "My teaching record is applied: graduate appointments at FIU in markets-lab instruction and in corporate finance and accounting tutoring, an invited International MBA guest lecture in 2025, and more than a decade of training and coaching professional staff. I hold an MBA from FIU and a B.Sc. in Banking and Finance from the London School of Economics.",
            "My CV is attached, with FIU faculty references. Thank you for your consideration; I would be glad to discuss the courses you need covered.",
        ],
    ),
}


def page(title, css, inner):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>{inner}</body></html>"""


def fill(html):
    return html.replace("{{EMAIL}}", EMAIL).replace("{{PHONE}}", PHONE)


def pdf(html, name):
    src = OUT / f"{name}.html"
    src.write_text(fill(html))
    dst = OUT / f"{name}.pdf"
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={dst}", src.as_uri()], check=True, capture_output=True)
    src.unlink()
    return dst


print(pdf(cv, "Malik_Yasir_Academic_CV"))
for key, L in LETTERS.items():
    paras = "".join(f"<p>{p}</p>" for p in L["body"])
    inner = (f'{sig}<div class="date">14 October 2026</div><div class="to">{L["to"]}</div>'
             f'<p><b>Re: {L["re_"]}</b></p><div class="lt"><p>Dear Members of the Search Committee,</p>{paras}'
             f'<div class="close">Sincerely,<br><br>Yasir A. Malik</div></div>')
    print(pdf(page("Cover letter", style + LETTER_CSS, inner), f"Malik_Yasir_Cover_Letter_{key}"))
