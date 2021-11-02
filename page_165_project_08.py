"""
Author: Nguyen Van Hoang
Date: 11/10/2021
Problem:Write a loop that accumulates the sum of the numbers in a list named data
Solution:
    ....
"""
import re
import string
fre={}
document_text = open('test.txt','r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b [a-z]{1-15} \b',text_string)
for word in match_pattern:
    count = fre.get(word,0)
    fre[word]=count+1
fre_list = fre.keys()
for words in sorted(fre_list):
    print(words,fre[words])