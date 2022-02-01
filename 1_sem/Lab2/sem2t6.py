#семинар 2
#t6
import turtle
turtle.shape('turtle')
turtle.speed()

n=12
a=100
fi=360/n
for i in range(n):
    turtle.forward(a)
    turtle.stamp()
    turtle.backward(a)
    turtle.left(fi)

