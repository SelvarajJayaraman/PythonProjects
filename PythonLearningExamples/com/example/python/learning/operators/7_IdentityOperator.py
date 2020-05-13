'''
Created on 13-May-2020

@author: selvaraj
'''
'''
# Identity   operator - is & is not
'''
a=10;
b=20;
c=b;

# To print memory location use id().
print("a is memory location address", end = " ");
print(id(a));
print("b is memory location address", end = " ");
print(id(b));
print("c is memory location address", end = " ");
print(id(c));

print("\n");

print("Is Operator value", end = " ");
print(a is b);
print("Is Operator value", end = " ");
print(c is b);

print("Is Not Operator value", end = " ");
print(a is not b);