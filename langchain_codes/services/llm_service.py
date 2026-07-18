import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_model():
    model =  ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0.5,
        google_api_key = GEMINI_API_KEY
    )

    return model