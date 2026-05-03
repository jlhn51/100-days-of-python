"""
Day 4: Rock, Paper, Scissors
A classic Rock, Paper, Scissors game played against a randomized computer opponent.
Concepts: lists, randomization (random modules), indexing, boolean logic
"""

import random

ROCK, PAPER, SCISSORS = 0, 1, 2

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please enter 0, 1 or 2.")

else:
    computer_choice = random.randint(0, 2)

    print(f"You chose:{ascii_art[user_choice]}")
    print(f"Computer chose: {ascii_art[computer_choice]}")
 
    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == PAPER and computer_choice == ROCK) or \
         (user_choice == SCISSORS and computer_choice == PAPER):
        print("You win!")
    else:
        print("You lose.")