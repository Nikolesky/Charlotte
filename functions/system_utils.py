def load_chat_history(filepath):
    """
    Loads chat history from a file.
    
    Args:
        filepath (str): The path to the chat history file.
        
    Purpose:
        loads the chat history from the given file for gemini api to use
    """

    history = []

    f = open(filepath, "r", encoding="utf-8")

    try:
        for line in f:
            
            line = line.strip()

            if ":" not in line:
                continue
            
            parts = line.split(":", 1)
            role_text = parts[0].strip().lower()
            message = parts[1].strip()

            if role_text == "You":
                role = "user"
            else:
                role = "model"

            history.append({"role": role, "parts": message})

    finally:
        f.close()

    return history

