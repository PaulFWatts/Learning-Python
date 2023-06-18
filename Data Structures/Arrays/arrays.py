import array

# Creating an array
numbers = array.array('i', [1, 2, 3, 4, 5])

# Printing the array
print("Original array:", numbers)

# Accessing elements in the array
print("Value at index 2:", numbers[2])
print("Value at index 4:", numbers[4])

# Updating a value in the array
numbers[3] = 10
print("Updated array:", numbers)

# Appending elements to the array
numbers.append(6)
numbers.append(7)
print("Array after appending elements:", numbers)

# Removing an element from the array
numbers.remove(3)
print("Array after removing 3:", numbers)

# Searching for an element in the array
element = 5
if element in numbers:
    print(f"{element} found in the array.")
else:
    print(f"{element} not found in the array.")

# Sorting the array
numbers.reverse()
print("Array after reversing:", numbers)

# Iterating over the array
print("Iterating over the array:")
for num in numbers:
    print(num)
