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

name = "john"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

engine.say(" As you head down the dark alleyway the light you saw quickly gets further and further away and you then notice 2 doors.")
time.sleep(a)
engine.say(" 1 on your right side and 1 on your left side. Which door do you choose?")
time.sleep(a)
engine.say("Say Left Side or Say Right Side")
listener = sr.Recognizer()
engine.runAndWait()
print("listening...")



try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if "left side" in command:
            engine.say(" You think just because this path isn't as dark it is safer. But you may be in for a suprise.")
    #YOU NEED TO INITIALIZE THE MICROPHONE IN EVERY IF STATEMENT
    #ALSO NEED ENGINE.RUNANDWAIT() AT THE END OF ALL BLOCKS OF CODE
            time.sleep(a)
            engine.say(" The door opens and you are faced with the brightest light you have ever seen.")
            time.sleep(a)
            engine.say(" As your eyes try to adjust. You feel these drips of something hitting the top of your head. You wipe your head and look into your hands")
            time.sleep(a)
            engine.say(" You see your hands covered in blood. As you shield your eyes and look up you see the ceiling is covered in spikes.")
            time.sleep(3)
            engine.say(" The spikes plunge from the ceiling and impale you.")
            time.sleep(3)
            engine.say(" YOU HAVE MADE A BAD CHOICE {}, CHOOSING TO BE LEAD BY THE LIGHT. THE LIGHT HAS COST YOU YOUR LIFE.".format(name))
            time.sleep(a)
            engine.say("GAME OVER")
            engine.runAndWait()
            city = False



        elif "right side" in command:
            engine.say(" You are headed down a dark path but the reward may be great!!")
            time.sleep(a)
            engine.say(" As the door opens you see a knife and a bow and arrow on the table, you have a feeling you will need one of them but which do you choose.")
            time.sleep(a)
            engine.say("Say Knife or Say Bow and Arrow to choose your weapon: ")
            listener = sr.Recognizer()
            print("listening...")
            engine.runAndWait()
            

            # try:
            #     with sr.Microphone() as source:

            #         voice = listener.listen(source)
            #         command = listener.recognize_google(voice)
            #         command = command.lower()

            if "knife" in command:
                engine.say(" You pick up the knife and notice it already has dried blood on it. Who's blood is this you wonder.")
                time.sleep(a)
                engine.say(" You head further into the dark room and you hear very faintly your name being called. {}........{}..... Please come help me".format(name, name))
                time.sleep(a)
                engine.say("Say voice to head towards the voice or Say room to keep exploring the room: ")
                listener = sr.Recognizer()
                engine.runAndWait()                
                print("listening...")


    #                 if "voice" in command:
    #                     engine.say(" As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beanthe yor feet.")
    #                     time.sleep(a)
    #                     engine.say(" You start to turn to run back down the stair and all of a sudden the stairs open up and you begin to fall into a even darker hole.")
    #                     time.sleep(a)
    #                     engine.say(" You finally land with a hard thud on a dirt floor.")
    #                     time.sleep(a)
    #                     engine.say(" You slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
    #                     time.sleep(a)
    #                     engine.say(" The shadow longes towards you and you remember you have the knife you pull it out.")
    #                     time.sleep(a)
    #                     engine.say(" As the shadow longes towards you to shove the knife out in front of you.")
    #                     time.sleep(a)
    #                     engine.say(" The knife plunges deep into the shadowy figure and at that moment you realize.")
    #                     time.sleep(3)
    #                     engine.say(" You too have been stabbed.")
    #                     time.sleep(a)
    #                     engine.say(" You were killed by the shadowy figure. In the end you chose the wrong weapon for this battle.")
    #                     time.sleep(4)
    #                     engine.say(" YOU HAVE LOST THE GAME")
    #                     time.sleep(a)
    #                     engine.runAndWait()
    #                     city = False

    #                 elif "room" in command:
    #                     engine.say(" You continue to explore the room and you find a key. Hold on to this key. it may prove useful.")
    #                     time.sleep(a)
    #                     engine.say(" You see a door with light coming from the bottom. The door is locked and you remember you have a key.")
    #                     time.sleep(a)
    #                     engine.say(" You try the key and it opens the door.")
    #                     time.sleep(a)
    #                     engine.say(" Once the door opens you find a pot of gold and a note. The note reads: ")
    #                     time.sleep(3)
    #                     engine.say(" You have avoid all dangers within my city. This gold is yours. YOU HAVE WON!!!")
    #                     time.sleep(a)
    #                     engine.say(" YOU HAVE WON THE GAME {}. ".format(name))
    #                     engine.runAndWait()
    #                     city = False

    # else:
    #             print("You picked an invalid option. You have lost the game.")
    #             city = False

            elif "bow and arrow" in command:
                 engine.say(" Once you pick up the bow and arrow you see a note under the equipment on the table.")
                 time.sleep(a)
            #     engine.say(" The note reads: ")
            #     time.sleep(a)
            #     engine.say(" The weapon you have chosen leads us to believe you may be the hero we have been searching for.")
            #     time.sleep(a)
            #     engine.say(" You only have 1 arrow. use it wisely. It just might save your life.")
            #     time.sleep(a)
            #     engine.say(" While scanning the room you hear a voice calling from the distance.")
            #     time.sleep(a)
            #     engine.say("Help...........Help............Help....")
            #     time.sleep(a)
            #     engine.say(" You head towards the sound and you see a stairwell.")
            #     time.sleep(a)
            #     engine.say(" Time to decide. Do you want to head up the stairs or stay and explore.")
            #     time.sleep(a)
            #     engine.say(" Say stairs or Say explore ")
                 listener = sr.Recognizer()
                 engine.runAndWait()
                 print("listening...")                       


    #         if "stairs" in command:
    #             time.sleep(a)
    #             engine.say(" As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beanthe yor feet.")
    #             time.sleep(a)
    #             engine.say(" You start to turn to run back down the stair and all of a sudden the stairs open up and you begin to fall into a even darker hole.")
    #             time.sleep(a)
    #             engine.say(" You finally land with a hard thud on a dirt floor.")
    #             time.sleep(a)
    #             engine.say(" You slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
    #             time.sleep(a)
    #             engine.say(" The shadow longes towards you.")
    #             time.sleep(a)
    #             engine.say(" You fire your only arrow hitting the shadowy figure in the heart.")
    #             time.sleep(a)
    #             engine.say(" As the figure slumps to the floor you see a door behind it. You head to the door and open it.")
    #             time.sleep(a)
    #             engine.say(" There you see a pot of gold and a note that reads: ")
    #             time.sleep(a)
    #             engine.say(" You have killed the Gaurdian of the gold. This gold is yours.")
    #             time.sleep(a)
    #             engine.say(" YOU HAVE WON THE GAME {}. ".format(name))
    #             engine.runAndWait()                            
    #             city = False


    #         elif "explore" in command:
    #             engine.say(" As you continue to explore the room, you start to fell really hot.")
    #             time.sleep(a)
    #             engine.say(" You start to feel as if you skin is burning.")
    #             time.sleep(a)
    #             engine.say(" The room a become so hot that you pass out.")
    #             time.sleep(a)
    #             engine.say(" You have succumb to the heat in the room. ")
    #             time.sleep(a)
    #             engine.say(" You have die.")
    #             engine.say(" YOU LOST THE GAME!!")
    #             engine.runAndWait()                            
    #             city = False



            # except sr.UnknownValueError:
            #     engine.say("I'm sorry I did not get that. Please try again.")
            #     engine.runAndWait()
            #     listener = sr.Recognizer()
            #     print("listening...")
            # except sr.RequestError as e:
            #     engine.say("I'm sorry I did not get that. Please try again.")
            #     engine.runAndWait()
            #     listener = sr.Recognizer()
            #     print("listening...")
except sr.UnknownValueError:
    engine.say("I'm sorry I did not understand you. Please try again.")
    listener = sr.Recognizer()
    engine.runAndWait()
    print("listening...")       
except sr.RequestError as e:
    engine.say("I'm sorry I did not get that. Please try again.")
    listener = sr.Recognizer()
    print("listening...")
    engine.runAndWait()
