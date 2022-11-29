from sys import platform
from tkinter import *

root = Tk()  # create a window
root.title("Icons")
root.geometry("400x400")  # width x height
if platform != "linux":
    root.iconbitmap('codemy.ico')


def clicked() -> None:
    input: str = e.get()
    my_label2: Label = Label(root, text="Hello " + input)
    my_label2.pack()


# create labels
my_label: Label = Label(root, text="Enter your name:")
my_label.pack()

# create entry box
e: Entry = Entry(root, font=("Helevetica", 18))
e.pack(pady=20)

# create buttons
my_button: Button = Button(root, text="Click me", command=clicked)
my_button.pack(pady=20)


root.mainloop()  # keep the window open
