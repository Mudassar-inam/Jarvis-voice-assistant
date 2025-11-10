import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import musicLibrary
import newsLibrary
import google.generativeai as genai
from dotenv import load_dotenv
import re
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize
recognizer = sr.Recognizer()

# Configure Gemini with rate limiting
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')  # Fast and efficient

# Rate limiting variables
last_gemini_request = None
gemini_request_count = 0
gemini_reset_time = datetime.now()
MAX_REQUESTS_PER_MINUTE = 10

# Fallback responses
FALLBACK_RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm doing great! Thanks for asking. How can I assist you?",
    "what is your name": "I am Jarvis, your AI voice assistant.",
    "who are you": "I'm Jarvis, an AI assistant here to help you.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a great day!",
    "what can you do": "I can open websites, play music, fetch news, and answer questions.",
    "time": f"The current time is {datetime.now().strftime('%I:%M %p')}",
}


def clean_text_for_speech(text):
    """Remove asterisks, links, and special characters for clean speech"""
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[#_`\[\]]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def speak(text):
    """Speak text after cleaning it"""
    try:
        clean_text = clean_text_for_speech(text)
        print(f"[SPEAKING]: {clean_text}")

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        
        engine.say(clean_text)
        engine.runAndWait()
        engine.stop()
        
        print("[SPEECH COMPLETED]")
    except Exception as e:
        print(f"Speech Error: {e}")


def get_fallback_response(question):
    """Check for simple fallback responses"""
    question_lower = question.lower().strip()
    
    for key, response in FALLBACK_RESPONSES.items():
        if key in question_lower:
            return response
    
    return None


def ask_gemini(question):
    """Ask Gemini AI with rate limiting and fallback"""
    global last_gemini_request, gemini_request_count, gemini_reset_time
    
    # Try fallback first
    fallback = get_fallback_response(question)
    if fallback:
        return fallback
    
    # Rate limiting logic
    current_time = datetime.now()
    
    # Reset counter every minute
    if (current_time - gemini_reset_time).seconds >= 60:
        gemini_request_count = 0
        gemini_reset_time = current_time
    
    # Check if we've hit the limit
    if gemini_request_count >= MAX_REQUESTS_PER_MINUTE:
        return "I'm currently at my rate limit. Please try again in a minute or ask me simple questions."
    
    # Ensure minimum delay between requests
    if last_gemini_request:
        elapsed = (current_time - last_gemini_request).total_seconds()
        if elapsed < 3:  # 3 seconds minimum
            time.sleep(3 - elapsed)
    
    try:
        last_gemini_request = datetime.now()
        gemini_request_count += 1
        
        brief_prompt = f"{question}\n\nAnswer in 2-3 short sentences."
        
        response = model.generate_content(brief_prompt)
        return response.text
        
    except Exception as e:
        error_message = str(e)
        print(f"Gemini Error: {error_message}")
        
        # Handle rate limit
        if "429" in error_message or "quota" in error_message.lower():
            return "I've reached my API limit for now. Try again in a minute, or ask me to open apps or get news instead."
        
        # Handle API key issues
        elif "API key" in error_message:
            return "There's an issue with my configuration. Please check the API key."
        
        else:
            return "Sorry, I couldn't process that request right now."


def processCommand(c):
    """Process voice commands"""
    
    # Website commands
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
        
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
        
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
        
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
        
    # App commands
    elif "open whatsapp" in c.lower():
        speak("Opening WhatsApp")
        os.system("explorer shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        
    elif "open snapchat" in c.lower():
        speak("Opening Snapchat")
        webbrowser.open("https://snapchat.com")
    
    # Music commands
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        except:
            speak("Song not found in library")
    
    # News commands
    elif "dawn news" in c.lower():
        newsLibrary.get_news(source="dawn", limit=5, speak_func=speak)
        
    elif "express news" in c.lower() or "tribune news" in c.lower():
        newsLibrary.get_news(source="express", limit=5, speak_func=speak)
        
    elif "geo news" in c.lower():
        newsLibrary.get_news(source="geo", limit=5, speak_func=speak)
        
    elif "news summary" in c.lower() or "quick news" in c.lower():
        newsLibrary.get_news_summary(source="all", limit=5, speak_func=speak)
        
    elif "news" in c.lower() or "headlines" in c.lower():
        newsLibrary.get_news(source="all", limit=6, speak_func=speak)
    
    # AI-powered general questions
    else:
        speak("Let me think about that")
        response = ask_gemini(c)
        
        print(f"\nGemini Response:\n{response}\n")
        speak(response)


if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                print("Recognizing...")

                word = r.recognize_google(audio)
                print(f"Heard: {word}")

            if word.lower() == "jarvis":
                speak("Yes Boss")
                
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source, timeout=4, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print("Error: {0}".format(e))