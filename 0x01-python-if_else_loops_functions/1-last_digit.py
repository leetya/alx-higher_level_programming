#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
if number < 0:
    negative = number * -1
    last_digit = negative % 10
else:
    last_digit = number % 10
print(f"Last digit of {number} is", last_digit, "end", end=" ")
if last_digit == 0:
    print("is 0")
elif last_digit > 5:
    print("is greater than 5")
else:
    print("is less than 6 and not 0")