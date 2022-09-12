"""
Title: Different principles of strings
Author: Zehong Jimmy Cao Date: Feb 2020
Purpose: To demonstrate how to use various string search functions
"""

# example 1: Locating a value in a string

test = "UtasICTdiscipline"

print(test.startswith("utas"))
print(test.startswith("Utas"))
print(test.startswith("U", 1)) # return if "U" @index 1
print(test.startswith("U", 0)) # return if "U" @index 0
print(test.startswith("Ut", 0, 1)) # start from 0; the computer do not count "end"
print(test.startswith("Ut", 0, 2)) #start from 0; the computer only count "end-1"

print()
print(test.endswith("line"))

print()
print(test.find("ict"))
print(test.find("ICT"))

print()
print(test.replace("discipline","department"))
print(test.replace("i","k"))
print(test.replace("i","k",1)) # only replace the 1st "i"

print()
print(test.count("i"))
print(test.count("i",10)) # start from index 10


# example 2

searchMe = '''Unit KIT001 provides students with an introduction to computer programming and its role in problem solving.
            The ICT graduates of the future require a combination of technical and professional skills
            in order to meet the needs of industry both within Australia and around the world.'''

print()
print("Variable 'searchMe' is: %s" % searchMe)

print()
print("Using the count for 'in':")
print(searchMe.count("in"))
print(searchMe.count(" in ")) # add spaces to avoid the characters in other words.

print()
print("Using the startswith for 'Unit':")
print(searchMe.startswith("Unit"))

print()
print("Using the endswith for 'world:")
print(searchMe.endswith("world"))
print(searchMe.endswith("world.")) # note: the period (.) at the ending point

print()
print("Using the replace:")
print(searchMe.replace("Unit", "Course").replace("KIT001","ICT"))
