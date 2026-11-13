
import turtle
from colorsys import hsv_to_rgb


def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Spiral Art")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)
    pen.hideturtle()

    h = 0

    for i in range(300):
        h = (h + 0.005) % 1.0

        # Change colors gradually
        r, g, b = hsv_to_rgb(h, 1, 1)
        pen.pencolor(r, g, b)

        # Draw spiral pattern
        pen.forward(i)
        pen.circle(120, 90)
        pen.right(25)

    turtle.done()


from turtle import *
from colorsys import *

def drawspiral():
    bgcolor("black")
    h = 0

    for i in range(200):
        h += 0.0015
        color(hsv_to_rgb(h, 1, 1))
        goto(0, 0)
        fd(i)
        circle(100, 50)
        rt(10)
        hideturtle()

    done()


#draw_spiral()
drawspiral()