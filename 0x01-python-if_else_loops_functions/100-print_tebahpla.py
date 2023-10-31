#!/usr/bin/python3
order = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - order)), end="")
    order = 32 if order == 0 else 0
