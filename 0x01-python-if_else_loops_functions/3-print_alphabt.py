#!/usr/bin/python3
# 3-print_alphabet_no_qe.py

"""Print the alphabet in lowercase, excluding 'q' and 'e', not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print("{}".format(chr(letter)), end="")
