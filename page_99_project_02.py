"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is a right triangle.
     Recall from the Pythagorean theorem that in a right triangle, the square of
    one side equals the sum of the squares of the other two sides.
Solution:

    ....
"""
print("Input lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
    print("Right-angled")
else:
    print("Not right-angled")
