"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    tokens = user_input.split()

    # break loop if input is 'q'
    if tokens[0] == "q":
        break

    # check len(tokens) and turn input strings into floats
    if len(tokens) == 2:
        num1 = float(tokens[1])

    elif len(tokens) == 3:
        num1 = float(tokens[1])
        num2 = float(tokens[2])

    else:
        print "That's not a valid input. Please try again."

    # check operator and run associated function
    if tokens[0] == "square":
        print square(num1)

    elif tokens[0] == "cube":
        print cube(num1)

    if tokens[0] == "+":
        print add(num1, num2)

    elif tokens[0] == "-":
        print subtract(num1, num2)

    elif tokens[0] == "*":
        print multiply(num1, num2)

    elif tokens[0] == "/":
        print divide(num1, num2)

    elif tokens[0] == "pow":
        print power(num1, num2)

    elif tokens[0] == "mod":
        print mod(num1, num2)
