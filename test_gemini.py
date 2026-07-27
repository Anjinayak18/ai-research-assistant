from src.rag.llm import GeminiLLM

llm = GeminiLLM()

print(llm.generate("Reply with exactly one word: SUCCESS"))
