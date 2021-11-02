"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:A bit shift is a procedure whereby the bits in a bit string are moved to the left or
to the right. For example, we can shift the bits in the string 1011 two places to
the left to produce the string 1110. Note that the leftmost two bits are wrapped
around to the right side of the string in this operation. Define two scripts,
shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script
shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit
to the rightmost position. The script shiftRight performs the inverse operation.
Each script prints the resulting string
Solution:

    ....
"""
def shiftLeft(bitstring):
    bitstring = bitstring[1:]+bitstring[0]
    return bitstring
bits = input("Enter a string of bits: ")
leftShift = shiftLeft(bits)
print()
print(leftShift)
print()
def shiftRight(bitstring):
    bitstring=bitstring[len(bitstring)-1] + bitstring[0:len(bitstring)-1]
    return bitstring
bits = input("Enter a string of bits: ")
rightShift = shiftRight(bits)
print()
print(rightShift)
print()