# Example to show capturing mouse clicks in screen

import turtle
import random


# This is called when the user left-clicks the mouse in the screen
def mouseClickEventHander(x, y):
    red = random.randint(0, 255)  # generate random number between 0 and 255
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    turtle.color(red, green, blue)

    turtle.goto(x, y)  # make turtle move to mouse coordinates


# This is called when the user right-clicks the mouse in the screen
def rightMouseClickEventHander(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.setup(400, 500)
window = (
    turtle.Screen()
)  # get the canvas screen associated with the turtle world so we can process events
window.colormode(255)  # change the way colours are specified to be in the range 0..255

window.title("mouse click drawing")
window.bgcolor("white")  # set screen background to white

turtle.pensize(3)
turtle.pendown()  # start drawing

window.onclick(
    mouseClickEventHander
)  # register an event handler.  Here we're saying, whenever
# the user (left) clicks the mouse, go and run
# mouseClickEventHandler, which automatically gets sent
# the mouse x and y coordinates as parameters

window.onclick(
    rightMouseClickEventHander, 2
)  # same as left click, except now register right-click (button 2)

window.mainloop()  # wait for events to occur
