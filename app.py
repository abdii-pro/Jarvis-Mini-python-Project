#pip install speechrecognition pyaudio
#pip install setuptools
#pip install pyttsx3

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    # print(c)

if __name__ == "__main__":
    speak("Jarvis Initializing....")
    while True:
        r = sr.Recognizer()
        

        # Listen for Awake Word
        try:
            with sr.Microphone() as source:
                print("Listing...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            print("Recognizing...")
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis is Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))