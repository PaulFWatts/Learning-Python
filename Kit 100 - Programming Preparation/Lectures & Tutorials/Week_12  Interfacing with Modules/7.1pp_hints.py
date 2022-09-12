#7.1PP for hints 

PI = 3.1415 # pi
COST = 6.99 # the cost is defined as $6.99 per square meter.

def printPaintCost(height,base,radius):

   areaCircle = PI * radius * radius
   areaTriangle = 0.5 * base * height

   print("The area of the circle")
   print("The area of the triangle")
   print("The total paint cost")

def main():

   answer = 'y'

   while answer == 'y':

      height = float(input("Enter the triangle height: "))
      base ...  
      radius ...
      
      printPaintCost(height,base,radius)
      
      answer = input("Do you want to run this again? (y/n):")

main()

