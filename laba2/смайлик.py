import turtle
turtle.shape('turtle')
turtle.begin_fill()
turtle.fillcolor('yellow')
for x in range (360):
    turtle.forward(2)
    turtle.left(1)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.left(90)
turtle.begin_fill()
turtle.fillcolor('blue')
for x in range (180):
    turtle.forward(1)
    turtle.left(2)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(140)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('blue')
for x in range (180):
    turtle.forward(1)
    turtle.right(2)
turtle.end_fill()
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.forward(13)
turtle.left(90)
turtle.width(10)
turtle.color('red')
turtle.pendown()
for i in range(180):
    turtle.forward(1)
    turtle.right(1)
turtle.penup()
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.pendown()
turtle.color('black')
turtle.forward(20)
