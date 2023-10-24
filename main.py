import random
from games.coin_flip import coin_flip
from games.dice_roll import dice_roll
from games.guess_random_number import guess_random_number

def main_menu():
    while True:

        print("main menu:")
        print("1. guess the random number- Aarnav")
        print("2. guess the random number- Susan")
        print("3. coin flip- Aarnav")
        print("4. dice roll- Susan")
        print("0. exit")

        choice = input("which game do you want to play: ")

        if choice == "1":
            guess_random_number()

        elif choice == "2":
            mathStudy()

        elif choice == "3":
            coin_flip()

        elif choice == "4":
            dice_roll()

        elif choice == "0":
            print("goodbye!")

            break

        else:
            print("invalid selection, please try again")

if __name__ == "__main__":
    main_menu()
