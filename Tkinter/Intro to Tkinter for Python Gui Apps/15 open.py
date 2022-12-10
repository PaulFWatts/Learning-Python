from sys import platform
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

root = Tk()
root.title("Hello World!")
root.geometry("500x700")
if platform != "linux":
    root.iconbitmap('codemy.ico')

# Create open dialog box function


def open_image():
    # Open File Dialog Box
    root.filename = filedialog.askopenfilename(
        initialdir='.', title="Open An Image File", filetypes=(("PNG File", "*.png"), ("All Files", "*.*")))  # type:ignore
    #my_label = Label(root, text=root.filename).pack(pady=10)
    global my_img
    # Open image and place on screen
    my_img = ImageTk.PhotoImage(Image.open(root.filename))  # type:ignore
    img_label = Label(root, image=my_img)
    img_label.pack(pady=10)


my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)


root.mainloop()
