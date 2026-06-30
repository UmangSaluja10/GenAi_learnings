"""
AI Career Coach
Entry point of the application
"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

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

    print("\nPlanning career roadmap...")
    planner.execute()

    print("\nResearching latest technologies")
    researcher.execute()

    print("\nWriting professional roadmap")
    writer.execute()

    print("\nReviewing final roadmap...")
    reviewer.execute()

    final_response = memory.get("reviewer")

    print("="*50)
    print("FINAL CAREER ROADMAP")
    print("="*50)
    print(final_response.output)


if __name__ == "__main__":
    main()