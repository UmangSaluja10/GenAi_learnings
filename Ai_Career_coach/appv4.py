"""
AI Career Coach
Entry point of the application
"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from orchestrator.agent_orchestrator import AgentOrchestrator

from routing.worflow_registry import WorkflowRegistry
from routing.workflow_router import WorkflowRouter

from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
from knowledge.knowledge_base import KnowledgeBase
from services.gemini_servise import GeminiService

def main() -> None:
    conversation_memory = ConversationMemory()
    gemini_service = GeminiService()
    knowledge_base = KnowledgeBase("data/career_knowledge.json")

    workflow_registry = WorkflowRegistry()
    workflow_router = WorkflowRouter(gemini_service, workflow_registry)

    while True:
        print("="*50)
        print("AI Career Coach")
        print("="*50)

        user_query = input("Enter your career goal : \n")

        if user_query.lower() in ["exit", "bye","quit"]:
            print("Exiting the application....")
            break

        conversation_memory.add_user_message(user_query)

        # Initialize shared components
        memory = SharedMemory()

        # Store user query
        memory.add("user_query",user_query)

        # Create Agents
        planner = PlannerAgent(memory, gemini_service, conversation_memory,knowledge_base)
        researcher = ResearchAgent(memory, gemini_service, conversation_memory,knowledge_base)
        writer = WriterAgent(memory, gemini_service, conversation_memory,knowledge_base)
        reviewer = ReviewerAgent(memory, gemini_service, conversation_memory,knowledge_base)

        orchestrator = AgentOrchestrator(memory, conversation_memory)
        orchestrator.register(planner)
        orchestrator.register(researcher)
        orchestrator.register(writer)
        orchestrator.register(reviewer)

        # Route User's Request
        decision = workflow_router.route(user_query)
        decision.display()

        # Retrieve the workflow
        workflow = workflow_registry.get_workflow(
            decision.workflow_name
        )

        for index, agent in enumerate(workflow,start=1):
            print(f"{index}. {agent.title()} Agent")

        final_response = orchestrator.execute(workflow)

        print("="*50)
        print("FINAL CAREER ROADMAP")
        print("="*50)
        print(final_response.output)

        conversation_memory.display()

if __name__ == "__main__":
    main()