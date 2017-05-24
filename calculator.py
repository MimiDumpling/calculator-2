"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if tokens[0] == "q":
        break

    elif tokens[0] == "+":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print add(num1, num2)

    elif tokens[0] == "-":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print subtract(num1, num2)

    elif tokens[0] == "*":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print multiply(num1, num2)

    elif tokens[0] == "/":
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print divide(num1, num2)

    elif tokens[0] == "square":
        num1 = int(tokens[1])
        print square(num1)

    elif tokens[0] == "cube":
        num1 = int(tokens[1])
        print cube(num1)

    elif tokens[0] == "pow":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print power(num1, num2)

    elif tokens[0] == "mod":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print mod(num1, num2)
