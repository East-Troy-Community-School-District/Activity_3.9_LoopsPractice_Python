'''
Count Down
Pawelski
10/28/2023
Introduction to Computer Science
'''

import time

count = 3
while count > 0:
    print(str(count) + "!")
    count = count - 1
    time.sleep(1)
print("Let's jam!")
