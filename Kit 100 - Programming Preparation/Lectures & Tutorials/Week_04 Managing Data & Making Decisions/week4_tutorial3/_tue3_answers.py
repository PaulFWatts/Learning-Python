"""
Kit100 Programming Preparation

Week 4 - Tutorial 3
"""


# 1. Assigning values

# Create a variable and assign it an integer value.
x = 5
t= type (x)
print ("print the variable's type", t)
print ("print the variable's value", x)


# Write a program that will output a Boolean value.
print(5 < 6)
print(5 > 6)
print(5 == 6)

# Work through the assigning variables example in Lecture 3.
varA=5;
varB=7;
print ("varA is", varA )
print ("varB is", varB )

# Write a program that will assign the same integer value to three different variables.
x = 5;
y = 5;
z = 5;

print (x, y, z)

# Work through the example in Lecture 3 that demonstrated simultaneous assignment of variables.
x = 3
y = 4
print (x, y)

x, y = y, x
print (x, y)

# Look through the follow table.
units_per_day=5; # allow? - yes
dayOfWeek=5; # allow? - yes
'3dGraph=5;' # allow? - no
June1997 =5; # allow? - yes
'Mixture#3=5;' # allow? - no

# Create a string variable called first_name, and a string variable called last_name.
first_name ="Zehong Jimmy";
last_name ="Cao";
print ("your name:", first_name, last_name)

# Create an int, a float, a Boolean, and a string variable.
x = 5
print(type(x))
y = 5.5
print(type(y))
z = True
print(type(z))
a = "Hello"
print(type(a))

# 2. Write an algorithm that uses arithmetic operators

# Write a program that will assign the same integer value to three different variables.
x = 7;
y = 7;
z = 7;
result = (x + y) * z
print (result)

# Write a program that displays the area of a rectangle with the width of 4.5 and height of 7.9
width = 4.5
height = 7.9
rectangle = width * height
print (rectangle)

# Write a program that will consider a number and display the number of 10’s in that number (ingore)

# 3. Creating multiline strings

print ('''Name is Jimmy
Address at Kingston
Email: zehong.cao@utas.edu.au ''')

# 4. Importing the datetime command

import datetime
print(datetime.datetime.now())

import calendar
cal=calendar.month(2020, 3)
print (cal)

# 5. Additional work if you have time

n = 123

num1 = int(n / 100);
num2 = int((n % 100) / 10)
num3 = n%10

reverse = 100*num3 + 10*num2 + num1
print(" The reverse is", reverse)



