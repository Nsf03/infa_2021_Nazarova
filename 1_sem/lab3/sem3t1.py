# семинар 3
# t1
import turtle
import random as rd

turtle.shape('turtle')
turtle.speed()

turtle.color('red')
for i in range(100):
    turtle.left(rd.randint(0, 360))
    turtle.forward(rd.randint(10, 50))
