from sys import platform
from tkinter import *

root = Tk()  # create a window
root.title("Hide and Show")
root.geometry("400x400")  # width x height
if platform != "linux":
    root.iconbitmap('codemy.ico')


def clicked() -> None:
    global my_label2
    input: str = e.get()
    my_label2 = Label(root, text="Hello " + input)
    my_label2.pack()


def hide() -> None:
    my_label2.pack_forget()
    # my_label2.destroy()


def show() -> None:
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

hide_button: Button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=20)

show_button: Button = Button(root, text="Show", command=show)
show_button.pack(pady=20)

root.mainloop()  # keep the window open
