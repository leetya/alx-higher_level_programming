#!/usr/bin/python3

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return (True)
    return (False)


def uppercase(str):
    for x in str:
        if x != len(str):
            print("{0}".format(x) if not islower(x)
                  else "{0}".format(chr(ord(x) - 32)), end='')
    print("")
