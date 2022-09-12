"""
Title: Modifying Lists
Purpose: To provide a demonstration of how to modify a list in Python
"""

# example 1 - list functions

myList = ['J', 'i' ,'m', 'm', 'y'] # name: Jimmy
print(myList)
print()

item = myList.pop() # pop(i) – Removes an entry from the end of the list, or from index i if it is specified.
print(myList)
print(item)
print()

item = myList.pop(0)
print(myList)
print(item)
print()

myList.remove('m') # remove(x) – Removes the first occurrence of entry x from the list if it exists.
print(myList)
print()

myList = [1, 2, 3, 4, 5, 6] # index(x) - Returns the index of the first item whose value is x if it exists.
print(myList.index(3))
print()

myList = [1, 1, 1, 1, 1, 2, 2, 1, 2, 3] # count(x) – Returns the number of times x occurs in the list if it exists
print(myList.count(1))
print()

# example 2 - count function

myList = [1, 1, 1, 1, 1, 2, 2, 1, 2, 3]
myList[0] += 1  # index 0 - add "1"
print(myList)

myList[0] += 1 #  index 0 - add "1" again
print(myList)

myList[3] += 2 #  index 3 - add "2" 
print(myList)

print()



