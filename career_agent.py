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
    
    #Think
    def think(self):
        prompt = f"""
        You are an AI carrer coach agent.
        user Goal: {self.goal}

        Available Tools:
        SKILL_TOOL
        CERTIFICATE_TOOL
        PROJECT_TOOL
        SALARY_TOOL

        Previous Observation : {self.observation}
        Think Carefully.
        Decide what information you still need.

        Return Only One of them:
        SKILL_TOOL
        CERTIFICATE_TOOL
        PROJECT_TOOL
        SALARY_TOOL
        FINISH
"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        return response.text.strip()
    
    #Action
    def execute_action(self,action):
        tool = TOOL_REGISTRY.get(action)
        if tool:
            return tool(self.goal)
        return None
    
    def generate_final_plan(self):
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
"""
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        print("="*50)
        print("Final Career Plan")
        print("="*50)

        print(response.text)

        # ReAct Loop
    def run(self):
        step=1
        while True:
            print("="*50)
            print(f"STEP : {step}")
            print("="*50)

            #Thought
            action = self.think()
            print("*****THOUGHT*****")
            print(action)

            #Finish
            if action == "FINISH":
                print("Enough Information Collected...")
                break

            #Action
            print("*****ACTION*****")
            res = self.execute_action(action)

            #Observation
            print("*****OBSERVATION*****")
            print(res)
            self.observation.append(res)
            step+=1
        self.generate_final_plan()

goal = input("Enter your career goal: ")
agent = CareerCoachAgent(goal)
agent.run()
