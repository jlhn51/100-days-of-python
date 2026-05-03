"""
Day 2: Tip Calculator
Calculates each person's share of a bill including tip.
Concepts: data types, type conversion (int, float), math operators, f-string formatting.
"""

print("Welcome to the Tip Calculator!")
total_bill = float(input("What is the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill * (1 + tip_percent / 100)
bill_per_person = bill_with_tip / num_people

print(f"\nEach person should pay: ${bill_per_person:.2f}")