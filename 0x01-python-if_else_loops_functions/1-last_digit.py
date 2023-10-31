#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit

output_message = "Last digit of"
output_message += " " + str(number)
output_message += " is"
output_message += " " + str(digit)
output_message += " and is"

if digit > 5:
    output_message += " greater than 5"
elif digit == 0:
    output_message += " 0"
else:
    output_message += " less than 6 and not 0"

print(output_message)
