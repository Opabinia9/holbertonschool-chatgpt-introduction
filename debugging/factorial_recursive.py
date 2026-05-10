#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Recursively computes the factorial by multiplying the number by the factorial
    of the number minus one, until reaching the base case of 0.
    
    Parameters:
        n (int): A non-negative integer for which the factorial is calculated.
    
    Returns:
        int: The factorial of n (n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command-line arguments and calculate factorial
f = factorial(int(sys.argv[1]))
print(f)

