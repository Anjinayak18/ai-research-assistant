from sqlalchemy.orm import Session

from src.database import models, schemas


def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(
        document_id=document.document_id,
        document_name=document.document_name,
        file_path=document.file_path,
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document


def get_documents(db: Session):
    return db.query(models.Document).all()


def get_document_by_id(db: Session, document_id: str):
    return (
        db.query(models.Document)
        .filter(models.Document.document_id == document_id)
        .first()
    )


def delete_document(db: Session, document_id: str):
    document = get_document_by_id(db, document_id)

    if document:
        db.delete(document)
        db.commit()

    return document
