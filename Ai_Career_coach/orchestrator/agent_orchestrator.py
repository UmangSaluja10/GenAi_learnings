"""
Agent Orchestrator
Responsible for manaigng the executionof AI Agents
"""

from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory


class AgentOrchestrator:
    """
    Executes AI Agents in sequence"""

    def __init__(self,memory: SharedMemory):
        self.memory = memory
        self.agents: List[BaseAgent] = []

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent to be executed
        Args:
            agent: 
                Agent to register
        """
        self.agents.append(agent)

    def execute(self):
        print("\nStarting Multi-Agent Workflow")
        for agent in self.agents:
            print(f"\nExecuting {agent.get_agent_name()} Agent...")
            response = agent.execute()
            print(f"{agent.get_agent_name()} completed successfully...")
        print("Workflow Completed...")
        return self.memory.get("reviewer")