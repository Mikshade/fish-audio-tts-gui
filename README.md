# 🎤 Fish Audio TTS — Desktop GUI

A simple desktop app to generate MP3 files using the [Fish Audio](https://fish.audio) Text-to-Speech API.

No command line needed. Just open it, type your text, click generate.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-ff5f5f?logo=ko-fi)](https://ko-fi.com/mikshade)

---

## ✨ Features

- 🎙️ Use any Fish Audio voice model via Reference ID
- 💾 Voice ID is saved — set it once, forget about it
- 📁 All MP3s saved to `/output` folder automatically
- ⚡ Simple, fast, no bloat

---

## 🚀 Getting Started

### 1. Install Python
Download Python 3.10+ from [python.org](https://python.org) and install it.
Make sure to check **"Add Python to PATH"** during installation.

### 2. Install dependencies
Open a terminal in the project folder and run:
```
pip install -r requirements.txt
```

### 3. Set up your config
Copy `config.example.json` and rename it to `config.json`:
```
cp config.example.json config.json
```
Then open `config.json` and fill in your details:
```json
{
  "api_key": "your_fish_audio_api_key",
  "voice_id": "the_reference_id_of_your_voice",
  "bitrate": 128
}
```

### 4. Run it
Double-click `Start.bat` — or run:
```
python fish_tts.py
```

---

## 🔑 Getting your API Key

1. Go to [fish.audio](https://fish.audio) and create an account
2. Navigate to your profile → API Keys
3. Create a new key and paste it into `config.json`

## 🎙️ Finding a Voice ID

1. Browse voices on [fish.audio](https://fish.audio)
2. Click on any voice model
3. Copy the ID from the URL or model page
4. Paste it as `voice_id` in `config.json` — or directly in the app

---

## 📁 Output

Generated MP3s are saved in the `/output` folder with a timestamp:
```
output/tts_20240312_201500.mp3
```

---

## 📋 Requirements

- Windows 10/11
- Python 3.10+
- Fish Audio account & API key

---

## ☕ Support

If this tool saved you some time, feel free to buy me a coffee!

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/mikshade)

## 📄 License

MIT — do whatever you want with it.
