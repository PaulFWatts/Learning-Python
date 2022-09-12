'''
3.1PP Sample Calculation Expression

Author: Paul Watts 569987
Date:   01/03/2022
Version: 1.0

This program calculates the time it takes for a car to travel 3 given distances
assuming there are no accidents or delays
'''

from pconst import const    

# Initialise variables
const.SPEED = 50 # constant speed
distance = 0 # Initial distance
time = 0 # Initial time

print ("\033[2J\033[1;1H") # clear screen

def calc_time(distance):
    '''
    This function calculates the time it takes for a car to travel a passed distance
    and displays the time taken in a formatted string
    '''
    # Calculate the time
    time = distance / const.SPEED

    # Display the result
    print("It will take the car",time,"hour(s) to travel",distance,"kilometres")

# call function 3 times with the 3 distances
calc_time(50)
calc_time(100)
calc_time(150)

