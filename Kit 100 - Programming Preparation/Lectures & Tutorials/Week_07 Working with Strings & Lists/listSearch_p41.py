"""
Title: Searching Lists - from Zehong Jimmy Cao
Purpose: To continue the demonstration of how to search a list in Python
"""

colours = ["red", "orange", "yellow","green", "blue"]

colourSelect = ""

while colourSelect.upper() != "QUIT": # if it equals to "true" -> keep the loop

    colourSelect = input("Please type a colour name, type quit to exit: ")

    if colours.count(colourSelect) >= 1:
        print("The colour exists in the list!")
        print("The colour occurred at index:",colours.index(colourSelect))

    elif colourSelect.upper() != "QUIT":
        print("The list doesn't contain the colour.")

