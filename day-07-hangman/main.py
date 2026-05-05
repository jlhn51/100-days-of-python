"""
Day 7: Hangman
A classic word-guessing game with ASCII art for the gallows.
Concepts: while loops, lists, modules, input validation, multi-file projects
"""

import random
from hangman_art import logo, stages
with open("hangman_words.txt") as file:
    word_list = [line.strip() for line in file]


STARTING_LIVES = 6

print(logo)
print("\nWelcome! Try to guess the word before the man hangs.")

chosen_word = random.choice(word_list)
guessed_letters = []
lives = STARTING_LIVES
game_over = False

while not game_over:
    # Build current display from guessed letters
    display = ""
    for letter in chosen_word:
        display += letter if letter in guessed_letters else "_"

    print(f"\nLives left: {lives}/{STARTING_LIVES}")
    print(f"Word: {' '.join(display)}")
    if guessed_letters:
        print(f"Already guessed: {', '.join(sorted(guessed_letters))}")

    guess = input("\nGuess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a-z).")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
    
    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Nice! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Sorry, no '{guess}' in the word. -1 life.")
        if lives > 0:
            print(stages[lives])

    # Check end conditions
    if lives == 0:
        game_over = True
        print(stages[0])
        print(f"\nYou lost! The word was '{chosen_word}.'")
    elif all(letter in guessed_letters for letter in chosen_word):
        game_over = True
        print(f"\nYou win! 🎉 The word was '{chosen_word}'.")