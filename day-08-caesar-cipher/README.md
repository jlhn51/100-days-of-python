# Day 8: Caesar Cipher

A command-line encryption tool that encodes or decodes messages by shifting each letter through the alphabet by a user-specified amount. Non-letter characters (spaces, numbers, symbols) pass through unchanged.

## What I learned
- Defining functions with multiple parameters
- Returning values from functions instead of printing inside them
- Using the modulo operator (`%`) to wrap around the end of a list
- Input validation with a `while` loop
- Looping a program until the user chooses to stop

## Example
```
Type 'encode' to encrypt, 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 5
Here is the encoded result: mjqqt btwqi
Type 'yes' if you want to go again. Otherwise, type 'no'.
```

## How to run
```bash
python main.py
```