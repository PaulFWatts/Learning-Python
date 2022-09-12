from tkinter import *

class MenuDemo:
    def __init__(self):
        
        window = Tk()
        window.title("Menu Demo")

        # Create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) # Display the menu bar

        # Create a pull-down menu, and add it to the menu bar
        menuOne = Menu(menubar)
        
        menubar.add_cascade(label = "Menu One", menu = menuOne)
        menuOne.add_command(label = "First Option")
        menuOne.add_command(label = "Second Option")

        exitMenu = Menu(menubar)

        menubar.add_cascade(label = "Exit", menu = exitMenu)
        exitMenu.add_command(label = "Quit")

        mainloop()

MenuDemo() # Create GUI
