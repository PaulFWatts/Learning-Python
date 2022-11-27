from tkinter import *

root = Tk()  # create a window
root.title("Hello World")
root.geometry("400x400")  # width x height


def clicked() -> None:
    my_label2: Label = Label(root, text="You clicked the button!")
    my_label2.grid(row=2, column=1)


# create labels
my_label: Label = Label(root, text="Hello World",
                        fg="blue", font=("Helvetica", 14))
my_label.grid(row=0, column=0)

# create buttons
my_button: Button = Button(root, text="Click me", command=clicked)
my_button.grid(row=2, column=0, sticky=W)

my_button2: Button = Button(root, text="Quit", command=root.quit)
my_button2.grid(row=3, column=0, sticky=W)

# create entry box
e: Entry = Entry(root, width=50, borderwidth=5)
e.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()  # keep the window open
