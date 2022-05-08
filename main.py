import random

def whoWins(choiceOne,choiceTwo):
    if choiceOne == 'rock':
        if choiceTwo == 'rock':
            return 0
        elif choiceTwo == 'paper':
            return 2
        elif choiceTwo == 'scissors':
            return 1
    elif choiceOne == 'paper':
        if choiceTwo == 'rock':
            return 1
        elif choiceTwo == 'paper':
            return 0
        elif choiceTwo == 'scissors':
            return 2
    elif choiceOne == 'scissors':
        if choiceTwo == 'rock':
            return 2
        elif choiceTwo == 'paper':
            return 1
        elif choiceTwo == 'scissors':
            return 0

choices = ['rock','paper', 'scissors']

play = True

while play == True:

    aiChoice = random.choice(choices)
    playerChoice = input('Choose:\nrock\npaper\nscissors\n')

    if not playerChoice in choices:
        print('Incorrect Input, Try Again!')
        continue

    if whoWins(aiChoice,playerChoice) == 0:
        print(f"The Computer Chose: {aiChoice}\nYou Chose: {playerChoice}\nTIE!")
        continue
    elif whoWins(aiChoice,playerChoice) == 1:
        print(f"The Computer Chose: {aiChoice}\nYou Chose: {playerChoice}\nCOMPUTER WINS")
    elif whoWins(aiChoice,playerChoice) == 2:
        print(f"The Computer Chose: {aiChoice}\nYou Chose: {playerChoice}\nPLAYER WINS")

    playAgain = input("Play again? y/n\n")
    if playAgain == 'n':
        play = False

print("Bye, Thanks for Playing!")