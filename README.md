# Speech to Text in Python

[![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Whisper](https://img.shields.io/badge/Whisper-OpenAI-412991?style=flat-square&logo=openai&logoColor=white)](https://github.com/openai/whisper)

Local audio transcription with OpenAI Whisper. No API keys, no cloud, no data leaving your machine.

## Why

You have an audio file you want transcribed. The usual options:

- **OpenAI / AssemblyAI / Deepgram APIs** - fast, accurate, but your audio goes to a server.
- **macOS dictation / Otter.ai** - also cloud.
- **This** - Whisper running entirely on your machine. Sensitive audio (interviews, medical notes, legal recordings) never leaves.

## Requirements

- Python 3.7+
- FFmpeg (for audio decoding)
- ~1-10 GB disk space depending on which Whisper model you load

## Install

```bash
pip install openai-whisper ffmpeg-python torchaudio
```

Install FFmpeg if you don't have it:

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg

# Windows (with Chocolatey)
choco install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

## Usage

Edit `text-to-speech.py` to point at your audio file:

```python
audio_path = "/path/to/your/audio.wav"
```

Then run:

```bash
python text-to-speech.py
```

Output: transcript printed to terminal and saved as a `.txt` file alongside the audio.

## Models

| Model | Speed | Accuracy | RAM |
|---|---|---|---|
| `tiny` | Fastest | Lowest | ~1 GB |
| `base` | Fast | Good | ~1 GB |
| `small` | Medium | Better | ~2 GB |
| `medium` | Slow | Better | ~5 GB |
| `large` | Slowest | Best | ~10 GB |

Change the model in the script:

```python
model = whisper.load_model("small")  # or "base", "medium", "large"
```

The first time you load a model, Whisper downloads it from the OpenAI CDN.

## Supported Audio Formats

Anything FFmpeg can decode: WAV, MP3, M4A, FLAC, OGG, AAC, WMA, etc.

## Troubleshooting

**FFmpeg errors** - verify the install with `ffmpeg -version`. On Windows, make sure `C:\ffmpeg\bin` is in your PATH.

**`FileNotFoundError`** - use an absolute path to the audio file. Check for typos in the filename.

**Model download fails** - first run requires internet to fetch the model. Check disk space too (models range from ~150 MB to ~3 GB).

**Poor accuracy** - try a larger model. Accuracy on noisy or accented audio scales heavily with model size. The `large` model handles non-English audio much better than `base`.

## License

MIT
