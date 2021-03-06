# -*- coding: utf-8 -*-
"""Mathematical Operations

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ni6jVnn5R-o9nS2LdiSHGQEEANfGKQAx
"""

import datetime
from datetime import date
import math

########## When I tested each condition from questions 1-3, I commented out the parts that I proved to be wrong (caused an error) so that the program would keep running


#Problem 1
#1a (False)
a = "Aryan"
b = "Inamdar"
print(a + b)

#1b (False)
bool1 = 10>5
bool2 = 10<5
print(bool1 - bool2)

#1c (False)
float1 = 2.5
float2 = 3.5
print(float1*float2)

#1d (False)
int1 = 10
int2 = 5
print(int1/int2)

# #1e (True)
# time1 = datetime.time(2,30,0)
# time2 = datetime.time(5,30,0)
# print(time1 + time2)

# #1f (True)
# time3 = datetime.time(2,30,0)
# time4 = datetime.time(5,30,0)
# print(time4 - time3)

# #1g (True)
# time5 = datetime.time(2,30,0)
# time6 = datetime.time(5,30,0)
# print(time5 * time6)

# #1h (True)
# time7 = datetime.time(2,30,0)
# time8 = datetime.time(5,30,0)
# print(time8 / time7)

#1i (False)
bool3 = 100>50
bool4 = 100<50
print(bool3 + bool4)

#Final Answer
print("Problem #1")
print("1e, 1f, 1g, 1h")

#--------------------------------------------

#Problem 2
# #2a (False)
# string = "String"
# bool = 5>3
# print(bool + string)

#2b (True)
float = 1.5
boolean = 6>1
print(boolean - float)

#2c (True)
integer = 5
float1 = 6.5
print(integer*float1)

#2d (True)
integer1 = 5
boolean1 = 6>3
print(integer1/boolean1)

# #2e (False)
# date = date.today()
# time = datetime.time(6,30,0)
# print(date + time)

# #2f (False)
# time9 = datetime.time(2,30,0)
# time10 = datetime.time(5,30,0)
# print(time9 + time10)

# #2g (False)
# dates = date.today()
# times = datetime.time(6,30,0)
# print(dates - times)

#2h (True)
date1 = date.today()
date2 = date.today()
print(date1 - date2)

#2i (True)
boolean2 = 1>0
boolean3 = 0>1
print(boolean2 * boolean3)

#Final Answer
print("Problem #2")
print("2b, 2c, 2d, 2h, 2i")

#---------------------------------------------

#Problem 3
#3a (True)
bool5 = 1 == 1
print(bool5)

#3b (False)
bool6 = 'One' == 'one'
print(bool6)

#3c (False)
bool7 = 'one' == '1'
print(bool7)

#3d (False)
bool8 = 'one' == 1
print(bool8)

#3e (True)
bool9 = 1 == 1.0000000000000000001
print(bool9)

#3f (True)
bool10 = 1 < 2
print(bool10)

#3g (True)
bool11 = '10' < '2'
print(bool11)

#3h (False)
bool12 = 1.1 == 6.3 - 5.2
print(bool12)

#3i (False)
print(round(1.24))

#Final Answer
print("Problem #3")
print("3a, 3e, 3f, 3g")

#---------------------------------------------

#Problem 4
#infinite loop added for correcting convenience
while True:
  try:
    while True:
      #Accept Inputs
      number1 = int(input("Please enter a number: "))
      number2 = int(input("Please enter another number: "))

      #if both numbers are single digits
      if ((-9 <= number1 <= 9) and (-9 <= number2 <= 9)):
        sum = number1 + number2
        difference = number1 - number2
        product = number1 * number2
        print("Sum, Difference, Product:")
        print(sum, difference, product)
        #if number2 is not 0
        if (number2 != 0):
          quotient = number1/number2
          print("Quotient:")
          print(quotient)
        #if number2 is 0
        elif (number2 == 0):
          print("Second number is 0. So, division is not allowed.")

      #if either number has more than one digit
      elif (((number1 <= -10) or (number1 >= 10)) or ((number2 <= -10) or (number2 >= 10))):
        print("Your input length is not 1. Please enter only single digit numbers as input.")
  #catch error if input is not of type 'int', which generates a ValueError
  except ValueError:
    print("You entered a non-numeric value. Please enter only single digit numbers as input.")