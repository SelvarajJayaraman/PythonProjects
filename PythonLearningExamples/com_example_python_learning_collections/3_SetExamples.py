'''
Created on 25-May-2020

@author: Selvaraj Jayaraman
'''
print("#  Python Set  statement");
print("*********************");

a={1,2,3};
print("A is type:",type(a));

b={};
print("B is type:",type(b));

c=set();
print("C is type:",type(c));

c.add(1);
c.add(2);
c.add(3);
print("After adding set collection values:",c);