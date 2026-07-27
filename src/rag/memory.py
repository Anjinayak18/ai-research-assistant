"""
Conversation Memory

Maintains conversation history for follow-up questions.
"""

from typing import List, Dict


class ConversationMemory:
    """Simple in-memory conversation store."""

    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.history: List[Dict[str, str]] = []

    def add(
        self,
        question: str,
        answer: str
    ) -> None:
        """
        Store a conversation turn.
        """

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        # Keep only the latest conversations
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

    def get_history(self) -> str:
        """
        Return formatted conversation history.
        """

        if not self.history:
            return "No previous conversation."

        conversations = []

        for item in self.history:

            conversations.append(
                f"""User:
{item['question']}

Assistant:
{item['answer']}
"""
            )

        return "\n".join(conversations)

    def clear(self) -> None:
        """
        Clear conversation history.
        """

        self.history.clear()

    def size(self) -> int:
        """
        Number of stored conversations.
        """

        return len(self.history)