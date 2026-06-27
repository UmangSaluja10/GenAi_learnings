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
class CareerCoachAgent:
    def __init__(self,goal):
        self.goal=goal
        self.observation = []
        self.plan = []
    #Create Plan
    def create_plan(self):
        print(f"[PLANNER] Creating execution plan...")
        prompt = f"""
        You are a Planner Agent.
        user Goal: {self.goal}

        Available Tools:
        SKILL_TOOL
        CERTIFICATE_TOOL
        PROJECT_TOOL
        SALARY_TOOL

        Your task:
        Create the BEST execution plan.

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
    
    #Execut PLan
    def execute_plan(self):
        print(f"[EXECUTOR] Executing plan")
        step =1
        for tool_name in self.plan:
            print("="*50)
            print(f"STEP : {step}")
            print("="*50)
            tool = TOOL_REGISTRY.get(tool_name)
            res = tool(self.goal)
            print("\nOBSERVATION:\n", res)
            self.observation.append(res)
            step+=1
        
    
    def generate_final_plan(self):
        print(f"[AGENT] Generating Final Carrier Plan")
        prompt = f"""
        User Goal: {self.goal}
        Collected Information: {self.observation}
        Generate:
        1. Career Summary
        2. Skills Required
        3. Certifications
        4. Projects 
        5. Salary expectations 
        6. 90-Day learning raodmap


        Generate a professional roadmap
"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        print("="*50)
        print("Final Career Plan")
        print("="*50)

        print(response.text)

    # Run Agent
    def run(self):
        #Create Plan
        self.plan = self.create_plan()
        print("="*50)
        print("EXECUTION PLAN")
        print("="*50)

        for index, tool in enumerate(self.plan, start=1):
            print(f"{index}, {tool}")
        
        #Execute plan
        self.execute_plan()

        #Final Response
        draft = self.generate_final_plan()

        
print("==========PLANNER AGENT==========")
goal = input("Enter your career goal: ")
agent = CareerCoachAgent(goal)
agent.run()
