# Robust Speech-to-Text with File Saving in Python using OpenAI Whisper

This Python script transcribes audio files to text using OpenAI's Whisper model and **now saves the transcription to a text file** in the same directory as the audio. This enhanced version is robust, handles errors, and provides convenient file output.

## Features

*   **Powered by OpenAI Whisper:** Accurate speech-to-text using a state-of-the-art deep-learning model.
*   **Error Handling:**  Handles file not found errors, model loading issues, and transcription errors.
*   **Model Selection:** Choose from different Whisper models (tiny, base, small, medium, large) for speed/accuracy balance.
*   **User-Friendly Input:** Prompts for the audio file path in the terminal.
*   **Clear Output:** Displays transcription in the console and indicates success/failure.
*   **Saves to Text File:** **Automatically saves the transcription as a `.txt` file in the same folder as the audio, using the same base filename.**
*   **Supports Various Audio Formats:** Whisper and `ffmpeg` compatible with many audio formats.

## Getting Started

Follow these steps to set up and use the script with file saving.

### Prerequisites

*   **Python:** Python 3.7+ installed on your system.
*   **ffmpeg:**  **`ffmpeg` must be installed and in your system's PATH.** (See "Troubleshooting" in `readme.md` for guidance).

### Installation

1.  **Install Dependencies:** Open your terminal and run:

    ```bash
    pip install openai-whisper ffmpeg-python torchaudio
    ```

    **Run this in your terminal, not in Python.**

2. Download FFmpeg:

Go to the official FFmpeg download page: FFmpeg Downloads.
Under the "Windows" section, download the build from gyan.dev (or another trusted source).
Choose the Static build for Windows.

### Usage

1.  **Save the Script:** Save the Python code as `speech_to_text.py`.

2.  **Run the Script:** Open your terminal, navigate to the script's directory, and execute:

    ```bash
    python speech_to_text.py
    ```

3.  **Enter Audio File Path:** When prompted, enter the **full path** to your audio file and press Enter.

4.  **Transcription and File Saving:**
    *   The script will transcribe the audio and print the text to the console.
    *   **A text file with the same name as your audio file (but with a `.txt` extension) will be created in the same directory as your audio file.**
    *   You will see a message in the console indicating the location where the transcript file was saved.

### Example

If you transcribe `my_recording.wav` located in `Documents/Audio/`, the script will:

1.  Print the transcription to the console.
2.  Create a file named `my_recording.txt` in the `Documents/Audio/` directory containing the transcribed text.

### Model Options

(Same Model Options section as before - no changes needed in this section)

### Troubleshooting

(Same Troubleshooting section as before - no changes needed in this section)

### Contributing

(Same Contributing section as before - no changes needed in this section)

### License

(Same License section as before - no changes needed in this section)

### Contact

(Same Contact section as before - no changes needed in this section)

---

**Enjoy transcribing your audio and automatically saving the results with Python and OpenAI Whisper!**
