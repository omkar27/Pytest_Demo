# src/math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def power(a, b):
    return pow(a**b)

def multiply(a, b):
    return a * b
 
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#bug fix
