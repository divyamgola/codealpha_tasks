def simple_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thanks for asking!")
        elif 'your name' in user_input:
            print("Chatbot: I'm just a simple chatbot.")
        elif 'help' in user_input:
            print("Chatbot: I can respond to greetings like hello/hi, how are you, etc.")
        else:
            print("Chatbot: I didn't understand that. Try saying hello or asking how I am.")

# Start the chatbot
simple_chatbot()