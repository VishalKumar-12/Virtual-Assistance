import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import tkinter as tk
from tkinter import PhotoImage

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female Voice
engine.setProperty('rate', 250)  # Rate of Speech 150

def speak(msg):
    """Convert text to speech."""
    engine.say(msg)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boss")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss, Vishal")
        print("Good Evening Boss, Vishal")
    speak("I am your jinni, how may I help you?")
    print("I am your jinni, how may I help you?")

def takeCommand():
    """Listen to the user's voice and convert it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
    except Exception as e:
        print("Say again, please.")
        return "none"
    return query

def run_alexa(query):
    """Process the user's commands."""
    query = query.lower()

    if 'play' in query:
        song = query.replace("play", "").strip()
        speak("Playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        speak("Current time is " + time)
    elif 'date' in query:
        speak("Sorry, I have a headache.")
    elif 'are you single' in query:
        speak("I am in a relationship with Wi-Fi!")
    elif 'joke' in query:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)
    elif 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'facebook' in query:
        webbrowser.open("fb.com")
    elif 'instagram' in query:
        webbrowser.open("instagram.com")
    elif 'stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'whatsapp' in query:
        webbrowser.open("whatsapp.com")
    elif 'google' in query:
        query = query.replace("google", "").replace("search", "").strip()
        webbrowser.open(f"https://google.com/search?q={query}")
    elif 'sleep' in query:
        speak("Going to sleep. Goodbye!")
        return False
    return True

def respond():
    """Handle the interaction when the button is clicked."""
    response_label.config(text="Listening...")
    query = takeCommand()
    response_label.config(text=f"You said: {query}")
    if query != "none":
        run_alexa(query)

# Create the main window
root = tk.Tk()
root.title("Virtual Assistant")


root.geometry("400x350+150+50")


name_label = tk.Label(root, text="Virtual Assistant", font=("Arial", 16))
name_label.pack(pady=10)

response_label = tk.Label(root, text="", font=("Arial", 12))
response_label.pack(pady=20)


interact_button = tk.Button(root, text="Ask a Question", command=respond)
interact_button.pack(pady=10)

#Load and create a button with a microphone icon
try:
    microphone_img = PhotoImage(file="microphone.png")  # Replace with the path to your microphone image
    microphone_button = tk.Button(root, image=microphone_img, command=respond)
    microphone_button.pack(pady=10)
except Exception as e:
    print(f"Error loading microphone image: {e}")
    microphone_button = tk.Button(root, text="Listen", command=respond)
    microphone_button.pack(pady=10)

wishMe()
# Run the application
root.mainloop()
