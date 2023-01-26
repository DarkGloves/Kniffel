from pystyle import Colors, Write, Center
from time import sleep
def Title():
    Write.Print(text = Center.Center("██╗░░██╗███╗░░██╗██╗███████╗███████╗███████╗██╗░░░░░\n██║░██╔╝████╗░██║██║██╔════╝██╔════╝██╔════╝██║░░░░░\n█████═╝░██╔██╗██║██║█████╗░░█████╗░░█████╗░░██║░░░░░\n██╔═██╗░██║╚████║██║██╔══╝░░██╔══╝░░██╔══╝░░██║░░░░░\n██║░╚██╗██║░╚███║██║██║░░░░░██║░░░░░███████╗███████╗\n╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝"), color= Colors.purple_to_blue, interval = 0.000125)
    Write.Input(Center.XCenter("\nPress ENTER to begin: "), Colors.white, interval=0.05)
def Howtoplay():
    Write.Print(text = Center.XCenter("┏┓ ┏┓        ┏━━━━┓  ┏━━━┳┓\n┃┃ ┃┃        ┃┏┓┏┓┃  ┃┏━┓┃┃\n┃┗━┛┣━━┳┓┏┓┏┓┗┛┃┃┣┻━┓┃┗━┛┃┃┏━━┳┓ ┏┓\n┃┏━┓┃┏┓┃┗┛┗┛┃  ┃┃┃┏┓┃┃┏━━┫┃┃┏┓┃┃ ┃┃\n┃┃ ┃┃┗┛┣┓┏┓┏┛  ┃┃┃┗┛┃┃┃  ┃┗┫┏┓┃┗━┛┃\n┗┛ ┗┻━━┛┗┛┗┛   ┗┛┗━━┛┗┛  ┗━┻┛┗┻━┓┏┛\n                              ┏━┛┃\n                              ┗━━┛"), color= Colors.purple_to_blue, interval = 0.000125)

    Write.Print("\n\nYou will see the values of 5 dices. The goal is to get the same number in all the dices. For this, you can re-roll 2 of them. If you get all the dices with the same number, you will win; else, you will fail.\n\n* NOTE: Each time you play a game, the results will be saved in a file called kniffel.txt. This file will be earsed each time you start a new game, so be careful if yoy want to save your results!", Colors.white, interval=0.0125)
    sleep(0.5)
    input("\n\nPress ENTER to start the game")
def game_over_XD():
    Write.Print(text = Center.Center("██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██╗██╗░░░░░███████╗██████╗░  ██╗░░██╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██║██║░░░░░██╔════╝██╔══██╗  ╚═╝░██╔╝\n░╚████╔╝░██║░░██║██║░░░██║  █████╗░░███████║██║██║░░░░░█████╗░░██║░░██║  ░░░██╔╝░\n░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██╔══██║██║██║░░░░░██╔══╝░░██║░░██║  ░░░╚██╗░\n░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░██║░░██║██║███████╗███████╗██████╔╝  ██╗░╚██╗\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═════╝░  ╚═╝░░╚═╝"), color= Colors.red, interval = 0.000125)
    input()
def win():
    Write.Print(text = Center.Center("██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗██╗  ██╗██████╗░\n╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║██║  ╚═╝██╔══██╗\n░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║  ░░░██║░░██║\n░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║╚═╝  ░░░██║░░██║\n░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██╗  ██╗██████╔╝\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═╝  ╚═╝╚═════╝░"), color= Colors.purple_to_blue, interval = 0.000125)
    Write.Print(Center.XCenter("\nYou so lucky!"), Colors.green, interval=0.008)
    input()