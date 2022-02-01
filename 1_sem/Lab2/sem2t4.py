#семинар 2
#t4
import turtle
turtle.shape('turtle')
turtle.speed(0.2)

n=100
a=5
fi=((n-2)/n)*180
print(fi)
for i in range(n):
    turtle.forward(a)
    turtle.left(180-fi)

