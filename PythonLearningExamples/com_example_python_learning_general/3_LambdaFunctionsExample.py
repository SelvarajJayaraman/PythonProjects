#!/usr/bin/env python
# coding:UTF-8
"""
Name    : 3_LambdaFunctionsExample.py
Author  : Selvaraj Jayaraman
Contact : techselva87@gmail.com
Time    : 30-05-2020 05:09 PM
Desc    :
"""
print("# Python Lambda Functions Example")
print("*********************************")

x = lambda k: k * 5
print("The lambda Single Argument function output:", x(5))

y = lambda a,b: a * b
print("The lambda Two Argument function output:", y(5,10))
