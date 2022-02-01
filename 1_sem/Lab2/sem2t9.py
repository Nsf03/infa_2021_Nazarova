#семинар 2
#t9
import turtle
from math import sin, pi

turtle.shape('turtle')
turtle.speed()
def mnog(n, r):
    fi=((n-2)/n)*180
    a=2*r*sin(pi/n)
    turtle.left(180 - fi/2)
    for i in range(n):
        turtle.forward(a)
        turtle.left(180 - fi)
    turtle.right(180 - fi / 2)
    turtle.penup()
r=50
for i in range (3, 13):
    mnog(i, r)
    turtle.forward(10)
    turtle.pendown()
    r+=15
