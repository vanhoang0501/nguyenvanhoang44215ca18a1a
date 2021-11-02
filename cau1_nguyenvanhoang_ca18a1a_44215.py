"""
Author: Nguyễn Văn Hoàng
Date: 29/10/2021
Problem:cau 1
Solution:
    ....
"""
def Cau1():
    def snt(n):
        """ so nguyen to"""
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f
    def in_snt(a=30, b=200):
        print(" cac so nguyen to: ")
        """Kiem tra so nguyen to trong khoang tu a den b"""
        for i in range(a, b + 1):
            if snt(i):
                print(i, end= " ")
                print()
    in_snt(30, 200)
if __name__ == '__main__':
    Cau1()