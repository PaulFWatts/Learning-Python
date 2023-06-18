"""
This program demonstrates working with hash tables in Python.

A hash table, also known as a dictionary, is a collection of key-value pairs
where each key is unique. In Python, hash tables are implemented using
dictionaries. This program showcases various operations on hash tables, such as
adding elements, accessing values, checking key existence, updating values,
removing key-value pairs, and iterating over the hash table.

"""

# Creating a hash table
hash_table = {}

# Adding elements to the hash table
hash_table["apple"] = 1
hash_table["banana"] = 2
hash_table["orange"] = 3
hash_table["kiwi"] = 4

# Printing the hash table
print("Original hash table:", hash_table)

# Accessing elements in the hash table
print("Value of 'apple':", hash_table["apple"])
print("Value of 'banana':", hash_table["banana"])

# Checking if a key exists in the hash table
if "orange" in hash_table:
    print("'orange' exists in the hash table.")
else:
    print("'orange' does not exist in the hash table.")

# Updating a value in the hash table
hash_table["kiwi"] = 5
print("Updated hash table:", hash_table)

# Removing a key-value pair from the hash table
del hash_table["banana"]
print("Hash table after removing 'banana':", hash_table)

# Iterating over the hash table
print("Iterating over the hash table:")
for key, value in hash_table.items():
    print(key, ":", value)
