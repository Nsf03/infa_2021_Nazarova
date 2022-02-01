#семинар 2
#t12
import turtle
from math import sin, pi

turtle.shape('turtle')
turtle.speed()
def dug(r):
    n = 130
    fi = ((n - 2) / n) * 180
    m=int(n*180/360)
    for i in range(m):
        turtle.forward(r)
        turtle.right(180 - fi)

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

turtle.left(90)
for i in range(4):
    dug(3)
    turtle.setheading(270)
    dug(0.5)
    turtle.setheading(90)