# example 1
try:
    x = 1/1
    
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
    

# example 2
try:
    value = int(input("Enter a number:"))
    print("Well Done")

except ValueError:
    print("A dummy user!")
else:
    print('A good user!')  
 
