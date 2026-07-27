from src.document_processing.chunker import Chunker
from src.document_processing.pdf_parser import PDFParser
from src.document_processing.text_cleaner import TextCleaner


class ProcessingPipeline:

    def __init__(self):
        self.parser = PDFParser()
        self.cleaner = TextCleaner()
        self.chunker = Chunker()

    def process(self, pdf_path, document_id, document_name):

        pages = self.parser.extract_text(pdf_path, document_id, document_name)

        # Debug
        print("=" * 60)
        print("Pages extracted:", len(pages))

        for page in pages:
            print(f"Page {page['page_number']} -> " f"{len(page['text'])} characters")
            print("Preview:", repr(page["text"][:100]))

        print("=" * 60)

        for page in pages:
            page["text"] = self.cleaner.clean(page["text"])

        chunks = self.chunker.split(pages)

        print("=" * 60)
        print("Chunks created:", len(chunks))
        print("=" * 60)

        return {"pages": len(pages), "chunks": chunks}
