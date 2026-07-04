"""
Workflow Router

Uses Gemini to intelligently select
the most appropriate workflow for user's request

Responsibiities:
1. Build the routing prompt
2. Retrieve available workflow form Registry
3. Ask Gemini to classify the request
4. Return Workflow Decision
"""

from services.gemini_servise import GeminiService
from routing.worflow_registry import WorkflowRegistry
from models.workflow_decision import WorkflowDecision

from google.genai import types

class WorkflowRouter:
    """
    LLM-Powered workflow router 
    Gemini analyzes the user's request and select the most appropriate workflow
    """

    def __init__(self, gemini_service: GeminiService, workflow_registry: WorkflowRegistry) -> None:
        """
        Initialize workflow Router
        """

        self.gemini = gemini_service
        self.registry = workflow_registry

    def route(self, user_query: str) -> WorkflowDecision:
        """
        Route the user query.
        Args:
            user_query: User request
        
        Returns:
        WorkflowDecision
        """

        prompt = self.build_prompt(user_query)
        response = self.gemini.generate_response(
            prompt = prompt,
            config = types.GenerateContentConfig(
                response_mime_type = "application/json",
                response_schema= WorkflowDecision
            )
        )

        return response.parsed

    def build_prompt(self, user_query: str) -> str:
        """
        Build the routing prompt
        Args:
            user_query: User request
            
        Returns:
            Prompt string
        """

        workflow_details = []
        for workflow in self.registry.get_available_workflows():
            workflow_details.append(f"- {workflow}")

        available_workflows = "\n".join(workflow_details)
        """
        roadmap-workflow
        certification-workflow
        project-workflow
        review-workflow
        """

        prompt = f"""
        You are an enterprise AI workfllow router.
        Your job is to determine which workflow ahould execute.
        Available workflows:
        {available_workflows}

        Instructions:
        1. Select ONLY ONE workflow
        2. Return your answer using the provided schema
        3. Do NOT explain anything
        
        User Request:
        {user_query}
        """

        return prompt