"""
Author: Nguyen Van Hoang
Date: 16/10/2021
Problem:The Koch snowflake is a fractal shape. At level 0, the shape is an equilateral triangle.
At level 1, each line segment is split into four equal parts, producing an equilateral bump in the middle
of each segment. Figure 7-15 shows these shapes at levels 0, 1, and 2.
At the top level, the script uses a function drawFractalLine to draw three fractal lines. Each line is
specified by a given distance, direction (angle), and level. The initial angles are 0, 2120, and 120
degrees. The initial distance can be any size, such as 200 pixels. The function drawFractalLine is
recursive. If the level is 0, then the turtle moves the given distance in the given direction. Otherwise,
the function draws four fractal lines with one-third of the given distance, angles that produce the given
effect, and the given level minus 1. Write a script that draws the Koch snowflake.
Solution:
    ....
"""
from time import sleep
from turtle import Turtle


def drawKochFractal(width, height, size, level):
    """Draws a Koch fractal of the given level and size."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)


def drawFractalLine(t, distance, theta, level):
    """Either draws a single line in a given direction
    or four fractal lines in new directions."""
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)


def drawPolarLine(t, distance, theta):
    """Moves the given distance in the given direction."""
    t.setheading(theta)
    t.forward(distance)


if __name__ == '__main__':
    level = int(input("Enter the level: "))
    drawKochFractal(200, 200, 150, level)
    sleep(5)