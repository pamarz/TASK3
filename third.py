#Basic chatpot
def chatbot():
    print("Hi, I'm a simple chatbot. Let's talk!")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hello", "hi"]:
            print("Chatbot: Hi there!")
        elif user_input.lower() in ["how are you", "how's it going"]:
            print("Chatbot: I'm doing well, thank you. How are you?")
        elif user_input.lower() == "quit":
            print("Chatbot: Bye!")
            break
        else:
            print("Chatbot: I don't understand. Can you rephrase?")

chatbot() 
