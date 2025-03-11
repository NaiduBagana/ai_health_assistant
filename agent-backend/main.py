from assistant import AIAssistant

def main():
    assistant = AIAssistant()
    print("Health Assistant: How can I help you today? (type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = assistant.process_query(user_input, "user123")
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()