# Represent the routing decision made by LLM
"""
Workflow Decision
Represnets the routing decision returned by the workflow router

Responsibilities:
1. Store the selected workflow
2. Store routing confdence
3. Store the reason for selecting the workflow
"""

from dataclasses import dataclass

@dataclass
class WorkflowDecision:
    
    workflow_name: str
    confidence: str
    reason: str

    def display(self) -> None:
        """
        Display the workflow decision
        """
        print("="*50)
        print("WORKFLOW DECISION")
        print("="*50)

        print("Workflow: ", self.workflow_name)
        print("Confidence: ", self.confidence)
        print("Reason: ", self.reason)