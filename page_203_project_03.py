"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:Elena complains that the recursive newton function in Project 2 includes an extra
argument for the estimate. The function’s users should not have to provide this
value, which is always the same, when they call this function.
Modify the definition of the function so that it uses a keyword argument with the appropriate
default value, and call the function without a second argument to demonstrate
that it solves this problem
Solution:
    ....
"""
import math

TOLERANCE = 0.000001


def newton(x, estimate):
    """Returns the square root of x."""
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)


def main():
    """Allows the user to obtain square roots."""
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton(x, 1))
        print("Python's estimate is ", math.sqrt(x))


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()