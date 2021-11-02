"""
Author: Nguyen Van Hoang
Date: 04/09/2021
Problem:
    Write a program that takes the radius of a sphere (a floating-point number) as
    input and then outputs the sphere’s diameter, circumference, surface area, and
    volume.
Solution:
    ....
"""
radius = float(input("Radius = "))
diameter = radius * 2
circumference = diameter * 3.14
surfaceArea = 4 * 3.14 * radius * radius
volume = 4/3 * 3.14 * radius * radius * radius
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area : ", surfaceArea)
print("Volume ", volume)
