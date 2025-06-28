# Charlotte

Charlotte is a modular, voice-enabled personal desktop assistant built using OpenAI's GPT-4o API. It works like your own intelligent copilot, designed to help you with everyday tasks on your laptop through natural conversation.

```
Charlotte-assistant/
├──README.md
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
```

# HOW TO COMMIT:
1) Fork this repository
2) Clone the forked repository to your local system
3) Create a new branch for your cloned repository and make the necessary changes
4) Push the changes to your new branch and put a pull request to pull your new branch to the main branch

**NOTE**: install all the requirements using ``` pip install -r requirements.txt``` and don't forget to use a Python Virtual Environment before you install anything or make any changes.
