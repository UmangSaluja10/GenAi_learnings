"""
Writer Agent
Converts research into a professional roadmap
"""

from agents.base_agent import BaseAgent
from prompts.writer_prompt import WRITER_PROMPT

class WriterAgent(BaseAgent):
    def get_agent_name(self):
        return "Writer"
    
    def get_memory_key(self):
        return "writer"
    
    def build_prompt(self):
        research_response = self.memory.get("research")
        return WRITER_PROMPT.format(
            research_output = research_response
        )