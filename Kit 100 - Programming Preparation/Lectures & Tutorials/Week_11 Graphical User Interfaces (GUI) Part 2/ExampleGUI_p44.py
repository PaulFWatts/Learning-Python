from tkinter import *

class KiloConverterGUI:
    
    def __init__(self):

        self.main_window = Tk()

        # some frames for the layout
        self.top_frame = Frame()
        self.mid_frame = Frame()
        self.bottom_frame = Frame()

        self.prompt_label = Label(self.top_frame,text="Enter a distance in kilometers: ")
        self.prompt_label.pack(side='left')
        
        self.kilo_entry = Entry(self.top_frame,width=10)
        self.kilo_entry.pack(side='left')

        self.descr_label = Label(self.mid_frame,text="Converted to miles: ")
        self.descr_label.pack(side='left')
        
        self.value = StringVar() #Tk function for String values in GUI
        self.miles_label = Label(self.mid_frame,textvariable=self.value)
        self.miles_label.pack(side='left')

        # action buttons
        self.calc_button = Button(self.bottom_frame,text='Convert',
                                  command=self.convert)
        self.calc_button.pack(side='left')
        
        self.quit_button = Button(self.bottom_frame,text='Quit',
                                  command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # show the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        mainloop()

    def convert(self):

        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        self.value.set("%.2f"%miles) #value is StringVar type, which has set method

KiloConverterGUI()
