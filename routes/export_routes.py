from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from src.database.base import get_db
from src.services.analytics_service import AnalyticsService

from src.export.csv_exporter import CSVExporter
from src.export.excel_exporter import ExcelExporter
from src.export.pdf_exporter import PDFExporter

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

analytics_service = AnalyticsService()


@router.get("/analytics/csv")
def export_csv(
    db: Session = Depends(get_db)
):

    data = analytics_service.get_overview(db)

    exporter = CSVExporter()

    path = exporter.export(
        "analytics.csv",
        data
    )

    return FileResponse(
        path,
        media_type="text/csv",
        filename="analytics.csv"
    )


@router.get("/analytics/excel")
def export_excel(
    db: Session = Depends(get_db)
):

    data = analytics_service.get_overview(db)

    exporter = ExcelExporter()

    path = exporter.export(
        "analytics.xlsx",
        data
    )

    return FileResponse(
        path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="analytics.xlsx"
    )


@router.get("/summary/pdf")
def export_pdf():

    exporter = PDFExporter()

    path = exporter.export(
        "summary.pdf",
        "AI Research & Knowledge Assistant Report",
        """
This report was generated automatically.

Features included:

• PDF Upload
• Semantic Search
• RAG Question Answering
• AI Summarization
• AI Comparison
• ML Document Classification
• Analytics Dashboard
• Export Reports
        """
    )

    return FileResponse(
        path,
        media_type="application/pdf",
        filename="summary.pdf"
    )