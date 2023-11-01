#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10
elif number < 0:
    last_num = number % 10
    if last_num != 0:
        last_num = last_num - 10
string = "Last digit of " + str(number) + " is " + str(last_num)
if last_num > 5:
    print(string + " and is greater than 5")
elif last_num == 0:
    print(string + " and is 0")
else:
    print(string + " and is less than 6 and not 0")
