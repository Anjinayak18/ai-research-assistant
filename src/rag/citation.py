"""
Citation Builder

Creates structured citations from retrieved ChromaDB results.
"""

from typing import Dict, List


class CitationBuilder:
    """Generate citations from search results."""

    @staticmethod
    def build(search_results: Dict) -> List[Dict]:
        """
        Returns a unique list of document/page citations.
        """

        citations = []
        seen = set()

        metadatas = search_results.get("metadatas", [[]])[0]

        for metadata in metadatas:

            document = metadata.get("document_name", "Unknown")
            page = metadata.get("page_number", "N/A")

            key = (document, page)

            if key in seen:
                continue

            seen.add(key)

            citations.append({"document": document, "page": page})

        return citations

    @staticmethod
    def format(citations: List[Dict]) -> str:
        """
        Returns a human-readable citation string.
        """

        if not citations:
            return "No citations available."

        lines = []

        for citation in citations:
            lines.append(f"- {citation['document']} (Page {citation['page']})")

        return "\n".join(lines)
