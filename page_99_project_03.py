"""
Author: Nguyen Van Hoang
Date: 16/09/2021
Problem:
    Modify the guessing-game program of Section 3.5 so that the user thinks of a
    number that the computer must guess. The computer must make no more than
    the minimum number of guesses, and it must prevent the user from cheating by
    entering misleading hints. (Hint: Use the math.log function to compute the minimum number of
    guesses needed after the lower and upper bounds are entered.)
Solution:

    ....
"""
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    else:
        print("You've got it in", count, "tries!")