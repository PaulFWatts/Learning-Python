'''
13.3HN Complex Class Definition and Usage
Author: Paul Watts 569987
Date: May, 2022

This program uses the provided rocket class to create a rocket object
and then uses the rocket object methods and attributes to launch the rocket and display
relevant rocket status information.
'''
# import the class data from rocket.py
from rocket import *

# create a new rocket from the rocket class
myRocket = Rocket("FalconX","Tesla",50)

# Print the rocket data - we need model, manufacturer and escape velocity.

print("\nThe rocket is a", (myRocket.getModel()), "series rocket manufactured by", myRocket.getManufacturer())
print("Escape velocity is set to:", (myRocket.getEscapeVelocity()))

# Print the rocket status - is it landed? 

if myRocket.getIsLanded() == True:
    print("\nThe rocket is currently landed!\n")

# Make the rocket take off
myRocket.takeOff()

# Print the rocket status now - is it flying?

if myRocket.getIsLanded() == False:
    print("The rocket is currently flying!\n")

print("Rocket accelerating...\n")

# Make the rocket accelerate until it reaches escape velocity speed

while myRocket.getSpeed() < myRocket.getEscapeVelocity():
    myRocket.accelerate()
    print("Rocket speed: ", myRocket.getSpeed())   

print("\nReached escape velocity!\n")

# Try to make the rocket land - you should get an error message as the speed is not zero!
myRocket.land()

print("\nRocket decelerating...\n")

# Make the rocket decelerate until it reaches zero speed
while myRocket.getSpeed() > 0:
    myRocket.decelerate()
    print("Rocket speed: ", myRocket.getSpeed())

# Try to make the rocket land - it should work now!
print()
myRocket.land()

