"""
Research Agent
Performs detailed research on the planner's roadmap
"""

from agents.base_agent import BaseAgent
from prompts.researcher_prompt import RESEARCH_PROMPT

class ResearchAgent(BaseAgent):
    def __init__(self, memory, gemini_service, conversation_memory, knowledge_base):
        super().__init__(memory, gemini_service, conversation_memory, knowledge_base)
        self.counter = 0
    def get_agent_name(self):
        return "Researcher"
    def get_memory_key(self):
        return "researcher"
    
    def build_prompt(self):
        self.counter +=1
        if self.counter < 3:
            raise RuntimeError("Unable to connect Gemini API") #raising a runtime error
        planner_response = self.memory.get("planner")
        return RESEARCH_PROMPT.format(
            planner_output = planner_response
        )