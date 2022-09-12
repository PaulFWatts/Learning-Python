'''
9.1CR Lists
Author: Paul Watts 569887
Date: April, 2022

This program does not require any user input.
It will display a list of numbers and then count the number of evens and odds in the list and display the
orginal list and resulting odds list and evens list as well as the counts for odds and evens.

'''

def displayAndCountOddsAndEvens(numbers):
    evens = [] # Initialise list for evens
    odds = [] # Initialise list for odds

   
    
    for i in numbers: # Iterate through each number in the list
        if i % 2 == 0: # If the number is even
            evens.append(i) # Add the number to the evens list
        else:
            odds.append(i) # Add the number to the odds list
            
    
    print("\nThe list is: ", numbers)
    
    if len(odds) > 0: # Check there are odds in the list
        print("Odd numbers:")
        print(*odds, sep = "\n")
    
    if len(evens) > 0: # check there evens in the list
        print("Even numbers:")
        print(*evens, sep = "\n")
        
    return len(evens), len(odds)
        
    


def main(): # main program

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Initialise list
    list2 = [2,4,6,8,10] # Initialise list
    list3 = [1,3,5,7,9] # Initialise list
    list4 = [] # Initialise list
    lists = [list1, list2, list3, list4] # Initialise list of lists
    evens_count, odds_count = 0, 0 # Initialise counts for evens and odds
    
    for i in lists:
        evens_count, odds_count = displayAndCountOddsAndEvens(i) # Call function to count evens and odds
        print("There were", odds_count, "odds and", evens_count, "evens")
    
       
    print("\nGoodbye!")

if __name__ == "__main__": # call main function
    main()

