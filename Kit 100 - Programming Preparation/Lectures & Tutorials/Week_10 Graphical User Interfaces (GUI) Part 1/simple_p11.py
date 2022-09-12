from tkinter import *
window = Tk() # Create a window

label = Label(window,text = "Welcome to Python") # Create label
button = Button(window,text = "Click me") # create a button

label.pack() # Place the label in the window and display it
button.pack() # Place the button in the window and display it

window.mainloop()  	# Create an event loop
                        # (the program waits for
                        # user interaction, such as mouse clicks
                        # and key presses)
