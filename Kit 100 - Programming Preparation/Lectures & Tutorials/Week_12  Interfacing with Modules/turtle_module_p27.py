import turtle

# create the turtle world, with turtle starting coordinates at 0,0 (the middle)

turtle.setup(width=300,height=300,startx=0,starty=0)

wait = input("Press ENTER to start...")

# start drawing
turtle.pendown()

# set the colour to red
turtle.color("red")

for i in range(1,37):
    # draw a square
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    
    # turn 10 degrees to the left before we start drawing another square
    turtle.left(10)

# hide the turtle (normally shown as an arrow head)
turtle.hideturtle()

# wait for a mouse click before closing the window
turtle.exitonclick()

