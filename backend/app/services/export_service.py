import csv
import io
from html import escape
from typing import Any

from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


class ExportService:
    @staticmethod
    def _row_value(row: dict[str, Any], header: str) -> Any:
        normalized_header = header.casefold().replace(" ", "_")
        for key, value in row.items():
            if str(key).casefold().replace(" ", "_") == normalized_header:
                return value
        return ""

    @staticmethod
    def _service_breakdown_rows(recommendation: dict[str, Any]) -> list[dict[str, Any]]:
        rows = recommendation.get("service_level_breakdown") or []
        if rows:
            return rows
        services = recommendation.get("services") or []
        return [{"service": service, "provider": recommendation.get("provider", ""), "monthly_estimate": ""} for service in services]

    @staticmethod
    def _cost_comparison_rows(recommendation: dict[str, Any]) -> list[dict[str, Any]]:
        comparison = recommendation.get("cost_estimate", {}).get("comparison") or {}
        if not isinstance(comparison, dict):
            return []
        return [{"provider": provider, "monthly_estimate": value} for provider, value in comparison.items()]

    @staticmethod
    def _similar_rows(recommendation: dict[str, Any]) -> list[dict[str, Any]]:
        return recommendation.get("similar_services") or []

    @staticmethod
    def _tabular_sections(data: dict[str, Any]) -> list[dict[str, Any]]:
        recommendation = data.get("recommendation", {}) or {}
        sections: list[dict[str, Any]] = []

        quick_summary = [
            {"category": "Provider", "value": recommendation.get("provider", "")},
            {"category": "Fit score", "value": recommendation.get("fit_score", "")},
            {"category": "Architecture", "value": recommendation.get("architecture", "")},
            {"category": "Monthly estimate", "value": (recommendation.get("cost_estimate", {}) or {}).get("monthly_estimate", "")},
        ]
        sections.append({
            "title": "Recommendation summary",
            "headers": ["Category", "Value"],
            "rows": quick_summary,
        })

        service_breakdown = ExportService._service_breakdown_rows(recommendation)
        if service_breakdown:
            sections.append({
                "title": "Service breakdown",
                "headers": ["Service", "Provider", "Monthly estimate"],
                "rows": service_breakdown,
            })

        similar_services = ExportService._similar_rows(recommendation)
        if similar_services:
            sections.append({
                "title": "Similar services",
                "headers": ["Service", "Provider", "Monthly estimate"],
                "rows": similar_services,
            })

        comparison_rows = ExportService._cost_comparison_rows(recommendation)
        if comparison_rows:
            sections.append({
                "title": "Cost comparison",
                "headers": ["Provider", "Monthly estimate"],
                "rows": comparison_rows,
            })

        return sections

    @staticmethod
    def to_csv(data: dict[str, Any]) -> str:
        """Serialize recommendation tables as CSV without narrative sections."""
        buffer = io.StringIO()
        writer = csv.writer(buffer)

        for section in ExportService._tabular_sections(data):
            writer.writerow([])
            writer.writerow([section["title"]])
            writer.writerow(section["headers"])
            for row in section["rows"]:
                writer.writerow([ExportService._row_value(row, header) for header in section["headers"]])

        return buffer.getvalue().lstrip("\n")

    @staticmethod
    def to_excel_bytes(data: dict[str, Any]) -> bytes:
        """Serialize recommendation tables into a multi-sheet Excel workbook."""
        workbook = Workbook()
        sections = ExportService._tabular_sections(data)

        for index, section in enumerate(sections):
            sheet = workbook.active if index == 0 else workbook.create_sheet(title=section["title"][:31])
            sheet.append(section["headers"])
            for row in section["rows"]:
                sheet.append([ExportService._row_value(row, header) for header in section["headers"]])

        buffer = io.BytesIO()
        workbook.save(buffer)
        return buffer.getvalue()

    @staticmethod
    def to_html_report(data: dict[str, Any]) -> str:
        """Build an interactive HTML report with narrative and tabular details."""
        recommendation = data.get("recommendation", {}) or {}
        sections = ExportService._tabular_sections(data)

        summary_cards = "".join(
            f"<div class='card'><span>{escape(str(item['category']))}</span><strong>{escape(str(item['value']))}</strong></div>"
            for item in sections[0]["rows"]
        )

        tables_html = []
        for section in sections:
            headers = section["headers"]
            rows = section["rows"]
            rows_html = "".join(
                "<tr>" + "".join(f"<td>{escape(str(ExportService._row_value(row, header)))}</td>" for header in headers) + "</tr>"
                for row in rows
            )
            headers_html = "".join(f"<th>{escape(str(header))}</th>" for header in headers)
            tables_html.append(
                f"""
                <details open>
                  <summary>{escape(str(section['title']))}</summary>
                  <table>
                    <thead><tr>{headers_html}</tr></thead>
                    <tbody>{rows_html}</tbody>
                  </table>
                </details>
                """
            )

        return f"""
        <html>
          <head>
            <meta charset="utf-8" />
            <title>Cloud Recommendation Report</title>
            <style>
              body {{ font-family: Arial, sans-serif; margin: 32px; color: #15202b; background: #f5f7fb; }}
              h1 {{ margin-bottom: 8px; }}
              .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin: 20px 0; }}
              .card {{ background: white; padding: 14px; border-radius: 10px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
              .card span {{ display: block; font-size: 12px; color: #5d6b82; text-transform: uppercase; }}
              .card strong {{ display: block; margin-top: 8px; font-size: 18px; }}
              table {{ width: 100%; border-collapse: collapse; background: white; margin-bottom: 20px; }}
              th, td {{ border: 1px solid #dfe5ee; padding: 10px; text-align: left; vertical-align: top; }}
              th {{ background: #edf3ff; }}
              details {{ margin: 18px 0; background: white; padding: 12px 16px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }}
              summary {{ cursor: pointer; font-weight: bold; margin-bottom: 10px; }}
              .narrative {{ background: white; border-radius: 10px; padding: 18px; margin-top: 22px; }}
            </style>
          </head>
          <body>
            <h1>Cloud Recommendation Report</h1>
            <p>Prepared for review and print-to-PDF conversion.</p>
            <div class="summary">{summary_cards}</div>

            <div class="narrative">
              <h2>Recommendation summary</h2>
              <p>{escape(str(recommendation.get('summary', '')))}</p>
              <p><strong>Recommended provider:</strong> {escape(str(recommendation.get('provider', '')))}</p>
              <p><strong>Architecture:</strong> {escape(str(recommendation.get('architecture', '')))}</p>
            </div>

            {''.join(tables_html)}
          </body>
        </html>
        """

    @staticmethod
    def to_pdf_bytes(data: dict[str, Any]) -> bytes:
        """Build a paginated, branded PDF report from a recommendation payload."""
        buffer = io.BytesIO()
        recommendation = data.get("recommendation", {}) or {}
        green = colors.HexColor("#86BC25")
        charcoal = colors.HexColor("#171717")
        muted = colors.HexColor("#5C6268")
        pale_green = colors.HexColor("#F1F7E8")
        rule = colors.HexColor("#D9DEE2")

        document = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.65 * inch,
            leftMargin=0.65 * inch,
            topMargin=0.95 * inch,
            bottomMargin=0.7 * inch,
            title="Cloud Solution Recommendation",
            author="Cloud Recommendation Engine",
        )

        base_styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "ReportTitle",
            parent=base_styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=28,
            textColor=charcoal,
            alignment=TA_LEFT,
            spaceAfter=8,
        )
        intro_style = ParagraphStyle(
            "ReportIntro",
            parent=base_styles["BodyText"],
            fontSize=10,
            leading=15,
            textColor=muted,
            spaceAfter=15,
        )
        section_style = ParagraphStyle(
            "ReportSection",
            parent=base_styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=charcoal,
            spaceBefore=13,
            spaceAfter=7,
            keepWithNext=True,
        )
        body_style = ParagraphStyle(
            "ReportBody",
            parent=base_styles["BodyText"],
            fontSize=9.5,
            leading=14,
            textColor=charcoal,
            spaceAfter=7,
        )
        table_header_style = ParagraphStyle(
            "ReportTableHeader",
            parent=body_style,
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=11,
            textColor=colors.white,
            spaceAfter=0,
        )
        table_cell_style = ParagraphStyle(
            "ReportTableCell",
            parent=body_style,
            fontSize=8.5,
            leading=11,
            spaceAfter=0,
        )

        def para(value: Any, style: ParagraphStyle = body_style) -> Paragraph:
            return Paragraph(escape(str(value if value is not None else "")), style)

        def draw_page(canvas, doc):
            canvas.saveState()
            page_width, page_height = letter
            canvas.setFillColor(charcoal)
            canvas.setFont("Helvetica-Bold", 15)
            canvas.drawRightString(page_width - doc.rightMargin - 5, page_height - 0.55 * inch, "Deloitte")
            canvas.setFillColor(green)
            canvas.circle(page_width - doc.rightMargin + 1, page_height - 0.57 * inch, 3, stroke=0, fill=1)
            canvas.setStrokeColor(green)
            canvas.setLineWidth(2)
            canvas.line(doc.leftMargin, page_height - 0.72 * inch, page_width - doc.rightMargin, page_height - 0.72 * inch)
            canvas.setStrokeColor(rule)
            canvas.setLineWidth(0.6)
            canvas.line(doc.leftMargin, 0.52 * inch, page_width - doc.rightMargin, 0.52 * inch)
            canvas.setFillColor(muted)
            canvas.setFont("Helvetica", 8)
            canvas.drawString(doc.leftMargin, 0.34 * inch, "Cloud solution recommendation")
            canvas.drawRightString(page_width - doc.rightMargin, 0.34 * inch, f"{doc.page}")
            canvas.restoreState()

        story = [
            Spacer(1, 0.05 * inch),
            para("Cloud Solution Recommendation", title_style),
            para(
                "Architecture and indicative cloud cost assessment based on the supplied workload requirements.",
                intro_style,
            ),
        ]

        summary = recommendation.get("summary")
        if summary:
            story.extend([
                para("Executive summary", section_style),
                para(summary),
            ])

        architecture = recommendation.get("architecture")
        if architecture:
            story.extend([
                para("Recommended architecture", section_style),
                para(architecture),
            ])

        summary_rows = [
            [para("RECOMMENDED PROVIDER", table_header_style), para("FIT SCORE", table_header_style), para("MONTHLY ESTIMATE", table_header_style)],
            [
                para(recommendation.get("provider", "Not specified"), table_cell_style),
                para(f"{recommendation.get('fit_score', 'N/A')}/100", table_cell_style),
                para((recommendation.get("cost_estimate", {}) or {}).get("monthly_estimate", "Not provided"), table_cell_style),
            ],
        ]
        summary_table = Table(summary_rows, colWidths=[2.45 * inch, 1.55 * inch, 2.8 * inch], hAlign="LEFT")
        summary_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), charcoal),
            ("BACKGROUND", (0, 1), (-1, 1), pale_green),
            ("BOX", (0, 0), (-1, -1), 0.5, rule),
            ("INNERGRID", (0, 0), (-1, -1), 0.4, rule),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        story.extend([Spacer(1, 4), summary_table])

        for section in ExportService._tabular_sections(data)[1:]:
            story.append(para(section["title"], section_style))
            table_data = [[para(header, table_header_style) for header in section["headers"]]]
            table_data.extend([
                [para(ExportService._row_value(row, header), table_cell_style) for header in section["headers"]]
                for row in section["rows"]
            ])
            column_count = len(section["headers"])
            if column_count == 2:
                column_widths = [2.6 * inch, 4.2 * inch]
            else:
                column_widths = [2.6 * inch, 1.6 * inch, 2.6 * inch]
            table = Table(table_data, colWidths=column_widths, repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), charcoal),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F6F6")]),
                ("BOX", (0, 0), (-1, -1), 0.5, rule),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, rule),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]))
            story.append(table)

        tradeoffs = recommendation.get("tradeoffs") or []
        if tradeoffs:
            story.append(para("Key trade-offs", section_style))
            for tradeoff in tradeoffs:
                story.append(para(f"- {tradeoff}"))

        document.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
        return buffer.getvalue()

    @staticmethod
    def export(data: dict[str, Any], fmt: str = "csv") -> tuple[bytes, str]:
        """Return exported bytes and their media type for a requested format."""
        fmt = (fmt or "csv").lower()
        if fmt == "csv":
            return ExportService.to_csv(data).encode("utf-8"), "text/csv; charset=utf-8"
        if fmt == "excel":
            return ExportService.to_excel_bytes(data), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        if fmt == "html":
            return ExportService.to_html_report(data).encode("utf-8"), "text/html; charset=utf-8"
        if fmt == "pdf":
            return ExportService.to_pdf_bytes(data), "application/pdf"
        return ExportService.to_csv(data).encode("utf-8"), "text/csv; charset=utf-8"
