"""
Context Builder

Builds a structured context string from ChromaDB search results.
This context is passed to the LLM.
"""

from typing import Dict, List


class ContextBuilder:
    """Build prompt-ready context from retrieved search results."""

    @staticmethod
    def build(search_results: Dict) -> str:
        """
        Converts ChromaDB search results into a formatted context block.
        """

        context_blocks: List[str] = []

        documents = search_results.get("documents", [[]])[0]
        metadatas = search_results.get("metadatas", [[]])[0]
        distances = search_results.get("distances", [[]])[0]

        for index, (document, metadata) in enumerate(
            zip(documents, metadatas)
        ):

            similarity = None

            if index < len(distances):
                similarity = round(1 - distances[index], 4)

            block = f"""
==============================
Source Document : {metadata.get("document_name", "Unknown")}
Page            : {metadata.get("page_number", "N/A")}
Similarity      : {similarity if similarity is not None else "N/A"}

Content:
{document}
==============================
"""

            context_blocks.append(block)

        return "\n".join(context_blocks)