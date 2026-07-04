"""
Workflow Registry
Maintains all workflows supported by AI Career Coach
[planner, researcher], [planner, writer, reviewer], [writer, reviewer]

Responsibilities:
1. Register all available workflow
2. Retrieve workflow by name
3. Validate workflow existence
4. Display all registered workflows
"""


from typing import Dict, List
class WorkflowRegistry:
    """
    Stores and manage all application workflows.
    """

    def __init__(self) -> None:
        """
        Initialize all the supported workflow
        """
        self._workflow: Dict[str, List] = {
            "roadmap": [
                "planner", "researcher", "writer", "reviewer"
            ],
            "certification": [
                "researcher", "writer"
            ],
            "project": [
                "researcher", "writer"
            ],
            "review": [
                "reviewer"
            ]
        }

    def get_workflow(self, workflow_name: str) -> List[str]:
        """
        Retrieve a workflow
        Args:
            workflow_name: Name of the workflow
        Returns:
            Ordered list of agent names
        """
        workflow_name = workflow_name.lower()
        if not self.workflow_exists(workflow_name):
            raise ValueError(f"Workflow {workflow_name} is not registered")
        
        return self._workflow(workflow_name)
    
    def workflow_exists(self, workflow_name: str) -> bool:
        """
        Check whether a workflow exists
        Args:
            workflow_name: Workflow name
        Returns:
            True if workflow exists
        """

        return workflow_name.lower() in self._workflow
    
    def get_available_workflows(self) -> List[str]:
        """
        Returns all registered workflow names
        Returns:
            List of workflow names
        """
        return list(self._workflow.keys())
    
    def register_workflow(self, workflow_name: str, agents: List[str]) -> None:
        """
        Register a new workflow
        Args:
            workflow_name: Workflow name
            agents: Ordered List of agent names
        """

        workflow_name = workflow_name.lower()
        if self.workflow_exists(workflow_name):
            raise ValueError(f"Workflow {workflow_name} already exists")
        
        self._workflow[workflow_name] = agents


    def display(self) -> None:
        """
        Display all registered workflow
        """

        print("="*50)
        print("WORKFLOW REGISTRY")
        print("="*50)

        for workflow_name, agents in self._workflow.items():
            print("WORKFLOW :", workflow_name.title())

            for index, agent in enumerate(agents, start=1):
                print(f"{index}. {agent.title()} Agent")

        print("="*50)