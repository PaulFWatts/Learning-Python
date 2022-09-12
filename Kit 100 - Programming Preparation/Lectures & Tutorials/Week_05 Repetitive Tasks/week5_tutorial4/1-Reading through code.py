# 1. Reading through code

'''
Minutes to days to years conversion
Author: David Herbert
Version 1.1
Date: March 2016
Purpose: To convert an entered int read as minutes to days and years
'''
# Obtain input
minutes = int(input("Enter the number of minutes: "))

numberOfDays = minutes // (24 * 60) # 24hours * 60min; # Floor Division(//) - Divides and returns the integer value of the quotient. 
numberOfYears = numberOfDays // 365 
numberOfActualDays = numberOfDays % 365 # Modulus(%) - Divides and returns the value of the remainder.

# Display results
print("%s minutes is approximately %s years and %s days" \
   % (minutes, numberOfYears, numberOfActualDays))
