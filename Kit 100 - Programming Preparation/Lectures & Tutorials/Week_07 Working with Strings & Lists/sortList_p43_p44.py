"""
Title: Searching Lists - support from Zehong Jimmy Cao in Feb 2020
Purpose: To continue the demonstration of how to sort a list in Python
"""
# example - sort
colours = ["red", "orange", "yellow", "green", "blue"]

print("Unsorted colour list: ")
for item in colours:
    print(item, " ", end='') # end='' - avoid creating new lines in 'for' loop
print()

colours.sort() #sort list
print()

print("Sorted colour list: ")
for item in colours:
    print(item, " ", end='')
print()


# example - reverse sort
print()

colours = ["red", "orange", "yellow", "green", "blue"]

print("Unsorted colour list: ")
for item in colours:
    print(item, " ", end='')
print()

colours.sort() #sort list
colours.reverse() #reversing sort list

print()

print("Reverse sorted colour list: ")

for item in colours:
    print(item, " ", end="")

print()
