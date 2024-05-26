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

        self.top_frame = Frame(self.window, background='yellow', width=500, height=100)
        self.top_frame.pack(fill='x')

        self.main_frame = Frame(self.window, background=bg_colour, width=500, height=(w_height-200))
        self.main_frame.pack(fill='both', expand=True)

        self.bottom_frame = Frame(self.window, background='cyan', width=500, height=150)
        self.bottom_frame.pack(fill='x', side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green')
        self.home_button.place(x=0, y=0)

        self.back_button = Button(self.top_frame, text="btih", height=2, width=5, bg='purple')
        self.back_button.place(x=0, y=0)

        self.exit_button = Button(self.main_frame, text="outta this house", height=2, width=5, bg='red', command=self.exit)
        self.exit_button.place(x=0, y=5)

        self.window.mainloop()

    def exit(self):
        self.window.destroy()