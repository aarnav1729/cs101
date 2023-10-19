import random

def dice_roll():
    tries_allowed = 3
    try_count = 0
    dice = random.randint(1, 6)

    while try_count < tries_allowed:
        dice_guess = int(input("guess the number between 1 & 6: "))

        if dice_guess == dice:
            print("congratulations, you just won!")
        else:
            print("sorry, you lost, try again")
        
        try_count += 1

    if try_count == tries_allowed:
        print("sorry, you're out of tries, the correct answer was", dice)