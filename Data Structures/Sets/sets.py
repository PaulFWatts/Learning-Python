# Creating a set
fruits = {"apple", "banana", "orange", "kiwi"}

# Printing the set
print("Original set:", fruits)

# Adding an element to the set
fruits.add("mango")
print("After adding 'mango':", fruits)

# Removing an element from the set
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Checking if an element exists in the set
if "apple" in fruits:
    print("'apple' exists in the set.")
else:
    print("'apple' does not exist in the set.")

# Iterating over the set
print("Iterating over the set:")
for fruit in fruits:
    print(fruit)

# Performing set operations
vegetables = {"carrot", "broccoli", "tomato"}

# Union of sets
combined = fruits.union(vegetables)
print("Union of sets:", combined)

# Intersection of sets
common = fruits.intersection(vegetables)
print("Intersection of sets:", common)

# Difference of sets
only_fruits = fruits.difference(vegetables)
print("Difference of sets (fruits - vegetables):", only_fruits)
