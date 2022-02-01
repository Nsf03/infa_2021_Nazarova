#семинар 2
#t7
import turtle
turtle.shape('turtle')
turtle.speed()

n = 5
i=0
while i < n:
    turtle.forward(100)
    turtle.right(180-180/n)
    i += 1

turtle.penup()
turtle.forward(200)
turtle.pendown()

n = 11
i=0
while i < n:
    turtle.forward(100)
    turtle.right(180-180/n)
    i += 1


