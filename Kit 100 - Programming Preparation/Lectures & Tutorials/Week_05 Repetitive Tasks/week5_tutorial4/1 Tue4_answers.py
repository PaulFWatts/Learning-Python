# Tue4 answers - test by Zehong Jimmy Cao

# 1. Reading through code

'''
Minutes to days to years conversion
Author: David Herbert
Version 1.1
Date: March 2016
Purpose: To convert an entered int read as minutes to days and years
'''
# Obtain input
minutes = int(input("Enter the number of minutes: "))

numberOfDays = minutes // (24 * 60) # 24hours * 60min; # Floor Division(//) - Divides and returns the integer value of the quotient. 
numberOfYears = numberOfDays // 365 
numberOfActualDays = numberOfDays % 365 # Modulus(%) - Divides and returns the value of the remainder.

# Display results
print("%s minutes is approximately %s years and %s days" \
   % (minutes, numberOfYears, numberOfActualDays))


# 2. Review good programming principles

'''Line length'''

width = 0;
height = 0;
color = 'red'
emphasis = 'strong'

# use () to wrap the text.
if (width == 0 and height == 0 and 
    color == 'red'and
    emphasis == 'strong' or highlight > 100):

    print ("Ohh...It works!")

'''Examples'''

import os
# here is the blankline
import sys

# hint - whitespace
# if operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). 

'spam(ham[1], {eggs:2})'

i=submitted=0
x=y=1
a=2
b=3

i=i+1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# 3. Review good programming principles

## 3a task

c = 'Y'
s = "whatever"
i = 34
b = False

if (c!='2'):  # do not use operator !=
    print ("This experession is", c!='2')

if (c<'y'): 
    print ("This experession is", c<'y')

if (s=="whatever"): 
    print ("This experession is", s=="whatever")

if (len(s)==i): 
    print ("This experession is", len(s)==i)

print("cat" + "dog") # no condition   


## 3b task

name = input("Please enter your title and first name: ")

#3b(i)

print("Hello " + name)

#3b(ii)
if (name[0:3] == "Mr "):
    print("Thank you sir")
    
#3b(iii)
if (len(name)%2 != 0):
    print("an odd name...")
else:
    print("an even name...")
    
#3b(iv)
if (len(name) == 2):
    print("two")
elif (len(name) == 3):
    print("three")
elif (len(name) == 4):
    print("four")
elif (len(name) == 5):
    print("five")
elif (len(name) == 6):
    print("six")
elif (len(name) == 7):
    print("seven")
elif (len(name) == 8):
    print("eight")
elif (len(name) == 9):
    print("nine")

#3b(v)
if ((name[0] >= '0') and (name[0] <= '9')):
    print("Not a valid name")
