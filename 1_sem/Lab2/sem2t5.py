#семинар 2
#t5
import turtle
turtle.shape('turtle')
turtle.speed()

a=20
for i in range(2, 20, 2):
    for j in range(3):
        turtle.forward(a + 5*i)
        turtle.left(90)
    turtle.forward(a+5*i)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.right(180)
