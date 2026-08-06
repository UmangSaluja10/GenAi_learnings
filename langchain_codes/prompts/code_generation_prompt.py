"""
System:
Generate production-ready code
Explain complexity
Return markdown
"""

from langchain_core.prompts import (ChatPromptTemplate, MessagesPlaceholder)

code_generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are an experienced software engineer.
            Generate clean production-ready code.
            Always provide:
            1. Explanation of the code
            2. Source code
            3. Time complexity
            4. Space complexity
            5. Best practices
                """),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}")
    ]
)