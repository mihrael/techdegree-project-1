"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

def game_controller():
    answer = random.randint(1, 10)
    global attempts
    attempts = 1
    wrong = True
    while wrong:
        guess = guess_function()
        if guess == answer:
            wrong = False
        else:
            print ("It's lower") if guess > answer else print("It's higher")
            attempts += 1
    if guess == answer:
        print("You guessed the correct number! It took you {} attempts".format(attempts))


def guess_function():
    number = True
    while number:
        try:
            guess = int(input("Guess a number between 1-10  "))
            if guess < 1 or guess > 10:
                raise ValueError("Your guess has to be a number between 1-10")
            else:
                number = False
        except ValueError as err:
            print("Your guess has to be a number between 1-10")
    return(guess)

def check_highscore(score):
    if highscore == 0:
        highscore = score



def start_game():
    high_score = 0
    play = True
    print("Welcome to the number guessing game!")
    while play:
        game_controller()

        if high_score == 0:
            high_score = attempts
        elif attempts < high_score:
            high_score = attempts
        print("The highscore is {}".format(high_score))

        play_again = input("Would you like to play again? [Yes/No]  ")

        try:
            if play_again.lower() not in ("yes","no"):
                raise ValueError("Your answer has to be either 'Yes' or 'No'")
            elif play_again.lower() == "no":
                play = False
        except ValueError as err:
            print("Your answer has to be either 'Yes' or 'No'")

    print("The game is over")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
