from tkinter import *
from app_settings import *
from os import *
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

        self.bottom_frame = Frame(self.window, background=bg_colour, width=500, height=150)
        self.bottom_frame.pack()

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='white')
        self.home_button.pack(side=LEFT, padx=10, pady=5)

        self.back_button = Button(self.bottom_frame, text="Quiz", height=2, width=5, bg='white')
        self.back_button.pack(side=LEFT, padx=100, pady=30)

        self.exit_button = Button(self.bottom_frame, text="exit", height=2, width=5, bg='white', command=self.exit)
        self.exit_button.pack(side=LEFT, padx=10, pady=5)

        self.window.mainloop()

    def exit(self):
        self.window.destroy()