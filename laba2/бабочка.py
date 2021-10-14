import turtle
turtle.shape('turtle')
turtle.left(90)
for x in range (4):
    for i in range(60):
        turtle.right(6)
        turtle.forward(1+0.3*x)
    for i in range(60):
        turtle.left(6)
        turtle.forward(1+0.3*x)
for i in range(15):
    turtle.left(0.4)
    turtle.forward(1)
turtle.forward(10)
turtle.left(180)
turtle.forward(10)
for i in range(15):
    turtle.right(0.4)
    turtle.forward(1)
turtle.left(180)
for i in range(15):
    turtle.right(0.4)
    turtle.forward(1)
turtle.forward(10)
turtle.left(180)
turtle.forward(10)
for i in range(15):
    turtle.left(0.4)
    turtle.forward(1)
turtle.penup()
turtle.forward(100)
    
