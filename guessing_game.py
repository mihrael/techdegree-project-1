"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

def guess_function():
    global guess
    guess = input("Guess a number between 1-10  ")
    guess = int(guess)
    if guess < 1 or guess > 10:
        raise ValueError("Your guess has to be a number between 1-10")
attempts = 1

def start_game():
    print("Welcome to the number guessing game!")
    global answer
    answer = random.randint(1, 10)
    while True:
        try:
            guess_function()
            break
        except ValueError as err:
            print("Your guess has to be a number between 1-10")
    global attempts
    while guess != answer:
        if guess == answer:
            break
        elif guess > answer:
            print("It's lower")
            guess_function()
        elif guess < answer:
            print("It's higher")
            guess_function()
        attempts += 1
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

if guess == answer:
    print("You guessed the correct number! It took you {} attempts".format(attempts))
    print("The game is over")
