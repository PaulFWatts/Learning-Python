
COUNT = 12 # Number of times to loop

again = "Y"

while again == "y" or again == "Y": # Loop until user enters "n" or "N"
    multiple= int(input("Please enter an integer to be multiple with: ")) # Get user input
    print("Multiplication Table")
    print("====================")
    for i in range(1, COUNT + 1):
       # print("{0} x {1} = {2}".format(multiple, i, multiple * i))
       print(i,"x" , multiple, " =", i *multiple)

    again=input("Do you wish to generate the table again (Y/N)? ")

