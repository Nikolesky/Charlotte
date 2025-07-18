
def speak_text(text):
    """
    Speaks the given text using the TTS engine.
    
    Args:
        text (str): The text to be spoken.
        
    Purpose:
        speaks the given text using the TTS engine
    """
    import pyttsx3
    
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set to the first available voice

    # Say the text
    engine.say(text)

    # Run the speech synthesis and wait for it to complete
    engine.runAndWait()
