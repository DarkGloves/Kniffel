###########
# MODULES #
###########
from random import randint
import os
import modules.titles as titles
try:
    from pystyle import Write, Colors
except ModuleNotFoundError:
    input("This script uses the module 'pystyle', press ENTER to download it\n")
    os.system("pip3 install pystyle")
    from pystyle import Write, Colors
##############
# Here we go #
##############
#1: Create Dices
dice1 = randint(1, 6)
dice2 = randint(1, 6)
dice3 = randint(1, 6)
dice4 = randint(1, 6)
dice5 = randint(1, 6)

#2:Define functions
def kniffle():
    if dice1 == dice2 == dice3 == dice4 == dice5:
        clear()
        doc.writelines("YOU WON!!!")
        titles.win()
        quit()
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printdices():
   Write.Print(text = '_______________\n| 1st dice: ' + str(dice1) + " |\n| 2nd dice: " + str(dice2) + " |\n| 3rd dice: " + str(dice3) + " |\n| 4th dice: " + str(dice4) + " |\n| 5th dice: " +  str(dice5) +  " |\n_______________" + "\n\n", color=Colors.white, interval=0.001)

def writetodoc():
        doc.writelines('_______________\n| 1st dice: ' + str(dice1) + " |\n| 2nd dice: " + str(dice2) + " |\n| 3rd dice: " + str(dice3) + " |\n| 4th dice: " + str(dice4) + " |\n| 5th dice: " +  str(dice5) +  " |\n_______________" + "\n\n")

#3: Code
#Starting Screen
titles.Title()
clear()
titles.Howtoplay()
clear()
 #Try to delete the previous result, if exists
try:
    os.remove("kniffel.txt")
except FileNotFoundError:
    pass

#Variables
i=0

#Create document and write result
doc = open("kniffel.txt", "w+")
doc.writelines(str("1st attemp:\n"))
writetodoc()
printdices()
while i != 2:   
    kniffle()
    choice = int(Write.Input("Which dice do you wanna rethrow? (1, 2, 3, 4 or 5)", Colors.purple))
    if choice == 1:
        dice1 = randint(1, 6)
    elif choice == 2:
        dice2 = randint(1, 6)
    elif choice == 3:
        dice3 = randint(1, 6)
    elif choice == 4:
        dice4 = randint(1, 6)
    elif choice == 5:
        dice5 = randint(1, 6)
    
    if i == 0:
        bucle = "2nd"
    else:
        bucle = "3rd"
    
    i = i+1
    clear()
    printdices()
    doc.writelines(str(bucle + " attemp:\n"))
    writetodoc()
clear()
titles.game_over_XD()
doc.writelines("Try again :(")
quit()
