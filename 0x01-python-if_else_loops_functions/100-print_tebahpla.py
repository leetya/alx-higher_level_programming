#!/usr/bin/python3

def convert_and_print():
    for x in range(90, 64, -1):
        print("{0}".format(chr(x)) if x % 2
              else "{0}".format(chr(x + 32)), end='')


convert_and_print()
