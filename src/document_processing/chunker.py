class Chunker:

    def __init__(self, chunk_size=1000, overlap=150):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, pages):

        chunks = []

        chunk_id = 1

        for page in pages:

            text = page["text"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]

                chunks.append(
                    {
                        "chunk_id": str(chunk_id),
                        "document_id": page["document_id"],
                        "document_name": page["document_name"],
                        "page_number": page["page_number"],
                        "text": chunk_text,
                    }
                )

                chunk_id += 1

                start += self.chunk_size - self.overlap

        return chunks
