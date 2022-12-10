from sys import platform
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.geometry("400x400")
if platform != "linux":
    root.iconbitmap('codemy.ico')

# Create popup function


def popup():
    response = messagebox.askyesno("Popup Title", "Look at my popup message")
    my_label = Label(root, text=response).pack(pady=10)

    if response == 1:
        my_label = Label(root, text="You Clicked Yes!").pack(pady=10)
    else:
        my_label = Label(root, text="You Clicked No!").pack(pady=10)

# Popup Boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# Note: some return 0 or 1, some return yes or no and some return ok


pop_button = Button(root, text="Click to Pop up!", command=popup)
pop_button.pack(pady=20)

root.mainloop()
