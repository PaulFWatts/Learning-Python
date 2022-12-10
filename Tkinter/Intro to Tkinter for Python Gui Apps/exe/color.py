from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap(
    "D:/course-repos/Learning-Python/Tkinter/Intro to Tkinter for Python Gui Apps/exe/codemy.ico"
)


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack()  # type:ignore
    my_label2 = Label(
        root, text="You Picked A Color!!", font=("Helvetica", 32), bg=my_color
    ).pack()  # type:ignore


my_button = Button(root, text="Pick A Color", command=color).pack()


root.mainloop()
