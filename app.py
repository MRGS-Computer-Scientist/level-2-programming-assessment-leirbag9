from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog, messagebox

w_width = 500
w_height = 700
bg_colour = "#FFFEBE"

####FONT####
title_font = ("MS PGothic", 30, "bold")

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x700")
        self.window.title("window")

        # Define self.home_frame first
        self.home_frame = Frame(self.window, background='gray', width=w_width, height=(w_height-200))
        self.home_frame.grid(row=0, column=0)

        # Load the image
        image = Image.open("imgs/Better_book.png")
        New_image = image.resize((200, 150))
        photo = ImageTk.PhotoImage(New_image)

        # Create the label with the image in self.home_frame
        self.bg_image = Label(self.home_frame, image=photo)
        self.bg_image.image = photo  # Keep a reference to the image to prevent garbage collection
        self.bg_image.grid(row=0, column=0)
        ##TOP##
        self.top_frame = Frame(self.window, background=bg_colour, width=500, height=(w_height-200))
        self.top_frame.grid(row=2, column=0, sticky=N)

        ## Main ##
        self.main_frame = Frame(self.window, background=bg_colour, width=500, height=(w_height-200))
        self.main_frame.grid(row=2, column=0, sticky="nsew")

        ####LIST START####
        self.list_frame = Frame(self.main_frame, background=bg_colour, width=800, height=(w_height-200))
        self.list_frame.grid(row=0, column=0, sticky="nsew")

        self.list_label = Label(self.list_frame, text="List", font=title_font)
        self.list_label.grid(row=0, column=0, padx=220, pady=(20, 10))

        self.list_box = Listbox(self.list_frame)
        self.list_box.grid(row=1, column=0, padx=20, pady=5)

        self.new_item = Button(self.list_frame, text="Add new item", command=self.add_new_item)
        self.new_item.grid(row=2, column=0, pady=(5, 20))
        ####LIST END####

        self.bottom_frame = Frame(self.window, background="orange", width=500, height=150)
        self.bottom_frame.grid(row=3, column=0, sticky="ew")

        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='white', command=self.show_home_frame)
        self.home_button.grid(row=0, column=0, padx=10, pady=5)

        self.list_button = Button(self.bottom_frame, image=="imgs/bookshelf.png" , height=2, width=5, bg='white', command=self.show_list_frame)
        self.list_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = Button(self.bottom_frame, text="exit", height=2, width=5, bg='red', command=self.exit)
        self.exit_button.grid(row=0, column=2, padx=100, pady=5)

    def add_new_item(self):
        user_input = simpledialog.askstring(title="Adding new item", prompt="What is your new item name:")
        if user_input:
            self.list_box.insert(0, user_input)
        
    def exit(self):
        confirm_exit = messagebox.askquestion("askquestion", "Are you sure?")
        if confirm_exit == 'yes':
            self.window.destroy()

    def show_home_frame(self):
        self.main_frame.grid_remove()
        self.home_frame.grid()

    def show_list_frame(self):
        self.home_frame.grid_remove()
        self.main_frame.grid()

app = App()
app.window.mainloop()
