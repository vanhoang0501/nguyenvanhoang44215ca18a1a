"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:
    Teachers in most school districts are paid on a schedule that provides a salary
    based on their number of years of teaching experience. For example, a beginning
    teacher in the Lexington School District might be paid $30,000 the first year. For
    each year of experience after this first year, up to 10 years, the teacher receives a
    2% increase over the preceding value. Write a program that displays a salary schedule,
     in tabular format, for teachers in a school district. The inputs are the starting
    salary, the percentage increase, and the number of years in the schedule. Each row
    in the schedule should contain the year number and the salary for that year.
Solution:

    ....
"""
salary = float(input("Enter the starting salary: $"))
percent = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))
print("")

print("Year Salary")
print("-------------")

for i in range(1, years + 1):
        print(i, "\t", end="")
        print("%.2f" % salary)
        salary = salary * (1 + percent / 100)
theSum = 0.0

data = input("Enter a number or press Enter to quit: ")

while data != "":

    number = float(data)

    theSum += number

    data = input("Enter a number or press Enter to quit: ")

    avg = theSum/number

    print("The sum is", theSum)

    print("The average is", avg)


