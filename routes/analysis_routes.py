from fastapi import APIRouter, Query

from src.services.analysis_service import AnalysisService

router = APIRouter(prefix="/analysis", tags=["AI Analysis"])

analysis_service = AnalysisService()


@router.post("/summarize")
def summarize(question: str = Query(...), summary_type: str = Query("executive")):

    return analysis_service.summarize(question=question, summary_type=summary_type)
