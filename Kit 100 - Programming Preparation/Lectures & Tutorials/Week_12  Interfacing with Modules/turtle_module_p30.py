import turtle
import random

turtle.setup(width=600,height=600,startx=0, starty=0)
turtle.reset()

colours = ["red","orange","yellow","green","blue","cyan","violet"]

for i in range(1,21):
    startx = random.randint(-200,200)
    starty = random.randint(-200,200)
    radius = random.randint(20,120)
    sides = random.randint(3,21)

    colourChoice = random.randint(0,len(colours)-1)
    turtle.penup()
    turtle.goto(startx,starty)

    turtle.fillcolor(colours[colourChoice])
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius,360,sides)
    turtle.end_fill()
    
    turtle.write(colours[colourChoice] + " circle with radius "
                 + str(radius) + " and " + str(sides) + " sides",
                 font=("Arial", 16, "italic"))

turtle.exitonclick()
