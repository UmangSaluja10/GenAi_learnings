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
print("GEMINI Chatbot for Career roadmap - Skills, Certificates & Salary")
print("="*50)

# Function-1 :Skills
def get_skills(role: str):
    """
    Return required skills for a role
    Parameters: role(str) - Career role selected by user
    Return: dict: Required skills
    """
    return{
        "role":role,
        "skills":[
            "Python","Machine Learning", "Data Science", "Deep Learning", "LLMs"
        ]
    }

def get_certificate(role:str):
    """
    Returns Certificattion info
    Parameters: role(str): Career role selected by user
    Returns: dict
    """
    return{
        "role":role,
        "certifications":[
            "AI-102", "AZ-104", "DP-300", "AWS Cloud Practitioner", "Google Gen AI"
        ]
    }

def get_salary(role:str):
    """
    Return expected salary range
    Parameters: role(str): Career role selected by user
    Returns: dict
    """
    return{
        "role":role,
        "salary_range": "15-20LPA"
    }

# Register Functions
tools=[
    get_skills,get_certificate,get_salary
]

query = input("Prompt: ")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = query,
    config = types.GenerateContentConfig(
        tools=tools
    )
)
print(response.text)