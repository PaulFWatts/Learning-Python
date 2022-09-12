"""
Title:Widget Demo 2
Purpose: To demonstrate the use of frame, button, checkbutton, radiobutton,
label, entry, message and text widgets
"""

from tkinter import * # Import all definitions from tkinter

class WidgetsDemo:
    
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title

        # Task: Add a label, an entry, a button, and a message to frame2

        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()

        label = Label(frame2, text = "Enter your name: ")

        self.name = StringVar() # hold a string value
        entryName = Entry(frame2, textvariable = self.name) # Create Entry (to entre the name)

        btGetName = Button(frame2, text = "Get Name", command = self.processButton) # get the button

        message = Message(frame2, text = "It is a widgets demo")

        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        window.mainloop() # Create an event loop

    def processButton(self):
                    print("Your name is " + self.name.get())
                    self.name.set("Hello " + self.name.get())

myWidgets = WidgetsDemo() # Create GUI
