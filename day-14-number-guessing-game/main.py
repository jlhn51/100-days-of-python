"""Day 12: Number Guessing Game — guess a number between 1 and 100 with three difficulty levels."""

import random
from art import logo

ATTEMPTS_BY_DIFFICULTY = {'easy': 10, 'medium': 7, 'hard': 5}

def generate_number() -> int:
    """Return a random integer between 1 and 100"""
    return random.randint(1, 100)


def guess_game(difficulty: str) -> str:
    """Play one round of the guessing game and return the result message
    
    The number of allowed attempts depends on the difficulty.
    """
    num_attempts = ATTEMPTS_BY_DIFFICULTY[difficulty]
    secret_number = generate_number()

    while num_attempts > 0:
        print(f"You have {num_attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print()

        while guess < 1 or guess > 100:
            guess = int(input("Please enter a number between 1 and 100: "))

        if guess > secret_number:
            print("Too high. Guess again.")
            num_attempts -= 1
        elif guess < secret_number:
            print("Too low. Guess again.")
            num_attempts -= 1
        else:
            return f"You got it. The answer was {secret_number}"

    return "You've run out of guesses. Restart the game to play again"


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")
level = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ").strip().lower()
while level not in ATTEMPTS_BY_DIFFICULTY:
    level = input("Please type 'easy', 'medium' or 'hard': ").strip().lower()
print(guess_game(level))