import random

def coin_flip():
    coin = random.randint(0, 1)

    flip_guess = input("heads or tails: ")

    if flip_guess == "heads" and coin == 0:
        print("congratulations, you just won!")
    elif flip_guess == "tails" and coin == 1:
        print("congratulations, you just won!")
    else:
        print("sorry, you lost")
