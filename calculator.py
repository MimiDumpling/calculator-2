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
    if tokens[0][0].lower() == "q":
        print "This means you want to exit. Goodbye!"
        break


    if len(tokens) == 1 or len(tokens) == 0:
        print "Sorry, that's not enough characters. Please try again."
        
    elif tokens[0] == "square" or tokens[0] == "cube":
        num1 = float(tokens[1])

        if tokens[0] == "square":
            print square(num1)
        else:
            print cube(num1)

    elif len(tokens) < 3:
        print "Sorry, that's not enough characters. Please try again."

    elif len(tokens) >= 3:   
        num1 = float(tokens[1])
        num2 = float(tokens[2]) 
    
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
