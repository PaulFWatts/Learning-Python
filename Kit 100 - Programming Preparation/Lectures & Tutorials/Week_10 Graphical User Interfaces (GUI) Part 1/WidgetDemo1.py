from tkinter import * # Import all definitions from tkinter

class WidgetsDemo:
   
   def __init__(self):
      window = Tk() # Create a window
      window.title("Widgets Demo") # Set a title

      # Task: Add ONE check button, and TWO radio buttons to frame1

      frame1 = Frame(window) # Create and add a frame (~a container) to window
      frame1.pack()

      self.v1 = IntVar() # Hold an integer - default value 0
      cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1,
                            command = self.processCheckbutton)

      self.v2 = IntVar()
      rdRed = Radiobutton(frame1, text = "Red", bg = "red", variable = self.v2,
                          value = 1, command = self.processRadiobutton)
      rdYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow",variable = self.v2,
                          value = 2,command = self.processRadiobutton)

      cbtBold.grid(row = 1, column = 1)   # Using the grid manager
      rdRed.grid(row = 1, column = 2)
      rdYellow.grid(row = 1, column = 3)

      window.mainloop() # Create an event loop


   def processCheckbutton(self):
      if self.v1.get() == 1 : # value 1 for the checked button; value 0 for unchecking.
         status = "checked"
      else:
         status = "unchecked"
      print("check button is " + status)

   def processRadiobutton(self):
      if self.v2.get() == 1 : # value 1 for red button; value 2 for yellow button
         colour = "Red"
      else:
         colour = "Yellow"
      print(colour + " is selected")

WidgetsDemo() # Create GUI

