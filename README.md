# Speech-to-Text in Python using OpenAI Whisper

This Python script leverages OpenAI's Whisper, a powerful deep-learning model, to accurately transcribe spoken words from an audio file into text. It's designed to be straightforward and easy to use, providing a quick way to convert audio to text using Python.

## Features

*   **Powered by OpenAI Whisper:** Utilizes a state-of-the-art deep-learning model for high-accuracy speech-to-text transcription.
*   **Simple and Easy to Use:**  Provides a clear and concise function to perform transcription with minimal code.
*   **Supports Various Audio Formats:**  Whisper and `ffmpeg` (implicitly required) support a wide range of audio file formats.

## Getting Started

Follow these steps to get the script up and running on your local machine.

### Prerequisites

*   **Python:** Ensure you have Python installed on your system. It's recommended to use Python 3.7 or later.

### Installation

1.  **Install Dependencies:** Open your system's terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run the following command to install the necessary Python packages:

    ```bash
    pip install openai-whisper ffmpeg torchaudio
    ```

    **Important:** Run this command in your terminal or command line interface. **Do not** include this command within your Python script.

### Usage

1.  **Import the Function:** In your Python script, import the `transcribe_with_whisper` function:

    ```python
    import whisper
    ```

2.  **Define the Transcription Function:** Copy and paste the following function into your Python script:

    ```python
    import whisper

    def transcribe_with_whisper(audio_file):
        print("Loading Whisper model...")
        model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
        print("Transcribing...")
        result = model.transcribe(audio_file)

        print("\nTranscription:\n", result["text"])
        return result["text"]
    ```

3.  **Call the Function with Your Audio File Path:**  Provide the path to your audio file to the `transcribe_with_whisper` function.  **Ensure the audio file path is correct and accessible by the script.**

    ```python
    audio_path = r"C:\Users\rtx11\Downloads\News Round Up.wav"  # Replace with your audio file path
    transcribe_with_whisper(audio_path)
    ```

    **Note on File Paths:**
    *   On Windows, use raw strings ( `r"your\path"` ) or double backslashes ( `"your\\\\path"` ) to avoid issues with backslash escaping in Python strings.
    *   On macOS/Linux, use forward slashes ( `"your/path"` ).

### Running the Script

1.  **Save Your Script:** Save your Python script (e.g., as `speech_to_text.py`).
2.  **Execute the Script:** Open your terminal, navigate to the directory where you saved your script, and run it using the Python interpreter:

    ```bash
    python speech_to_text.py
    ```

    This will execute the script, load the Whisper model, transcribe the audio file, and print the transcribed text to your console.

## Model Options

The `whisper.load_model()` function accepts different model sizes. You can choose a model based on your needs and available resources:

*   **`"tiny"`:**  Fastest and smallest, but least accurate.
*   **`"base"`:**  A good balance between speed and accuracy. (Default in the script)
*   **`"small"`:**  More accurate than "base", but slower.
*   **`"medium"`:**  More accurate than "small", but slower.
*   **`"large"`:**  Most accurate, but slowest and requires more resources (GPU recommended for optimal performance).

To use a different model, simply change the argument within the `whisper.load_model()` function:

```python
model = whisper.load_model("small")  # Example: Using the 'small' model
