import random
from games.coin_flip import coin_flip
from games.guess_random_number import guess_random_number
from games.mathStudyBuddy import mathStudyBuddy
from games.True_or_False import torf
from games.three_dice import three_dice
from games.heath_game import heath_game
from games.make_cake import make_cake
from games.guess_the_letter import guess_letter
from games.blackjack import blackjack
from games.RockPaperScissors import RockPaperScissors

def main_menu():
    while True:

        print("main menu:")
        print("1. guess the random number- aarnav")
        print("2. math study buddy- wyatt")
        print("3. coin flip- aarnav")
        print("4. blackjack- elisha")
        print("5. true or false- jonathan")
        print("6. three dice game- anna")
        print("7. make your own cake- leon")
        print("8. heath game- layla")
        print("9. guess the letter- cornelius")
        print("10. rock paper scissors- marcus")
        print("0. exit")

        choice = input("which game do you want to play: ")

        if choice == "1":
            guess_random_number()

        elif choice == "2":
            mathStudyBuddy()

        elif choice == "3":
            coin_flip()

        elif choice == "4":
            blackjack()

        elif choice == "5":
            torf()

        elif choice == "6":
            three_dice()

        elif choice == "7":
            heath_game()

        elif choice == "8":
            make_cake()

        elif choice == "9":
            guess_letter()

        elif choice == "10":
            RockPaperScissors()

        elif choice == "0":
            print("goodbye!")

            break

        else:
            print("invalid selection, please try again")

if __name__ == "__main__":
    main_menu()