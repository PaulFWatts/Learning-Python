"""
Title: Modifying Lists 2
Purpose: To continue the demonstration of how to modify a list in Python
"""

# example 1 - create a list called test_list

testList = []

print("Finding out the length of testList")
print(len(testList))
print()

print("Add a value to testList")
testList.append(1) # append(x) – Adds a new entry to the end of the list.
print()

print("Checking to see if a value has been added to the end of testList.")
print(len(testList))
print()

print("What is the value in position 0 of testList")
print(testList[0])
print()

print("Inserting a value to a particular location.")
#In this case we are inserting value 2 into position 0 of testList
#please note it is the "insert" instead of "replace" function
testList.insert(0,2) # insert(i, x) – Adds a new entry x to the position specified by index i.
print()

print("Displaying our updated testList")
print(testList)



# example 2 - create a list called testList

testList = [2, 1]

print(testList)
print()

print("Creating a copy of testList...")
copyList = testList[:]
print()

# Adding a list to the end of another list
testList.extend(copyList) # extend(newlist) – Appends items from newlist onto the end of the current list
print()

print("Joing testList and copyList creates:")
print(testList)
print()

#Remove a value from the end of a list
testList.pop() 
print("Using 'pop()' leaves us with this version of testList")
print(testList)
print()

print("Remove a value from postion 1 in testList with 'remove()'")
testList.remove(1)
print()

print("testList now has these values.")
print(testList)
print()

print("Use 'del.list[:]' to clear the values of testList.")
del testList[:] # or use clear() – removes all entries from the list.
print()

#We can check to see if the list no longer contains values with len()
print("The length of testList is now:")
print(len(testList))





