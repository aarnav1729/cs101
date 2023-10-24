# CSC 101
# 24 October 2023
# Professor Susan Furtney
# Wyatt Bechtle
# L00483947
# Math Study Buddy Game
#-------------------------+
# Pseudocode
#-----------+
# Step 1) Display program explanation
# Step 2) Prompt user for difficulty level
# Step 3) For i in range(5):
#		    Generate question based on diff. level
#		    Calculate solution
#		    Prompt user to answer
#		    If correct:
#			    Display correct
#			    Add one to score
#		    Else:
#			    Display incorrect and answer
# Step 4) Display the user's overall results
# Step 5) Prompt user to play again or exit
#-------------------------------------------------------+
import random

programExplanation = '''\nHello!
This game acts as a personal study buddy for basic arithmetic problem solving.
Simply select the desired difficulty level for each question asked. Then, five 
questions will be generated based on the desired difficulty. The user will only
get one chance to answer correctly, however, the correct answer will be displayed
if answered incorrectly. After the five questions have been answered, the total
score will be displayed.
\nGood Luck!
'''

print(programExplanation, end = '')

difficultyLevelMenu = '''\nDifficulty Level Menu
----------------------
  Easy: 1
Medium: 2
  Hard: 3
'''

possibleDifficultyLevels =['1', '2', '3']

possibleOperators = [' + ', ' - ', ' * ', ' / ']

playerGameScore = 0
playerSessionScore = 0
gameIteration = 0
playAgain = True

while playAgain:

    difficultySelection = '99'

    while not(difficultySelection in possibleDifficultyLevels):
        print(difficultyLevelMenu)
        
        difficultySelection = input('Please Select a Difficulty Level (Ex. 2): ')

        if not(difficultySelection in possibleDifficultyLevels):
            print('\nError: Invalid Input... Please only enter values 1-3')

    for i in range(5):
        if difficultySelection == '1':
            numberOne = random.randint(0,9)
            numberTwo = random.randint(1,9)
            operator = possibleOperators[random.randint(0,(len(possibleOperators) - 1))]
            question = str(numberOne) + operator + str(numberTwo) 
        elif difficultySelection == '2':
            numberOne = random.randint(-9,9)
            numberTwo = random.randint(1,9)
            operator = possibleOperators[random.randint(0,(len(possibleOperators) - 1))]
            question = str(numberOne) + operator + str(numberTwo)
        else:
            numberOne = round(random.uniform(-9,9), 2)
            numberTwo = round(random.uniform(1,9), 2)
            operator = possibleOperators[random.randint(0,(len(possibleOperators) - 1))]
            question = f'{numberOne:.2f}{operator}{numberTwo:.2f}'

        if operator == ' + ':
            answer = numberOne + numberTwo
        elif operator == ' - ':
            answer = numberOne - numberTwo
        elif operator == ' * ':
            answer = numberOne * numberTwo
        else:
            if numberTwo != 0:
                answer = numberOne / numberTwo
            else:
                answer = 1

        answer = round(answer, 2)
        userAnswer = 'zzz'

        while isinstance(userAnswer, str):
            print('\nProvide decimal answers with a maximum of 2 decimal places.')
            print('Perform all decimal rounding as: 1.555 = 1.55; 1.556 = 1.56.')
            userAnswer = input(f'\nPlease Answer question #{i + 1} of 5 (Ex. 4.2):\n{question} = ')

            if userAnswer.replace('-','').isdigit():
                userAnswer = int(userAnswer)
            elif userAnswer.replace('-','').replace('.','').isdigit():
                userAnswer = float(userAnswer)
            else:
                print('\nError: Invalid Input... Please only enter numerical values. Ex: 3; 1; 2.3')

        if userAnswer == answer:
            print('\nCorrect! Adding one to player score...')
            playerGameScore += 1
        else:
            print(f'\nIncorrect... The answer to {question} is {answer:.2f}')

        if i == 4:
            playerSessionScore += playerGameScore
            gameIteration += 1
            divisor = 5 * gameIteration
            print(f'\n   The game score is: {playerGameScore/5:.2%}')
            print(f'The session score is: {playerSessionScore/(5*gameIteration):.2%}')
            playerGameScore = 0
            playAgain = '99'
            playAgainMenu = '''\nPlay Again Menu
-----------------
Yes : 1
 No : 2'''
            while playAgain == '99':
                print(playAgainMenu)
                playAgain = input('Play again (Ex. 1): ')
                if playAgain == '1':
                    playAgain = True
                elif playAgain == '2':
                    playAgain = False
                else:
                    playAgain = '99'
                    print('\nError: Invalid Input... Please only enter 1 to go again or 2 to exit. Ex: 1; 2')
print('\nThanks for Playing!\n')