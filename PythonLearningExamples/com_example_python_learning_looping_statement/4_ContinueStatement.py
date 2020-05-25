'''
Created on 17-May-2020

@author: Selvaraj Jayaraman
'''
print("#14 Python Continue  statement Example");
print("************************************");

counter = 0;

while (counter < 10):
    counter+=1;
    if(counter == 5):
        print("If statement entered");
        continue;
    print("Counter value is:",counter);
print("Loop statement terminated");