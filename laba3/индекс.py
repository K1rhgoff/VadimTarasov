import turtle
chislo = input()
turtle.pu()
turtle.setpos(-300,0)
one = [2, 1, 5]
two = [0, 1, 3, 4, 5]
three = [0, 1, 2, 3, 4]
four = [0, 2, 3, 1, 5]
five = [1, 0, 2, 3, 5, 4]
six = [1, 2, 4, 5, 3, 2]
seven = [0, 1, 2, 4]
eight = [2, 0, 1, 3, 2, 4, 5, 3]
nine = [4, 3, 2, 0, 1, 3]
zero = [0, 1, 5, 4, 0]
def cords():
    global coords
    x = turtle.xcor()
    y = turtle.ycor()
    coords = [(x,y+50), (x+50,y+50), (x,y), (x+50,y), (x,y-50), (x+50,y-50), (x+100, y)]
def go(number):
    cords()
    turtle.setpos(coords[number[0]])
    turtle.pd()
    for i in range(len(number)-1):
        turtle.setpos(coords[number[i+1]])
    turtle.pu()
    turtle.setpos(coords[6])
func_list = [zero, one, two, three, four, five, six, seven, eight, nine]
for i in range(len(chislo)):
    go(func_list[int(chislo[i])])

