from google import genai
from google.genai import types
from config import GENAI_API_KEY
from functions.system_utils import load_chat_history
from voice.text_to_speech import speak_text

def start_chat():
    """
    Starts a chat session using Google Generative AI.
    """
    # Configure the API key
    client = genai.Client(api_key=GENAI_API_KEY)

    #Set up the google search retrival tool
    grounding_tool = types.Tool(
        google_search = types.GoogleSearch()
    )
    #configure generation settings
    config = types.GenerateContentConfig(
        system_instruction= "You are Charlotte, Nikolesky's assistant. You don't hesitate, are funny and frank.",
        tools = [grounding_tool],
        temperature = 0.7
    )

    # Load chat history if available
    history = load_chat_history("history.txt")

    chat = client.chats.create(
        model = "gemini-2.0-flash",
        config = config,
        history= history
    )

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

        # Print the response as a stream
        print(f"Charlotte: {response.candidates[0].content.parts[0].text}")

        speak_text(response.candidates[0].content.parts[0].text)
        

        #store the chat history
        f = open("history.txt", "a")

        f.write(f"You: {user_input}\n")
        f.write(f"Charlotte: {response.candidates[0].content.parts[0].text}\n")
        f.close()