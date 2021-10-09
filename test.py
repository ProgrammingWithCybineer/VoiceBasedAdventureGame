import pyttsx3
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import sys


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)


try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)


except sr.RequestError as e:
    print("Error")

