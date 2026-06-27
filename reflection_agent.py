#Basic imports
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()
from research_agent import ResearchAgent

#load API key
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI API key not found...")

#create GEMINI Client
client = genai.Client(
    api_key=API_KEY
)

class ReflectionAgent:
    """
    Reflection Agent
    Responsibilities:
    1. Review the first draft
    2. Identify weaknesses
    3. Suggest imporvements
    4. Generate improved reports
    """

    def __init__(self):
        pass
    # Review Draft
    def review_draft(self, draft):
        print("="*50)
        print("Reviewing Draft")
        print("="*50)
        prompt = f"""
        You are a senior AI reviewer.
        Review the following career report.
        Career Report: {draft}

        Evaluate the report on:
        1. Accuracy
        2. Completeness
        3. Calrity
        4. Practicality
        5. Missing Information
        6. Actionable Advice

        Rules:
        - Do not rewrite the report
        - Only provide the feedback
        - Mention strengths
        - Mention weakness
        - Suggest improvements
        """
        response = client.models.generate_content(
           model = "gemini-2.5-flash",
           contents = prompt
        )

        print("="*50)
        print("Reviewer Feedback...")
        print("="*50)
        print(response.text)
        return response.text

    # Imporved Draft
    def improve_draft(self,draft,feedback):
        print("="*50)
        print("Imporving Draft")
        print("="*50)
        prompt = f"""
        You are expert AI Career Consultant.
        Below is the original report:
        -------------------------------------------------------------------------------
        {draft}
        -------------------------------------------------------------------------------
        {feedback}
        -------------------------------------------------------------------------------
        Your task:
        Rewrite the report.
        Requirements:
        - Address every reviewer comment.
        - keep the good parts.
        - Improve weak sections.
        - Add missing Information.
        - Make recommendation more practical.
        - Make roadmap more actionable.
        """
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        print("="*50)
        print("Improved Report...")
        print("="*50)
        print(response.text)
        return response.text

    # Reflect
    def reflect(self,draft):
        "Draft->Review->Improve->final Report"

        feedback = self.review_draft(draft)
        final_report = self.improve_draft(draft,feedback)

        return final_report


print("========== AI Career System ==========")

goal = input("Enter your career goal: ")

research_agent = ResearchAgent(goal)
draft = research_agent.run()

reflection_agent = ReflectionAgent()
final_report = reflection_agent.reflect(draft)

print("="*50)
print("FINAL OUTPUT")
print("="*50)
print(final_report)