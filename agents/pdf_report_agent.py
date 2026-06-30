from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFReportAgent:

    def generate(
        self,
        filename,
        results,
        health_score,
        strengths,
        improvement_areas,
        theme_discovery,
        root_cause_analysis,
        benchmark_report,
        priority_ranking,
        guest_persona_report,
        trend_report,
        executive_summary,
        recommendations
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        # ---------------------------------------------------
        # TITLE
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "HotelInsight AI",
                styles["Title"]
            )
        )

        content.append(
            Paragraph(
                "By Shetketu Mitra",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        content.append(
            Paragraph(
                "Executive Report",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                f"Total Reviews: {results['total_reviews']:,}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average Score: {results['average_score']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Health Score: {health_score}/100",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        # ---------------------------------------------------
        # STRENGTHS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "Hotel Strengths",
                styles["Heading2"]
            )
        )

        for item in strengths:

            content.append(
                Paragraph(
                    f"• {item[0]}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # IMPROVEMENT AREAS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "Improvement Areas",
                styles["Heading2"]
            )
        )

        for item in improvement_areas:

            content.append(
                Paragraph(
                    f"• {item[0]}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # AI THEME DISCOVERY
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "AI Theme Discovery",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(theme_discovery),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # ROOT CAUSE ANALYSIS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "AI Root Cause Analysis",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(root_cause_analysis),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # BENCHMARK ANALYSIS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "AI Benchmark Analysis",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(benchmark_report),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # PRIORITY ISSUES
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "Priority Issues",
                styles["Heading2"]
            )
        )

        for i, item in enumerate(priority_ranking, start=1):

            content.append(
                Paragraph(
                    f"{i}. {item[0]} (Net Score: {item[1]:,})",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # GUEST PERSONAS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "AI Guest Personas",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(guest_persona_report),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # TREND ANALYSIS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "AI Trend Analysis",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(trend_report),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # EXECUTIVE SUMMARY
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "Executive Summary",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(executive_summary),
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

        # ---------------------------------------------------
        # RECOMMENDATIONS
        # ---------------------------------------------------

        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading2"]
            )
        )

        if isinstance(recommendations, list):

            for recommendation in recommendations:

                content.append(
                    Paragraph(
                        f"• {recommendation}",
                        styles["Normal"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    str(recommendations),
                    styles["Normal"]
                )
            )

        # ---------------------------------------------------
        # BUILD PDF
        # ---------------------------------------------------

        doc.build(content)

        return filename