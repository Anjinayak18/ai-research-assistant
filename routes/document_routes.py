import os
import shutil
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from config.settings import settings
from src.database import crud, schemas
from src.database.base import get_db

from src.document_processing.pipeline import ProcessingPipeline
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.vector_store.manager import VectorStoreManager
from src.ml.predictor import DocumentClassifier


router = APIRouter(
    prefix="/documents",
    tags=["Document Management"]
)

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # -----------------------------
    # Validate File
    # -----------------------------
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # -----------------------------
    # Generate Document ID
    # -----------------------------
    document_id = str(uuid.uuid4())

    filename = f"{document_id}_{file.filename}"

    file_path = os.path.join(
        settings.UPLOAD_DIR,
        filename
    )

    # -----------------------------
    # Save Uploaded File
    # -----------------------------
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # -----------------------------
    # Save Metadata
    # -----------------------------
    document = schemas.DocumentCreate(
        document_id=document_id,
        document_name=file.filename,
        file_path=file_path
    )

    saved_document = crud.create_document(
        db,
        document
    )

    # -----------------------------
    # Process PDF
    # -----------------------------
    pipeline = ProcessingPipeline()

    result = pipeline.process(
        file_path,
        document_id,
        file.filename
    )

    # -----------------------------
    # Generate Text Chunks
    # -----------------------------
    texts = [
        chunk["text"]
        for chunk in result["chunks"]
    ]

    # -----------------------------
    # ML Document Classification
    # -----------------------------
    classifier = DocumentClassifier()

    document_text = " ".join(texts[:10])

    classification = classifier.predict(
        document_text
    )

    saved_document.category = classification["category"]

    # -----------------------------
    # Generate Embeddings
    # -----------------------------
    embedding_model = EmbeddingGenerator()

    embeddings = embedding_model.generate_embeddings(
        texts
    )

    # -----------------------------
    # Store in ChromaDB
    # -----------------------------
    vector_store = VectorStoreManager()

    vector_store.add_documents(
        result["chunks"],
        embeddings
    )

    # -----------------------------
    # Update Database
    # -----------------------------
    saved_document.total_pages = result["pages"]
    saved_document.total_chunks = len(result["chunks"])
    saved_document.processing_status = "PROCESSED"

    db.commit()
    db.refresh(saved_document)

    # -----------------------------
    # Response
    # -----------------------------
    return {
        "message": "Document uploaded successfully.",
        "document": {
            "id": saved_document.id,
            "document_id": saved_document.document_id,
            "document_name": saved_document.document_name,
            "category": saved_document.category,
            "classification_confidence": classification["confidence"],
            "total_pages": saved_document.total_pages,
            "total_chunks": saved_document.total_chunks,
            "processing_status": saved_document.processing_status,
            "upload_timestamp": saved_document.upload_timestamp
        }
    }


@router.get("/")
def list_documents(
    db: Session = Depends(get_db)
):
    documents = crud.get_documents(db)

    return {
        "count": len(documents),
        "documents": documents
    }


@router.delete("/{document_id}")
def delete_document(
    document_id: str,
    db: Session = Depends(get_db)
):
    document = crud.delete_document(
        db,
        document_id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    return {
        "message": "Document deleted successfully."
    }