# Cornelius Thao's game
import random

def guess_letter():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    secret_letter = random.choice(alphabet)

    print("Welcome to Guess the Alphabet Letter!")
    print("I'm thinking of a random letter from A to Z.")

    attempts = 0
    max_attempts = 3
    proceed = 'y'
    while proceed == 'y':
        while attempts < max_attempts:
            guess = input("Enter your guess (a single letter): ").lower()

            if len(guess) != 1 or not guess.isalpha() or guess not in alphabet:
                print("Please enter a valid single letter from A to Z.")
                guess = input("Enter your guess (a single letter): ").lower()

            if guess == secret_letter:
                print(f"Congratulations! You guessed the letter: {secret_letter}")
                proceed = input("Do you want to play again(enter y for yes): ")
            else:
                attempts += 1
                if attempts == 2:
                    if secret_letter in alphabet[:12]:
                        print("Hint: The letter is between 'A' and 'L'.")
                    else:
                        print("Hint: The letter is between 'M' and 'Z'.")
                elif attempts == 3:
                    print(f"Game over! The secret letter was {secret_letter}.")
                    proceed = input("Do you want to play again(enter y for yes): ")
                    if proceed == 'y':
                        main()
                else:
                    print("Try again.")