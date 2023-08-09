#!/usr/bin/python3

for letter_code in range(97, 123):
    letter = chr(letter_code)
    if letter != 'q' and letter != 'e':
        print(letter, end="")
