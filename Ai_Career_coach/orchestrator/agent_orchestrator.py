"""
Agent Orchestrator
Responsible for manaigng the executionof AI Agents

Responsibilities:
1. Register AI Agent
2. Execute selected workflow
3. Retry failed agents
4. Track execution details
5. Return the final response
"""

from typing import List
from agents.base_agent import BaseAgent
from memory.shared_memory import SharedMemory

from models.agent_response import AgentResponse
from typing import List, Dict
from models.agent_execution_results import AgentExecutionResult
from concurrent.futures import ThreadPoolExecutor
import time

class AgentOrchestrator:
    """
    Executes AI Agents in sequence
    """

    MAX_RETRIES = 3

    def __init__(self,memory: SharedMemory, conversation_memory):
        """
        Initialize the agent orchestrator with necessary services and memory.
        """
        self.memory = memory
        self.agents: List[BaseAgent] = []
        self.conversation_memory = conversation_memory
        self._agents: Dict[str,BaseAgent] = {}
        self._execution_results:List[AgentExecutionResult] = []
        self._aproval_required_agents = {
            "reviewer"
        }

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

        self._execution_results.clear()
        
        final_response = None
        for step, agent_name in enumerate(workflow, start=1):
            
            # Parallel Execution Stage
            if isinstance(agent_name, list):
                parallel_response = self._execute_parallel(agent_name)
                if parallel_response:
                    #Store the last response only
                    final_response  = parallel_response[-1]
            # Sequential Agent Execution
            else:
                agent = self._agents.get(agent_name.lower())
                if agent is None:
                    raise ValueError(f"Agent {agent_name} is not registered")
                
                print(f"\nStep {step}: Executing {agent.get_agent_name()} Agent...")

                # Human Approval Check
                if agent_name.lower() in self._aproval_required_agents:
                    approved = self._request_human_approval(agent)

                    if not approved:
                        print(f"{agent.get_agent_name()} execution cancelled...")
                        self._execution_results.append(
                        AgentExecutionResult(
                            agent_name = agent.get_agent_name(),
                            status = "SKIPPED",
                            attempts = 0,
                            execution_time = 0.0,
                            error_message="Execution rejected by user"
                        )
                    )
                        print("\nWorkflow stopped by user...")
                        break
                # final_response = agent.execute()
                final_response = self._execute_with_retry(agent)
                print(f"{agent.get_agent_name()} completed successfully...")

        print("Workflow Completed...")
        return final_response
    
    def _execute_with_retry(self,agent: BaseAgent) -> AgentResponse:
        """
        Execute an AI Agent with retry mechanism
        Args:
            AI Agent Instance
        Returns:
            AgentResponse
        """

        start_time =  time.perf_counter()
        last_exception = None

        for attempt in range(1,self.MAX_RETRIES+1):
            try:
                print(f"Attempt: {attempt}")
                response = agent.execute()
                
                execution_time = (time.perf_counter() - start_time)
                self._execution_results.append(
                    AgentExecutionResult(
                        agent_name = agent.get_agent_name(),
                        status = "SUCCESS",
                        attempts = attempt,
                        execution_time= execution_time
                    )
                )

                print("Success")
                return response
            except Exception as ex:
                last_exception = ex
                print(f"Attempt {attempt} Failed...")
                

                if attempt < self.MAX_RETRIES:
                   print("Retrying.....")
        execution_time = (
            time.perf_counter() - start_time
        )
        self._execution_results.append(
                    AgentExecutionResult(
                        agent_name = agent.get_agent_name(),
                        status = "FAILED",
                        attempts = self.MAX_RETRIES,
                        execution_time= execution_time,
                        error_message= str(last_exception)
                    )
                )
        raise RuntimeError(
            f"{agent.get_agent_name()}"
            f"after {self.MAX_RETRIES} attempts"
        ) from last_exception
    

    def _request_human_approval(self, agent: BaseAgent) -> bool:
        """
        Ask the user for approval before executing a critical AI Agent.
        
        Args:
            agent:
                Agent requiring approval
        Returns:
            True if approved 
            False otherwise
        """
        print("="*50)
        print("Human Approval Required")
        print("="*50)
        print(f"{agent.get_agent_name()} Agent requires manual approval")

        while True:
            choice = input("Approve execution ? (Y/N): ").strip().lower()
            if choice == "y":
                return True
            if choice == "n":
                return False
            
            print("Invalid input. Please enter Y or N.")


    def _execute_parallel(self, agent_names: list[str]):
        print("\nExecuting Parallel Agents...\n")
        with ThreadPoolExecutor(
            max_workers = len(agent_names)
        ) as executor:
            futures = []
            for agent_name in agent_names:
                agent = self._agents[agent_name.lower()]
                futures.append(
                    executor.submit(self._execute_with_retry, agent)
                )
            responses = []
            for future in futures:
                responses.append(future.result())

        return responses

    def get_execution_results(self) -> List[AgentExecutionResult]:
        """
        Return execution summary
        """
        return self._execution_results
    
    def display_execution_summary(self) -> None:
        """
        Display execution summary
        """

        print("="*50)
        print("AGENT EXECUTION SUMMARY")
        print("="*50)

        for result in self._execution_results:
            result.display()
            print("-"*50)
        print("="*50)