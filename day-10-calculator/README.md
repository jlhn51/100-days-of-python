# Day 10: Calculator

A command-line calculator that performs addition, subtraction, multiplication, and division. After each calculation, the user can continue chaining operations on the result or restart with a fresh calculation.

## What I learned
- Storing functions as dictionary values for clean dispatch
- Looking up and calling functions by key (`operations[op](a, b)`)
- Recursion: a function that calls itself to "restart"
- Writing docstrings following PEP 257 conventions
- Input validation with a `while` loop

## Example
```
[calculator logo]
What is your first number:  10
+
-
*
/
Pick an operation:  +
What's the next number:  5
10.0 + 5.0 = 15.0
Type 'y' to continue with 15.0, or 'n' to start a new calculation:  y
Pick an operation:  *
What's the next number:  2
15.0 * 2.0 = 30.0
```

## How to run
```bash
python main.py
```