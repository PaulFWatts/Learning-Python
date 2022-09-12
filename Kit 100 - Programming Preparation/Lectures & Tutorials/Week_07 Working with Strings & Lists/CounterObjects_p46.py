"""
Title: Using a Counter Objects

Purpose: To demonstrate  how to use a counter object in Python
"""

from collections import Counter # import Counter

myList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]

# counter() - track how many times equivalent values are added.
# output format - [value: times]
listCount = Counter(myList) # note: captional letter "C"

print(listCount)

for thisItem in listCount.items():
    print("Item: " , thisItem[0], "Appears:", thisItem[1]) # thisItem[0] = [value]; thisItem[1] = [times]

print("The value 1 appears {0} times.".format(listCount.get(1))) # get(value) - returns the times of the value
