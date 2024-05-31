from tkinter import *
from PIL import ImageTk, Image
from app_settings import *
w_width = 500
w_height = 800
bg_colour = "#E7DDFF"

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title("window")

        self.home_frame = Frame(self.window, background='gray', width=w_width, height=(w_height-200))
        self.home_frame.pack()

        # Load the image
        image = Image.open("imgs/Book.png")
        photo = ImageTk.PhotoImage(image)

        # Create the label with the image in self.home_frame
        bg_image = Label(self.home_frame, image=photo)
        bg_image.image = photo  # Keep a reference to the image to prevent garbage collection
        bg_image.pack()

        self.top_frame = Frame(self.window, background='white', width=500, height=100)
        self.top_frame.pack(fill='x')

        ## Main ##
        self.main_frame = Frame(self.window, background=bg_colour, width=500, height=(w_height-200))
        self.main_frame.pack(fill='both', expand=True)

        ## END ##
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
