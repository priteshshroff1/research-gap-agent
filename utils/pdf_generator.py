import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer
)

def generate_pdf(report_text: str, output_path: str):
    """
    Generate a professional PDF report from Markdown/plain text.
    """
    # Ensure output directory exists
    dirpath = os.path.dirname(output_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    doc = SimpleDocTemplate(
        output_path,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch
    )

    styles = getSampleStyleSheet()

    normal_style = styles["Normal"]
    heading1 = styles["Heading1"]
    heading2 = styles["Heading2"]
    heading3 = styles["Heading3"]

    elements = []

    lines = report_text.split("\n")

    for line in lines:

        line = line.strip()

        if line == "":
            elements.append(Spacer(1, 8))
            continue

        if line.startswith("# "):
            elements.append(
                Paragraph(
                    line[2:],
                    heading1
                )
            )
            elements.append(Spacer(1, 10))

        elif line.startswith("## "):
            elements.append(
                Paragraph(
                    line[3:],
                    heading2
                )
            )
            elements.append(Spacer(1, 8))

        elif line.startswith("### "):
            elements.append(
                Paragraph(
                    line[4:],
                    heading3
                )
            )
            elements.append(Spacer(1, 6))

        elif line.startswith("- "):
            elements.append(
                Paragraph(
                    f"• {line[2:]}",
                    normal_style
                )
            )

        else:
            elements.append(
                Paragraph(
                    line,
                    normal_style
                )
            )

            elements.append(
                Spacer(1, 4)
            )

    doc.build(elements)
