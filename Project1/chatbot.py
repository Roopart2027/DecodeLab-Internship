import datetime
import random


# Function to clean user input
def sanitize_input(user_input):
    return user_input.strip().lower()


# Function to generate chatbot response
def get_response(user_input):

    responses = {
        "greeting": [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Hey! Welcome to DecoBot!"
        ],

        "farewell": [
            "Goodbye! Have a great day!",
            "Bye! See you again!"
        ],

        "time": [
            f"The current date and time is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        ],

        "identity": [
            "I am DecoBot, a rule-based AI chatbot built for the DecodeLabs AI Engineering Internship."
        ],

        "help": [
            "You can say hello, ask for time, ask who I am, or type exit to quit."
        ]
    }


    keywords = {
        "hello": "greeting",
        "hi": "greeting",
        "hey": "greeting",

        "bye": "farewell",
        "exit": "farewell",
        "quit": "farewell",

        "time": "time",
        "date": "time",

        "who are you": "identity",
        "who": "identity",

        "help": "help"
    }


    # Check exact input
    if user_input in keywords:
        intent = keywords[user_input]
        return random.choice(responses[intent])


    # Check keywords inside sentences
    for keyword, intent in keywords.items():
        if keyword in user_input:
            return random.choice(responses[intent])


    # Fallback response
    return "I'm sorry, I didn't understand that. Type 'help' to see what I can do."


# Main chatbot function
def run_chatbot():

    print("🤖 DecoBot initialized!")
    print("Type 'help' to see available commands.")
    print("Type 'exit', 'quit', or 'bye' to stop the chatbot.")
    print("-" * 50)


    while True:

        user_input = input("You: ")

        clean_input = sanitize_input(user_input)


        # Handle empty input
        if not clean_input:
            print("DecoBot: Please enter something.")
            continue


        # Exit condition
        if clean_input in ["exit", "quit", "bye"]:
            print("DecoBot: Goodbye! Have a great day!")
            break


        # Get chatbot response
        response = get_response(clean_input)

        print("DecoBot:", response)


# Start the chatbot
if __name__ == "__main__":
    run_chatbot()