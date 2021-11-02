"""
Author: Nguyen Van Hoang
Date: 25/10/2021
Problem:Write a recursive function that expects a pathname as an argument. The pathname can be either the name of
 a file or the name of a directory. If the pathname
refers to a file, its name is displayed, followed by its contents. Otherwise, if the
pathname refers to a directory, the function is applied to each name in the directory. Test this function in a new
program.
Solution:
    ....
"""
import os
import os.path


def displayFiles(path):
 """visits all of the files and directories in path and displays the files' contents."""
 if os.path.isfile(path):
     print("File name:"+path)
     f = open(path,'r')
     print(f.read())
 else:
     print("Directory name:"+path)
     lyst = os.listdir(path)
     for element in lyst:
         recursive_element = os.path.join(path,element)
         print("element:",element)
         print("recursive_element",recursive_element)
         displayFiles(recursive_element)
if __name__ == '__main__':
    print(f"Directory:{os.getcwd()}")
    displayFiles(os.getcwd())
