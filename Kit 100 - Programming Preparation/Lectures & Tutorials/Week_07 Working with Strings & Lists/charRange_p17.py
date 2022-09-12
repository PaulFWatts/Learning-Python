"""
Title: Different principles of strings

Purpose: To demonstrate how to select individual characters in strings
"""


firstString = "Hello World"
secondString = "Python is so much fun!"

print(firstString[0])
print(firstString[0:5])
print(firstString[:5])
print(firstString[6:])

thirdString = firstString[:6] + secondString[:6]
print(thirdString)

print(secondString[:7]*5)
