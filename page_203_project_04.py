"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:Restructure Newton’s method (Case Study 3.6) by decomposing it into three
cooperating functions. The newton function can use either the recursive strategy
of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
limit is assigned to a function named limitReached, whereas the task of computing a new
approximation is assigned to a function named improveEstimate. Each
function expects the relevant arguments and returns an appropriate value.
Solution:
    ....
"""
TOLERANCE = 0.000001


def newton(x, estimate=1):
    if limitReached(x, estimate):
        return estimate
    else:
        return newton(x, improveEstimate(x, estimate))


def limitReached(x, estimate):
    difference = abs(x - estimate ** 2)
    return difference <= TOLERANCE


def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2


def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program is estimate is", newton(x))