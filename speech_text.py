import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio
with sr.Microphone() as source:
    print("Listening for your search query...")
    audio = recognizer.listen(source)

try:
    # Convert speech to text
    query = recognizer.recognize_google(audio)
    print(f"Search query: {query}")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
    query = input("Enter your search query manually: ")  # Allow manual input if speech is unclear
except sr.RequestError:
    print("Sorry, the service is down.")
    query = input("Enter your search query manually: ")  # Allow manual input if the service is down

# Initialize TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Speak the search query
engine.say(f"Searching for {query}")
engine.runAndWait()

# Perform search using webbrowser
webbrowser.open(f"https://www.google.com/search?q={query}")
