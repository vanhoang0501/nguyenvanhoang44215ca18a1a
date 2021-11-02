"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
Solution:
    ....
"""
from functools import reduce

fileName = input("Enter the input file name: ")
inputFile = open(fileName, 'r')

lyst = []
for line in inputFile:
    lyst.extend(line.split())

lyst = list(map(float, lyst))
print("lyst:",lyst)

sum = reduce(lambda x, y: x + y, lyst)

if len(lyst) == 0:
    average = 0
else:
    average = sum / len(lyst)
print("The average is", average)


