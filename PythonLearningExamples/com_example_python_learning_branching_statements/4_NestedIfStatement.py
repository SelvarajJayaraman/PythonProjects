'''
Created on 13-May-2020

@author: Selvaraj Jayaraman
'''

print("#12 Python Branching statements Example");
print("*************************************************");

# Nested If Statement Example

print("# Nested If Statement Example");
print("*****************************");

a=int(input("Enter Value of a:"));
b=int(input("Enter Value of b:"));

if (a < b):
    if(a > 10):
        print("Value of a is greater then 10 ");
    else:
        print("Value of a is lesser than 10");
else:
    print("terminate");
