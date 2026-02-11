import math

def square_root(x):
    if x < 0:
        raise ValueError("Negative number not allowed")
    return math.sqrt(x)

def power(a, b):
    return a ** b

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)
