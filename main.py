
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

WIDTH = 500
HEIGHT = 500

xVELOCITY = 3
yVELOCITY = 2

window = Tk()
window.title("Batman Animation")
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(window, width=WIDTH, height=HEIGHT,
                highlightthickness=0)
canvas.pack()

image_dir = Path(__file__).resolve().parent / "images"

# Background image
background = Image.open(image_dir / "bg.jpeg")
background = background.resize((WIDTH, HEIGHT))
bg_photo = ImageTk.PhotoImage(background)

canvas.create_image(0, 0, anchor=NW, image=bg_photo)

# Batman image
image = Image.open(image_dir / "batman.jpeg")

# Resize Batman so he can move around the screen
image.thumbnail((100, 100))

photo_image = ImageTk.PhotoImage(image)

my_image = canvas.create_image(
    0, 0,
    anchor=NW,
    image=photo_image
)

image_width = photo_image.width()
image_height = photo_image.height()


def animate():
    global xVELOCITY, yVELOCITY

    # Move Batman
    canvas.move(my_image, xVELOCITY, yVELOCITY)

    # Get current position
    x, y = canvas.coords(my_image)

    # Bounce from left and right walls
    if x >= WIDTH - image_width:
        xVELOCITY = -abs(xVELOCITY)
    elif x <= 0:
        xVELOCITY = abs(xVELOCITY)

    # Bounce from top and bottom walls
    if y >= HEIGHT - image_height:
        yVELOCITY = -abs(yVELOCITY)
    elif y <= 0:
        yVELOCITY = abs(yVELOCITY)

    # Schedule next animation frame
    window.after(10, animate)


animate()
window.mainloop()
