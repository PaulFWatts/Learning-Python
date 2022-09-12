'''
5.2PP Looping (while)

Author: Paul Watts 569987
Date:   20/03/2022
Version: 1.0

This program first tells the user what it does, and then asks the user to enter a series of integers (positive or negative). 
The user should enter zero to signal the end of the series. 
After all the numbers have been entered, the program displays their product and the count of how many numbers were entered. 
'''

# Initialise variables

number = 1 # The number entered by the user
first = True # Flag to indicate if this is the first number entered
count = 0 # The number of numbers entered

print ("\033[2J\033[1;1H") # clear screen

# Display program description
print("This program will take a series of integer numbers and multiply them together.")
print("------------------------------------------------------------------------------\n")

# Get user input
while number != 0:
    number = int(input("Enter an integer number (0 to end): ")) # Obtain the next number
    if number != 0: # If the user entered zero, then the loop will end
        count += 1 # Increment the count of numbers entered
        if first: # If this is the first number entered, then set the product to the first number
            product = number
            first = False # Set the flag to false
        else:
            product = product * number # Multiply the product by the next number
    else:
        print("\nThe product of all the numbers entered is:", product)
        print("The number of numbers entered is:", count)



