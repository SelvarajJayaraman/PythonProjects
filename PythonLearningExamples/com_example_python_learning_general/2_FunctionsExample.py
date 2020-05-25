#!/usr/bin/env python
# coding:UTF-8
"""
Name    : 2_FunctionsExample.py
Author  : Selvaraj Jayaraman
Contact : techselva87@gmail.com
Time    : 25-05-2020 09:20 PM
Desc    :
"""
print("# Python Functions Example")
print("**************************")


def noParameterFunc():
    print("Welcome to No Parameter Function")


def parameterFunc(name):
    print("Welcome to Parameter function: ", name)


def defaultParameterFunc(name="xyz"):
    print("Welcome to default parameter function: ", name)


def returnTypeFunc(x):
    y = x + 5
    return y


noParameterFunc()
parameterFunc("Selva")
defaultParameterFunc()

a = returnTypeFunc(10)
print("Return type method value:", a)
