#!/usr/bin/env python
# coding: UTF-8
"""
Name    : 4_DictionaryExample.py
Author  : Selvaraj Jayaraman
Contact : techselva87@gmail.com
Time    : 25-05-2020 07:51 PM
Desc    :
"""
print("#  Python Dictionary Statement")
print("******************************")

a = {}
print("type of a:", type(a))

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Data contains in a:", a)

# To fetch specific value from dictionary
print("To fetch data from dictionary using get method: ", a.get('b'))
print("To fetch data from dictionary using key: ", a['a'])

# To iterate values from dictionary
print("Iterated values from dictionary:")
for i in a:
    print(a[i])

print("Iterate keys from dictionary:")
for x in a:
    print(x)

print("Iterate values from dictionary using values method:")
for y in a.values():
    print(y)

print("To print key/values from dictionary")
for x,y in a.items():
    print(x,y)

print("To find the length of dictionary:", len(a))

del a['b']
print("After deletion of item from dictionary:", a)