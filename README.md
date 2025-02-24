Goal: Transcribe audio to text using Python and OpenAI's Whisper, saving the transcript to a file.

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
```bash
Run: pip install openai-whisper ffmpeg-python torchaudio
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
```
* Run script: Open terminal, navigate to script folder (cd ...), run
```bash
python speech_to_text.py.
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
