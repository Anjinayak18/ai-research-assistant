import os

from sqlalchemy.orm import Session

from src.database import models
from src.vector_store.manager import VectorStoreManager


class AnalyticsService:

    def __init__(self):
        self.vector_store = VectorStoreManager()

    def get_overview(
        self,
        db: Session
    ):

        documents = db.query(models.Document).all()

        total_documents = len(documents)

        processed_documents = len(
            [
                d for d in documents
                if d.processing_status == "PROCESSED"
            ]
        )

        failed_documents = len(
            [
                d for d in documents
                if d.processing_status == "FAILED"
            ]
        )

        total_pages = sum(
            d.total_pages or 0
            for d in documents
        )

        total_chunks = sum(
            d.total_chunks or 0
            for d in documents
        )

        try:
            vector_count = self.vector_store.collection.count()
        except Exception:
            vector_count = 0

        upload_size = 0

        if os.path.exists("data/raw_documents"):
            for root, _, files in os.walk("data/raw_documents"):
                for file in files:
                    upload_size += os.path.getsize(
                        os.path.join(root, file)
                    )

        return {
            "total_documents": total_documents,
            "processed_documents": processed_documents,
            "failed_documents": failed_documents,
            "total_pages": total_pages,
            "total_chunks": total_chunks,
            "vector_embeddings": vector_count,
            "uploaded_data_mb": round(
                upload_size / (1024 * 1024),
                2
            )
        }