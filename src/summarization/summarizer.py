import time

from src.rag.context_builder import ContextBuilder
from src.rag.llm import GeminiLLM
from src.summarization.prompts import build_summary_prompt


class DocumentSummarizer:

    def __init__(self):

        self.llm = GeminiLLM()

    def summarize(self, search_results, summary_type="executive"):

        start = time.perf_counter()

        context = ContextBuilder.build(search_results)

        prompt = build_summary_prompt(context=context, summary_type=summary_type)

        summary = self.llm.generate(prompt)

        elapsed = (time.perf_counter() - start) * 1000

        return {
            "success": True,
            "summary": summary,
            "summary_type": summary_type,
            "processing_time_ms": round(elapsed, 2),
        }
