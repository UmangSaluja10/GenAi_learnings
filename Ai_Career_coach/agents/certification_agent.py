"""
Certification Agent
Suggest the industry certification for career goal
"""

from agents.base_agent import BaseAgent
from prompts.certification_prompt import CERTIFICATION_PROMPT

class CertificationAgent(BaseAgent):
    def get_agent_name(self):
        return "Certification"
    
    def get_memory_key(self):
        return "certification"
    
    def build_prompt(self):
        user_query = self.memory.get("user_query")
        return CERTIFICATION_PROMPT.format(user_query = user_query)