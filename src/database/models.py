from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from src.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(String, unique=True, nullable=False)

    document_name = Column(String, nullable=False)

    upload_timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    total_pages = Column(
        Integer,
        default=0
    )

    total_chunks = Column(
        Integer,
        default=0
    )

    processing_status = Column(
        String,
        default="PENDING"
    )

    category = Column(
        String,
        default="Unknown"
    )

    file_path = Column(
        String,
        nullable=False
    )