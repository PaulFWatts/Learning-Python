'''
Title: continue in for loop Example
Purpose: To demonstrate how a continue clause
         works in a for loop 
'''
letterNum = 1

for letter in "apple_orange":

    if letter == "n":
        
        print ("Encountered n, not processed.")
        continue
        
    print ("Letter %2d is %s" % (letterNum, letter))

    letterNum += 1

