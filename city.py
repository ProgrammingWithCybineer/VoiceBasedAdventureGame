from IPython.display import clear_output
import time
import pyttsx3
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import sys




a = 2
b = 0.2
c = 0.08
city = True
choices_city = ["alleyway", "paper", "quit"]


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 140)
engine.say(" Welcome to the city of the lost. Here you will discover a deep dark secret and if you are lucky enough you will survive.")
time.sleep(a)
engine.say(" As you start walking down the city street you see a piece of paper on the ground, at the same time you notice a flash coming from a dark alleyway")
time.sleep(a)
engine.say(" Time to decide. Do you want to pick up the paper or head down the alleyway.")
time.sleep(a)
engine.say(" Say alleyway or Say paper ")
    # clear_output()
engine.runAndWait()
listener = sr.Recognizer()
print("listening...")

try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if "alleyway" in command:
            import alleyway


        elif "paper" in command:
            import paper



        elif "quit" in command:
            engine.say(" Thank you starting the journey, we do hope you come back and try again.")
            city = False
            


        elif choices_city not in command:
            engine.say(" That is not a valid choice, please try again. ")
            print("Listening...")



except sr.UnknownValueError:
    engine.say("I'm sorry I did not get that. Please try again.")
    engine.runAndWait()
    listener = sr.Recognizer()
    print("listening...")
except sr.RequestError as e:
    engine.runAndWait()
    listener = sr.Recognizer()
    print("listening...")

