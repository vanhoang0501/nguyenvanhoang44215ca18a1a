"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:Write a script that decrypts a message coded by the method used in Project 6.
Solution:

    ....
"""
def bits2String(b = " "):
    return chr(int(b, 2) - 1)
def shift(n = " "):
    temp = list(n)
    new = (temp[-1:] + temp[0:-1])
    ret = " "
    for i in new:
        ret += i
    return ret
coded = input('Enter the coded text:')
process = coded.split()
decoded = " "
for q in process:
    decoded += bits2String(shift(q))
print(decoded)