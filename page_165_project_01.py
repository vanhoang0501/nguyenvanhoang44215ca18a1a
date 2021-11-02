"""
Author: Nguyen Van Hoang
Date: 11/10/2021
Problem:Write a loop that accumulates the sum of the numbers in a list named data
Solution:
    ....
"""
import statistics
print("//////Enter set of numbers//////")
print("/////To stop entering number enter */////")
var = True
number_list = []
while (var == True):
    num = input("Enter number : ")
    if (num == '*'):
        var = False
        break
    else:
        num = int(num)
        number_list.append(num)
print("/////your input LIST is :")
print(number_list)
print()
def median(number_list):
    length = len(number_list)
    if ((length % 2) == 0):
        first = number_list[int((length / 2)) - 1]
        second = number_list[int(length / 2)]
        i = (first + second) / 2
        return i
    else:
        return number_list[length // 2]
def mode(number_list):
    return statistics.mode(number_list)
def mean(number_list):
    return statistics.mean(number_list)
print("Median of the given list is:", median(number_list))
print()
print("Median of the given list is:", mean(number_list))
print()
print("Median of the given list is:", mode(number_list))