"""
AI Career Coach
Entry point of the application
"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

from orchestrator.agent_orchestrator import AgentOrchestrator

from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
from services.gemini_servise import GeminiService

def main() -> None:
    conversation_memory = ConversationMemory()
    gemini_service = GeminiService()
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
        planner = PlannerAgent(memory, gemini_service, conversation_memory)
        researcher = ResearchAgent(memory, gemini_service, conversation_memory)
        writer = WriterAgent(memory, gemini_service, conversation_memory)
        reviewer = ReviewerAgent(memory, gemini_service, conversation_memory)

        orchestrator = AgentOrchestrator(memory, conversation_memory)
        orchestrator.register(planner)
        orchestrator.register(researcher)
        orchestrator.register(writer)
        orchestrator.register(reviewer)


        final_response = orchestrator.execute()

        print("="*50)
        print("FINAL CAREER ROADMAP")
        print("="*50)
        print(final_response.output)

        conversation_memory.display()

if __name__ == "__main__":
    main()