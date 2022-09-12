'''
4.2PP Decision Making

Author: Paul Watts 569987
Date:   04/04/2022
Version: 2.0 (Resubmission)

This program asks a user their age and then their pre-surcharge meal cost. It then displays the correct total cost for the meal after the surcharge multiplier has been applied.
'''

# Initialise variables
MEAL_SURCHARGE_1 = 0.95 # Multiplier for age 10 or less
MEAL_SURCHARGE_2 = 1.5 # Multiplier for age more than 10 but less than or equal to 20
MEAL_SURCHARGE_3 = 2.5 # Multiplier for age more than 20 but less than or equal to 40
MEAL_SURCHARGE_4 = 3.5 # Multiplier for age more than 40
age = 0.0 # User's age
mealCost = 0.0 # User's pre-surcharge meal cost
surcharge = 0.0 # Surcharge multiplier
totalCost = 0.0 # Total cost of meal

# Ask user for age and pre-surcharge meal cost
print ("\033[2J\033[1;1H") # clear screen
age = float(input("Enter your age: "))
mealCost = float(input("Enter your pre-surcharge meal cost: "))

# Calculate surcharge multiplier
if age <= 10:
    surcharge = MEAL_SURCHARGE_1
elif age > 10 and age <= 20:
    surcharge = MEAL_SURCHARGE_2
elif age > 20 and age <= 40:
    surcharge = MEAL_SURCHARGE_3
elif age > 40:
    surcharge = MEAL_SURCHARGE_4

# Display the total cost of the meal after the surcharge multiplier has been applied
totalCost = mealCost * surcharge
print ("The total cost of your meal is", round(totalCost,2), "dollars.")

