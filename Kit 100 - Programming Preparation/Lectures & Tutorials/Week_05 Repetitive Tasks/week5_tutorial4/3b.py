## 3b task

name = input("Please enter your title and first name: ")

#3b(i)

print("Hello " + name)

#3b(ii)
if (name[0:3] == "Mr "):
    print("Thank you sir")
    
#3b(iii)
if (len(name)%2 != 0):
    print("an odd name...")
else:
    print("an even name...")
    
#3b(iv)
if (len(name) == 2):
    print("two")
elif (len(name) == 3):
    print("three")
elif (len(name) == 4):
    print("four")
elif (len(name) == 5):
    print("five")
elif (len(name) == 6):
    print("six")
elif (len(name) == 7):
    print("seven")
elif (len(name) == 8):
    print("eight")
elif (len(name) == 9):
    print("nine")

#3b(v)
if ((name[0] >= '0') and (name[0] <= '9')):
    print("Not a valid name")
