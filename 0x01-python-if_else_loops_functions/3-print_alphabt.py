#!/usr/bin/python3
output = ""

for letter_lc in range(97, 123):
    if chr(letter_lc) not in ('q', 'e'):
        output += "{}".format(chr(letter_lc))

print(output, end="")
