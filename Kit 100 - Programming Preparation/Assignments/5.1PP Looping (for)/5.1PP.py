'''
5.1PP Looping (for)

Author: Paul Watts 569987
Date:   May, 2022
Version: 2.0 (re-submission)

This program asks a user their their stair-climbing rate (in steps per minute), followed by a time duration (in minutes).
The program will then display a heading, followed by several rows of data (using a for loop), with each row (suitably aligned to the heading) displaying the elapsed minute (starting at 1), followed by the cumulative number of steps climbed.  The last row time should match the duration entered by the user.
Your program should finally indicate which minute (if at all) they would reach the lookout situated 1000 steps above that starting point. If the lookout was not reached, a suitable message should be displayed.
'''

# Initialise variables
HEIGHT = 1000 # Height of lookout
rate = 0 # User's rate of climb
minutes = 0 # User's time duration

print ("\033[2J\033[1;1H") # clear the screen

# Ask user for stair-climbing rate and time duration
rate = int(input("Enter your stair-climbing rate (in steps per minute): "))
minutes = int(input("Enter the time duration (in minutes): "))

# Display the heading
print("\nTime\tStep total")
print("----\t----------")

# Display the elapsed minutes and cumulative number of steps climbed
for i in range(1, minutes + 1):
    print(i, "\t", i * rate)

# Display the lookout
if rate * minutes < 1000:
    print("\nYou did not reach the lookout at " + str(HEIGHT) + " steps!")
else:
    print("\nYou reached The lookout at " + str(HEIGHT) + " steps in ", HEIGHT/rate, " minutes")

