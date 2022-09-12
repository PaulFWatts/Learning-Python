from tkinter import *

class ImageDemo:
    def __init__(self):
        
        window = Tk()
        window.title("Image Demo")
        
        # Create PhotoImage objects
        catImage = PhotoImage(file = "images/cat.gif")
        dogImage = PhotoImage(file = "images/dog.gif")
        utasImage= PhotoImage(file = "images/utas.gif")

        #frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()

        Label(frame1,image = catImage).pack(side = LEFT)

        canvas = Canvas(frame1)
        canvas.create_image(90,90, image = dogImage)
        canvas["width"] = 250
        canvas["height"] = 180
        canvas.pack(side = LEFT)

        #frame2 to contain button
        frame2 = Frame(window)
        frame2.pack()

        Button(frame2,image = utasImage).pack(side = LEFT)

        window.mainloop()

ImageDemo() #Create the GUI
