from src.embeddings.embedding_generator import EmbeddingGenerator
from src.vector_store.manager import VectorStoreManager
from src.summarization.summarizer import DocumentSummarizer


class AnalysisService:

    def __init__(self):

        self.embedding_model = EmbeddingGenerator()

        self.vector_store = VectorStoreManager()

        self.summarizer = DocumentSummarizer()

    def summarize(
        self,
        question: str,
        summary_type="executive",
        top_k=10
    ):

        embedding = self.embedding_model.generate_embeddings(
            [question]
        )[0]

        search_results = self.vector_store.search(
            embedding,
            top_k=top_k
        )

        return self.summarizer.summarize(
            search_results=search_results,
            summary_type=summary_type
        )