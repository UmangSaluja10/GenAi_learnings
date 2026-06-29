"""
Gemini service
Responsible for communicating with the Gemini API

Responsibilites:
1. Initialize Gemini client
2. Send prompt to Gemini
3. Return the complete Gemini response
4. Keep API-specific code isolated from Agents
"""

from google import genai
from typing import Any, Optional
from config import Config

class GeminiService:
    """
    Wrapper around Google's Gemini API
    """

    def __init__(self):
        Config.validate()
        self.client = genai.Client(api_key = Config.GEMINI_API_KEY)

    def generate_response(self, prompt: str, config: Optional[Any]) -> Any:
        """
        Send prompt to Gemini and return response
        Args:
            promtp: Complete prompt to send
            conif: Optional GenerateContentConfig
        Returns: 
            Ai generated response
        """

        try:
            response = self.client.models.generate_content(
                model = Config.MODEL_NAME,
                prompts = prompt,
                config = config)
            return response
        
        except Exception as ex:
            raise RuntimeError(
                f"Gemini API Error: {ex}"
            )