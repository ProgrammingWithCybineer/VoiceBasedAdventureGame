#change this game from a text based Adventure game into a VOICE based Adventure game
from IPython.display import clear_output
import time
import pyttsx3
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import sys




#need a way for the computer to tell what type of question you are asking
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
engine.say("Welcome To The World Of The Unknown. Say 'exit' at anypoint to leave the journey.")
engine.say("Where would you like to start your journey.")
engine.say("In a City or in a Forest. Say City or Forest") 
engine.runAndWait()
listener = sr.Recognizer()

done = False

while not done:
    print("listening...")
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "city" in command: # need code to jump to city.py and run that file
                #print(command)
                import city
            elif "forest" in command: # need code to jump to forest.py and run that file
                #print(command)
                import forest
            elif "exit" in command: # need to get code to say statement instead of pronting statement
                import exit

    except sr.RequestError as e:
        engine.say("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        engine.say("I'm sorry I did not understand you, please try again")
    


#code can understand all important choices of the game.
#next need to make code read to me text given



# a = 2
# b = 0.2
# c = 0.08



# name = input("Please type your name: ").upper()
# time.sleep(a)
# print("")
# time.sleep(a)
# print("    ********************************************************")
# time.sleep(a)
# print("    |                                                      |")
# time.sleep(a)
# print("    |                     Welcome                          |")
# time.sleep(a)
# print("    |         To The World Of The Unknown",name,"             |")
# time.sleep(a)
# print("    |      Type 'quit' at anypoint to leave the journey    |")
# time.sleep(a)
# print("    |                                                      |")
# time.sleep(a)
# print("    ********************************************************")
# time.sleep(a)
# print("")
 
# time.sleep(a)