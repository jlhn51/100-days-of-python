"""
Day 1: Band Name Generator
A simple program that generates a band name from user input.
Concepts: print, input, string concatenation, variables, f-strings
"""

print("Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in?\n").strip().title()
pet = input("What's your pet's name?\n").strip().title()
print(f"\nYour Band Name could be {city} {pet}. 🎸")