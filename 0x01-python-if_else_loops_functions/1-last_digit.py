#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = number %-10
elif number >= 0:
    last_num = number % 10
if last_num > 5:
    print(f"last digit of{number} is {last_num} and is greater than 5")
elif last digit == 0:
    print(f"last digit of {number}is {last_num}and is 0")
else:
    print(f"last digit of {number} is {last_num} is less than 6 and not 0")
