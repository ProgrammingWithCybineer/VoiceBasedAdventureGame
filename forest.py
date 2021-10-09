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
forest = True
choices_forest = ["night","day", "footprint", "follow","lake", "fairy"]

name = ""

while forest:
        print(" Welcome {}, to the magical mystical forest were nothing is as it seems".format(name))
        time.sleep(a)
        print(" How you got to the forest is unknown and how to leave the forest is even more of a mystery.\n")
        time.sleep(a)
        print(" Time for your first choice of the game weather it is day or night. Be aware the time of day may or maynot affect the creatures you run into")
        time.sleep(a)
        answer = input(" Type 'Day' or Type 'Night' to choose when you entered the forest:\n ").lower()
        clear_output()


        if answer == "day":
            print(" As you walk through the thick lush forest you noticed all the pretty flowers, the lovely smell of a fresh rain.")
            time.sleep(a)
            print(" You also notice what looks to be a weird shaped footprint in the wet dirt.")
            time.sleep(a)
            print(" At the same time you see what you could swear was a fairy fly past you saying you name. {}.... {} follow me!!!!!!".format(name, name))
            time.sleep(a)
            answer = input(" Follow the fairy or examine the footprint. Type fairy or footprint: ")
            clear_output()

            if answer == "fairy":
                print(" You start to follow the fairy and as she flies past the leaves and \n the grass the glitter that follows her starts to turn everything into a brighter color of what it original was.")
                time.sleep(a)
                print(" The colors catch your attention and you notice that her glitter is also revealing a path. You decide to reach out and touch the glitter.")
                time.sleep(a)
                print(" Instantly your fingers begins to burn. You notice a lake to your right and the fairy starts to fly to the left.")
                time.sleep(a)
                print(" Time to decide. Do you head towards the lake to sooth your burning hand and risk losing sight of the fairy or do you continue to follow the fairy and risky what ever may happen to your hand.")
                answer = input(" Type 'Follow' to follow the fairy or Type 'Lake' to head towards the lake: ").lower()

                if answer == "lake":
                 print(" You head towards the lake as fast as you can.")
                 time.sleep(a)
                 print(" You plunge your arm into the glowing water.")
                 time.sleep(a)
                 print(" Instantly your arm stops burning and you see a rope at the bottom of the water")
                 time.sleep(a)
                 print(" You pull at the rope and a hatch opens beneath the dirt behind you. ")
                 time.sleep(a)
                 print(" you walk up to the hatch and see a pot of gold with a note.")
                 time.sleep(a)
                 print(" The note read: ")
                 time.sleep(a)
                 print(" Because you did not let the fairy lead you aware deeper into my forest you can keep this pot of gold.")
                 time.sleep(a)
                 print(" YOU HAVE WON THE GAME.")
                 forest = False
                 break

                elif answer == "follow":
                    print(" Your curiosity has cost you dearly.")
                    time.sleep(a)
                    print(" even though your hand/arm is burning you have chosen to follow the fairy.")
                    time.sleep(a)
                    print(" While following her you didn't realize what was following you until it was to late.")
                    time.sleep(a)
                    print(" As you turn around you see the biggest dragon you could ever imagine.")
                    time.sleep(a)
                    print(" The dragon says to you: ")
                    time.sleep(3)
                    print(".... How dare you follow my fairy into my forest. You have come to far stranger.")
                    time.sleep(a)
                    print(" The dragon then leans in and swallows you in one bite.")
                    time.sleep(a)
                    print(" Due to your curiosity and disregard for your own injury.")
                    time.sleep(3)
                    print(" You Have Died!!! ")
                    print(" YOU HAVE LOST THE GAME!!")
                    print(" GAME OVER")

                    forest = False
                    break
        
            if answer == "footprint":
                print(" While looking at the footprint you fail to notice Goblin that snuck up behind you. ")
                time.sleep(a)
                print(" As you turn around he impales you with the horn protruding from his chest.")
                time.sleep(a)
                print(" You have Died.")
                time.sleep(a)
                print(" YOU HAVE LOST THE GAME.")
                time.sleep(a)
                print(" GAME OVER!!!")

                forest = False
                break

        if answer == "night":
            print(" Why would anyone want to be in a spooky forest at night. ")
            time.sleep(a)
            print(" The first creature you see is a huge dragon.")
            time.sleep(a)
            print(" The dragon blow fire on you.")
            time.sleep(a)
            print(" YOU HAVE DIED.")
            time.sleep(a)
            print(" YOU HAVE LOST THE GAME!!!")
            print(" GAME OVER!!!")
            
            forest = False
            time.sleep(4) 
            break

        
        if answer == "quit":
            print(" Thank you starting the journey {}, we do hope you come back and try again.".format(name))
            forest = False
            break


        elif answer not in choices_forest:
            print(" That is not a choice. You Lose The Game ")
            forest = False
            time.sleep(4) 
            continue


        elif answer == "quit":
            print(" Thank you starting the journey {}, we do hope you come back and try again.".format(name))
            city = False
            forest = False

            time.sleep(4) 