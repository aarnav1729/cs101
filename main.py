

# Guessing the number game
print("Guess what number 1-20 the computer is thinking of in 2 tries")


import random
number = random.randint(1, 20)  


if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


for i in range(2):  
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You win! You're a genius")
        break
    else:
        print("You are incorrect!")


if guess != number:
    print("Unfortunately, you are out of turns. Try Again")
