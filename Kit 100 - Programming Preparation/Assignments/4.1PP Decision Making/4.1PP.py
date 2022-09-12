'''
4.1PP Decision Making

Author: Paul Watts 569987
Date:   04/04/2022
Version: 2.0 (Resubmission)

This program asks the user to enter an object’s weight in Newtons, and then calculates and displays its mass in kilograms. If the object's calculated mass is more than 500 kilograms, it displays a message indicating that it is too heavy. If the object's mass is less than 100 kilograms, it displays a message indicating that it is too light.
'''

# Initialise variables
ACCELERATION = 9.8 # Acceleration due to gravity
weight = 0.0    # Weight in Newtons
mass = 0.0      # Mass in Kilograms

print ("\033[2J\033[1;1H") # clear screen

# Obtain weight from user  
weight = float(input("Enter the weight of the object in Newtons: "))

# Calculate mass in kilograms
mass = weight / ACCELERATION

# Display mass in kilograms (rounded to 2 decimal places), test for too light and too heavy
if mass > 500:
    print ("The object's mass is ", round(mass,2), " kilograms, which is too heavy.")
elif mass < 100:
    print ("The object's mass is ", round(mass,2), " kilograms, which is too light.")
else:
    print ("The object's mass is", round(mass,2), "kilograms.")
