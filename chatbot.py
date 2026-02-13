name = input("Enter your name: ")

print("Chatbot: You can talk here " +name)
print("Type 'bye' to exit.\n")

while True:
    user_input = input(name + ": ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye!!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi!!")

    elif "how are you" in user_input:
        print("Chatbot: I'm fine, thank you.")

    elif "help" in user_input:
        print("Chatbot: Try saying Hello or How are you ?")

    else:
        print("Chatbot: Sorry, I don't understand.")
