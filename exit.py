import pyttsx3
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import sys

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Thank you for starting the Journey. We are sorry to see you go. Come back soon")
engine.runAndWait()
