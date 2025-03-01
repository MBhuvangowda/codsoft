def chatbot():
    print("Welcome to the Rule-Based Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi there! How can I help you today?")
        elif user_input in["how are you?"]:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        elif user_input in ["what can you do?"]:
            print("Chatbot: I can answer basic questions based on predefined rules.")
        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Farewell! Have a great day ahead!")
            break
        elif "time" in user_input:
            print("Chatbot: I can't check the current time, but you can look at a clock!")
        else:
            print("Chatbot: Sorry, I don't understand that. Can you ask something else?")

chatbot()