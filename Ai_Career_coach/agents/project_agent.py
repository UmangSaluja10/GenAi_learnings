"""
Project Agent
Generate the real-world AI projects based on the user's career goal

Responsibilities:
1. Suggest beginner projects 
2. Suggest intermediate projects
3. Suggest advanced projects
"""

from agents.base_agent import BaseAgent
from prompts.project_prompt import PROJECT_PROMPT

class ProjectAgent(BaseAgent):
    def get_agent_name(self):
        return "Project"
    
    def get_memory_key(self):
        return "project"
    
    def build_prompt(self):
        user_query = self.memory.get("user_query")
        return PROJECT_PROMPT.format(user_query = user_query)