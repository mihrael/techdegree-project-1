"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random


def start_game():
    print("Welcome to the number guessing game!")
    answer = random.randint(1, 10)
    guess = input("Guess a number between 1-10")
    attempts = 1
    while guess != answer:
        if guess > answer:
            print("It's lower")
            continue
        elif guess < answer:
            print("It's higher")
            continue
        else: input("Guess a new number between 1-10")
        attemps += 1

print("You guessed the correct number! It took you {} attempts".format(attempts))
print("The game is over")
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
