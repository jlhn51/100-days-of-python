"""
Day 8: Caesar Cipher
A command-line Caesar cipher that encodes and decodes messages by 
shifting letters through the alphabet by a user-specified amount.
"""

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(encode_or_decode, original_text, shift_amount):

    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    return output_text


restart = True

while restart:

    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n").strip().lower()
    while direction not in ("encode", "decode"):
        direction = input("Please type 'encode' or 'decode': \n")

    text = input("Type your message: \n").strip().lower()
    shift = int(input("Type the shift number: \n"))

    result = caesar(direction, text, shift)
    print(f"Here is the {direction}d result: {result}")

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    restart = (go_again == 'yes')