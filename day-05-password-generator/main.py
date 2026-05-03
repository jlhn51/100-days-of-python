"""
Day 5: PyPassword Generator
Generates a random password with user-specified count of letters, numbers, and symbols.
The result is shuffled so the character types are not in predictable order.
Concepts: for loops, lists, random module (choice, shuffle), string joining.
"""

import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


password_lst = []

for _ in range(nr_letters):
    password_lst.append(random.choice(letters))

for _ in range(nr_numbers):
    password_lst.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_lst.append(random.choice(symbols))

random.shuffle(password_lst)
password = "".join(password_lst)

print(f"Your password is: {password}")