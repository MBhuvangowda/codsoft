def chatbot_response(user_input):
    if "hello" in user_input: return "Hello!"
    if "how are you" in user_input: return "I'm fine!"
    if "name" in user_input: return "I'm a chatbot."
    if "bye" in user_input: return "Goodbye!"
    return "I don't understand."

while True:
    user_input = input("You: ")
    if "bye" in user_input:
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")