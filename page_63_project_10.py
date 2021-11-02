"""
Author: Nguyen Van Hoang
Date: 04/09/2021
Problem:
    An employee’s total weekly pay equals the hourly wage multiplied by the total
    number of regular hours plus any overtime pay. Overtime pay equals the total
    overtime hours multiplied by 1.5 times the hourly wage. Write a program that
    takes as inputs the hourly wage, total regular hours, and total overtime hours and
    displays an employee’s total weekly pay.
Solution:
    ....
"""
wage1Hours = float(input("Enter the wage: "))
RegularHours = float(input("Enter the regular hours: "))
print("regular weekly pay: ", wage1Hours * RegularHours)
OvertimeHours = float(input("Enter the overtime hours: "))
OvertimePay = 1.5 * wage1Hours
print("Total weekly pay: ", wage1Hours * RegularHours + OvertimeHours * OvertimePay)

