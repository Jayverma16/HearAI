import whisper
import os

class Transcriber:
    def __init__(self, model_name="base"):
        self.model_name = model_name
        print(f"Loading Whisper model: {model_name}...")
        try:
            self.model = whisper.load_model(model_name)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def transcribe(self, audio_file):
        if not self.model:
            return "Error: Model not loaded."
        
        if not os.path.exists(audio_file):
            return "Error: Audio file not found."

        print(f"Transcribing {audio_file}...")
        try:
            result = self.model.transcribe(audio_file)
            return result["text"].strip()
        except Exception as e:
            return f"Error during transcription: {e}"
