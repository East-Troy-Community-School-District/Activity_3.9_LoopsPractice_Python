'''
Addition Flash Cards
Pawelski
10/28/2023
Introduction to Computer Science
'''

import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
answer = num1 + num2
guess = int(input("What is " + str(num1) + " + " + str(num2) + "? >> "))
if guess == answer:
    print("Correct!")
else:
    print("Wrong!")
