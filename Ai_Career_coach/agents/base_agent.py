# Receive input -> Create Prompt -> Call Gemini -> Return Response

"""
Base Agent
Every AI Agent inherits from this class
Responsibilities:
1. Build prompt
2. Send prompt to GeminiService
3. Create AgentResponse
4. Store response in SharedMemory
5. Return AgentResponse
"""

from abc import ABC, abstractmethod
from services.gemini_servise import GeminiService
from memory.shared_memory import SharedMemory
from models.agent_response import AgentResponse

class BaseAgent(ABC):
    """
    Abstrct Base Class for all AI Agents
    """
    def __init__(self,memory: SharedMemory, gemini_service: GeminiService):
        super().__init__()
        self.memory = memory
        self.gemini = gemini_service
    

    @abstractmethod
    def get_agent_name(self)-> str:
        """
        Return the display name of the agent
        Example: Planner, research
        """
        pass

    @abstractmethod
    def get_memory_key(self)-> str:
        """
        Return the memory key where the output should be stored
        """
        pass

    @abstractmethod
    def build_prompt(self)-> str:
        """
        Build the prompt using data available in shared memory
        """
        pass

    def execute(self) -> str:
        """
        Execute the complete Ai Agent workflow
        Build Prompt -> call Gemini ->
        Create AgentResponse ->
        Store in SharedMemory -> Return Response
        """
        prompt = self.build_prompt()
        gemini_response = self.gemini.generate_response(prompt)
        agent_response = AgentResponse(
            agent_name = self.get_agent_name(),
            output = gemini_response.text
        )
        self.memory.add(
            self.get_memory_key(),
            agent_response)
        return agent_response
    
    
    def ask_gemini(self,prompt: str) -> str:
        """
        Send Prompt to gemini
        """
        return self.gemini.generate_response(prompt)