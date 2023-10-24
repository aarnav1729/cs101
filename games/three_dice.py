#new game

import random

def three_dice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    sumofdice=dice1+dice2+dice3

    print("This is a game that will roll 3 dice and you have to guess the sum")

    help=input("\nWould you like a hint? Y/N ")
    newhelp=help.upper()
    if newhelp== 'Y':
        print("\nDice 1 is a ", dice1)
    else:
        print("Good Luck!")

    guess=100
    numbertried=0
    while guess!=sumofdice and numbertried<2:
        guess=int(input("\nPlease enter your guess of the sum of the dice: "))
        numbertried=numbertried+1
        
        if guess==sumofdice:
            print("\nYou guess it correctly! Good Job")
        else:
            if guess>sumofdice:
                print("\nYour guess is too high")
                print("Try Again")
            else:
                print("\Your guess is too low")
                
    print("\n Dice 1 was a ", dice1)
    print("\n Dice 2 was a ", dice2)
    print("\nDice 3 was a ", dice3)
