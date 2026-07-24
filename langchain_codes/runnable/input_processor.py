from langchain_core.runnables import RunnableLambda

def preprocess_input(data: dict) -> dict:
    """
    Preprocess user input before sending it to the Prompt Template
    """

    question = data["question"].strip()
    task = data["task"]
    language = "Python"
    history = data["history"]

    return {
        "task": task,
        "question": question,
        "language": language,
        "history": history
    }

input_processor = RunnableLambda(preprocess_input)