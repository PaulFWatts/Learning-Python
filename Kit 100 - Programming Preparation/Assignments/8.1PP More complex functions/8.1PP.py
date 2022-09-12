'''
8.1PP More Complex Functions
Author: Paul Watts 569887
Date: April, 2022

This program asks a user to enter a medicine barcode and then calculates the checksum.
The barcode contains a mixture of digits and letters. the checksum is calculated by ignoring the letters and adding the digits. The program will then output the checksum along with how many digits were in the barcode.
'''

def getChecksum(barcode): # Function to calculate the checksum
    sum = 0 # Initialise variable for sum
    digit_count = 0 # Initialise variable for digit count
    for c in barcode: # Loop through each character in the barcode
        if c.isdigit(): # If the character is a digit
            sum += int(c) # Add the digit to the sum
            digit_count += 1 # Increment the digit count
    return sum, digit_count

def main(): # main program
    again = "Y" # Initialise variable for while loop
    print ("\033[2J\033[1;1H") # clear screen

    while again == "y" or again == "Y": # Loop until user enters "n" or "N"
        codes = input("\nEnter the barcode: ") # Get user input

        mysum,mycount=getChecksum(codes) # Call the function to calculate the checksum
        print("The checksum is", mysum, " and ",mycount, "digits were entered")
        again=input("\nDo you want to run this program again (y/n)? ")

    print("Goodbye!")

if __name__ == "__main__": # call main function
    main()

