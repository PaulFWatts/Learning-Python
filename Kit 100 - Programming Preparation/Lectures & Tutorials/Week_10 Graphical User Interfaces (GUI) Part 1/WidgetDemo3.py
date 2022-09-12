"""
Title:Widget Demo
Purpose: To demonstrate the use of frame, button, checkbutton, radiobutton,
label, entry, message and text widgets
"""

from tkinter import * # Import all definitions from tkinter

class WidgetsDemo:

    def __init__(self):

        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title

        # Task: Add Texts

        text = Text(window) # Create and add text to the window
        text.pack()

        text.insert(END, "Tip\nThe best way to learn tkinter to is read")
        text.insert(END, " these carefully designed examples and use them")
        text.insert(END, " to create your applications.")

        window.mainloop() # Create an event loop

myWidgets = WidgetsDemo() # Create GUI
