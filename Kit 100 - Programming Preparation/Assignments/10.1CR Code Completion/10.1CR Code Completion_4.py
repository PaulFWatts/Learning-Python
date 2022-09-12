'''
10.1CR Code Completion - Code Example 4
Author: Paul Watts 569987
Date: May, 2022

This program will adds the code for the given code example to produce the
desired output

'''

cheeses = ["original","lemon","strawberry","peanut"]
print("Welcome to the cheese cake Shop")
choice = input("Enter cheese: ").lower()
found = False

while found != True:
    for cheese in cheeses:
        if choice.find(cheese) != -1:
            found = True
            
    if found == False:
        print("No, we don't have that.")
        break
        
    else:
        print("Yes, we have that!")

