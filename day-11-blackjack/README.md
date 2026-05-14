# Day 11: Blackjack

A command-line Blackjack game against an automated computer dealer. The player hits or stands until they bust, stand, or hit 21; the computer then auto-draws to 17. Natural Blackjacks (21 on two cards) are tracked as a special outcome.

## What I learned
- Bottom-up function design (helpers first, then orchestration)
- Modeling game state with lists and tracking aces in scoring
- The 0-for-Blackjack convention for distinguishing natural 21 from regular 21
- Using `while True:` with `break` for loops with multiple exit conditions
- Encoding game outcomes in a single comparison function
- Eliminating dead code by checking which branches can actually fire

## Example
```
[blackjack logo]

Your cards: [10, 5], current score: 15
Computer's first card: 7
Type 'y' to get another card, 'n' to pass: y

Your cards: [10, 5, 6], current score: 21
Computer's first card: 7

Your final hand: [10, 5, 6], final score: 21
Computer's final hand: [7, 4, 9], final score: 20
You win 🎉

Do you want to play another round? Type 'y' or 'n': 
```

## How to run
```bash
python main.py
```