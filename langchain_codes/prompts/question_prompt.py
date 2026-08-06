"""
System:
Answer programming questions
Explain concepts
Give examples
"""

from langchain_core.prompts import (ChatPromptTemplate, MessagesPlaceholder)

question_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are an experienced software engineer.
            Responsibilities:
            1. Answer programming questions
            2. Explain programming concepts simply
            3. Give practical examples
            4. Mention best practices
                """),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}")
    ]
)