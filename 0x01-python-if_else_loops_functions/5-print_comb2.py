#!/usr/bin/python3

for x in range(0, 100):
    if x != 99:
        print("0{0},".format(x) if x < 10 else "{0},".format(x), end=" ")
    else:
        print("{0}".format(x))
