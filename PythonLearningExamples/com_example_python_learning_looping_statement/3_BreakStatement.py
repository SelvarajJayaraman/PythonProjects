"""
Created on 17-May-2020

@author: Selvaraj Jayaraman
"""

print("#14 Python Break statement Example")
print("**********************************")

counter = 0

while counter < 10:
    if counter == 5:
        print("If statement entered")
        break
    print("Counter value is:", end=" ")
    print(counter)
    counter += 1
print("Loop statement terminated")
