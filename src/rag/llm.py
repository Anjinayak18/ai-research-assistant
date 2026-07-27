"""
Gemini LLM wrapper.

This module is responsible for:
- Connecting to Gemini
- Sending prompts
- Returning generated text
"""

import logging

from google import genai

from config.settings import settings


logger = logging.getLogger(__name__)


class GeminiLLM:
    """Wrapper around Google's Gemini API."""

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

        self.model = "gemini-2.5-flash"

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_output_tokens: int = 2048
    ) -> str:
        """
        Generate an answer from Gemini.

        Returns:
            str: Generated response.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={
                    "temperature": temperature,
                    "max_output_tokens": max_output_tokens,
                }
            )

            return response.text.strip()

        except Exception as e:

            logger.exception(
                "Gemini generation failed."
            )

            raise RuntimeError(
                f"LLM Error: {str(e)}"
            )