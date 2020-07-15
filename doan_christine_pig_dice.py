# Programmer: Christine Doan

# Prompt: The game of "pig" with some insert of pig puns.
#
#   The object of the game is to score as many points as possible.
#   You can either roll a die or keep your current total.
#   If you roll a 1, you lose. If you roll any other number, it is
#   added to your current score.
#

import random

# Function where it will ask if you want to roll the die or hold the die.

def get_roll_or_hold():
    validAnswer = False
    while not validAnswer:
        answer = input('R)oll or H)old? ')
        answer = answer.upper()
        if answer == 'R' or answer == 'H':
            validAnswer = True
        else:
            print(input("Not sow if that's the right input. Enter R)oll or H)old. "))
    return answer

# Function asks if you want to play again or not

def play_again():
    validAnswer = False
    while not validAnswer:
        answer = input('The game was sow fun! Play again? (Y/N) > ')
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            validAnswer = True
        else:
            print('Please enter (Y/N).')
    return answer

# The main function where you play the game.
# Programmer's note: I made this function purely out of organizing the program.

def main():
    playing = True
    print ("""Welcome to the game of "pig". I promise it won't be boaring. """)

    total = 0
    rolling = True
    while rolling:
        result = get_roll_or_hold()
        if result == 'R':
            die = random.randint(1, 6)
            print('You rolled a ', die)
            if die == 1:
                print('You lost this round. Sorry.')
                print(total)
                rolling = False
            else:
                total += die
                print('Your current total is ', total)
        else:
            rolling = False
        if result == 'H':
            print('Your current total is ', total, ". Sure looks like a hamful.")

    else:
        playing = play_again()
        if playing == 'N':
            playing = False
            print ('Thanks for playing. That was pen-ty of fun.')
            exit()
        else:
            main()


main()