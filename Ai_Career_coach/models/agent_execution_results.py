"""
Agent Execution Result

Represent the execution deails of AI Agent

Responsibilities:
1. Store execution status
2. Store retry attempts
3. Store execution duration
4. Store any execution error
5. Display execution summary
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class AgentExecutionResult:
    """
    Stores execution details for an Ai Agent
    """

    agent_name: str
    status: str
    attempts: int
    execution_time: float
    error_message: Optional[str] = None

    def display(self) -> None:
        """
        Display execution details
        """

        print(f"Agent               : {self.agent_name}")
        print(f"Status              : {self.status}")
        print(f"Attempts            : {self.attempts}")
        print(f"Execution Time      : {self.execution_time:.2f} sec")
        if self.error_message:
            print(f"Error Message       : {self.error_message}")