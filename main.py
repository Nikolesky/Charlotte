from google import genai
from google.genai import types
from config import GENAI_API_KEY

client = genai.Client(api_key=GENAI_API_KEY)

chat = client.chats.create(model='gemini-2.0-flash')

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = client.models.generate_content_stream(
        model='gemini-2.0-flash',
        config=types.GenerateContentConfig(
        system_instruction="You are Nikolesky's personalized AI assistant, Charlotte. You are helpful, creative, and friendly.",),
        contents=user_input
        )
    print("Charlotte: ", end='')
    for stream in response:
        print(stream.text)
