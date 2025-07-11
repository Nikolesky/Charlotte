import google.generativeai as genai
from google.generativeai import types
from config import GENAI_API_KEY
from functions.system_utils import load_chat_history

def start_chat():
    """
    Starts a chat session using Google Generative AI.
    """
    # Configure the API key
    genai.configure(api_key=GENAI_API_KEY)

    #get the model
    model = genai.GenerativeModel(model_name = "gemini-2.0-flash", system_instruction="You are Charlotte, Nikolesky's assistant. You don't hesitate, are funny and frank.")

    # Load chat history if available
    history = load_chat_history("history.txt")

    chat = model.start_chat(history=history)

    print("Welcome to the chat! Type 'exit' or 'quit' to end the chat.")


    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting chat. Goodbye!")
            break

        # Generate content
        response = chat.send_message(user_input)

        # Print the response
        print("Charlotte: ", response.candidates[0].content.parts[0].text)

        #store the chat history
        f = open("history.txt", "a")

        f.write(f"You: {user_input}\n")
        f.write(f"Charlotte: {response.candidates[0].content.parts[0].text}\n")
        f.close()
        