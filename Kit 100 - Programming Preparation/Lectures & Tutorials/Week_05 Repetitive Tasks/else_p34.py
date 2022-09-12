print ("I search for the 'a' character.")

value = input("Type less than 7 characters: ")

letterNum = 1

for letter in value:

    print ("Letter %d is %s" % (letterNum, letter))

    letterNum += 1

    if letter == "a":      
        print ("You typed an 'a'!")
        break

else:
    print ("You did not type any 'a' characters.")
