#!/usr/bin/python3

def islower(c):
    # Check if the character is a lowercase letter
    return 97 <= ord(c) <= 122

# Test cases
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
print(islower('1'))  # False
