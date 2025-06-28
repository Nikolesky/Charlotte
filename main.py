from google import genai
from config import GENAI_API_KEY

client = genai.Client(api_key=GENAI_API_KEY)

chat = client.chats.create(model='gemini-2.0-flash',)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chat.send_message(user_input)
    print(f"AI: {response.text}")
