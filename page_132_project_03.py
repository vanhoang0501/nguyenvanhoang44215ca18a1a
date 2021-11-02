"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:

    ....
"""
text = input("Nhập vào văn bản muốn mã hóa: ") #Nhận đoạn văn bản rõ
k = int(input("Nhập vào khóa dịch chuyển: ")) # Nhận khóa nhập vào từ bàn phím, ép kiểu về số nguyên
decimal = '' #Khởi tạo một chuỗi ký tự rỗng để cộng dồn kết quả mã hóa
print("Plain Text : " + text)
print("Shift pattern : " + str(k))

for i in range(len(text)):
    char = text[i]
    if "A"<=char<="Z": #Mã chữ HOA
        decimal = decimal + chr((ord(char) + k - 6) %2 + 6) # kết quả bản mã///

print(decimal)

