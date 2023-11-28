#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert the character to uppercase using ASCII values
        upper_char = chr(ord(char) - ord('a') + ord('A')) \
            if 'a' <= char <= 'z' else char
        print(upper_char, end='')
    print()
