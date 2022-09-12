#Swapping values Example 2

varA = 5        
varB = 7  
      
print ("varA current value - " + str(varA)) 
print ("varB current value - " + str(varB))
      
varA, varB = varB, varA    
            
print ("varA new value - " + str(varA))	# convert a number to a string to join the Strings
print ("varB new value - " + str(varB))

print ("varA new value -", varA) # items are seperated with a sapce in between	
print ("varB new value -", varB)

print ("varA new value", varA, sep=" - ")   # overwrite the default seperator: a space
print ("varB new value", varB, sep=" - ")
