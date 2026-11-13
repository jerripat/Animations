from tkinter import *
import custom_tkinter

custom_tkinter.set_appearance_mode("dark")
custom_tkinter.set_default_color_theme("blue")

root = custom_tkinter.CTk()

root.title("CustomTkinter Animation")
root.geometry("700x450")
global my_y
my_y = 450 / 2 + 350


def up():
    global my_y
    my_y -= 20
    if my_y >= 195:
        my_text.place(x=700 / 2, y=my_y, anchor=CENTER)
        up_button.configure(text=my_y)
        root.after(5, up)  # Call the up function again after 5 milliseconds


def down():
    global my_y
    my_y += 20
    if my_y <= 555:
        my_text.place(x=700 / 2, y=my_y, anchor=CENTER)
        up_button.configure(text=my_y)
        root.after(10, down)  # Call the down function again after 10 milliseconds


my_frame = custom_tkinter.CTkFrame(master=root, width=600, height=400)
my_frame.pack(pady=20, padx=20)

up_button = custom_tkinter.CTkButton(master=my_frame, text="Up", command=up)
up_button.grid(row=0, column=0, padx=10)

down_button = custom_tkinter.CTkButton(master=my_frame, text="Down", command=down)
down_button.grid(row=0, column=1, padx=10)

my_text = custom_tkinter.CTkTextbox(root, width=400, height=200)
my_text.place(x=700 / 2, y=my_y, anchor=CENTER)

root.mainloop()
