#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg_len) if (arg_len) > 1
              else "{} argument:".format(arg_len))
        for i, x in enumerate(argv):
            if i != 0:
                print("{}: {}".format(i, x))
