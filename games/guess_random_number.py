import random

def guess_random_number():
    random_number = random.randint(-7, 7)

    tries_allowed = 4
    try_count = 0

    while try_count < tries_allowed:
        if random_number < 0:
            print("the number is negative")
        elif random_number > 0:
            print("the number is positive")
        else:
            print("the number is neither positive nor negative")
        
        if random_number % 2 == 0:
            print("the number is even")
        else:
            print("the number is odd")

        user_guess = int(input("guess the number between -7 & 7: "))

        if user_guess == random_number:
            print("congratulations, you just won!")
            break
        else:
            diff = abs(random_number - user_guess)
            print("you were off by", diff, "try again")
        
        try_count += 1 

    if try_count == tries_allowed:
        print("sorry, you're out of tries, the correct answer was", random_number)