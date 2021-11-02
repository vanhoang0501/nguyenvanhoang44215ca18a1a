"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file.
Solution:

    ....
"""
filename = input("Nhap ten tep:")
outfile = input("Nhap ten tep dau ra:")
try:
    with open(filename, 'r')as f, open(outfile, 'w') as w:
        for line in f:
            w.write(line)
except FileNotFoundError:
    print(filename+"Khong ton tai!")