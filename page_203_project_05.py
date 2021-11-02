"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.
(Hint: For a list of length 2 or greater, loop through the list and compare pairs of
items, from left to right, and return False if the first item in a pair is greater.)
Solution:
    ....
"""
def isSorted(lyst):
    if len(lyst) == 0:
        return True
    for i in range(len(lyst)-1):
        if lyst[i] > lyst[i+1]:
            return False
        return True


def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))


main()