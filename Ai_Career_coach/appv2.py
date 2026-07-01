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
from services.gemini_servise import GeminiService

def main() -> None:
    print("="*50)
    print("AI Career Coach")
    print("="*50)

    user_query = input("Enter your career goal : \n")

    # Initialize shared components
    memory = SharedMemory()
    gemini_service = GeminiService()

    # Store user query
    memory.add("user_query",user_query)

    # Create Agents
    planner = PlannerAgent(memory, gemini_service)
    researcher = ResearchAgent(memory, gemini_service)
    writer = WriterAgent(memory, gemini_service)
    reviewer = ReviewerAgent(memory, gemini_service)
    
    orchestrator = AgentOrchestrator(memory)
    orchestrator.register(planner)
    orchestrator.register(researcher)
    orchestrator.register(writer)
    orchestrator.register(reviewer)

    final_response = orchestrator.execute()

    print("="*50)
    print("FINAL CAREER ROADMAP")
    print("="*50)
    print(final_response.output)


if __name__ == "__main__":
    main()