"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

def game_controller():
    answer = random.randint(1, 10)
    attempts = 0
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
    global guess
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


def start_game():
    play_again = True
    print("Welcome to the number guessing game!")
    while play_again:
        game_controller()
        play_again = input ("Would you like to play again? [Yes/No]  ")
        if play_again.lower == "no":
            play_again = False
    else:
        print("The game is over")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
