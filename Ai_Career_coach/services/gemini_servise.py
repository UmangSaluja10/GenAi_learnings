"""
Gemini service
Responsible for communicating with the Gemini API
"""

from google import genai
from config import Config

class GeminiService:
    """
    Wrapper around Google's Gemini API
    """

    def __init__(self):
        Config.validate()
        self.client = genai.Client(api_key = Config.GEMINI_API_KEY)

    def generate_response(self, prompt: str) -> str:
        """
        Send prompt to Gemini and return response
        Args:
            promtp: Complete prompt to send
        Returns: 
            Ai generated response
        """

        try:
            response = self.client.models.generate_content(
                model = Config.MODEL_NAME,
                prompts = prompt)
            return response.text
        except Exception as ex:
            raise RuntimeError(
                f"Gemini API Error: {ex}"
            )