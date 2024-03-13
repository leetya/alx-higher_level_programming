#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number_status = ["is zero", "is negative", "is positive"]
print(number, number_status[number if number == 0 else 2 if number > 0 else 1])
