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

### Option A — Just use the .exe (Windows, no Python needed)

1. Go to [Releases](../../releases) and download `FishAudioTTS.exe`
2. Put it in its own folder (it will create `config.json` and `output/` next to itself)
3. Double-click and you're done

### Option B — Run from source

1. Install Python 3.10+ from [python.org](https://python.org)
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run it:
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
