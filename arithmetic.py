"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two input integers."""
    
    return int(num1 + num2)

def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    
    return int(num1 - num2)

def multiply(num1, num2):
    """Multiply the two inputs together."""
   
    return int(num1 * num2)

def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
   
    return float(num1/num2)

def square(num1):
    """Return the square of the input."""
    
    return int(num1 ** 2)

def cube(num1):
    """Return the cube of the input."""
    
    return int(num1 ** 3)

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    
    return int(num1 ** num2)

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    
    return num1 % num2
