# example 1

try:
    x = 1/0
except:
    print('Something went wrong.')

# example 2

try:
    x = 1/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')
