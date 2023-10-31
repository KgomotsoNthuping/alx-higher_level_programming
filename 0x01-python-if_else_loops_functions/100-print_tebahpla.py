#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 == 0:
        b = chr(a)
    else:
        b = chr(a-32)
    print("{}".format(b), end="")
