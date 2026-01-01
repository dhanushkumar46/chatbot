import random
import re
print(" Chatbot: Hello! Type 'bye' to exit.")
conversation_count = 0
user_name = ""
while True:
    conversation_count += 1
    user_input = input("You: ").strip().lower()

    if user_input == "":
        print(" Chatbot: Please say something ")
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        print(" Chatbot: Hello! How can I help you today?")
    elif "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip().title()
        print(f" Chatbot: Nice to meet you, {user_name} ")

    elif "your name" in user_input or "who are you" in user_input:
        print(" Chatbot: I am a rule-based chatbot written in Python ")
    elif "how are you" in user_input:
        print(" Chatbot: I'm doing great! Hope you are too ")
    elif any(word in user_input for word in ["sad", "unhappy", "depressed"]):
        print(" Chatbot: I'm sorry you're feeling that way . Things will get better ")

    elif any(word in user_input for word in ["happy", "excited"]):
        print(" Chatbot: That's awesome! Keep smiling ")

    elif "bored" in user_input:
        print(" Chatbot: Let's fix that! Want to hear a joke or a fun fact? ")
    elif "my age is" in user_input:
        age = re.findall(r'\d+', user_input)
        if age:
            print(f" Chatbot: Wow! {age[0]} is a great age ")
    elif any(word in user_input for word in ["hobby", "hobbies"]):
        print(" Chatbot: That's nice! Hobbies make life more interesting ")
    elif any(word in user_input for word in ["study", "exam", "college"]):
        print(" Chatbot: Stay focused! Consistency is the key to success ")
    elif any(word in user_input for word in ["python", "programming", "coding"]):
        print(" Chatbot: Programming is fun! Practice daily and build projects ")
    elif any(word in user_input for word in ["motivate", "motivation", "inspire"]):
        quotes = [
            "Believe in yourself and all that you are ",
            "Success is the sum of small efforts repeated daily ",
            "Don't stop until you're proud "
        ]
        print(f" Chatbot: {random.choice(quotes)}")
    elif "fun fact" in user_input:
        facts = [
            "Honey never spoils ",
            "Octopuses have three hearts ",
            "Bananas are berries "
        ]
        print(f" Chatbot: {random.choice(facts)}")
    elif "favorite color" in user_input:
        print(" Chatbot: Nice choice! Colors reflect personality ")
    elif any(word in user_input for word in ["thanks", "thank you"]):
        responses = ["You're welcome ", "Anytime!", "Happy to help "]
        print(f" Chatbot: {random.choice(responses)}")
    elif "joke" in user_input:
        jokes = [
            "Why don’t programmers like nature? Too many bugs ",
            "Why did Python cross the road? To import the other side ",
            "Why do Java developers wear glasses? Because they don’t C# "
        ]
        print(f" Chatbot: {random.choice(jokes)}")
    elif any(op in user_input for op in ["+", "-", "*", "/", "plus", "minus", "times", "divided"]):
        numbers = re.findall(r'\d+', user_input)
        if len(numbers) >= 2:
            a, b = int(numbers[0]), int(numbers[1])
            if "+" in user_input or "plus" in user_input:
                print(f" Chatbot: {a} + {b} = {a + b}")
            elif "-" in user_input or "minus" in user_input:
                print(f" Chatbot: {a} - {b} = {a - b}")
            elif "*" in user_input or "times" in user_input:
                print(f" Chatbot: {a} × {b} = {a * b}")
            elif "/" in user_input or "divided" in user_input:
                print(" Chatbot: Cannot divide by zero " if b == 0 else f" Chatbot: {a} ÷ {b} = {a / b}")
    elif any(word in user_input for word in ["bye", "exit", "quit", "goodbye"]):
        print(f" Chatbot: Goodbye {user_name if user_name else ''}! We chatted {conversation_count} times ")
        break
    else:
        fallback = [
            "Hmm I didn't understand that.",
            "Can you rephrase it?",
            "Try typing 'help' to know what I can do"
        ]
        print(f" Chatbot: {random.choice(fallback)}")
