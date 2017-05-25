"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    tokens = user_input.split()  


    if len(tokens) == 0:
        print "Sorry, you need to input characters for the calculator to work. Please try again."

    # break loop if input is 'q'
    elif tokens[0][0].lower() == "q":
        print "This means you want to exit. Goodbye!"
        break

    elif len(tokens) == 1: 
        print "Sorry, that's not enough characters. Please try again."
        continue    

    num1 = float(tokens[1])

    if len(tokens) == 2:
        num2 = float(tokens[2])
        
        if tokens[0] == "square":
            print square(num1)

        elif tokens[0] == "cube":
            print cube(num1)

    elif len(tokens) > 2:
        
        elif tokens[0] == "+":
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
