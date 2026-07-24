from langchain_core.runnables import RunnableLambda

def preprocess_input(data: dict) -> dict:
    """
    Preprocess user input before sending it to the Prompt Template
    """

    question = data["question"].strip()
    task = data["task"]
    language = "Python"

    return {
        "task": task,
        "question": question,
        "language": language
    }

input_processor = RunnableLambda(preprocess_input)