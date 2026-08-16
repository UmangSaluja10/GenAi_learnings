from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START,END,StateGraph
from typing_extensions import TypedDict

load_dotenv()

# State 
class GraphState(TypedDict):
    user_query: str
    response: str

# LLM
llm = ChatGoogleGenerativeAI(
    model = "gemini-flash-latest"
)

# Node
def chatBot(state: GraphState):
    result = llm.invoke(state['user_query'])
    return {
        "response" : result.content
    }

# Build Graph
builder = StateGraph(GraphState)
builder.add_node("chatbot", chatBot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)
graph = builder.compile()

#Execute
result = graph.invoke(
    {
        "user_query": "Explain LangGraph in one sentence"
    }
)

print(result["response"])