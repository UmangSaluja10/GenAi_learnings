#Basic Imports

from google import genai
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
print("GEMINI Chatbot")
print("="*50)

def get_current_time():
    return datetime.now().strftime("%I:%M:%S, %p")

def calculator(expression):
    try:
        return eval(expression)
    except Exception as ex:
        return "Invalid expression"

def motivational_quotes():
    quotes = [
        "Consistency is the key to success",
        "Hard work beats talent when talent doesn't work hard",
        "Action speaks more than words",
        "Dream big, Start small, Act now..."
        ]
    return random.choice(quotes)

def generate_roadmap(topic):
    return f"""
    Roadmap for {topic}:
    1. Learn fundamentals
    2. Practice Projects
    3. Build Portfolio
    4. Apply for Jobs
    """

Tools = {
    "TIME_TOOL": get_current_time,
    "CALCULATOR_TOOL": calculator,
    "QUOTE_TOOL": motivational_quotes,
    "ROADMAP_TOOL": generate_roadmap
}

def select_tool(query):
    prompt = f"""
        You are a tool selector.
        Available Tools:
        TIME_TOOL
        CALCULATOR_TOOL
        QUOTE_TOOL
        ROADMAP_TOOL

        Return only tool name
        User Query: {query}
    """
    response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
    print(f"Assistant: {response.text}")
