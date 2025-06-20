def chatbot():
    print(" ChatBot: Hello! I’m a simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("ChatBot: Hi!")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks!")
        elif user_input == "what's your name":
            print("ChatBot: I'm ChatBot, your friendly assistant.")
        elif user_input == "bye":
            print("ChatBot: Goodbye! 👋")
            break
        else:
            print("ChatBot: I didn’t understand that.")

# Run the chatbot
chatbot()
