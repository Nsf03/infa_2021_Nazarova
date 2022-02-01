#семинар 2
#t13
import turtle
from math import sin, pi

turtle.shape('turtle')
turtle.speed()
def dug(r):
    n = 50
    fi = ((n - 2) / n) * 180
    m=int(n*180/360)
    for i in range(m):
        turtle.forward(r)
        turtle.right(180 - fi)

def okr(r):
        n = 50
        fi = ((n - 2) / n) * 180
        for i in range(n):
            turtle.forward(r)
            turtle.left(180 - fi)

turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

turtle.fillcolor('#FFFF99')
turtle.begin_fill()
okr(30)
turtle.end_fill()

turtle.penup()
turtle.goto(20, 40)
turtle.setheading(90)
turtle.width(10)
turtle.pendown()
turtle.backward(60)
turtle.setheading(270)
dug(3)

turtle.penup()
turtle.goto(-60, 90)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
okr(5)
turtle.end_fill()

turtle.penup()
turtle.goto(170, 90)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
okr(5)
turtle.end_fill()

turtle.penup()
turtle.goto(70, -90)
turtle.pendown()
turtle.color('red')
turtle.setheading(270)
dug(7)
