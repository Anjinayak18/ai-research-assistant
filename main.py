from fastapi import FastAPI

from config.logging import logger
from config.settings import settings
from routes.analysis_routes import router as analysis_router
from routes.document_routes import router as document_router
from routes.search_routes import router as search_router
from src.database import models
from src.database.base import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Research & Knowledge Assistant",
)


# Register routers
app.include_router(document_router)
app.include_router(search_router)
app.include_router(analysis_router)


@app.on_event("startup")
def startup():
    logger.info("Application Started")


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Research & Knowledge Assistant API is Running",
    }
