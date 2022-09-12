




# example 1 - pass by value

name = "Jannet"

def myFunction():
    myName = "Jimmy"

print (name)


# example 2 - pass by value

name = "Jannet"

def myFunction():
    myName = name
    print (myName)

myFunction()
print (name)


# example 3 - return values

def swap(a,b,c):
    return c,b,a

v1,v2,v3 = swap(1, 2,3)
print (v1,v2,v3)


# example 4 - an argument being passed to a main function.

def main():
    value = 5
    show_double(value)
    
# The show_double function accepts an argument
# and displays double its value.
def show_double(number):
    result = number * 2
    print(result)

# Call the main function.
main()


# example 5 - pass to a main function.

def main():
    # Get the user's age.
    first_age = int(input('Enter your age: '))

    # Get the user's best friend's age.
    second_age = int(input("Enter your best friend's age: "))

    # Get the sum of both ages.
    total = sum(first_age, second_age)

    # Display the total age.
    print('Together you are', total, 'years old.')

# The sum function accepts two numeric arguments and
# returns the sum of those arguments.
def sum(num1, num2):
    result = num1 + num2
    return result

# Call the main function.
main()



