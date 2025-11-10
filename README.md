# 🎙️ JARVIS – AI Voice Assistant (Python)

A personal AI voice assistant built using **Python**, capable of:

✅ Speech Recognition  
✅ Text-to-Speech interaction  
✅ Opening apps & websites  
✅ Playing songs from a custom music library  
✅ Fetching real-time news (RSS feeds)  
✅ AI-powered responses using **Gemini API**

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🎤 Voice activation | Say **"Jarvis"** to wake the assistant |
| 🌐 Open Apps/Websites | Google, Facebook, Instagram, WhatsApp Desktop, etc. |
| 🎶 Music Player | Plays songs stored in `musicLibrary.py` |
| 📰 News Updates | Fetches latest headlines using RSS feeds via `newsLibrary.py` |
| 🤖 AI Question Answering | Uses **Google Gemini API** with auto fallback responses |
| ⚙️ Rate Limiting | Prevents API overuse (automatic delay + minute-based request control) |

---

## 🧠 Tech Stack

| Dependency | Usage |
|------------|-------|
| `speech_recognition` | Listen to and convert voice to text |
| `pyttsx3` | Text-to-speech |
| `webbrowser`, `os` | Opening apps and websites |
| `google.generativeai` | Gemini API |
| `feedparser` | Fetching RSS news feed |
| `dotenv` | Load API key securely |

---

## 📁 Project Structure

📦 JARVIS
│
├── jarvis.py # Main program logic
├── musicLibrary.py # Dictionary of songs + URLs
├── newsLibrary.py # Fetches news via RSS feeds
└── .env # Stores GEMINI_API_KEY (not uploaded)

yaml
Copy code

---

## 🔧 How to Run

### 1️⃣ Install dependencies
```sh
pip install speechrecognition pyttsx3 google-generativeai feedparser python-dotenv

Note: PyAudio may require additional system dependencies:

Windows: pip install pyaudio
macOS: brew install portaudio && pip install pyaudio
Linux: sudo apt-get install python3-pyaudio

2️⃣ Add your Gemini API key and News API Key
Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_news_api_key_here

Get API Keys:

Gemini API: Get from Google AI Studio
News API: Get from NewsAPI.org (optional)


Customize your music library in musicLibrary.py:

pythonmusic = {
    "song_name": "youtube_or_spotify_link",
    "another_song": "link_here"
}

3️⃣ Run the script
sh
Copy code
python jarvis.py
Say "Jarvis", then give commands like:

open google

play skyfall

what is artificial intelligence?

geo news

what is the time?

📸 Demo Video (LinkedIn)
Coming soon — will be added after video upload

⭐ Show Support
If you like this project:

⭐ Star the repo on GitHub

Fork and enhance it

