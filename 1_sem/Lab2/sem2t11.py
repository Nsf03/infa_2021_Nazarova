#семинар 2
#t11
import turtle
from math import sin, pi

turtle.shape('turtle')
turtle.speed(20)
def okr(r):
    n = 50
    fi = ((n - 2) / n) * 180
    for i in range(n):
        turtle.forward(r)
        turtle.left(180 - fi)

turtle.left(90)
for i in range(5, 11):
    okr(i)
    turtle.right(180)
    okr(i)
    turtle.right(180)
