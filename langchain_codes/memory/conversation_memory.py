from langchain_core. messages import(HumanMessage, AIMessage)

class ConversationMemory:
    def __init__(self):
        self.message = []

    def add_user_message(self, question):
        self.message.append(
            HumanMessage(content = question)
        )

    def add_ai_message(self,answer):
        self.message.append(
            AIMessage(content=answer)
        )

    def get_message(self):
        return self.message

    def clear(self):
        self.message.clear()