Goal: Transcribe audio to text using local processing without sending sensitive data to the cloud.

Key Features:

Accurate: OpenAI Whisper powered transcription.
Robust: Error handling for common issues.
Flexible: Model choice for speed/accuracy.
Simple: Terminal input for audio file path.
Automatic: Saves transcript to a .txt file.
Versatile: Wide audio format support (via ffmpeg).
Quick Setup:

1. Prerequisites:
* Python: Install Python 3.7+ from python.org.
* FFmpeg:  Crucial for audio processing. See "FFmpeg Install (Windows)" below if needed.

2. Installation:
* Open Terminal/Command Prompt.
* Run:
```bash
pip install openai-whisper ffmpeg-python torchaudio
```
FFmpeg Install (Windows - If needed):
* Download: From [FFmpeg website link] (Gyan.dev builds recommended). Get the static ZIP for Windows.
* Extract: To a folder (e.g., C:\ffmpeg).
* Add to PATH:
* Win + R, type sysdm.cpl, Enter.
* Advanced tab -> Environment Variables.
* Under "System variables," find and edit "Path."
* Add a "New" entry:  Path to your ffmpeg\bin folder (e.g., C:\ffmpeg\bin).
* OK all windows to save.
* Verify: Open new terminal, run ffmpeg -version. Should show version info.

3. Usage:
* Save script: Save the Python code as speech_to_text.py.
```bash
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
```
* Open terminal, navigate to script folder (cd ...),
* Run
```bash
python speech_to_text.py
```
* Enter audio path: When prompted, paste/type your audio file path and press Enter.
* Output: Transcription text in terminal and saved as audio_file_name.txt in the same folder as audio.

4. Example:
* Audio file: voice_note.wav in Downloads folder.
* Run script, enter path (adjust username): C:\Users\YourUsername\Downloads\voice_note.wav
* Transcript: voice_note.txt in Downloads folder.

5. Model Options (Edit Script for Change):
* "tiny": Fastest, least accurate.
* "base": Default, balanced speed/accuracy.
* "small": Higher accuracy, slower.
* "medium": Even higher accuracy, slower.
* "large": Highest accuracy, slowest, needs more resources.
* To change: Edit speech_to_text.py, find model_name="base" in transcribe_with_whisper function, change "base" to your desired model (e.g., "small").

6. Troubleshooting (Common Issues):
* FFmpeg errors:
* Re-install FFmpeg, check PATH setup, restart terminal, verify with ffmpeg -version.
* FileNotFoundError:
* Check audio path spelling, capitalization, file exists at path, use absolute paths.
* Model loading errors:
* Internet needed for first model download, ensure connection, check disk space.
* Poor accuracy:
* Improve audio quality (less noise), try larger Whisper model, consider language/technical vocabulary limitations.
