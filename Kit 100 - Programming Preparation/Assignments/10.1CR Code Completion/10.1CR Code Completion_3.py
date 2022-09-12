'''
10.1CR Code Completion - Code Example 3
Author: Paul Watts 569987
Date: May, 2022

This program will adds the code for the given code example to produce the
desired output

'''

cheeses = ["Original","lemon","Strawberry","Peanut"]
replies = ["Sorry", "No", "No", "Yes sir.. No"]

j = 0
for i in cheeses:
    print("Do you have any ", i, "?",sep="")
    print(replies[j])
    j = j + 1


