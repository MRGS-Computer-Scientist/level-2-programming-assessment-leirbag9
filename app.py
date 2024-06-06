from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
w_width = 500
w_height = 800
bg_colour = "#E7DDFF"

####FONT####
title_font = ("MS PGothic", 30, "bold")
class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title("window")

        # Define self.home_frame first
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
        
        ####LIST START####
        self.list_frame = Frame(background=bg_colour, width=w_width, height=(w_height-200))

        self.list_label = Label(self.list_frame, text="List", font=title_font)
        self.list_label.pack()

        self.list_box = Listbox(self.list_frame)
        self.list_box.pack()

        self.new_item = Button(self.list_frame, text="Add new item", command=self.add_new_item)
        self.new_item.pack()
        self.bottom_frame = Frame(self.window, background=bg_colour, width=500, height=150)
        self.bottom_frame.pack()
        ####LIST END####

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='white')
        self.home_button.pack(side=LEFT, padx=10, pady=5)

        self.back_button = Button(self.bottom_frame, text="Quiz", height=2, width=5, bg='white')
        self.back_button.pack(side=LEFT, padx=100, pady=30)

        self.exit_button = Button(self.bottom_frame, text="exit", height=2, width=5, bg='white', command=self.exit)
        self.exit_button.pack(side=LEFT, padx=10, pady=5)


        def add_new_item(self):
        user_input = simpledialog.askstring(title="Adding new item",
                                  prompt="What is your new item name:")
        self.list_box.insert(0, user_input)
        
        
        self.window.mainloop()

    def exit(self):
        self.window.destroy()