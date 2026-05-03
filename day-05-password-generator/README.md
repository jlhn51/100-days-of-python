# Day 5: PyPassword Generator

A command-line password generator that creates a randomized password from a user-specified mix of letters, numbers and symbols. The output is shuffle so character types appear in unpredicable order.

## What I learned
- `for` loops with `range()`
- The `random` module (`random.choice()`, `random.shuffle`)
- The `string` module for character sets
- Building strings from lists with `"".join()`
- Using `_` for intentionally unused loop variables

## Example
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
4
Your password is: 4j!Kd2#Bm9F8z
```

## How to run
```bash
python main.py
```