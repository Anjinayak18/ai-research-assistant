"""
Production RAG QA Chain

Workflow:

Question
    ↓
Generate Query Embedding
    ↓
Retrieve Top-K Chunks
    ↓
Build Context
    ↓
Build Prompt
    ↓
Gemini
    ↓
Generate Citations
    ↓
Save Conversation
    ↓
Return Response
"""

import time

from src.embeddings.embedding_generator import EmbeddingGenerator
from src.rag.citation import CitationBuilder
from src.rag.context_builder import ContextBuilder
from src.rag.llm import GeminiLLM
from src.rag.memory import ConversationMemory
from src.rag.prompts import build_rag_prompt
from src.rag.response_formatter import ResponseFormatter
from src.vector_store.manager import VectorStoreManager


class QAChain:

    def __init__(self):

        self.embedding_model = EmbeddingGenerator()

        self.vector_store = VectorStoreManager()

        self.llm = GeminiLLM()

        self.memory = ConversationMemory()

    def ask(self, question: str):

        start_time = time.perf_counter()

        try:

            # Generate embedding
            query_embedding = self.embedding_model.generate_embeddings([question])[0]

            # Retrieve documents
            search_results = self.vector_store.search(query_embedding)

            # Build context
            context = ContextBuilder.build(search_results)

            if not context.strip():

                return ResponseFormatter.error(question, "No relevant documents found.")

            # Build prompt
            prompt = build_rag_prompt(
                context=context, question=question, history=self.memory.get_history()
            )

            # Ask Gemini
            answer = self.llm.generate(prompt)

            # Save conversation
            self.memory.add(question, answer)

            # Build citations
            citations = CitationBuilder.build(search_results)

            elapsed = (time.perf_counter() - start_time) * 1000

            return ResponseFormatter.success(
                question=question,
                answer=answer,
                citations=citations,
                retrieved_context=context,
                processing_time_ms=elapsed,
            )

        except Exception as e:

            elapsed = (time.perf_counter() - start_time) * 1000

            return ResponseFormatter.error(question, str(e))
