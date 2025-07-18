import sounddevice as sd
import numpy as np
import os
from scipy.io.wavfile import write

def record_audio(
    output_folder="my_recordings",
    output_filename="recorded_audio.wav",
    sample_rate=44100,
    channels=2
):
    """
    Interactive audio recorder. Type 'start' to begin and 'stop' to end recording.
    Saves the result as a WAV file in the specified folder.
    """
    output_path = os.path.join(output_folder, output_filename)
    os.makedirs(output_folder, exist_ok=True)

    recorded_frames = []

    def callback(indata, frames, time, status):
        if status:
            print("Status:", status)
        recorded_frames.append(indata.copy())

    print("Type 'start' to begin recording and 'stop' to end recording:")

    while True:
        cmd = input(">> ").strip().lower()

        if cmd == "start":
            print("Recording... Type 'stop' to stop.")
            recorded_frames.clear()
            with sd.InputStream(samplerate=sample_rate, channels=channels, callback=callback):
                while True:
                    if input(">> ").strip().lower() == "stop":
                        break
            print("Recording stopped.")

            # Combine all recorded chunks into one array
            audio_data = np.concatenate(recorded_frames, axis=0)

            # Save as WAV
            write(output_path, sample_rate, audio_data)
            print(f"Saved recording to {output_path}")

        elif cmd == "exit":
            print("Exiting recording session.")
            break
        else:
            print("Unknown command. Use 'start', 'stop', or 'exit'.")
