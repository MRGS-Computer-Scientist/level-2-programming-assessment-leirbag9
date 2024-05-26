from tkinter import *
from app_settings import *
w_width = 500
w_height = 800
bg_colour = "#E7DDFF"
class App():
    
    
     def __init__(self):
        self.window = Tk()
        self.window.geometry("1980x500")
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title("windoe")

        self.top_frame = Frame(background ='yellow' , width=500, height=100)
        self.top_frame.pack()

        self.main_frame = Frame(background=bg_colour , width=500, height=(w_height-200))
        self.main_frame.pack()

        self.bottom_frame = Frame(background = 'cyan', width=500, height=150)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green')
        self.home_button.place(x=0,y=0)

        self.window.mainloop()