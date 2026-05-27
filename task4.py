# Advanced Basic Chatbot - CodeAlpha Internship Project

def chatbot():

    print("===================================")
    print("         BASIC CHATBOT")
    print("===================================")
    print("Type 'bye' to end the chat.\n")

    while True:

        user_message = input("You: ").lower()

        # Multiple greetings
        if user_message in ["hello", "hi", "hey"]:
            bot_reply = "Hello! Nice to meet you."

        elif user_message in ["how are you", "how are you?"]:
            bot_reply = "I'm fine, thanks for asking!"

        elif user_message in ["what is your name", "your name"]:
            bot_reply = "My name is ChatBot."

        elif user_message in ["good morning"]:
            bot_reply = "Good Morning! Have a great day."

        elif user_message in ["good night"]:
            bot_reply = "Good Night! Sweet dreams."

        elif user_message in ["thanks", "thank you"]:
            bot_reply = "You're welcome!"

        elif user_message == "bye":
            bot_reply = "Goodbye! Have a nice day."
            print("Bot:", bot_reply)
            break

        else:
            bot_reply = "Sorry, I don't understand that."

        print("Bot:", bot_reply)

# Run chatbot
chatbot()