"""
Author: Nguyen Van Hoang
Date: 16/10/2021
Problem:The twentieth-century Dutch artist Piet Mondrian developed a style of abstract
painting that exhibited simple recursive patterns. To generate such a pattern
with a computer, one would begin with a filled rectangle in a random color and
then repeatedly fill two unequal subdivisions with random colors, as shown in
Figure 7-16.
As you can see, the algorithm continues the process of subdivision until an “aesthetically right moment”
is reached. In this version, the algorithm divides the current rectangle into portions representing
1/3 and 2/3 of its area and alternates these subdivisions along the horizontal and vertical axes.
Design, implement, and test a script that uses a recursive function to draw these patterns.
Solution:
    ....
"""
import random
from turtle import Turtle
from time import sleep

def fillRectangle(t, x1, y1, x2, y2):
    """Fills a rectangle with the given corner points
    using a random color."""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(t, x1, y1, x2, y2, level):
    """Draws a Mondrian-like painting at the given level."""
    if level > 0:
        fillRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)

        if vertical == 1:  # Vertical split
            mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                     level - 1)
            mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2,
                     level - 1)

        else:  # Horizontal split

            mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1,
                     level - 1)
            mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2,
                     level - 1)

def main():
    level = int(input("Enter the level: "))
    t = Turtle()
    t.hideturtle()
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    mondrian(t, -width, height,
             width, -height, level)
    sleep(5)

main()

