#!/usr/bin/python3

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return (True)
    return (False)


def uppercase(str):
    for x in str[:-1]:
        print("{0}".format(x) if not islower(x)
              else "{0}".format(chr(ord(x) - 32)), end='')
    if str[:-1]:
        print("")
    else:
        print("{0}".format(str[-1:]) if not islower(str[-1:])
              else "{0}".format(chr(ord(str[-1:]) - 32))) 
