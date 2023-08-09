#!/usr/bin/python3
# 2-printalphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
for letter_code in range(97, 123):
    print(chr(letter_code), end="")
