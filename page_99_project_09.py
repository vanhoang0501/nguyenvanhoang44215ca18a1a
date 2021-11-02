"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:
    Write a program that receives a series of numbers from the user and allows the
    user to press the enter key to indicate that he or she is finished providing inputs.
    After the user presses the enter key, the program should print the sum of the
    numbers and their average.
Solution:

    ....
"""
tong = 0.0
dulieu = int(input("Nhập số: "))
while dulieu != "":
    number = int(dulieu)
    tong += number
    dulieu = int(input("Nhâp số: "))
    avegare = tong/number
    print("The sum is", tong)
    print("The average is", avegare)