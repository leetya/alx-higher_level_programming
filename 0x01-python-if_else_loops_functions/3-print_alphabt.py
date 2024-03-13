#!/usr/bin/python3

for x in range(97, 123):
    print("{0}".format(chr(x)) if x != 101 and x != 113 else "", end="")
