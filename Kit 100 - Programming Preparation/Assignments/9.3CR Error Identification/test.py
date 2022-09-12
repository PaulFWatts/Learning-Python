def seriesSum(number=0):
    sum = 0
    """Calculate the sum of all integers up to and including the number passed in"""
    
    sum = (number * (number + 1)) / 2
    return sum
            

print("I calculate the sum of a series!")
again = "y"

while again == "y" or again == "Y":
    num = int(input("Enter an integer: "))
    print("The value of number is", num)
    print ("The sum of all numbers up to your number", num, " is " , seriesSum(num))
    again = (input("Do you want to enter another number? (Y/N)"))

