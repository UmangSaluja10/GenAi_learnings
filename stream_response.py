#Basic Imports
from google import genai
from dotenv import load_dotenv
import os
import time
load_dotenv()

#load API key
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI API key not found...")

#create GEMINI Client
client = genai.Client(
    api_key=API_KEY
)

#Store chat history
user_history = []

#Context Management
MAX_HISTORY = 20

system_prompt = """
You are a friendly AI assistant.
Rules: 
1. Be helpful
2. Be professional
3. Keep answers clean and concise
4. Remember previous consversation context 
"""

print("="*50)
print("Gemini Chatbot")
print("="*50)

while True:
    user_input = input("Prompt: ")
    if user_input.lower() in ["bye", "quit", "exit"]:
        break
    #Store user message
    user_history.append(f"User: {user_input}")
    
    if len(user_history) > MAX_HISTORY:
        user_history = user_history[-MAX_HISTORY]
    
    conversation_context = system_prompt+"\n"
    conversation_context+="\n".join(user_history)

    start_time = time.time()
    full_response = ""
    
    try:
        #Call GEMINI
        stream = client.models.generate_content_stream(
            model = "gemini-2.5-flash",
            contents = conversation_context
        )
        
        for chunk in stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_response +=chunk.text
        
        end_time = time.time()
        total_time = round(end_time-start_time)
        print(
            f"\nResponse time: {total_time} seconds"
            )
        
        #Store bot response
        user_history.append(f"Bot Response: {full_response}")
    except Exception as ex:
        print("Error: ")
        print(ex)
        continue
        