'''
Title: break in for loop Example
Purpose: To demonstrate how a break clause works
         in a for loop 
'''

value = input("Type less than 7 characters:")
letterNum = 1

for letter in value:
    print ("Letter %d is %s" % (letterNum, letter))
    
    letterNum += 1
    if letterNum >= 7:

        #break   
        print ("The string you entered is too long!")

# print("This is outside the for loop")
