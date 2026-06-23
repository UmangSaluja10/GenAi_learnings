from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
user_history = []
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
    user_history.append(f"User: {user_input}")
    conversation_context = system_prompt+"\n"
    conversation_context+="\n".join(user_history)
    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = conversation_context
        )
        bot_response = response.text
        print(bot_response)
        user_history.append(f"Bot Response: {bot_response}")
    except Exception as ex:
        print("Gemini service temporarily unavailable")
        print(ex)
        continue
        