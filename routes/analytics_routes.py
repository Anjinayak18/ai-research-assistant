from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.base import get_db
from src.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

analytics_service = AnalyticsService()


@router.get("/overview")
def analytics_overview(
    db: Session = Depends(get_db)
):
    return analytics_service.get_overview(db)