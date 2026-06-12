
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    Spacer,
    SimpleDocTemplate,
    Table,
    TableStyle,
)


def generate_pdf(
    report_text,
    landscape,
    output_path,
):
    """
    Generate Research Intelligence PDF Report.
    """

    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(
            directory,
            exist_ok=True,
        )

    doc = SimpleDocTemplate(
        output_path,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    heading1 = styles["Heading1"]
    heading2 = styles["Heading2"]
    heading3 = styles["Heading3"]
    normal = styles["Normal"]

    elements = []

    # ----------------------------------------------------
    # Cover Page
    # ----------------------------------------------------

    elements.append(
        Paragraph(
            "Research Intelligence Report",
            heading1,
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    elements.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y %H:%M')}",
            normal,
        )
    )

    elements.append(
        Spacer(1, 25)
    )

    # ----------------------------------------------------
    # Dashboard Values
    # ----------------------------------------------------

    total_papers = landscape.get(
        "total_papers",
        0,
    )

    avg_citations = round(
        landscape.get(
            "average_citations",
            0,
        ),
        2,
    )

    highest = landscape.get(
        "highest_citations",
        0,
    )

    trend = landscape.get(
        "publication_trend",
        {},
    )

    momentum = "Unknown"

    if len(trend) >= 2:

        years = sorted(
            trend.keys()
        )

        if trend[years[-1]] > trend[years[0]]:
            momentum = "Growing"

        else:
            momentum = "Stable"

    # ----------------------------------------------------
    # Dashboard
    # ----------------------------------------------------

    elements.append(
        Paragraph(
            "Research Intelligence Dashboard",
            heading2,
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    dashboard = [

        [
            "📄 Papers",
            "⭐ Avg Citations",
            "🏆 Highest Citations",
            "🔥 Momentum",
        ],

        [
            str(total_papers),
            str(avg_citations),
            str(highest),
            momentum,
        ],

    ]

    table = Table(
        dashboard,
        colWidths=[
            120,
            120,
            120,
            120,
        ],
    )

    table.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2E8B57"),
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER",
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.grey,
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, 1),
                    colors.whitesmoke,
                ),

                (
                    "FONTNAME",
                    (0, 1),
                    (-1, 1),
                    "Helvetica-Bold",
                ),

                (
                    "FONTSIZE",
                    (0, 1),
                    (-1, 1),
                    14,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 1),
                    (-1, 1),
                    12,
                ),

                (
                    "TOPPADDING",
                    (0, 1),
                    (-1, 1),
                    10,
                ),

            ]

        )

    )

    elements.append(table)

    elements.append(
        Spacer(1, 20)
    )

    # ----------------------------------------------------
    # Publication Trend
    # ----------------------------------------------------

    if trend:

        elements.append(
            Paragraph(
                "Publication Trend",
                heading2,
            )
        )

        elements.append(
            Spacer(1, 10)
        )

        maximum = max(
            trend.values()
        )

        for year in sorted(
            trend.keys()
        ):

            count = trend[year]

            length = max(
                1,
                int(
                    (count / maximum) * 20
                ),
            )

            bar = "█" * length

            elements.append(
                Paragraph(
                    f"{year} &nbsp;&nbsp; {bar} ({count})",
                    normal,
                )
            )

        elements.append(
            Spacer(1, 20)
        )

    # ----------------------------------------------------
    # Top Papers
    # ----------------------------------------------------

    top_papers = landscape.get(
        "top_papers",
        [],
    )

    if top_papers:

        elements.append(
            Paragraph(
                "Top Influential Papers",
                heading2,
            )
        )

        elements.append(
            Spacer(1, 10)
        )

        for idx, paper in enumerate(
            top_papers,
            start=1,
        ):

            title = paper.get(
                "title",
                "Unknown",
            )

            year = paper.get(
                "year",
                "",
            )

            citations = paper.get(
                "citations",
                0,
            )

            impact = round(
                paper.get(
                    "impact_score",
                    0,
                ),
                3,
            )

            elements.append(
                Paragraph(
                    f"<b>{idx}. {title}</b>",
                    normal,
                )
            )

            elements.append(
                Paragraph(
                    f"Year: {year} | Citations: {citations} | Impact Score: {impact}",
                    normal,
                )
            )

            elements.append(
                Spacer(1, 8)
            )

        elements.append(
            Spacer(1, 15)
        )

    # ----------------------------------------------------
    # AI Report
    # ----------------------------------------------------

    elements.append(
        Paragraph(
            "Research Gap Report",
            heading2,
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    for line in report_text.split("\n"):

        line = line.strip()

        if not line:

            elements.append(
                Spacer(1, 6)
            )

            continue

        if line.startswith("# "):

            elements.append(
                Paragraph(
                    line[2:],
                    heading1,
                )
            )

        elif line.startswith("## "):

            elements.append(
                Paragraph(
                    line[3:],
                    heading2,
                )
            )

        elif line.startswith("### "):

            elements.append(
                Paragraph(
                    line[4:],
                    heading3,
                )
            )

        elif line.startswith("- "):

            elements.append(
                Paragraph(
                    f"• {line[2:]}",
                    normal,
                )
            )

        else:

            elements.append(
                Paragraph(
                    line,
                    normal,
                )
            )

        elements.append(
            Spacer(1, 4)
        )

    doc.build(
        elements
    )

