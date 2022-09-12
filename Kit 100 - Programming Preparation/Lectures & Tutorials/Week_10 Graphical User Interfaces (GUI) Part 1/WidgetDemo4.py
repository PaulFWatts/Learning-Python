"""
Title:Widget Demo
Purpose: To demonstrate the use of frame, button, checkbutton, radiobutton,
label, entry, mesCosage and text widgets
"""

from tkinter import * # Import all definitions from tkinter

class WidgetsDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title

        # Task: Add ONE check button, and TWO radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rdRed = Radiobutton(frame1, text = "Red", bg = "red", variable = self.v2, value = 1, command = self.processRadiobutton)
        rdYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = self.v2, value = 2, command = self.processRadiobutton)
        cbtBold.grid(row = 1, column = 1)   # Using the grid manager
        rdRed.grid(row = 1, column = 2)
        rdYellow.grid(row = 1, column = 3)

        # Task: Add a label, an entry, a button, and a message to frame2
        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) # Create Entry
        btGetName = Button(frame2, text = "Get Name",
                          command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        # Task: Add Text
        text = Text(window) # Create and add text to the window
        text.pack()
        text.insert(END, "Tip\nThe best way to learn tkinter to is read")
        text.insert(END, " these carefully designed examples and use them")
        text.insert(END, " to create your applications.")

        window.mainloop() # Create an event loop

    def processCheckbutton(self):
       if self.v1.get() == 1:
          status = "checked"
       else:
          status = "unchecked"
       print("check button is " + status)

    def processRadiobutton(self):
       if self.v2.get() == 1:
          colour = "Red"
       else:
          colour = "Yellow"
       print(colour + " is selected")

    def processButton(self):
       print("Your name is " + self.name.get())

myWidgets = WidgetsDemo() # Create GUI
