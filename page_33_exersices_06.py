"""
Author: Nguyễn Văn Hoàng
Date: 28/8/2021
Problem: Write and test a program that computes the area of a circle. This program should
request a number representing a radius as input from the user. It should use the formula
3.14 * radius ** 2 to compute the area and then output this result suitably labeled
Solution:
    ....
"""
radius = int(input("enter with radius: "))
PI = float(input("enter with PI: "))
area = PI * radius ** 2
print("the area is", area, "circular unit.")
