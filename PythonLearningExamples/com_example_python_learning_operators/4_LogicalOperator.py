'''
Created on 11-May-2020

@author: selvaraj
'''

print("#9 Python Logical Operator");
print("***********************");

a = ((2 < 3) and  (3 < 4));
print("Logical And Operator value:",  end = " ");
print(a);

b = ((2 < 3) or  (3 < 1));
print("Logical OR Operator value:",  end = " ");
print(b);

c = not(3 < 2);
print("Logical Not Operator value:",  end = " ");
print(c);
