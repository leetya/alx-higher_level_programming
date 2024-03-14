#!/usr/bin/python3

for x in range(9):
    for y in range(x + 1, 10):
        if (x == 8):
            print("{0}{1}".format(x, y))
        else:
            print("{0}{1}, ".format(x, y), end='')
