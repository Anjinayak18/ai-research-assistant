import fitz


class PDFParser:

    def extract_text(
        self,
        pdf_path: str,
        document_id: str,
        document_name: str
    ):

        document = fitz.open(pdf_path)

        pages = []

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            text = page.get_text("text")

            pages.append({
                "document_id": document_id,
                "document_name": document_name,
                "page_number": page_number + 1,
                "text": text.strip()
            })

        document.close()

        return pages