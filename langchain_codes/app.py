from services.llm_service import get_model
from prompts.coding_prompt import coding_prompt
from parser.output_parser import output_parser

def main():
    model = get_model()
    # | - Pipe operator
    # Pipe operator - Creating a processing pipeline
    chain = coding_prompt | model | output_parser

    while True:
        question = input("Ask coding question: ")

        if question.lower() == "exit":
            print("Thankyou for using AI Coding Assistant")
            break

        print("\nGenerating Response")
        # prompt = coding_prompt.invoke({
        #     "question":question
        # })
        # reponse = model.invoke(prompt)
        response = chain.invoke({
            "question":question
        })
        print(response)
        print("\n" + "="*60)

if __name__ == "__main__":
    main()