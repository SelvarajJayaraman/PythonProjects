#!/usr/bin/env python
# coding:UTF-8
"""
Name    : 1_MutableImmutableObjectExample.py
Author  : Selvaraj Jayaraman
Contact : techselva87@gmail.com
Time    : 25-05-2020 09:04 PM
Desc    :
"""
print("# Python MutableImmutable Objects")
print("*********************************")

'''
Mutable objects - List,Set,dictionary
Immutable objects - Int,Float,String
'''

print(" ********** Mutable object examples - Start ****************")

a = [1, 2, 3, 4, 5]
b = a

print("value of a:", a)
print("value of b:", b)

print("Memory address of a:", id(a))
print("Memory address of b:", id(b))

# Modify the list values
a[2] = 10
print("After modified values of a:", a)
print("After modified values of b:", b)

print("After modification memory address of a:", id(a))
print("After modification memory address of b:", id(b))

print(" ********** Mutable object examples - End ****************")

print("\n");

print(" ********** Immutable object examples - start ****************")

x = 10
print("value of x:", x)

y = x
print("value of y:",y)

print("Memory address of x: ", id(x))
print("Memory address of y: ", id(y))

x = 20

print("After Modifying value of x: ", x)
print("After modifying value of y: ", y)

print("After Modifying Memory address of x: ", id(x))
print("After Modifying Memory address of y: ", id(y))

print(" ********** Immutable object examples - end ******************")


