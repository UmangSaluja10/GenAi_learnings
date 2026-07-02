"""
Conversation Memory
Maintains the conversation history between the user and the AI application.

Responsibilities:
1. Store user messages
2. Store AI responses
3. Retrieve complete conversation history
4. Build conversation context for the AI agents
"""

from typing import List

class ConversationMemory:
    """
    Maintains conversation history.
    The stored messages are later included inside prompts so that AI Agents can
    understand the previous conversation context
    """

    def __init__(self):
        """
        Initialize an empty conversation history.
        """
        self.messages: List[str] = []

    def add_user_message(self, message:str) -> None:
        """
        Store a user message
        Args:
            message:
                User input.
        """
        self.messages.append(f"User: {message}")

    def add_ai_message(self, message:str) -> None:
        """
        Store AI response
        Args:
            message:
                AI generatedresponse.
        """
        self.messages.append(f"AI: {message}")

    def get_context(self) -> str:
        """
        Return the complete conversation
        Returns:
            Conversation history as a string
        """

        return "\n".join(self.messages)
    
    def clear(self) -> None:
        """
        Clear the conversation history
        """

        self.messages.clear()

    def display(self, max_length: int =  120) -> None:
        """
        Display the conversation history
        Useful while debugging
        Args:
            max_length:
                Maximum length of the conversation to display
        """

        print("\n"+"="*50)
        print("CONVERSATION MEMORY")
        print("="*50)

        if not self.messages:
            print("No conversation history available.")
        else:
            for message in self.messages:
                preview = message[:max_length]+"..." 
                print(preview)