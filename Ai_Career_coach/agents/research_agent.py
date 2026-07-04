"""
Research Agent
Performs detailed research on the planner's roadmap
"""

from agents.base_agent import BaseAgent
from prompts.researcher_prompt import RESEARCH_PROMPT

class ResearchAgent(BaseAgent):
    def get_agent_name(self):
        return "Researcher"
    
    def get_memory_key(self):
        return "researcher"
    
    def build_prompt(self):
        planner_response = self.memory.get("planner")
        return RESEARCH_PROMPT.format(
            planner_output = planner_response
        )