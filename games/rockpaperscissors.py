#Levi Bechtle
#CSC 101 
#Created game
#Rock, Paper, Scissors
#------------------------------------------------------------------
#Step 1)Import random
#Step 2)Display program explenation
#Step 3)While gamesplayed < 3
#Step 4)    Get user input
#Step 5)    Get random choice from the computer
#Step 6)    print resaults
#Step 7)     If user-rock > scissors, scissors > paper, paper > rock
#               print you are winning and score
#               add 1 to both gamesplayed and user userwin
#Step 8)     Elif computer-rock > scissors, scissors > paper, paper > rock
#               print you are lossing and score
#               add 1 to both gamesplayed and user computerwin
#Step 9)     Else 
#               print Its a tie
#Step 10)If gamesplayed is equel to 3 and userwin is equal to 2
#           print Thank you for playing you have won
#Step 11)Elif gamesplayed is equel to 3 and computerwin is equal to 2
#           print Thank you for playing you have lost
#------------------------------------------------------------------
# rock > scissors, scissors > paper, paper > rock
import random 

print("\nHello Folks") 
print("This program will play a best out of 3 game of rock, paper, scissors with a user.")  

gamesplayed = 0 
userwin = 0 
computerwin = 0  

while gamesplayed < 3 and userwin < 2 and computerwin < 2:  
        user = input("\nWhat's your pick? 'rock', 'paper', 'scissors'?\nPick: ") 

        if user == 'paper' or user == 'rock' or user == 'scissors':
            computer = random.choice(['rock', 'paper', 'scissors'])  
            print('You have picked', user, 'The computer picked', computer) 

        else:
            print("Sorry, that input was invalid please enter 'rock', 'paper', or 'scissors'.")
            continue

        if (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper') \
        or (user == 'rock' and computer == 'scissors'): 
            gamesplayed += 1 
            userwin += 1 
            print('You have won! You have', userwin, 'wins and the computer has', computerwin) 

        elif (computer == 'paper' and user == 'rock') or (computer == 'scissors' and user == 'paper') \
        or (computer == 'rock' and user == 'scissors'): 
            gamesplayed += 1 
            computerwin += 1 
            print('You have lost! You have', userwin, 'wins and the computer has', computerwin) 

        else: 
             print('It\'s a tie!') 

if gamesplayed == 3 and userwin == 2 or gamesplayed == 2 and userwin == 2: 
     print('\nThank you for playing you have won the game!') 

elif gamesplayed == 3 and computerwin == 2 or gamesplayed == 2 and computerwin == 2: 
     print('\nThank you for playing you have lost the game.') 