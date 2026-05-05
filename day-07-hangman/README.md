# Day 7: Hangman

A classic word-guessing game played in the terminal, with ASCII art for the gallows. The player has 6 lives to guess a randomly chosen word one letter at a time.

## What I learned
- Splitting code across multiple files (`hangman_art.py`, `hangman_words.py`)
- Importing specific names with `from module import name`
- Input validation (length checks, `.isalpha()`)
- Using `continue` to skip the rest of a loop iteration
- Separating constants from mutable state (`STARTING_LIVES` vs. `lives`)
- Building strings with `*` repetition and `.join()`
- Designing the user experience: validation, feedback, polish
- Reading data from a text file with `open()` and `with`
- List comprehensions for building lists from iterables

## Example
```
[hangman logo art here]

Welcome! Try to guess the word before the man hangs.

Lives left: 6/6
Word: _ _ _ _ _ _

Guess a letter: a
Nice! 'a' is in the word.

Lives left: 6/6
Word: _ a _ a _ a
Already guessed: a

Guess a letter: ...
```

## How to run
```bash
python main.py
```