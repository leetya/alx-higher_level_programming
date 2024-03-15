#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    res = 0
    for x in argv[1:]:
        res += int(x)
    print(res)
