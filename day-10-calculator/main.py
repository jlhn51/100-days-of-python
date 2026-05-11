"""Day 10: Calculator — a recursive calculator with chained operations."""

from art import logo

def add(n1, n2):
    """Return the sum of n1 and n2"""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference of n1 and n2"""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of n1 and n2"""
    return n1 * n2

def divide(n1, n2):
    """Return the quotient of n1 and n2"""
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    """
    Run an interactive calculator that prompts for numbers and operations.
    
    Continues using the result of each calculation, or restarts on user request.
    """
    print(logo)
    num1 = float(input("What is your first number:  "))
    continue_calc = True

    while continue_calc:
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation:  ")
        num2 = float(input("What's the next number:  "))

        result = operations[op](num1, num2)
        print(f'{num1} {op} {num2} = {result:g}')

        while True:
            calculate = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation:  ").strip().lower()
            if calculate in ('y', 'n'):
                break
            print("Please type 'y' or 'n'.")

        if calculate == 'y':
            num1 = result
        else:
            calculator()
            break

calculator()