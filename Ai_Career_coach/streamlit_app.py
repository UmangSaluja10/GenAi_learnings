"""
AI Career coach studio
"""

# pip install streamlit
import streamlit as st
from backend_logic import main


# Page configuration
st.set_page_config(
    page_title = "AI Career Coach Studio",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state="expanded"
)


# Session State
if "history" not in st.session_state:
    st.session_state.history = []


with st.sidebar:
    st.title("🤖 AI Career Coach")
    st.success("🟢 Ready")  
    st.divider()

    # Conversation History
    st.subheader("📃 Conversation History")

    if len(st.session_state.history) == 0:
        st.info("No conversation yet...")

    else:
        for query in reversed(st.session_state.history):
            st.button(query, use_container_width=True)

    st.divider()

    # System Information
    st.subheader("⚙ System Information")
    st.write("Backend: Connected")
    st.write("Workflow: Idle")
    st.write("Memory: Not initialized...")


# Main Page
st.title("🚀 AI Career Coach Studio")  
st.caption("Enterprise Multi-Agent AI Application")

st.divider()

# User Input
st.subheader("✨ Career Goal")
user_query = st.text_area(
    "",
    height = 150,
    placeholder = "Example: I want to become an AI Engineer"
)

generate = st.button(
    "Generate Career Roadmap",
    use_container_width = True
)

if generate:
    if user_query.strip() == "":
        st.warning("Please Enter your career goal")
    else:
        st.session_state.history.append(user_query)
        with st.spinner(
            "Executing Multi-Agent Workflow"
        ):
            final_response = main(user_query)
            st.success("🟢 Workflow executed sucessfully...")
            st.markdown(final_response)