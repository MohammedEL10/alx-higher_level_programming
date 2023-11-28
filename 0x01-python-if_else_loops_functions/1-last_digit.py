#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number <  0:
    digit = -digit
print(f"last digit of {number:d} is {digit_num}")
if digit > 5:
    print(f"greater than 5")
elif digit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")


