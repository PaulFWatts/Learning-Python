from sys import platform
from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.geometry("400x400")
if platform != "linux":
    root.iconbitmap('codemy.ico')

# Create radio button function


def radio():
    if v.get() == "one":
        my_label = Label(root, text="You Clicked Radio Button One!")
    else:
        my_label = Label(root, text="You Clicked Radio Button Two!")

    my_label.pack(pady=10)


# Radio Buttons
v = StringVar()
v.set("one")


rbutton_1 = Radiobutton(root, text="One", variable=v, value="one").pack()
rbutton_2 = Radiobutton(root, text="Two", variable=v, value="two").pack()

my_button = Button(root, text="Click Me", command=radio)
my_button.pack(pady=20)

root.mainloop()
