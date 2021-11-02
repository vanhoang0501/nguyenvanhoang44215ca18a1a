"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:Convert Newton’s method for approximating square roots in Project 1 to a
recursive function named newton. (Hint: The estimate of the square root should be
passed as a second argument to the function.)
Solution:
    ....
"""
import math

TOLERANCE = 0.000001

def newton(x):
    """Returns the square root of x."""
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate

def main():
    """Allows the user to obtain square roots."""
while True:
    x = input("Enter a positive number or enter/return to quit: ")
    if x == "":
        break
    x = float(x)
    print("The program's estimate is", newton(x))
    print("Python's estimate is ", math.sqrt(x))

if __name__ == "__main__":
    main()