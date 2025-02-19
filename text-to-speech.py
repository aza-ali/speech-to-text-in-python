import whisper

def transcribe_with_whisper(audio_file):
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
    print("Transcribing...")
    result = model.transcribe(audio_file)
    
    print("\nTranscription:\n", result["text"])
    return result["text"]

# Usage Example
audio_path = r"C:\Users\rtx11\Downloads\News Round Up.wav"  # Corrected path
transcribe_with_whisper(audio_path)
