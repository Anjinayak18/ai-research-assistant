"""
Response Formatter

Provides a standardized response structure for all RAG APIs.
"""

from datetime import datetime
from typing import Any, Dict, List


class ResponseFormatter:
    """Formats RAG responses into a consistent API schema."""

    @staticmethod
    def success(
        question: str,
        answer: str,
        citations: List[Dict[str, Any]],
        retrieved_context: str,
        processing_time_ms: float
    ) -> Dict[str, Any]:

        return {
            "success": True,
            "timestamp": datetime.utcnow().isoformat(),
            "question": question,
            "answer": answer,
            "citations": citations,
            "retrieved_context": retrieved_context,
            "retrieved_chunks": len(citations),
            "processing_time_ms": round(processing_time_ms, 2)
        }

    @staticmethod
    def error(
        question: str,
        message: str
    ) -> Dict[str, Any]:

        return {
            "success": False,
            "timestamp": datetime.utcnow().isoformat(),
            "question": question,
            "answer": None,
            "citations": [],
            "retrieved_context": "",
            "retrieved_chunks": 0,
            "processing_time_ms": 0,
            "error": message
        }