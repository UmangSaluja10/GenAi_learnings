"""
System:
Explain every lines.
Mention improvements
Mention design pattern
Mention optimization
"""

from langchain_core.prompts import (ChatPromptTemplate, MessagesPlaceholder)

code_explaination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are an experienced software engineer.
            Explain the given code.
            Responsibilities:
            1. Line by line explaination
            2. Mention about Complexity
            3. Mention improvements
            4. Clear code suggestions
                """),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}")
    ]
)