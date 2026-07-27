from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    document_name: str


class DocumentCreate(DocumentBase):
    document_id: str
    file_path: str


class DocumentResponse(DocumentBase):
    id: int
    document_id: str
    upload_timestamp: datetime
    total_pages: int
    total_chunks: int
    processing_status: str
    category: str
    file_path: str

    model_config = ConfigDict(from_attributes=True)
