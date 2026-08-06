from chains.question_chain import question_chain
from chains.code_generation_chain import code_generation_chain 
from chains.code_explaination_chain import code_explaination_chain

from chains.coding_chain import coding_chain
from memory.conversation_memory import ConversationMemory

chain_map = {
    "1": question_chain,
    "2": code_generation_chain,
    "3": code_explaination_chain
}

def show_menu():
    print("Choose an option: ")
    print("="*60)
    print("1. Ask a coding question")
    print("2. Generate Code Snippet")
    print("3. Explain Code")
    print("4. Exit")

def get_user_query(choice):
    if choice == "1":
        return input("Ask coding question: ")
    elif choice == "2":
        return input("Provide a description for code snippet generation: ")
    elif choice == "3":
        return input("Paste the code you want to be explained: ")
    else:
        return None

def main():

    memory = ConversationMemory()

    # model = get_model()
    # | - Pipe operator
    # Pipe operator - Creating a processing pipeline
    # chain = coding_prompt | model | output_parser

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            print("Thankyou for using AI Coding Assistant")
            break

        if choice not in ["1","2","3"]:
            print("Invalid choice. Please try again.")

        question = get_user_query(choice)
        if not question:
            continue

        print("\nGenerating Response")
        try:
            selected_chain = chain_map.get(choice)
            response = selected_chain.invoke({
                "history": memory.get_history(),
                "question": question
            })
            memory.add_user_message(question)
            memory.add_ai_message(response)


            print(response)
            print("\n" + "="*60)
        except Exception as ex:
            print(ex)
            continue


if __name__ == "__main__":
    main()