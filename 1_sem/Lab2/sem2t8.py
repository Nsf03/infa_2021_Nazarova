#семинар 2
#t8
import turtle
turtle.shape('turtle')
turtle.speed()
a=5
k=5
for i in range(30):
    b=a+i*2*k
    for j in range(2):
        turtle.forward(b)
        turtle.left(90)
    turtle.forward(b + k)
    turtle.left(90)
    turtle.forward(b + k)
    turtle.left(90)