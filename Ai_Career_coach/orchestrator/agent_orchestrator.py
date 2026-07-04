"""
Agent Orchestrator
Responsible for manaigng the executionof AI Agents
"""

from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory

from models.agent_response import AgentResponse
from typing import List, Dict

class AgentOrchestrator:
    """
    Executes AI Agents in sequence"""

    def __init__(self,memory: SharedMemory, conversation_memory):
        """
        Initialize the agent orchestrator with necessary services and memory.
        """
        self.memory = memory
        self.agents: List[BaseAgent] = []
        self.conversation_memory = conversation_memory
        self._agents: Dict[str,BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent to be executed
        Args:
            agent: 
                Agent to register
        """
        # self.agents.append(agent)
        self._agents[
            agent.get_agent_name().lower()
        ] = agent

    # def execute(self):
    #     print("\nStarting Multi-Agent Workflow")
    #     for agent in self.agents:
    #         print(f"\nExecuting {agent.get_agent_name()} Agent...")
    #         response = agent.execute()
    #         print(f"{agent.get_agent_name()} completed successfully...")
    #     print("Workflow Completed...")
    #     return self.memory.get("reviewer")
    
    
    def execute(self, workflow: List[str]) -> AgentResponse:
        """
        Execute the selected workflow
        Args:
            workflow: Ordered list of agent names

        Returns:
            Final AgentResponse
        """
        print("\nStarting Multi-Agent Workflow")
        
        final_response = None
        for step, agent_name in enumerate(workflow, start=1):
            agent = self._agents.get(agent_name.lower())
            if agent is None:
                raise ValueError(f"Agent {agent_name} is not registered")
            
            print(f"\nStep {step}: Executing {agent.get_agent_name()} Agent...")
            final_response = agent.execute()
            print(f"{agent.get_agent_name()} completed successfully...")

        print("Workflow Completed...")
        return final_response
    