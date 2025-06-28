# Charlotte

Charlotte is a modular, voice-enabled personal desktop assistant built using OpenAI's GPT-4o API. It works like your own intelligent copilot, designed to help you with everyday tasks on your laptop through natural conversation.

Charlotte-assistant/
├── main.py                 # Entry point
├── config.py               # Your API keys and settings
├── functions/
│   ├── __init__.py
│   ├── system_utils.py     # Functions like opening apps, checking time
├── chat_engine.py          # Handles communication with GPT-4o
├── voice/
│   ├── speech_to_text.py   # Optional: convert voice to text
│   ├── text_to_speech.py   # Optional: speak replies aloud
└── requirements.txt

