from tkinter import *

window = Tk() # Create a window

btShowOrHide = Button(window, text = "Show", bg = "white")

btShowOrHide.pack()

#change properties after Button creation..
btShowOrHide["text"] = "Hide"
btShowOrHide["bg"] = "red"
btShowOrHide["highlightbackground"] = "red"
btShowOrHide["fg"] = "#AB84F9" # Change font colour to #AB84F9
btShowOrHide["cursor"] = "plus" # Change mouse cursor to plus
btShowOrHide["justify"] = LEFT # Set justify to LEFT

window.mainloop()


