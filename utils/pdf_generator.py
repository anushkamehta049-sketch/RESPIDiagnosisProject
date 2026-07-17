from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(patient, age, gender, disease, confidence, symptoms):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{patient}_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>RespiDiagnosis AI</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Patient:</b> {patient}", styles["Normal"]))
    story.append(Paragraph(f"<b>Age:</b> {age}", styles["Normal"]))
    story.append(Paragraph(f"<b>Gender:</b> {gender}", styles["Normal"]))
    story.append(Paragraph(f"<b>Symptoms:</b> {symptoms}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Predicted Disease:</b> {disease}", styles["Heading2"]))

    story.append(Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(
        "This report is generated using the RespiDiagnosis AI system. "
        "Please consult a pulmonologist for clinical confirmation.",
        styles["Normal"]
    ))

    doc.build(story)

    return filename