"""Day 9: Secret Auction — a blind auction with dictionary-based bid tracking."""

import os
from art import logo

print(logo)
print("Welcome to the Secret Auction Program!")


def highest_bidder(bids: dict[str, int]) -> tuple[str, int]:
    max_bid = 0
    winner = ""
    for key, value in bids.items():
        if value > max_bid:
            max_bid = value
            winner = key

    return winner, max_bid

bids_dict = {}
add_bid = True
while add_bid:
    name = input("What is your name? ").strip().title()
    bid = int(input("What's your bid? $"))
    other_bid = input("Are there other bidders? Type 'yes' or 'no'.\n")

    if other_bid == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')

    bids_dict[name] = bid
    add_bid = (other_bid == 'yes')

os.system('cls' if os.name == 'nt' else 'clear')
bid_winner, highest_bid = highest_bidder(bids_dict)
print(f"{bid_winner} is the winner of the bid with ${highest_bid}.")