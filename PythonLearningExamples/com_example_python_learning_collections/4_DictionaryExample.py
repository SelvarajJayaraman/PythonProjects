#!/usr/bin/env python
# coding: UTF-8
"""
Name    : 4_DictionaryExample.py
Author  : Selvaraj Jayaraman
Contact : techselva87@gmail.com
Time    : 25-05-2020 07:51 PM
Desc    :
"""
a = {};
print("type of a:", type(a))

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Data contains in a:", a)

# to fetch specific value from dictionary
print("To fetch data from dictionary using get method: ", a.get('b'))
print("To fetch data from dictionary using key: ", a['a'])

# To iterate values from dictionary
print("Iterated values from dictionary:")
for i in a:
    print(a[i])
