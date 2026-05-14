"""Day 11: Blackjack - A command-line Blackjack game with auto-playing computer dealer and Ace handling."""

import os
import random
from art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card() -> int:
    """Return one random card."""
    return random.choice(CARDS)


def calculate_score(cards: list[int]) -> int:
    """Return the score of a list of cards. Returns 0 for a natural blackjack."""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    score = sum(cards)
    ace_count = sum(1 for card in cards if card == 11)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score
    

def compare_score(user_score: int, computer_score: int) -> str:
    """Return a result string based on user and computer scores."""
    if user_score == computer_score:
        return "It's a draw ⚖️"
    elif computer_score == 0:
        return "You lose — opponent has Blackjack 💀"
    elif user_score == 0:
        return "You win with Blackjack 🎉"
    elif user_score > 21:
        return "You bust — you lose 💀"
    elif computer_score > 21:
        return "Opponent busts — you win 🎉"
    elif user_score > computer_score:
        return "You win 🎉"
    return "You lose 💀"


def play_game():
    """Orchestrate one full round of blackjack"""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card()]
    computer_score = calculate_score(computer_cards)

    while True:
        user_score = calculate_score(user_cards)

        # show state
        print()
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # decide whether to keep playing
        if user_score == 0 or user_score >= 21:
            break  # someone has blackjack or user busted - round is over

        choice = input("Type 'y' to get another card, 'n' to pass: ")
        if choice == 'y':
            user_cards.append(deal_card())
        else:
            break  # user stands
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

play_round = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

if play_round == 'y':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        play_game()
        print()
        again = input("Do you want to play another round? Type 'y' or 'n': ")
        if again != 'y':
            break