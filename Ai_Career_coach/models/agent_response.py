"""
Agent Response Model
Represent the standardized response returned by every AI Agent.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class AgentResponse:
    """
    Standard response returned by every AI Agent
    """
    # Name of the agent
    agent_name: str

    # AI Generated output
    output: str

    # Execution status of Agent
    status: str = "SUCCESS"

    #Error Message(if any)
    error: Optional[str] = None

    #Rsponse Genration Time
    timestamp: datetime = field(
        default_factory=datetime.now
    )

    def is_success(self) -> bool:
        """
        Return True if execution ws successful.
        """
        return self.status.upper() == "SUCCESS"
    
    def __str__(self):
        """
        Pretty string representation
        """
        return (
            f"\nAgent : {self.agent_name}"
            f"\nStatus : {self.status}"
            f"\nTimeStamp : {self.timestamp}"
            f"\nOutput : {self.output}"
        )