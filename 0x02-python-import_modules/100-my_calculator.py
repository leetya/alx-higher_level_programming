#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    operators = ["+", "-", "*", "/"]
    operate_func = [add, sub, mul, div]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    for i, x in enumerate(operators):
        if argv[2] == x:
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
            operate_func[i](int(argv[1]), int(argv[3]))))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
