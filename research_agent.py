#Basic Imports
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time
import random
import datetime
from datetime import datetime
load_dotenv()

#load API key
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI API key not found...")

#create GEMINI Client
client = genai.Client(
    api_key=API_KEY
)

print("="*50)
print("Career Agents - Skills, Certificates & Salary")
print("="*50)

# Function-1 :Skills
def get_skills(goal: str):
    """
    Return required skills for a role
    Parameters: goal(str) - Career goal selected by user
    Return: dict: Required skills
    """
    return"""
    Required skills:
        -Python
        -Machine Learning
        -Data Science
        -Deep Learning
        -LLMs
        -RAG
"""

def get_certificate(goal:str):
    """
    Returns Certificattion info
    Parameters: goal(str): Career goal selected by user
    Returns: dict
    """
    return"""
    Required certifications:
        -AI-102
        -AZ-104
        -DP-300
        -AWS Cloud Practitioner
        -Google Gen AI
"""

def get_salary(goal:str):
    """
    Return expected salary range
    Parameters: goal(str): Career goal selected by user
    Returns: dict
    """
    return"""
    Salary Expectations:
    -Entry level: 8-12 LPA
    -Mid level: 15-25LPA
    -Senior Level: 30+LPA

"""

def project_tool(goal:str):
    """
    Returns Projects info
    Parameter: goal(str): Career goal selected by user
    Return dict
    """
    return """
    Projects recommended:
    - AI Chatbot
    - PDG RAG Assistant
    - Research Agent
    - Career Coach Agent
"""

# Register Functions
TOOL_REGISTRY={
    "SKILL_TOOL": get_skills,
    "CERTIFICATE_TOOL": get_certificate,
    "SALARY_TOOL": get_salary,
    "PROJECT_TOOL": project_tool
}

#Agent
class ResearchAgent:
    def __init__(self,goal):
        self.goal=goal
        self.observation = []
        self.plan = []
        self.evidence = []

    #Create Plan
    def create_research_plan(self):
        print(f"[RESEARCH] Creating research plan...")
        prompt = f"""
        You are a Research Planner .
        user Goal: {self.goal}

        Available Tools:
        SKILL_TOOL
        CERTIFICATE_TOOL
        PROJECT_TOOL
        SALARY_TOOL

        Your task:
        Create the BEST research plan.

        Rules:
        1. Use only required tools
        2. Do not use unneccessary tools
        3. Return one tool per line
        4. Return ONLY tool name

        Example:
        SKILL_TOOL
        CERTIFICATE_TOOL
        PROJECT_TOOL
        SALARY_TOOL
"""
        
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        plan = []  #local plan not that above self.plan(that was global)
        for line in response.text.split("\n"):
            tool = line.strip()
            if tool in TOOL_REGISTRY:
                plan.append(tool)

        return plan
    #Gather evidence
    def gather_evidence(self):
        print(f"Gathering Evidence...")
        step =1
        for tool_name in self.plan:
    
            tool = TOOL_REGISTRY.get(tool_name)
            res = tool(self.goal)
            print("="*50)
            print(tool_name)
            print("="*50)

            print(res)

            self.evidence.append(f"{tool_name}\n{res}")
        
    #Analyze evidence
    def analyze_evidence(self):
        print("ANALYZING EVIDENCE")
        prompt=f"""
        You are an AI Career Analyst
        Goal:
        {self.goal}

        Evidence:
        {self.evidence}

        Generate:
        1. Key findings
        2. Opportunities
        3. Challenges

        Return Analysis

"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        return response.text
    # Final Response
    def generate_recommendation(self, analysis):
        print(f"Generating Recommendation")
        prompt = f"""
        User Goal: {self.goal}
        Analysis: {analysis}
        Generate:
        - Executive summary
        - Recommendations
        - Learning Path
        - Final Verdict

"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        print("="*50)
        print("Final Recommendation")
        print("="*50)

        print(response.text)

    # Run Agent
    def run(self):
        #Create Plan
        self.plan = self.create_research_plan()
        print("="*50)
        print("RESEARCH PLAN")
        print("="*50)

        for index, tool in enumerate(self.plan, start=1):
            print(f"{index}, {tool}")
        
        #Execute plan
        analysis = self.gather_evidence()
        print("ANALYSIS: ")
        print(analysis)
        #Final Response
        self.generate_recommendation(analysis)

        
print("==========RESEARCH AGENT==========")
goal = input("Enter your career goal: ")
agent = ResearchAgent(goal)
agent.run()
