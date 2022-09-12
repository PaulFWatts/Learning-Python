import turtle 

turtle.setup(width=900,height=900,startx=0,starty=0)
turtle.reset()


turtle.speed(0.1)

for i in range(180):
    turtle.forward(100)
    turtle.right(33)
    turtle.forward(25)
    turtle.left(34)
    turtle.forward(52)
    turtle.right(30)
    
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
    
    turtle.right(2)
    
turtle.done()
