#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    val = 0
    for i in sys.argv:
        val += int(i)
        print("{}".format(val))
