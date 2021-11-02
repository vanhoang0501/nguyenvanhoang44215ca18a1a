"""
Author: Nguyen Van Hoang
Date: 11/10/2021
Problem:Write a loop that accumulates the sum of the numbers in a list named data
Solution:
    ....
"""
def filefn():
	f = open("test.txt","w+")
	for i in range(10):
		f.Write("This is line %d\r\n" %(i+1))
	f.close()
	fin = open("test.txt","r")
	prt = "y"
	lines=fin.readlines()
	while prt != 'n':
		n = int(input("Enter the line number you want to print: "))
		print(lines[n])
		prt = input("Want to print any other linr? y or n: ")
	fin.close()
if __name__ ==  "__main__":
	filefn()