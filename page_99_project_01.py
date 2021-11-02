"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is an equilateral
    triangle.
Solution:

    ....
"""
print("Input lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b == c:
    print("equilateral triangle")
else:
    print("Not equilateral triangle")
