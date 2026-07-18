# Import os module to access environment variables
import os

# Load variales from .env file
from dotenv import load_dotenv

# LangChain wrapper for Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

#Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key not found...")


# Create Gemini Model
model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.5,
    google_api_key = GEMINI_API_KEY
)

print("="*60)
print("Welcome to LangChain...")
print("="*60)

question = input("Ask your question: ")
print("\nGenerating Response...\n")

response = model.invoke(question)

print("="*60)
print("AI Response")
print(response.content)
print("="*60)

