from services.llm_service import get_model
from prompts.coding_prompt import coding_prompt

def main():
    model = get_model()
    while True:
        question = input("Ask coding question: ")

        if question.lower() == "exit":
            print("Thankyou for using AI Coding Assistant")
            break

        print("\nGenerating Response")
        prompt = coding_prompt.invoke({
            "question":question
        })
        response = model.invoke(prompt)
        print(response.content)
        print("\n" + "="*60)

if __name__ == "__main__":
    main()