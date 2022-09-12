"""
Title: Different formatting of strings
Purpose: To demonstrate how to format a string
"""

print("Field formatted as a decimal value:")
formatted = "{:d}" # d (decimal)
print(formatted.format(7000))

print()
print("Field formatted with a thousands separator to output:")
formatted = "{:,d}" # add a thousands separator
print(formatted.format(7000))

print()
print("The {0} of 100 is {1:b}".format("binary", 100)) # b (binary)

print()
print ("My average of this {0} was {1:.2f}%".format("semester", 78.234876)) #f (fixed lowercase point) # keep 2 points (0.23).

