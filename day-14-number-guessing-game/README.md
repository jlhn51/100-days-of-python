# Day 12: Number Guessing Game

A command-line number guessing game where the player tries to guess a randomly chosen number between 1 and 100. Three difficulty levels (easy, medium, hard) determine how many attempts are allowed, and the program gives "too high" or "too low" hints after each guess.

## What I learned
- Module-level constants stored in a dictionary for clean lookup
- Single source of truth: validating input against the same dict that drives game logic
- Separating input validation from game logic
- Returning result strings from functions instead of printing inside them
- Difficulty tuning based on the optimal algorithm (binary search needs 7 guesses for 1–100)

## Example
```
[number-guessing logo]

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100...
Choose a difficulty. Type 'easy', 'medium' or 'hard': medium

You have 7 remaining to guess the number.
Make a guess: 50
Too high. Guess again.

You have 6 remaining to guess the number.
Make a guess: 25
Too low. Guess again.

You have 5 remaining to guess the number.
Make a guess: 37
You got it. The answer was 37
```

## How to run
```bash
python main.py
```