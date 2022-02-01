#семинар 2
#t10
import turtle
from math import sin, pi

turtle.shape('turtle')
turtle.speed(0.2)
def okr(r):
    n = 50
    fi = ((n - 2) / n) * 180
    for i in range(n):
        turtle.forward(r)
        turtle.left(180 - fi)
r=4
for i in range(1, 4):
    okr(r)
    turtle.right(180)
    okr(r)
    turtle.right(180)
    turtle.right(60)
