import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime


def say(text):
    print("Program : " + text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        try:
            engine.setProperty('voice', voices[-1].id)
        except IndexError:
            print("Voice index out of range. Using default voice.")
    else:
        print("No voices available. Using default voice.")
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            say("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            say("Sorry, my speech service is down.")
            return ""


if __name__ == '__main__':
    say('Hello my dear')
    while True:
        text_input = take_command()
        if text_input:
            say(text_input)
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"], ["linkedin", "https://linkedin.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in text_input.lower():
                say(f"Opening {site[0]} Dear")
                webbrowser.open(site[1])

        if "open music" in text_input:
            music_path = "E:/Programing/PythonProjects/JarvisAI/Songs/song.mp3"
            os.startfile(music_path)

        if "the time" in text_input:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"My dear the time is {strfTime}")

        if "open vs code".lower() in text_input.lower():
            path = "E:/Vs Code/Microsoft VS Code/bin/Code.exe"
            os.system(f"open {path}")

