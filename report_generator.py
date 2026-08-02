from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
    candidate,
    ats_score,
    matched_skills,
    missing_skills,
    suggestions
):

    pdf_file = "AI_Resume_ATS_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("AI Resume Screening Report", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Candidate Information</b>", styles["Heading2"]))

    story.append(Paragraph(f"Email : {candidate['email']}", styles["Normal"]))
    story.append(Paragraph(f"Phone : {candidate['phone']}", styles["Normal"]))
    story.append(Paragraph(f"GitHub : {candidate['github']}", styles["Normal"]))
    story.append(Paragraph(f"LinkedIn : {candidate['linkedin']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>ATS Score :</b> {ats_score:.2f}%", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched_skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Suggestions</b>", styles["Heading2"]))

    for suggestion in suggestions:
        story.append(Paragraph(f"• {suggestion}", styles["Normal"]))

    doc.build(story)

    return pdf_file