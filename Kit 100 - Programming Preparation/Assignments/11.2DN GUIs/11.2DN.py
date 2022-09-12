'''
11.2DN Grapical User Interface (GUI)
Author: Paul Watts 569987
Date: May, 2022

This program creates a GUI which has two lables, one text entry field, and two buttons.
The GUI allows the user to enter a 'click count' into the text entry field and then click a
'Fidget Click' button to see that number decreased by one every click. 
A status label displays a message to the user based on the resutling number from clicking the 'Fidget Click' button.
'''

from tkinter import *

class FidgetClick:
    
    def __init__(self): # Constructor
        window = Tk() # Create a window 
        window.title("Fidget Click") # Set a title
    
        
        self.enterLbl = Label(window,text="Enter click count:") # Create a label
        self.statusLbl = Label(window, width=38, anchor="w", text="status:") # Create a label
        
        self.btnQuit = Button(window, text="Quit",command=window.destroy) # Create a button
        self.btnClick = Button(window, text="Fidget Click",command=self.click) # Create a button
        
        self.number = StringVar() # Create a string variable
        self.txtbox = Entry(window,textvariable=self.number) # Create a text box and associciate it with the string variable

        # Arrange the widgets in the window
                
        self.enterLbl.grid(row=1, column=1) # Place the label
        self.txtbox.grid(row=1, column=2) # Place the text box
        self.statusLbl.grid(row=2, column=1, columnspan=2) # Place the status message
        self.btnClick.grid(row=3, column=1) # Place the FidgetClick button
        self.btnQuit.grid(row=3, column=2) # Place the Quit button
                
        window.mainloop() # Start the GUI event loop
    
    def click(self):
        number = self.number.get() # Get the number entered in the text box
        number = int(number) # Convert the number to an integer
        number = number - 1 # Decrement the number
        self.number.set(number) # Set the resultant number in the text box
        
        # Display the status message based on the resultant number 
    
        if (number > 10):
            self.statusLbl.config  (text="status: Keep going...")
        elif (number > 5 and number <= 10):
            self.statusLbl.config  (text="status: You are nearly there!")
        elif (number > 0 and number <= 5):
            self.statusLbl.config  (text="status:  " + str(number - 1) + " more to go")
        elif (number == 0):
            self.statusLbl.config  (text="status: You must enter another fidget click count") 
        
GUI = FidgetClick() # Create an instance of the class


