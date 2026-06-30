"""
Planner Agent
Create the initial career learning plan
"""

from agents.base_agent import BaseAgent
from prompts.planner_prompt import PLANNER_PROMPT

class PlannerAgent(BaseAgent):
    def get_agent_name(self):
        return "Planner"
    
    def get_memory_key(self):
        return "planner"
    
    def build_prompt(self):
        user_query = self.memory.get("user_query")
        return PLANNER_PROMPT.format(user_query = user_query)