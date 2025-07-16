

def respond_to(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "👋 Hi there!"
    elif user_input in ["how are you", "how are you doing"]:
        return "😊 I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "👋 Goodbye! Have a great day!"
    elif user_input in ["what's your name", "who are you"]:
        return "🤖 I'm your friendly chatbot."
    elif user_input in ["help", "options"]:
        return "💡 You can try saying: hello, how are you, bye."
    else:
        return "❓ Sorry, I didn’t understand that."

def run_chatbot():
    print("🤖 ChatBot is now online! (type 'bye' to quit)\n")
    while True:
        user_message = input("You: ")
        reply = respond_to(user_message)
        print("Bot:", reply)

        if user_message.lower() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    run_chatbot()
