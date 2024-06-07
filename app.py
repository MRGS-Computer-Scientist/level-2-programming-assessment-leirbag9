from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
from appsettings import *
from tkinter import messagebox 
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
        self.home_frame.grid(row=0, column=0)

        # Load the image
        image = Image.open("imgs/Book.png")
        photo = ImageTk.PhotoImage(image)

        # Create the label with the image in self.home_frame
        bg_image = Label(self.home_frame, image=photo)
        bg_image.image = photo  # Keep a reference to the image to prevent garbage collection
        bg_image.grid(row=0, column=0)

        self.top_frame = Frame(self.window, background='white', width=500, height=100)
        self.top_frame.grid(row=1, column=0, sticky="ew")

        ## Main ##
        self.main_frame = Frame(self.window, background=bg_colour, width=500, height=w_height-200)
        self.main_frame.grid(row=2, column=0, sticky="nsew")

        ## END ##
        
        ####LIST START####
        self.list_frame = Frame(self.window, background=bg_colour, width=w_width, height=(w_height-200))
        self.list_frame.grid(row=2, column=0, sticky="nsew")

        self.list_label = Label(self.list_frame, text="List", font=title_font)
        self.list_label.grid(row=0, column=0, padx=200 , pady=(20, 10))

        self.list_box = Listbox(self.list_frame)
        self.list_box.grid(row=1, column=0, padx=20, pady=5)

        self.new_item = Button(self.list_frame, text="Add new item", command=self.add_new_item)
        self.new_item.grid(row=2, column=0, pady=(5, 20))

        self.bottom_frame = Frame(self.window, background=bg_colour, width=500, height=150)
        self.bottom_frame.grid(row=3, column=0, sticky="ew")

        ####LIST END####

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='white')
        self.home_button.grid(row=0, column=0, padx=10, pady=5)

        self.back_button = Button(self.bottom_frame, text="list", height=2, width=5, bg='white')
        self.back_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = Button(self.bottom_frame, text="exit", height=2, width=5, bg='red', command=self.exit)
        self.exit_button.grid(row=0, column=2, padx=100, pady=5)

    def add_new_item(self):
        user_input = simpledialog.askstring(title="Adding new item",
                                  prompt="What is your new item name:")
        self.list_box.insert(0, user_input)
        
    def exit(self):
        confirm_exit = messagebox.askquestion("askquestion", "Are you sure?")
        print(confirm_exit)
        if confirm_exit == 'yes':
            self.window.destroy()
        else:
            print("Continue")
            pass

app = App()
app.window.mainloop()
