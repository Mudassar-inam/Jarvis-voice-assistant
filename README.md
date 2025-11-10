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

## 🛠️ Technologies Used

- **Python 3.x**
- **SpeechRecognition** - Voice input processing
- **pyttsx3** - Text-to-speech conversion
- **Google Generative AI (Gemini)** - AI-powered responses
- **feedparser** - RSS news feed parsing
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

```bash
pip install speechrecognition pyttsx3 google-generativeai python-dotenv feedparser pyaudio
```

**Note**: PyAudio may require additional system dependencies:
- **Windows**: `pip install pyaudio`
- **macOS**: `brew install portaudio && pip install pyaudio`
- **Linux**: `sudo apt-get install python3-pyaudio`

## ⚙️ Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. **Create a `.env` file** in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

3. **Get API Keys**:
   - **Gemini API**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **News API**: Get from [NewsAPI.org](https://newsapi.org/) (optional)

4. **Customize your music library** in `musicLibrary.py`:
```python
music = {
    "song_name": "youtube_or_spotify_link",
    "another_song": "link_here"
}
```

## 🚀 Usage

Run the assistant:
```bash
python JARVIS1.py
```

**Wake Word**: Say **"Jarvis"** to activate

### Voice Commands:

| Command | Action |
|---------|--------|
| "Open Google" | Opens Google in browser |
| "Open Facebook" | Opens Facebook |
| "Open Instagram" | Opens Instagram |
| "Open YouTube" | Opens YouTube |
| "Open LinkedIn" | Opens LinkedIn |
| "Open WhatsApp" | Launches WhatsApp Desktop |
| "Play [song_name]" | Plays song from your library |
| "News" or "Headlines" | Fetches latest Pakistani news from all sources |
| "Dawn news" | Fetches news from Dawn.com only |
| "Express news" | Fetches news from Express Tribune only |
| "Geo news" | Fetches news from Geo News only |
| "News summary" | Quick display of headlines without reading |
| Any question | Gets answer from Gemini AI |

## 📁 Project Structure

```
jarvis-voice-assistant/
│
├── JARVIS1.py          # Main application file
├── musicLibrary.py     # Music links dictionary
├── newsLibrary.py      # News fetching module
├── .env                # API keys (not tracked in git)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## 🐛 Troubleshooting

**Microphone not detected**:
- Check microphone permissions in system settings
- Verify microphone is set as default recording device

**Speech recognition errors**:
- Ensure stable internet connection (Google Speech API requires internet)
- Speak clearly near the microphone

**WhatsApp won't open (Windows)**:
- Ensure WhatsApp Desktop is installed from Microsoft Store
- Update the app package name if needed

## 🔮 Future Enhancements

- [ ] Add more voice commands
- [ ] Integrate with calendar and reminders
- [ ] Add email reading/sending capabilities
- [ ] Smart home device control
- [ ] Offline speech recognition
- [ ] Multi-language support

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/jarvis-voice-assistant/issues).

## 👨‍💻 Author

**Your Name**
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)

## ⭐ Show your support

Give a ⭐️ if you like this project!

---

**Note**: This is an educational project. Please use API keys responsibly and respect rate limits.

