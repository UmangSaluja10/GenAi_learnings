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
from memory.conversation_memory import ConversationMemory
from knowledge.knowledge_base import KnowledgeBase

class BaseAgent(ABC):
    """
    Abstrct Base Class for all AI Agents
    """
    def __init__(self,memory: SharedMemory, gemini_service: GeminiService, conversation_memory : ConversationMemory, knowledge_base: KnowledgeBase) -> None:
        """
        Initialize the base agent with necessary services and memory.
        """
        super().__init__()
        self.memory = memory
        self.gemini = gemini_service
        self.conversation_memory = conversation_memory
        self.knowledge_base = knowledge_base

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
        agent_prompt = self.build_prompt()
        conversation = self.conversation_memory.get_context()
        knowledge_context = self.knowledge_base.retrieve(
            self.conversation_memory.get_context()
        )
        prompt = f"""
        
        Conversation History:
        -------------------------
        {conversation}

        Knowledge Base:
        -------------------------
        {knowledge_context}

        Current Task:
        -------------------------
        {agent_prompt}
        """
        gemini_response = self.gemini.generate_response(prompt)
        
        self.conversation_memory.add_ai_message(gemini_response.text)
        
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