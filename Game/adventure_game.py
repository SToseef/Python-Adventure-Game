import os, time, winsound, pygame, sys
from time import sleep
from pygame import mixer

# Ctrl H to replace all (ignore shortcut)


## Adding Sound to Game ##
## Footsteps ##
pygame.mixer.init()
footsteps = pygame.mixer.Sound(r'Game\audio\Footsteps.wav')


drawline= print("")

name = input("Type your name: ")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
gender = input("Are you: \n[1] Male \n[2] Female\n ")
if gender == "2":
    gender1 = "her"
    gender2 = "she"
elif gender == "1":
    gender1 = "his"
    gender2 = "he"

weapon = False

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print(">-----------------------------------------------------<")
print("\n   Welcome Commander", name, "to this space adventure! \n")
print(">-----------------------------------------------------<")

time.sleep(6)
os.system('cls' if os.name == 'nt' else 'clear')

print(name, "is on board the Starship Cruiser.\n")
time.sleep(3)
print("The Starship is silent...\n")
time.sleep(3)
print(name, "has just woken up from cyrogenic sleep.\n")
time.sleep(3)
print(gender2, "steps out of the pod...\n")
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)
print("The ship comes to an abrupt stop.\n")
time.sleep(3)

def goback():
    print(name,"heads back...")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    introScene()

def introScene():

        answer = input( "You can check: \n[1] Maintenance \n[2] Navigation \n\n")


        if answer == "1":
            print("\nSlowly,", name, "goes down to maintenance...")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCommander",name, "enters maintenance.\n")
            time.sleep(3)
            print("On the floor is a knife.")
            time.sleep(4)


            answer = input("\nYou can: \n[1] Take the Knife \n[2] Ignore. \n")
                
            if answer == "1":
                print("\nYou took the Knife\n")
                weapon = True
                time.sleep(4)
                goback()
            else:
                goback()

        elif answer == "2":
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n"+ name, "goes to navigation...")
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(gender1, "feet tap against the cold floor...\n")
            footsteps.play()
            time.sleep(4)

            bridge = input("You come to a bridge. You can go: \n[1] Go back \n[2] Walk across \n")
            
            if bridge == "1":
                goback()

            elif bridge == "2":
                print("\nCommander", name, "walked through the bridge...")
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Not valid. You Lose.")
            introScene()

def Strangerscene():
    answer = input("You meet a stranger, you can: \n[1] Talk to him \n[2] Ignore him \n\n")
                
    if answer == "1":
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + name, "decided to talked to him.")
        time.sleep(3)
        print("\nThe Stranger looks at", name + "...")
        time.sleep(5)

        answer = input("\nWhat would you like to say to him? \n1.[Why are you here?] \n2.[Who are you?] \n")
                
        if answer == "1":
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCommander", name,"asks the stranger why he is here.\n")
            time.sleep(4)
            print("He replies, he is lost...\n")
            time.sleep(3)
            print("Suddenly, he grabs hold of", name)

            answer = input("\nHow do you proceed? \n1.[Fight back] \n2.[Step back] \n\n")
                
            if answer == "1": 

                            if weapon == False: # If player didn't pick up weapon 
                                time.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("\n"+ name,"tries to fights back.\n")
                                time.sleep(3)
                                print("The stranger is too strong...\n")
                                time.sleep(4)
                                print("You Lost!\n")

                            elif weapon: # If player did pick up weapon 
                                print(name, "attacks the stranger with the weapon.")
                                time.sleep(3)
                                print("The stranger has fled...")

            elif answer == "2":
                            print("\n You avoided danger... \n")
                            time.sleep(3)
                            print("You Won!\n")
            
            else:
                     print("Not valid. You Lose.")

introScene()
Strangerscene()

pygame.quit()