'''
Created on 25-May-2020

@author: Selvaraj Jayaraman
'''
print("#  Python Set  statement");
print("************************");

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

c.remove(2);
print("After using remove method:",c);

c.pop();
print("After pop method:",c);

#mixed collection in set
d={(1,2),(3,4)};
print("Mixed Set collection:",d);

#Java- DeepCopy
e={1,2,3,4};
f=e;
print("Deep copy of set collection:",e);
print("Deep copy of set collection:",f);

e.add(5);
f.add(6);
print("Deep copy of set collection:",e);
print("Deep copy of set collection:",f);

#ShallowCopy
g= e.copy();
print("Shallow copy of set collection:",g);
e.add(7);
print("after adding value in set(e) collection:",e);
print("after adding value in set(e) and copy(g) collection:",g);

