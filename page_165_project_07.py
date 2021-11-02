"""
Author: Nguyen Van Hoang
Date: 11/10/2021
Problem:Write a loop that accumulates the sum of the numbers in a list named data
Solution:
    ....
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words=[];
for line in fh:
    words += line.split()
words.sort()
print("The unique words in  alphabetical order are:")
for word in words:
    if word in lst:
            continue
    else:
            lst.append(word)
            print(word)
