'''
Addition Flash Cards
1/18/2023
Python I
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
