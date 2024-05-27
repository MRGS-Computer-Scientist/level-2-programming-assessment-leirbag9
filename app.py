from tkinter import *
from appsettings import *

w_width = 500
w_height = 800
bg_colour = "#E7DDFF"

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title("window")

        self.top_frame = Frame(self.window, background='white', width=500, height=100)
        self.top_frame.pack(fill='x')

        self.main_frame = Frame(self.window, background=bg_colour, width=500, height=(w_height-200))
        self.main_frame.pack(fill='both', expand=True)

        self.bottom_frame = Frame(self.window, background='white', width=500, height=150)
        self.bottom_frame.pack(fill='x', side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='white')
        self.home_button.place(x=0, y=0)

        self.back_button = Button(self.top_frame, text="Ex", height=2, width=5, bg='purple')
        self.back_button.place(x=15, y=0)

        self.exit_button = Button(self.top_frame, text="exit", height=4, width=10, bg='red', command=self.exit)
        self.exit_button.place(x=0, y=0)

        self.window.mainloop()

    def exit(self):
        self.window.destroy()