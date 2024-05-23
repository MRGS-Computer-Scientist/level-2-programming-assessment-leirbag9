from tkinter import * 
from appsettings import *

w_width = 500
w_height = 800
bg_colour = "#E7DDFF"

class App():

    def __init__(self):
        window = Tk()
        window.geometry("500x500")
        window.geometry(str(w_width) + "x" + str(w_height))
        window.title("windoe")

        top_frame = Frame(background ='yellow' , width=w_width, height=100)
        top_frame.pack()

        main_frame = Frame(background=bg_colour , width=w_width, height=(w_height-200))
        main_frame.pack()

        bottom_frame = Frame(background = 'cyan', width=w_width, height=150)
        bottom_frame.pack(side='bottom')

        start_button = Button(bottom_frame, text="start", height=5, width=5, bg='pink')
        window.mainloop()