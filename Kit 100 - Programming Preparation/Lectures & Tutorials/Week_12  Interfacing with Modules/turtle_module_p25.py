import turtle

# create the turle world, with turtle starting coordinates at 0,0 (the middle)

turtle.setup(width=300,height=300,startx=0,starty=0)

wait = input("Press enter to start drawing..")

# start drawing
turtle.pendown()

# set the colour to red
turtle.color("red")

# draw a square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# hide the turtle (arrow head)
turtle.hideturtle()

# wait for a mouse click before closing the window
turtle.exitonclick()
