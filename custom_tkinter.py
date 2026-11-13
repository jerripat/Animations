
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("CustomTkinter Animation")
root.geometry("600x350")
menu = customtkinter.CTkOptionMenu(root, values=["Option 1", "Option 2", "Option 3"])
menu.pack(pady=20)

def hello():
    if my_label.cget("text") == "Hello World":
        my_label.configure(text="Click Me")
        my_button.configure(text="Click Me")
    else:
        my_label.configure(text="Hello World")
        my_button.configure(text="Hello World")

def game():
    if check_var.get() == "Yes":
        print("Let's play a game!")
    else:
        print("Maybe next time.")




check_var =customtkinter.StringVar(value="off")
my_check = customtkinter.CTkCheckBox(root, text="Would you like to play a game?", variable=check_var, onvalue="Yes", offvalue="No", command=game)
my_check.pack(pady=20)
my_button = customtkinter.CTkButton(
    root,
    text="Click me",
    corner_radius=5,
    height=100,
    width=200,
    font=("Helvetica", 20),
    command=hello
)
my_button.pack(pady=20)

my_label = customtkinter.CTkLabel(
    root,
    text="Click Me",
    font=("Arial", 20)
)
my_label.pack(pady=20)

root.mainloop()
