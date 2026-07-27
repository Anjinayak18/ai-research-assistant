"""
Summarization Prompt Templates
"""


def build_summary_prompt(
    context: str,
    summary_type: str = "executive"
) -> str:

    prompt_map = {

        "executive": """
Generate a concise executive summary.

Focus on:
- Main topic
- Key points
- Overall conclusion
""",

        "detailed": """
Generate a detailed summary.

Include:
- All important concepts
- Technical details
- Explanations
""",

        "bullet": """
Summarize the document as bullet points.

Use concise bullets.
""",

        "key_findings": """
Extract the most important findings from the document.

Return only the important findings.
"""
    }

    instruction = prompt_map.get(
        summary_type,
        prompt_map["executive"]
    )

    return f"""
You are an AI Research Assistant.

{instruction}

Document:

{context}

Summary:
"""