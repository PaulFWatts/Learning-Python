# This program demonstrates a function that accepts
# two arguments.

# example 1

def hello(greeting, name):
    print(greeting)
    print(name)

hello("Hi", "Jimmy")


# example 2
   
def main():
    print('The sum of 12 and 45 is')
    print(show_sum(12, 45))

# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    return result

# Call the main function.
main()


# example 3
def appendFlag(target, value):
   target += value
   return target

t=appendFlag('KIT','001')
print(t)

# example 4
def addIt(value1, value2): 

   print(value1,"+",value2,"=",value1+value2)


addIt(3,4)

