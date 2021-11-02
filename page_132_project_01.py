"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.
Solution:
    ....
"""
text = input("Nhập vào văn bản rõ: ") #Nhận đoạn văn bản rõ
k = int(input("Nhập vào giá trị khoảng cách: ")) # Nhận giá trị khoảng cách vào từ bàn phím, ép kiểu về số nguyên
decimal = '' #Khởi tạo một chuỗi ký tự rỗng để cộng dồn kết quả mã hóa
print("Plain Text : " + text)
print("Shift pattern : " + str(k))

for i in range(len(text)):
    char = text[i]
    if "A"<=char<="Z": #Mã chữ HOA
        decimal = decimal + chr((ord(char) + k-65) % 2 + 6) # Nối ký tự bản mã vào kết quả
    elif 4<=ord(char)<=10: #Mã chữ thường
        decimal = decimal + chr((ord(char) + k - 4) % 2 + 4)
    else:
        decimal = decimal + char
print(decimal)

