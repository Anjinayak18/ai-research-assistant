"""
Search Routes

Provides:

GET  /search   -> Semantic Search
POST /ask      -> RAG Question Answering
"""

from fastapi import APIRouter, HTTPException, Query

from src.embeddings.embedding_generator import EmbeddingGenerator
from src.vector_store.manager import VectorStoreManager
from src.rag.qa_chain import QAChain

router = APIRouter(
    tags=["Search & RAG"]
)

embedding_model = EmbeddingGenerator()
vector_store = VectorStoreManager()
qa_chain = QAChain()


@router.get("/search")
def semantic_search(
    query: str = Query(..., min_length=1),
    top_k: int = Query(5, ge=1, le=20)
):
    """
    Semantic Search
    """

    try:

        embedding = embedding_model.generate_embeddings(
            [query]
        )[0]

        results = vector_store.search(
            embedding,
            top_k=top_k
        )

        return results

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/ask")
def ask(
    question: str
):
    """
    Retrieval Augmented Generation
    """

    return qa_chain.ask(question)