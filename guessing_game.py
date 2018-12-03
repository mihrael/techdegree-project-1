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

def start_game():
    print("Welcome to the number guessing game!")
    answer = random.randint(1, 10)
    guess_function()
    global attempts
    attempts = 1
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

print("You guessed the correct number! It took you {} attempts".format(attempts))
print("The game is over")
