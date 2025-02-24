import whisper
import os

# Function to load the model and handle errors
def load_model():
    try:
        model = whisper.load_model("base")  # You can change to "small", "medium", or "large"
        return model
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

# Function to transcribe audio
def transcribe_audio(model, audio_path):
    if not os.path.exists(audio_path):
        print("Error: Audio file does not exist.")
        return None

    try:
        # Perform transcription
        result = model.transcribe(audio_path)
        return result['text']
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

# Main code execution
def main():
    # Load the Whisper model
    model = load_model()

    if model:
        # Path to the audio file
        audio_path = r"C:\Users\rtx11\Downloads\newsroundup.wav"  # Update with your actual audio file path
        
        # Transcribe the audio
        transcription = transcribe_audio(model, audio_path)
        
        if transcription:
            print("Transcription: ", transcription)
        else:
            print("Transcription failed.")
    else:
        print("Failed to load Whisper model.")

# Run the main function
if __name__ == "__main__":
    main()
