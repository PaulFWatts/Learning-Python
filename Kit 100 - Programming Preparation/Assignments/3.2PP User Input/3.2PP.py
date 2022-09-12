'''
3.2PP User Input

Author: Paul Watts 569987
Date:   20/03/2022
Version: 1.0

This program converts a Fahrenheit temperatures entered by the user to a Celsius temperature (C) as well as Kelvin temperatures (K)
'''

# Initialise variables
fahrenheit = 0.0 # Initial Fahrenheit temperature
celsius = 0.0 # Initial Celsius temperature
kelvin = 0.0 # Initial Kelvin temperature

print ("\033[2J\033[1;1H") # clear the screen

# Get the temperature from the user
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert the temperature to Celsius
celsius = (fahrenheit - 32) * 5/9

# Convert the temperature to Kelvin
kelvin = celsius + 273.15

# Display the result rounded to 2 decimnal places
print("The temperature in Celsius is",round(celsius,2),"and the temperature in Kelvin is",round(kelvin,2))
