# Receive input -> Create Prompt -> Call Gemini -> Return Response

"""
Base Agent
Every AI Agent inherits from this class
"""

from abc import ABC, abstractmethod
from services.gemini_servise import GeminiService
from memory.shared_memory import SharedMemory

class BaseAgent(ABC):
    """
    Abstrct Base Class for all AI Agents
    """
    def __init__(self,memory: SharedMemory):
        super().__init__()
        self.memory = memory
        self.gemini = GeminiService()

    @abstractmethod
    def execute(self) -> str:
        """
        Execute Agent
        """
        pass

    def ask_gemini(self,prompt: str) -> str:
        """
        Send Prompt to gemini
        """
        return self.gemini.generate_response(prompt)