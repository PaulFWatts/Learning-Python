'''
6.1PP Loops (for and while)
Author: Paul Watts 569887
Date: March, 2022

This program counts how many letters 'a','b','c','d','e', and 'f'
are in a string entered by the user in order to determine the categories
of medicines they need to order. Only the above letters are allowed however 
they may be repeated.
'''

again = "Y" # Initialise variable for while loop

while again == "y" or again == "Y": # Loop until user enters "n" or "N"
    a_count = 0 # counter for number of "a" characters
    b_count = 0 # counter for number of "b" characters
    c_count = 0 # counter for number of "c" characters
    d_count = 0 # counter for number of "d" characters
    e_count = 0 # counter for number of "e" characters
    f_count = 0 # counter for number of "f" characters

    print ("\033[2J\033[1;1H") # clear screen
    codes = input("Enter the medicine code (a,b,c,d,e and f) ") # Get user input

    for i in codes: # Loop through each character in the string
        if i == "a":
            a_count += 1
        elif i == "b":
            b_count += 1
        elif i == "c":
            c_count += 1
        elif i == "d":
            d_count += 1
        elif i == "e":
            e_count += 1
        elif i == "f":
            f_count += 1
        else:
            print("Invalid code")
            break

    print("Here are the results")
    print("There were" , a_count, "'a' codes")
    print("There were" , b_count, "'b' codes")
    print("There were" , c_count, "'c' codes")
    print("There were" , d_count, "'d' codes")
    print("There were" , e_count, "'e' codes")
    print("There were" , f_count, "'f' codes")

    again=input("Do you want to run this program again (y/n)? ")

