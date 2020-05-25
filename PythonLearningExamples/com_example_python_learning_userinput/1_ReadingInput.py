"""
Created on 11-May-2020

@author: selvaraj
"""
print("#5 Python Reading Input Examples")
print("********************************")

# To Read input from Users (Default type: String)
print("User Input Example 1")
print("******************")
userEnterText = input("Enter your Name:\t")
print("User entered text  data type")
print(type(userEnterText))
print("User Entered Text is:" + userEnterText)

# To Read Input from users and type cast to required datatype
print("User Input Example 2")
print("******************")
UserEnteredValue1 = int(input("Enter value 1:\t"))
UserEnteredValue2 = int(input("Enter value 2:\t"))
print("Additional value:")
print(UserEnteredValue1 + UserEnteredValue2)

# To Read Input values as expression
print("User Input Example 3")
print("******************")
UserEnteredValue3 = eval(input("Enter your expression here:\t"))
print("Expression return dataype  is:")
print(type(UserEnteredValue3))
print("Expression returned value is:")
print(UserEnteredValue3)
