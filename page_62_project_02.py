"""
Author: Nguyen Van Hoang
Date: 04/09/2021
Problem:
    You can calculate the surface area of a cube if you know the length of an edge.
    Write a program that takes the length of an edge (an integer) as input and prints
    the cube’s surface area as output.
Solution:
    ....
"""
edge = float(input("Edge Length: "))
area = 6 * edge**2
print("Surface Area: "+str(area))
