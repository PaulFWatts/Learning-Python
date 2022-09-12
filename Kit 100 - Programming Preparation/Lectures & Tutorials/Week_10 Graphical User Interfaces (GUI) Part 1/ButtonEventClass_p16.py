"""
Title: Process Button Event
Purpose: To demonstrate the processing of button events with functions
         in a class
"""
# Now we have object-oriented programming (OOP) style. 

from tkinter import * # Import all definitions from Tkinter

class ProcessButtonEvent:

    def __init__(self):
        window = Tk() # Create a window

        btOK = Button(window, text = "OK", highlightbackground = "red",fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "yellow",command = self.processCancel)
        
        
        btOK.pack() # Place the OK button in the window
        btCancel.pack() # Place the Cancel button in the window

        window.mainloop() # Create a event loop

    def processOK(self):
        print("Ok button is clicked")

    def processCancel(self):
        print("Cancel button is clicked")

myGUI = ProcessButtonEvent() # Create an object to invoke __init__ method
print("This is where I am at!")
