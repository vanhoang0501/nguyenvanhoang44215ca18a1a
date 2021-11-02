"""
Author: Nguyen Van Hoang
Date: 16/10/2021
Problem:Darkening an image requires adjusting its pixels toward black as a limit, whereas
lightening an image requires adjusting them toward white as a limit. Because
black is RGB (0, 0, 0) and white is RGB (255, 255, 255), adjusting the three RGB
values of each pixel by the same amount in either direction will have the desired
effect. Of course, the algorithms must avoid exceeding either limit during the
adjustments.
 Lightening and darkening are actually special cases of a process known as color
filtering. A color filter is any RGB triple applied to an entire image. The filtering
algorithm adjusts each pixel by the amounts specified in the triple. For example,
you can increase the amount of red in an image by applying a color filter with a
positive red value and green and blue values of 0. The filter (20, 0, 0) would make
an image’s overall color slightly redder. Alternatively, you can reduce the amount
of red by applying a color filter with a negative red value. Once again, the algorithms must avoid exceeding the limits on the RGB values.
 Develop three algorithms for lightening, darkening, and color filtering as three
related Python functions, lighten, darken, and colorFilter. The first two
functions should expect an image and a positive integer as arguments. The third
function should expect an image and a tuple of integers (the RGB values) as arguments. The following session shows how these functions can be used with the
images image1, image2, and image3, which are initially transparent:
>>> image1 = Image(100, 50)
>>> image2 = Image(100, 50)
>>> image3 = Image(100, 50)
>>> darken(image1, 128)                # Converts to gray
>>> darken(image2, 64)                 # Converts to dark gray
>>> colorFilter(image3, (255, 0, 0))   # Converts to red
 Note that the function colorFilter should do most of the work
Solution:

    ....
"""
from images import Image


def colorFilter(image, rgbTriple):
    """Adds the given rgb values to each pixel after normalizing."""

    def baseValue(value, offset):
        """Normalizes value so that 0 <= value <= 255."""
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = baseValue(r, rgbTriple[0])
            g = baseValue(g, rgbTriple[1])
            b = baseValue(b, rgbTriple[2])
            image.setPixel(x, y, (r, g, b))


def lighten(image, amount):
    """Lightens image by amount."""
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    """Darkens image by amount."""
    colorFilter(image, (-amount, -amount, -amount))


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image")
    image.draw()
    lighten(image, 20)
    # darken(image, 20)
    image.draw()

main()
"""
solution: This module supports simple image processing.  The Image class represents
either an image loaded from a GIF file or a blank image.  To instantiate
an image from a file, enter

image = Image(aGifFileName)                   

To instantiate a blank image, enter

image = Image(aWidth, aHeight)

Image methods:

draw()                          Displays the image in a window 
getWidth()  -> anInt            The width in pixels
getHeight() -> anInt            The height in pixels
getPixel(x, y)  -> (r, g, b)    The RGB values of pixel at x, y
setPixel(x, y, (r, g, b))       Resets pixel at x, y to (r, g, b)
save()                          Saves the image to the current file name
save(aFileName)                 Saves the image to fileName

"""
import os
import os.path

import tkinter

tk = tkinter

##########################################################################
# Module Exceptions

_root = None


class ImageView(tk.Canvas):
    def __init__(self, image,
                 title="New Image",
                 autoflush=False):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master,
                           width=image.getWidth(),
                           height=image.getHeight())
        self.master.title(title)
        self.pack()
        master.resizable(0, 0)
        self.image = image
        self.height = image.getHeight()
        self.width = image.getWidth()
        self.autoflush = autoflush
        self.closed = False

    def close(self):
        """Close the window"""
        self.closed = True
        self.master.destroy()
        self.image.canvas = None
        _root.quit()

    def isClosed(self):
        return self.closed

    def getHeight(self):
        """Return the height of the window"""
        return self.height

    def getWidth(self):
        """Return the width of the window"""
        return self.width


class Image:

    def __init__(self, *args):
        self.canvas = None
        if len(args) == 1:
            name = args[0]
            if type(name) != str:
                raise Exception('Must be a file name')
            if name[-4:].upper() != '.GIF':
                raise Exception('File must be a GIF')
            if not os.path.exists(args[0]):
                raise Exception('File not in current directory')
            self.image = tk.PhotoImage(file=args[0], master=_root)
            self.filename = args[0]
            self.width = self.image.width()
            self.height = self.image.height()
        else:  # arguments are width and height
            self.width, self.height = args
            self.image = tk.PhotoImage(master=_root,
                                       width=self.width,
                                       height=self.height)
            self.filename = ""

    def getWidth(self):
        """Returns the width of the image in pixels"""
        return self.width

    def getHeight(self):
        """Returns the height of the image in pixels"""
        return self.height

    def getPixel(self, x, y):
        """Returns a tuple (r,g,b) with the RGB color values for pixel (x,y)
        r,g,b are in range(256)

        """
        value = self.image.get(x, y)
        print("value:", value)
        if type(value) == int:
            return (value, value, value)
        else:
            return value

    def setPixel(self, x, y, color):
        """Sets pixel (x,y) to the color given by RGB values r, g, and b.
        r,g,b should be in range(256)

        """
        self.image.put("{#%02x%02x%02x}" % color, (x, y))

    def draw(self):
        """Creates and opens a window on an image.
        The user must close the window to return control to
        the caller."""
        if not self.canvas:
            self.canvas = ImageView(self,
                                    self.filename)
        self.canvas.create_image(self.width / 2,
                                 self.height / 2,
                                 image=self.image)
        _root.mainloop()

    def save(self, filename=""):
        """Saves the image to filename.  If no file name
        is provided, uses the image's file name if there
        is one; otherwise, simply returns.
        If the .gif extension is not present, it is added.
        """
        if filename == "":
            return
        else:
            self.filename = filename
        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        if ext != "gif":
            filename += ".gif"
            self.filename = filename
        self.image.write(self.filename, format="gif")

    def clone(self):
        new = Image(self.width, self.height)
        new.image = self.image.copy()
        return new

    def __str__(self):
        rep = ""
        if self.filename:
            rep += ("File name: " + self.filename + "\n")
        rep += ("Width:  " + str(self.width) + \
                "\nHeight: " + str(self.height))
        return rep


_root = tk.Tk()
_root.withdraw()