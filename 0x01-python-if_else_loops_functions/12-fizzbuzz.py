#!/usr/bin/python3

def fizzbuzz():
    for x in range(1, 101):
        print(x if x % 3 and x % 5 else
              "FizzBuzz" if not x % 3 and not x % 5
              else "Buzz" if not x % 5 else "Fizz", end=' ')
