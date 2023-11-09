print("Guess which color of the rainbow the computer has generated in 3 tries")
import random
roygbiv = ["red", "orange","yellow","green","blue","indigo","violet"]
print("the colors of the rainbow are red, orange, yellow, blue, green, indigo, and violet")
answer=(random.choice(roygbiv))
print("Letter count: ", len(answer))

guess=input("Enter your guess: ")
for i in range(2):
    if guess == answer:
        break
    else:
        print("Please try again")
        guess=input("Enter your guess: ")

if guess==answer:
    print("Congratulations, you guessed correctly!")
else:
    print("Sorry, you are out of turns. The answer was:",answer) 
    print("Play again.")

    print("Sorry, you are out of turns. Play again.")