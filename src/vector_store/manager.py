import chromadb

from config.settings import settings


class VectorStoreManager:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.VECTOR_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="research_documents"
        )

    def add_documents(
        self,
        chunks,
        embeddings
    ):

        ids = []

        documents = []

        metadatas = []

        for chunk, embedding in zip(chunks, embeddings):

            ids.append(chunk["chunk_id"])

            documents.append(chunk["text"])

            metadatas.append({
                "document_id": chunk["document_id"],
                "document_name": chunk["document_name"],
                "page_number": chunk["page_number"]
            })

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )