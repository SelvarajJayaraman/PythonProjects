"""
Created on 13-May-2020

@author: Selvaraj Jayaraman
"""
'''
# Identity   operator - is & is not
'''
a = 10
b = 20
c = b

# To print memory location use id().
print("a is memory location address", id(a))
print("b is memory location address", id(b))
print("c is memory location address", id(c))

print("Is Operator value", a is b)
print("Is Operator value", c is b)
print("Is Not Operator value", a is not b)
