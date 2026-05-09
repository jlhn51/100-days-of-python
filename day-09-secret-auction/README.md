# Day 9: Secret Auction

A blind auction program where multiple bidders enter their name and bid privately. The screen clears between bidders so no one sees the others' bids. After all bids are in, the program announces the highest bidder and their winning amount.

## What I learned
- Dictionaries: creating, adding key-value pairs, iterating
- Looping through dictionary entries with `.items()`
- Returning multiple values from a function (tuple unpacking)
- Type hints (`dict[str, int]`, `tuple[str, int]`)
- Cross-platform screen clearing with the `os` module

## Example
```
[auction logo]
Welcome to the Secret Auction Program!

What is your name? Alice
What's your bid? $150
Are there other bidders? Type 'yes' or 'no'.
yes

[screen clears]

What is your name? Bob
What's your bid? $200
Are there other bidders? Type 'yes' or 'no'.
no

[screen clears]

Bob is the winner of the bid with $200.
```

## How to run
```bash
python main.py
```