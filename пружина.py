import turtle
turtle.shape('turtle')
turtle.left(90)
for x in range (1000):
    for i in range(180):
        turtle.forward(1)
        turtle.right(1)
    for i in range(180):
        turtle.forward(0.3)
        turtle.right(1)
