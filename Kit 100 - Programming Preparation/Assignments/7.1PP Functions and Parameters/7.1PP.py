'''
7.1PP - Functions and Parameters
Author: Paul Watts 569987
Date: 06/04/2022

This program calculates the cost of paint for an unusual (a triangle "hat" on a circular disk) facade sign for a building.
'''

PI=3.1415 # constant for pi
UNIT_COST = 6.99 # constant for cost of paint per unit

# function to calculate the area of a circle from it's radius
def areaCircle(radius):   
    area = PI * (radius ** 2) # formula for area of a circle
    return(area)

# function to calculate the area of a triangle from it's base and height
def areaTriangle(base, height):
    area = (base * height) / 2 # formula for area of a triangle
    return(area)

# function to calculate the cost of paint for the facade sign
def printPaintCost(height,base,radius):
    circle_area = areaCircle(radius) # call function to calculate area of a circle
    triangle_area = areaTriangle(base, height) # call function to calculate area of a triangle
    paint_cost = (circle_area + triangle_area) * UNIT_COST # calculate the cost of paint
    print("\nThe area of the circle is: ","%.2f"%circle_area," meters squared")
    print("The area of the triangle is: ","%.2f"% triangle_area," meters squared")
    print("The paint cost is: $", "%.2f"%paint_cost)

def main(): # main program
    print("\nThis program will calculate the cost of paint for a building facade.")
    answer = "y" # variable to control the loop

    while answer != "n": # loop until user enters "n"      
        height = float(input("\nEnter the triangle height: ")) # get the triangle height
        base = float(input("Enter the triangle base: ")) # get the triangle base
        radius = float(input("Enter the the circle radius: ")) # get the circle radius
        printPaintCost(height,base,radius) # call function to calculate and print the cost of paint
        answer = input("\nDo you want to run this again? (y/n): ")
    else:  # if user enters "n" then the program will end
            print("\nGoodbye!")

if __name__ == "__main__": # call main function
    main()



